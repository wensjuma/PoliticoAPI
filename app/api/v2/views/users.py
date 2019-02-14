from flask import request, abort, Blueprint, make_response, jsonify, request
import datetime
from app.api import utils
from app.api.v2 import utilities
from app.api.v2.models.model_users import UserModel
import psycopg2

import os
import jwt
user_blueprints= Blueprint('users', __name__, url_prefix="/api/v2")

KEY = os.getenv('SECRET_KEY')


@user_blueprints.route("/auth/signup", methods=["POST"])
def signup():
    """
        Sign a user up
    """
    try:
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        username = data["username"]
        othername = data.get("othername", "none")
        email = data["email"]
        phone = data["phone"]
        passportUrl = data.get("passportUrl")
        password = data["password"]
        retypedpassword = data["retypedpassword"]
        isPolitician = data.get("isPolitician", False)
        isAdmin=data.get("isAdmin", False)

    except:
       return abort(utils.res_method(400, "error", 'wrong json formated keys'))
    
    utilities.PasswordsMatch(password, retypedpassword)
    
    utilities.isEmailValid(email)
    utilities.is_phone_number_valid(phone)

    utilities.check_matching_items_in_db_table({"username": username}, "users")
    utilities.check_matching_items_in_db_table({"email": email}, "users")

    newuser = UserModel(username, email, password, firstname,
                        lastname, phone, passportUrl, isPolitician, othername, isAdmin)
    newuser.save_user()

    return utils.res_method(201, "data", [{
        "user": {
            "email": newuser.email,
            "username": newuser.username
        },
        "token": newuser.password
    }])


# login route
@user_blueprints.route("/auth/signin", methods=['POST'])
def user_login():
    try:
        data = request.get_json()
        request_email = data['email']
        password = data['password']

    except KeyError:
        abort(utils.res_method(400, "error", "Provide correct values for email & password"))

    utilities.isEmailValid(request_email)
    try:
        user = UserModel.get_user_by_mail(request_email)
        if not user:
            abort(utils.res_method(404, "error", "User does not exist"))


        # id = user[0][0]
        # username = user[0][1]
        hashed_password = user[0][2]
        req_email= request_email.strip()

        password = UserModel.check_if_password_n_hash_match(
            hashed_password, password)
        if not password:
            return make_response(jsonify({
            "message": "Try again. E-mail or password is incorrect!"
        }
        ), 403)

        token = jwt.encode({
                "email": req_email,
                # "user_id": user[0]['user_id'],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=3000)
            }, os.getenv('JWT_SECRET_KEY', default='SdaHv342nx!jknr837bjwd?c,lsajjjhw673hdsbgeh'))
        return make_response(jsonify({
                            "message": "Login successful",
                            "token": token.decode("UTF-8"),
                            # "role": user[0]['role']
                            }), 200)

        
    except psycopg2.DatabaseError as _error:
        abort(utils.res_method(500, "error", "Server error"))


# password reset route
@user_blueprints.route("/auth/reset", methods=["POST"])
def reset_password():
    try:
        data = request.get_json()
        email = data["email"]
    except KeyError:
        abort(utils.res_method(400, "error", "Should be email"))

    
    utilities.isEmailValid(email)
    
    try:
        user = UserModel.get_user_by_mail(email)
        if not user:
            abort(utils.res_method(404, "error",
                                    "User does not exist. Create an account first"))
        return utils.res_method(200, "data", [{
            "message": "Check your email for password reset link",
            "email": email
        }])
    except psycopg2.DatabaseError as _error:
        abort(utils.res_method(500, "error", "Server error"))


# def logout(self):
#         """POST /auth/logout"""
        
#         token = request.headers['Authorization']
#         user = users.UserModel(token=token)
#         user.logout()

#         return make_response(jsonify({
#             'message': 'User Logged out successfully'
#         }))
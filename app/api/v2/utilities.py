import os
import re
from flask import abort, request, make_response, jsonify
from functools import wraps
from app.api.utils import res_method
from app.api.v2.models import database
from app.api.v2.models.database import select_data_from_db
from flask_jwt import jwt
from flask_jwt import JWT

KEY = os.getenv('SECRET_KEY')

"""
consists of utilities required by 
different files in v2 of this app
"""


def PasswordsMatch(first_pass, sec_pass):
    """
        this function checks if the passwords.
    """
    if(first_pass!= sec_pass):
        abort(res_method(400, "error", "passwords dont match"))
    return True


def is_phone_number_valid(phone):
    """
        This checks if a number phone number is valid
    """
    if not re.match('^[0-9]*$', phone):
        abort(res_method(400, "Error", "Phone number should be integers only"))


def isEmailValid(email):
    """
        this function checks if the email is valid
        via regex
    """
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        abort(res_method(400, "error", "email is invalid"))
    return True


def check_matching_items_in_db_table(params, table_name):
    """
        check if a value of key provided is 
        available in the database table
        if there's a duplicate then the test fails
    """
    for key, value in params.items():
        query = """
        SELECT {} from {} WHERE {}.{} = '{}'
        """.format(key, table_name, table_name, key, value)
        duplicated = select_data_from_db(query)
        if duplicated:
            abort(res_method(409, "error",
                              "Error. '{}' '{}' is already in use".format(key, value)))


def token_required(f):
    """
        This higher order function checks for token in the request
        Headers
    """
    # @wraps(f)
    # def decorated(*args, **kwargs):
    #     token = None
    #     if 'x-access-token' in request.headers:
    #         token = request.headers['x-access-token']
    #     if not token:
    #         return res_method(401, "error", "Token is missing")
    #     try:
    #         data = jwt.decode(token, KEY, algorithms='HS256')
    #         query = """
    #         SELECT email FROM users
    #         WHERE users.email = '{}'""".format(data['email'])

    #         user = select_data_from_db(query)

    #     except:
    #         return res_method(401, "error", "Token is expired or invalid")

    #     return f(user, *args, **kwargs)
    # return decorated
def verify_tokens():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
    if not token:
        abort(make_response(jsonify({
                                "Message": "You need to login"}), 401))

    query = """SELECT token FROM auth WHERE  token = '{}'""".format(token)
    blacklisted = database.select_data_from_db(query)
    if blacklisted:
        abort(make_response(jsonify({
                        "Message": "Kindly login again"}), 401))
    try:
        data = jwt.decode(token, os.getenv('JWT_SECRET_KEY', default='SdaHv342nx!jknr837bjwd?c,lsajjjhw673hdsbgeh'))
        return data["email"], data["user_id"]

    except:
        abort(make_response(jsonify({
            "Message": "The token is either expired or wrong"
        }), 403))   
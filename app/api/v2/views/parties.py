from flask import request, abort
import os, jwt
from app.api import utils
from app.api.v2 import utilities 
from app.api.v2.utilities import token_required, check_matching_items_in_db_table

from app.api.v2.models.model_party import PartiesModel
from app.api.v2.models import database
import psycopg2
from flask import Blueprint, make_response, jsonify

party_blueprints= Blueprint('part', __name__, url_prefix="/api/v2")



@party_blueprints.route("/party", methods=["GET"])
# def get_all_parties():
#     """
#         This method gets all parties
#     """
#     parties = PartiesModel.get_all_parties()
    
#     if parties:
#         return utils.res_method(200, "data", parties)
#     return utils.res_method(200, "data", [])

@party_blueprints.route("/party", methods=["POST"])
def create_party():
    """
        method for admin to create a specific party
    """
    token = utilities.verify_tokens()
    # try:
    #     email = user[0][0]
    # except:
    #     return utils.res_method(401, "error", "You don't have an account")

    try:
        data = request.get_json()
        party_name = data['party_name']
        hqAddress = data["hqAddress"]
        logoUrl = data.get("logoUrl", "")

    except KeyError:
        abort(utils.res_method(400, "error", "Should be name, hqAddress & logoUrl"))

    try:

        """
            Only admin can create parties
        """
        if token:
            newparty = PartiesModel(
                id= id, party_name=party_name, hqAddress=hqAddress, logoUrl=logoUrl)

            check_matching_items_in_db_table({"name": party_name}, "parties")

            newparty.save_party()

            return utils.res_method(201, "data", [{
                "name": party_name
            }])

        return utils.res_method(401, "error", "You are not an admin")

    except psycopg2.DatabaseError as _error:
        abort(utils.res_method(500, "error", "Server error"))
@party_blueprints.route("/<id>", methods=["GET", "DELETE"])
def get_specific_party(id):
    pass
    


@party_blueprints.route("/party/<id>", methods=["PUT"])
def edit_specific_party(id):
    parties = PartiesModel.update_party(id)
    
    if parties:
        return utils.res_method(200, "data", parties)
    return utils.res_method(400, "error", "Request not successful!")
   


@party_blueprints.route("/<id>", methods=["DELETE"])
def delete_specific_party(id):
    query = """SELECT * FROM parties WHERE id = {}""".format(id)
    party = database.select_data_from_db(query)
        
    if not party:
            return make_response(jsonify({
            "message": "Party with id {} does not exist".format(id)
            }), 404)

    party = party.PartiesModel(id=id)
    party.delete()

    return make_response(jsonify({
            "message": "Product deleted successfully"
        }), 200)
@staticmethod
def get_all_parties():
        """
            Get all parties
        """
        get_all_parties_query = """
        SELECT * FROM parties
        """
        return database.select_data_from_db(get_all_parties_query)
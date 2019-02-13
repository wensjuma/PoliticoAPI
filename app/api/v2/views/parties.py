from flask import request, abort

# from app.api.v2 import user_blueprints
from app.api import utils

from app.api.v2.utilities import token_required, check_matching_items_in_db_table

from app.api.v2.models.model_party import PartiesModel

import psycopg2
from flask import Blueprint

party_blueprints= Blueprint('part', __name__, url_prefix="/api/v2")



@party_blueprints.route("/party", methods=["GET"])
def get_all_parties():
    """
        This method gets all parties
    """
    parties = PartiesModel.get_all_parties()
    
    if parties:
        return utils.res_method(200, "data", parties)
    return utils.res_method(200, "data", [])

@party_blueprints.route("/party", methods=["POST"])
@token_required
def create_party(user):
    """
        method for admin to create a specific party
    """
    try:
        email = user[0][0]
    except:
        return utils.res_method(401, "error", "You don't have an account")

    try:
        data = request.get_json()
        party_name = data['party_name']
        hqAddress = data["hqAddress"]
        logoUrl = data.get("logoUrl", "")

    except KeyError:
        abort(utils.res_method(400, "error", "Should be name, hqAddress & logoUrl"))

    try:

        """
            Only admin can create emails
        """
        if email == "johndoe@gmail.com":
            newparty = PartiesModel(
                party_name=party_name, hqAddress=hqAddress, logoUrl=logoUrl)

            check_matching_items_in_db_table({"name": party_name}, "parties")

            newparty.save_party()

            return utils.res_method(201, "data", [{
                "name": party_name
            }])

        return utils.res_method(401, "error", "You are not an admin")

    except psycopg2.DatabaseError as _error:
        abort(utils.res_method(500, "error", "Server error"))
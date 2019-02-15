from flask import request, abort, Blueprint

 
from app.api import utils
from .. import utilities
from app.api.v2.utilities import token_required, check_matching_items_in_db_table

from app.api.v2.models.model_offices import OfficesModel

import psycopg2

office_blueprint= Blueprint('v2_offices',__name__, url_prefix='/api/v2')
@office_blueprint.route("/office", methods=["POST"])
# @token_required
def create_office(user):
     """
        method for admin to create a specific party
    """
     token = utilities.verify_tokens()
    
     try:
        data = request.get_json()
        office_name = data['office_name']
        
       

     except KeyError:
        abort(utils.res_method(400, "error", "Should be name, hqAddress & logoUrl"))

     try:

        """
            Only admin can create parties
        """
        if token:
            newoffice = OfficesModel(
                 office_name=office_name, type= type,)

            check_matching_items_in_db_table({"office_name": office_name}, "Office")

            newoffice.save_office()

            return utils.res_method(201, "data", [{
                "office_name": office_name
            }])

        return utils.res_method(401, "error", "You are not an admin")

     except psycopg2.DatabaseError as _error:
        abort(utils.res_method(500, "error", "Server error"))


@office_blueprint.route("/office", methods=['GET'])
def get_all_offices():
    """
        Get all offices from the
        database. No authentication is required here.
    """
    offices = OfficesModel.get_all_offices()
    
    if offices:
        return utils.res_method(200, "data", offices)
    return utils.res_method(404, "error", " data not found!!")


@office_blueprint.route("/office/<int:office_id>", methods=["GET"])
def get_specific_office(office_id):
    """
       GETs all offices to the users 
    """
    office = OfficesModel.get_specific_office(office_id)
    if office:
        return utils.res_method(200, "data", office)
    return utils.res_method(404, "error", "Office is not not found")
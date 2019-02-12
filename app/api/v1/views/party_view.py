from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import data_model
# from app.api.v1.models.data_model  import DataModel, PARTIES
# from app.api.utils import valid_string, res_method, retrieve_specific_data, retrieve_all_data,return_response
# from app.api.utils import res_method,sanitize_input, validate_string_data_type, validate_office_type, return_error,check_is_valid_url
# from app.api.utils import  validate_int_data_type
from app.api.utils import res_method, retrieve_all_data, retrieve_specific_data, res_method, format_response

PARTY = data_model.DataModel()

party_route = Blueprint('party', __name__, url_prefix='/api/v1')
@party_route.route('/party',methods=['GET'])
def get_parties():
       return res_method(200, "data", retrieve_all_data(PARTY, "party"))
@party_route.route('/party', methods=['POST'])
def save_party():
    try:
        
        data = request.get_json(force=True)
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400  
    name = data["name"]
    hqAddress = data["hqAddress"]
    logoUrl = data["logoUrl"]

    party = PARTY.add_party(name, hqAddress,logoUrl)
    if party:
        return format_response(201, "party was created",party)
    return format_response(400,"an error occured")

        # data = request.get_json(force=True)
        # name = data["name"]
        # hqAddress = data["hqAddress"]
        # logoUrl = data["logoUrl"]
        # if(validate_string_data_type(name) == False):
        #     return return_error(400, "the name should be of correct data type")
        # if(validate_string_data_type(hqAddress) == False):
        #     return return_error(400, "the HQ be of correct data type")
        # if(check_is_valid_url(logoUrl) == False):
        #     return return_error(400, "the Logo url is not in the correct format")

        # if(sanitize_input(name)) == False:
        #     return return_error(400, "name is in the wrong format")
        # if (sanitize_input(hqAddress)) == False:
        #     return return_error(400, "hq address is in the wrong format")
                      
      
@party_route.route("/party/<int:party_id>", methods=['PUT'])
def update_party(party_id):
    try:
        data = request.get_json(force=True)  
        id=party_id
        name = data["name"]
        hqAddress = data["hqAddress"]
        logoUrl= data["logoUrl"]   
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400
        
    PARTY.edit_party(id,name, hqAddress, logoUrl)
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"Update success"}]
    })),200

@party_route.route('/party/<int:id>', methods=['GET'])
def single_party(id):
    try:
        party= retrieve_specific_data(PARTY, "party", id)
    except:
        return make_response({
            'status':404,
            'message':"data item not found"
        })

    if party:
        return res_method(200, "data", party)
    return res_method( 404, "error", "party of that Id could not be Found!!" )

@party_route.route('/party/<int:party_id>',methods=['DELETE'])
def delete_party(party_id):
    try:
        party=PARTY.delete_party(party_id)
    except:
        return make_response({
            'status':400,
            'message':"Not delete function"
        })
    if party:
        return make_response(jsonify({
            "status":200,
            "data":[{"message":"Delete sucessful"}]
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "message":"Error on deletion!!"
    }), 404)



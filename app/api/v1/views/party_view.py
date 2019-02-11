from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import data_model

PARTY = data_model.DataModel()

party_route = Blueprint('party', __name__, url_prefix='/api/v1')
@party_route.route('/party',methods=['GET'])
def get_parties():
    data = PARTY.get_parties()
    return make_response(jsonify({
        'status':200,
        'data':data
    })),200
@party_route.route('/party', methods=['POST'])
def save_party():
        data= request.get_json()
        name= data['name']
        hqAddress= data['hqAddress']
        logoUrl= data['logoUrl']
        
        party = PARTY.add_party(name, hqAddress, logoUrl)
        if party:
            return make_response(jsonify({
            "status":201,
            "data":"Party Added successifuly!"
            }),201)
        return make_response(jsonify({
            "status": 400,
            "message":"wrong details suplied!"
        }))

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
    party=PARTY.specific_party(id)
    if party:
        return make_response(jsonify({
            "status":200,
            "data": party
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "message":"Data not found!!"
    }), 404)

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



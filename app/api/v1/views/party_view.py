from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import party_model

PARTY = party_model.Party()

party_route = Blueprint('party', __name__, url_prefix='/api/v1')
@party_route.route('/getparty',methods=['GET'])
def get_parties():
    data = PARTY.get_parties()
    return make_response(jsonify({
        'status':200,
        'data':data
    })),200
@party_route.route('/addparty', methods=['POST'])
def save_party():
        data= request.get_json()
        name= data['name']
        slogan= data['slogan']
        
        party = PARTY.add_party(name, slogan)
        if party:
            return make_response(jsonify({
            "status":201,
            "data":"Party Added successifuly!"
            }),201)
        return make_response(jsonify({
            "status": 400,
            "message":"wrong details suplied!"
        }))

@party_route.route("/editparty/<int:party_id>", methods=['PUT'])
def update_party(party_id):
    try:
        data = request.get_json(force=True)  
        id=party_id
        name = data["name"]
        slogan = data["slogan"]    
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400
        
    PARTY.edit_party(id,name,slogan)
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"Update success"}]
    })),200
@party_route.route('/singleparty/<int:id>', methods=['GET'])
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

@party_route.route('/deleteparty/<int:party_id>',methods=['DELETE'])
def delete_party(party_id):
    PARTY.delete_party(party_id)
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"Delete sucessful"}]
    }))

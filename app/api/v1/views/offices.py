from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import data_model
OFFICE = data_model.OfficeModel()

office_route = Blueprint('office', __name__, url_prefix='/api/v1')
@office_route.route('/office',methods=['GET'])
def get_offices():
    data = OFFICE.get_office_list()
    return make_response(jsonify({
        'status':200,
        'data':data
    })),200
@office_route.route('/office', methods=['POST'])
def save_office():
        data= request.get_json()
        name= data['name']
        type= data['type']      
        OFFICE.add_office(name, type)
        return make_response(jsonify({
            "status":201,
            "data":"Office Added!!"
        }),201)

@office_route.route("/office/<int:id>", methods=['GET'])
def get_single_office(id):

    office = OFFICE.get_single_office(id)

    if office:
        return make_response(jsonify({
            "status": 200,
            "data": office
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "No such office !!"
    }), 404)
@office_route.route("/office/<int:office_id>", methods=['PUT'])
def update_office(office_id):
    try:
        data = request.get_json(force=True)  
        id=office_id
        name = data["name"]
        type = data["type"]
         
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400
        
    OFFICE.edit_office(id,name, type)
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"Update success"}]
    })),200
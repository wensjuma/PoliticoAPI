from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import data_model
import json
from app.api.utils import res_method,retrieve_all_data, retrieve_specific_data
OFFICE = data_model.DataModel()

office_route = Blueprint('office', __name__, url_prefix='/api/v1')

@office_route.route('/')

def index():
    return make_response(jsonify({
        "Message": "Welcome to our API "
    }))
@office_route.route('/office',methods=['GET'])
def get_offices():
    data = OFFICE.retrieve_all_offices()
    return make_response(jsonify({
        'status':200,
        'data':data
    })),200
@office_route.route('/office', methods=['POST'])
def save_office():
    try:
        data= request.get_json()
        name= data['name']
        type= data['type']      
        office=OFFICE.add_office(name, type)
    except:
        return make_response(jsonify({
            "status":400,
            "message":"Invalid input !!"
        })),400
    
    if office:
             return make_response(jsonify({
            "status":201,
            "data":"Office Added!!"
        }),201)
    return make_response(jsonify({
        'status':'400',
        'message':'Request not allowed!!'
    }))

@office_route.route("/office/<int:id>", methods=['GET'])
def get_single_office(id):
    office= retrieve_specific_data(OFFICE, "office", id)
    if office:  
        return res_method(200, "data", office)
    return res_method( 404, "error", "office of that Id could not be Found!!" )

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

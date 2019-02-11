from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import data_model
import json
OFFICE = data_model.DataModel()

office_route = Blueprint('office', __name__, url_prefix='/api/v1')
def res_method(status, key, message):
    dict={
        'status':'status'
    }
    dict[key]=message
    return make_response(jsonify(dict), status)
@office_route.route('/')
def index():
    return "<br><br><br> <hr><center><h2>Welcome to Politico API</h2> <h3>Use routes <i>api/v1/office</i>  and  <i>api/v1/party</i> to retrieve data</h3></center><hr>"
@office_route.route('/office',methods=['GET'])
def get_offices():
    data = OFFICE.get_office_list()
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
        return res_method(400, "error", "check your format!!")
    
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

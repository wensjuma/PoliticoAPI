from flask import Flask, Blueprint, make_response, request,jsonify 
from app.api.v1.models import data_model

OFFICE = data_model.OfficeModel()

office_route = Blueprint('office', __name__, url_prefix='/api/v1')
@office_route.route('/getoffice',methods=['GET'])
def get_offices():
    data = OFFICE.get_offices()
    return make_response(jsonify({
        'status':200,
        'data':data
    })),200
@office_route.route('/addoffice', methods=['POST'])
def save_party():
        data= request.get_json()
        name= data['name']
        post= data['post']
        
        OFFICE.add_office(name, post)
        return make_response(jsonify({
            "status":201,
            "data":"Office Added!!"
        }),201)
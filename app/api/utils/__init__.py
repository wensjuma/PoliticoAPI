from flask import Flask, jsonify, make_response
import re


def res_method(status,key, message):
    dict ={
        "status":status
    }
    dict[key]=message
    return make_response(jsonify(dict), status)

        
def retrieve_all_data(model, type):
    if(type=="offices"):
        return model.retrieve_all_offices()
    elif(type=="parties"):
        return model.retrieve_all_parties()
    return []
def retrieve_specific_data(model, type, id):
    if(type=="office"):
        return model.retrieve_office(id)
    elif (type=="party"):
        return model.retrieve_party(id)
    return []


def sanitize_input(input_data):
    """check if input is of alphanumeric characters"""
    if input_data.isalpha() == False:
        return False

def validate_string_data_type(data_passed):
    """ensures the input passed is of str type."""
    if not isinstance(data_passed, str):
        return False
    return True

def return_error(status_code, message):
    """ function to format the response """
    response = {
        "status": status_code,
        "error": message,
    }
    return make_response(jsonify(response), status_code)
def return_response(status_code, message, data=list()):
    """ function to format the response """
    response = {
        "status": status_code,
        "message": message,
        "data": data,
    }
    return make_response(jsonify(response), status_code)




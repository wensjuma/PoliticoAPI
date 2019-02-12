from flask import Flask, jsonify, make_response
import re

def valid_string(is_input_string):
    if is_input_string:
        return isinstance(is_input_string, str)
    else:
        return False
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
def format_response(status_code, msg, data=list()):
    
    response = {
        "status":status_code,
        "message": msg,
        "data":data
    }
    return make_response(jsonify(response),status_code)

# def sanitize_input(input_data):
#     """check if input is of alphanumeric characters"""
#     if input_data.isalpha() == False:
#         return False
# def validate_int_data_type(data_passed):
#     """ ensures the inputs are of int  type"""
#     if not isinstance(data_passed, int):
#         return False
#     return True
# def validate_string_data_type(data_passed):
#     """ensures the input passed is of str type."""
#     if not isinstance(data_passed, str):
#         return False
#     return True
# def generate_id(list_of_items):
#     """generates the id of a new item given a list"""
#     return len(list_of_items) +1
# def return_error(status_code, message):
#     """ function to format the response """
#     response = {
#         "status": status_code,
#         "error": message,
#     }
#     return make_response(jsonify(response), status_code)
# def return_response(status_code, message, data=list()):
#     """ function to format the response """
#     response = {
#         "status": status_code,
#         "message": message,
#         "data": data,
#     }
#     return make_response(jsonify(response), status_code)
# def check_json_party_keys(request):
#     """checks if keys of the payload are correct"""
#     request_keys = ["name", "hqAddress", "logoUrl"]
#     errors = []
#     for key in request_keys:
#         if not key in request.json:
#             errors.append(key)
#         return errors

# def validate_office_type(data):
#     """ensures the office name is of the defined parameters"""
#     accepted = ["federal", "legislative", "local", "state"]
#     if data not in accepted:
#         return False
#     return True

# def check_json_office_keys(request):
#     """checks if keys of the office payload is correct"""
#     request_keys = ["name", "office_type"]
#     errors = []
#     for key in request_keys:
#         if not key in request.json:
#             errors.append(key)
#         return errors



# def check_is_valid_url(url):
#     """valid url"""
#     if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
#                url):
#        return True
#     return False

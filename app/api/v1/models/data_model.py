from flask import Flask, abort

OFFICES=[]

class OfficeModel(object):
    def __init__(self):
        self.office = OFFICES
    
    def get_office_list(self):
        return self.office
    
    def add_office(self, name, type):
        data = {
            'id':len(self.office)+1,
            'name':name,
            'type':type
        }
        self.office.append(data)
        return self.office
        
    def get_single_office(self, id):
        return [office for office in self.office if office["id"] == id]

    def edit_office(self,office_id, name, type):
        office=[office for office in self.office if office['id']== office_id]
        if len(office) == 0:
            return abort(400)
        office[0]['name'] = name,
        office[0]['type'] = type
        
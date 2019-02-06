OFFICES=[]

class OfficeModel(object):
    def __init__(self):
        self.office = OFFICES
    
    def get_office_list(self):
        return self.office
    
    def add_office(self, name, post):
        data = {
            'id':len(self.office)+1,
            'name':name,
            'post':post
        }
        self.office.append(data)
        return self.office
        
    def get_single_office(self, id):
        return [office for office in self.office if office["id"] == id]
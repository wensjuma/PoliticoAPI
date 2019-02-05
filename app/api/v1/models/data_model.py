OFFICES=[]

class OfficeModel(object):
    def __init__(self):
        self.office = OFFICES
    
    def get_offices(self):
        return self.office
    
    def add_office(self, name, post):
        data = {
            'id':len(self.office)+1,
            'name':name,
            'post':post
        }
        self.office.append(data)
        return self.office
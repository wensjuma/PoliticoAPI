from flask import Flask, abort
                                                                    
OFFICES=[]
PARTY=[]
    
class DataModel(object):
    def __init__(self):
        self.office = OFFICES
        self.party= PARTY
    
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
    
    def get_parties(self):
        return self.party
    
    def add_party(self, name, hqAddress, logoUrl):
        data = {
           'id':len(self.party)+1,
            'name':name,
            'hqAddress':hqAddress,
            'logoUrl':logoUrl
        }
        self.party.append(data)
        return self.party

    def edit_party(self,party_id, name, hqAddress, logoUrl):
        party=[party for party in self.party if party['id']== party_id]
        if len(party) == 0:
            return abort(400)
        party[0]['name'] = name,
        party[0]['hqAddress'] = hqAddress,
        party[0]['logoUrl'] = logoUrl
       
    def delete_party(self,party_id):
    
        party = [party for party in self.party if party['id'] == party_id]

        if len(party) == 0:
            abort(400)
        self.party.remove(party[0])
    def specific_party(self, id):
        return [party for party in self.party if party['id'] == id]

        
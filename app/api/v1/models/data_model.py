from flask import Flask, abort
                                                                    

data_dict={
    "party":[],"office":[]
}
    
class DataModel:
    def __init__(self):
        self.dict = data_dict
        
    
    def retrieve_all_offices(self):
        return self.dict
    
    def add_office(self, name, type):
        data = {
            'id':len(self.dict['office'])+1,
            'name':name,
            'type':type
        }
        self.dict['office'].append(data)
        return self.dict['office']
        
    def retrieve_office(self, id):
        return [office for office in self.dict['office'] if office["id"] == id]

    def edit_office(self,office_id, name, type):
        office=[office for office in self.dict['office'] if office['id']== office_id]
        if len(office) == 0:
            return abort(400)
        office[0]['name'] = name,
        office[0]['type'] = type
    
    def retrieve_all_parties(self):
        return self.dict['party']
    
    def add_party(self, name, hqAddress, logoUrl):
        data = {
           'id':len(self.dict['party'])+1,
            'name':name,
            'hqAddress':hqAddress,
            'logoUrl':logoUrl
        }
        self.dict['party'].append(data)
        return self.dict['party']

    def edit_party(self,party_id, name, hqAddress, logoUrl):
        party=[party for party in self.dict['party'] if party['id']== party_id]
        if len(party) == 0:
            return abort(400)
        party[0]['name'] = name,
        party[0]['hqAddress'] = hqAddress,
        party[0]['logoUrl'] = logoUrl
       
    def delete_party(self,party_id):
    
        party = [party for party in self.dict['party'] if party['id'] == party_id]

        if len(party) == 0:
            abort(400)
        self.dict['party'].remove(party[0])
    def retrieve_party(self, id):
        return [party for party in self.dict['party'] if party['id'] == id]

        
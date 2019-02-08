from flask import Flask, abort
PARTY=[]


class Party(object):
    def __init__(self):
        self.party = PARTY
    
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


       

    
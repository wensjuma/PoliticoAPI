from flask import Flask, abort
PARTY=[]


class Party(object):
    def __init__(self):
        self.party = PARTY
    
    def get_parties(self):
        return self.party
    
    def add_party(self, name, slogan):
        data = {
            'id':len(self.party) + 1,
            'name':name,
            'slogan':slogan
        }
        self.party.append(data)
        return self.party

    def edit_party(self,party_id, name, slogan):
        party=[party for party in self.party if party['id']== party_id]
        if len(party) == 0:
            return abort(400)
        party[0]['name'] = name,
        party[0]['slogan']= slogan  

       

    
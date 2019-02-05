
PARTY=[]
OFFICE=[]

class Party(object):
    def __init__(self):
        self.party = PARTY
    
    def get_parties(self):
        return self.party
    
    def add_party(self, name, slogan):
        data = {
            'id':len(self.party)+1,
            'title':name,
            'slogan':slogan
        }
        self.party.append(data)
        return self.party


    
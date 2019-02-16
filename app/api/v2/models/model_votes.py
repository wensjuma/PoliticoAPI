
import re
from app.api.v2.models import database
from app.api.v2 import utilities

class VoteModel():
    def __init__(self, created_by, office, candidate):
        self.voter = created_by
        self.office = office
        self.candidate= candidate
        
    def cast_vote(self):
        
      
            create_votes_query = """
            INSERT INTO votes(created_by, office, candidate) VALUES(
                '{}', '{}', {}
            )""".format(self.voter, self.office, self.candidate)
            database.query_data_from_db(create_votes_query)
        

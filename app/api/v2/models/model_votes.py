
import re
from app.api.v2.models import database
from app.api.v2 import utilities

VOTES=[]

class Vote():
    def __init__(self):
        self.vote = VOTES
    
    def save(self, created_on, created_by, office, candidate):
        query =  """INSERT INTO votes(createdOn, createdBy, office, candidate)
        VALUES('{}','{}','{}','{}')""".format(created_on, created_by, office, candidate)
        database.query_data_from_db(query)
    

    def fetch_all_votes(self):
        """Fetches all votes cast
        the database
        """
        query = """ SELECT * FROM votes """
        # query = """SELECT offices.name AS office, users.firstname AS firstname, users.lastname AS lastname,
        #         COUNT (votes.candidate) AS votes FROM votes JOIN offices ON offices.office_id = votes.office
        #         JOIN  users ON users.user_id = votes.candidate GROUP BY users.firstname, users.lastname, offices.name
        #       """
        return database.select_data_from_db(query)
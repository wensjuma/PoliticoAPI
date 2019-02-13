
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from . import database


class PartiesModel:
    """
        v2 parties model
    """

    def __init__(self, party_name, hqAddress, logoUrl):
        self.name = party_name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    def save_party(self):
        """
        Add a new party to db
        """
        add_party = """
        INSERT INTO parties(party_name, hqAddress, logoUrl) VALUES(
            '{}', '{}', '{}'
        )""".format(self.name, self.hqAddress, self.logoUrl)

        database.query_parties_data(add_party)

    @staticmethod
    def get_all_parties():
        """
            Get all parties
        """
        retrieve_all_parties= """
        SELECT id, name, hqAddress, logoUrl FROM parties
        """
        return database.query_parties_data(retrieve_all_parties)
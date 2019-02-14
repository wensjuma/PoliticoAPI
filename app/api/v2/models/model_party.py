
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from . import database


class PartiesModel:
    """
        v2 parties model
    """

    def __init__(self, id, party_name, hqAddress, logoUrl):
        self.id=id
        self.party_name = party_name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    def save_party(self):
        """
        Add a new party to db
        """
        add_party = """
        INSERT INTO parties(party_name, hqAddress, logoUrl) VALUES(
            '{}', '{}', '{}'
        )""".format(self.party_name, self.hqAddress, self.logoUrl)

        database.query_parties_data(add_party)

    @staticmethod
    def get_all_parties():
        """
            Get all parties
        """
        retrieve_all_parties= """
        SELECT id, party_name, hqAddress, logoUrl FROM parties
        """
        return database.query_parties_data(retrieve_all_parties)
    def update_party(self):
        query = """UPDATE parties SET party_name = {},
        hqAddress = {}, logoUrl={} WHERE id = {}""".format(self.party_name,
                                                        self.hqAddress, self.logoUrl, self.id)

        database.query_parties_data(query)
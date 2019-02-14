
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

        database.select_data_from_db(add_party)

    @staticmethod
    def formatParty(iterable):
        """
            This function will help in formatting the party data 
            in a record format when its called in getting_all_parties
            or getting a specific party.
        """
        data = []
        for party in iterable:
            formattedParty= {'id': party[0],
                               'office_name': party[1],
                               'type': party[2]}
            data.append(formattedParty)
        return data

    @staticmethod
    def get_all_parties():
        """
            Fetch all the offices from the database.
        """
        get_all_parties = """
        SELECT * FROM parties
        """
        return PartiesModel.formatParty(database.select_data_from_db(get_all_parties))

    @staticmethod
    def get_specific_party(office_id):
        
        select_single_office = """
        SELECT * FROM parties WHERE id = '{}'
        """.format(office_id)

        return PartiesModel.formatParty(database.select_data_from_db(select_single_office))    
    # @staticmethod
    # def get_all_parties():
    #     """
    #         Get all parties
    #     """
    #     retrieve_all_parties= """
    #     SELECT id, party_name, hqAddress, logoUrl FROM parties
    #     """
    #     return database.query_parties_data(retrieve_all_parties)
    # def update_party(self):
    #     query = """UPDATE parties SET party_name = {},
    #     hqAddress = {}, logoUrl={} WHERE id = {}""".format(self.party_name,
    #                                                     self.hqAddress, self.logoUrl, self.id)

    #     database.query_parties_data(query)
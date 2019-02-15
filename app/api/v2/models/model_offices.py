from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from . import database


class OfficesModel:
    """
        office models
    """

    def __init__(self, office_name, type):
        """
            Initialize an OfficesModel.
        """
        self.name = office_name
        self.type = type

    def save_office(self):
        """
        Add a new office to the
        database (ADMIN ONLY OPERATION)
        """
        ceate_office_query = """
        INSERT INTO office(office_name, type) VALUES(
            '{}', '{}'
        )""".format(self.name, self.type)
        database.query_data_from_db(ceate_office_query)

    @staticmethod
    def formatOffices(iterable):
        """
            This function will help in formatting the offices data 
            in a record format when its called in getting_all_offices
            or getting a specific office.
        """
        data = []
        for office in iterable:
            formattedOffice = {'id': office[0],
                               'office_name': office[1],
                               'type': office[2]}
            data.append(formattedOffice)
        return data

    @staticmethod
    def get_all_offices():
        """
            Fetch all the offices from the database.
        """
        get_all_offices = """
        SELECT * FROM office
        """
        return OfficesModel.formatOffices(database.select_data_from_db(get_all_offices))

    @staticmethod
    def get_specific_office(office_id):
        
        select_single_office = """
        SELECT * FROM office WHERE id = '{}'
        """.format(office_id)

        return OfficesModel.formatOffices(database.select_data_from_db(select_single_office))
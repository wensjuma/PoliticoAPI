from flask import request, abort, Blueprint
from app.api import utils
from .. import utilities
from app.api.v2.utilities import token_required, check_matching_items_in_db_table

from app.api.v2.models.model_votes import VoteModel

import psycopg2
votes_bp= Blueprint("votes", __name__, url_prefix='/api/v2')
votes_bp.route('/vote', methods=['POST'])
def create_vote():

    data = request.get_json()
    created_by = data['created_by']
    office= data['office']
    candidate= data['candidate']
    newvote = VoteModel(created_by=created_by, office= office, candidate= candidate)

    check_matching_items_in_db_table({"created_by": created_by}, "votes")

    newvote.cast_vote()

    return utils.res_method(201, "data", [{
                "created_by":created_by
            }])

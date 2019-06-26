from datetime import datetime
from flask import Blueprint, Flask, request, jsonify
from dbc.team_dbc import TeamDBC
from os import environ, path
from time import mktime
import flickr_api as flickr
import flickr_api as f

from config import API_KEY

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/', methods=['GET'])
def get_teams():
    #Go get all the teams in the db
    # teams = team_dbc.get_teams()
    return jsonify({'teams': 'Hello'}), 200


@api_blueprint.route('/<team_id>', methods=['GET'])
def get_team(team_id):
    #get single team data
    team = team_dbc.get_teams(team_id=team_id)
    return jsonify({'team': team}), 200


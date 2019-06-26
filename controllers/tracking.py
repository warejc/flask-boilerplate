from datetime import datetime
from flask import Blueprint, Flask, request, jsonify, render_template
from dbc.team_dbc import TeamDBC
from os import environ, path
from time import mktime


tracking_blueprint = Blueprint('tracking', __name__, url_prefix='/tracking')

@tracking_blueprint.route('/', methods=['GET'])
def get_parameters():
    #go to service, get saved parameter data
    parameters = [{'123':{"name": "Bench", "last_value": 170}}]
    return render_template('pages/tracking.html', parameters=parameters)
    #return jsonify({'parameters': parameters})

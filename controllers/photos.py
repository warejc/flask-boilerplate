from datetime import datetime
from flask import Blueprint, Flask, request, jsonify, render_template
from dbc.team_dbc import TeamDBC
from os import environ, path
from time import mktime
import flickr_api as flickr

photos_blueprint = Blueprint('photos', __name__, url_prefix='/photos')

@photos_blueprint.route('/', methods=['GET'])
def get_photos():
    #reach out to flickr and get photos
    try:
        flickr.set_keys(api_key='#', api_secret='#')
        photos = flickr.Person.findByUserName("warejc").getPublicPhotos()
        photo_urls = [photo.getPhotoFile(size_label="Medium") for photo in photos]
    except Exception as e:
        return jsonify({'Exception': str(e)})

    return render_template('pages/photos.html', photo_urls=photo_urls)

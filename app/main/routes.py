
from flask import request, render_template, session, flash, redirect, \
    url_for, jsonify, send_from_directory, send_file, Response
from pandas.core.base import NoNewAttributesMixin

from app.models import line, station
from app.data import update_db
from app.main import bp


@bp.route('/update', methods=['GET'])
def update():
    update_db()
    return jsonify("ok")


@bp.route('/lines', methods=['GET'])
def lines():
    data = line.fetch_lines()
    return data

@bp.route('/stations/<int:id>', methods=['GET'])
def stations(id):
    if id == None:
        data = station.fetch_stations()
    else:
        data = station.fetch_stations(id)
    return data

@bp.route('/stations', methods=['GET'])
def stations_all():
    data = station.fetch_stations()
    return data
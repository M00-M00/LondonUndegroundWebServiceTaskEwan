from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin, current_user,login_required
from app import db
#from app import login
from time import time
import jwt




line_station = db.Table('line_station',
    db.Column('station_fid', db.Integer, db.ForeignKey('line.id')),
    db.Column('line_id', db.Integer, db.ForeignKey('station.fid'))
)



class station(db.Model):
    fid = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(128))
    network  = db.Column (db.String(128), default ="LONDON_UNDEGROUND")
    lines = db.relationship("line", secondary= line_station, lazy = 'dynamic',
    back_populates = "stations")


    @staticmethod
    def list_element_to_db(record):
        r = record
        Station  = station(
        fid = r["FID"],
        name  = r["NAME"])
        db.session.add(Station)
        db.session.commit()
        for l in r["LIST_LINES"]:
            Line = line.query.filter_by(name = l).first()
            if Line is not None:
                Station.lines.append(Line)
                db.session.add(Station)
                db.session.commit()
        return Station
    
    

    @staticmethod
    def update_db(data_list):
        objects = [station.list_element_to_db(s) for s in data_list]

        
    @staticmethod
    def fetch_stations(lid = None):
        if lid != None:
            try:
                Line = line.query.filter_by(id = lid).first()
                stations = Line.stations
                total = stations.count()
            except AttributeError:
                return ("Invalid Line ID")
        else:
            stations = station.query.all()
            total = len(stations)
        data = {
             "_meta" : {
                 "total_stations": total,
             },
            'stations': [station.to_json() for station in stations],
             }
        return data


    def to_json(self):
        json_station = {
            "fid" : self.fid,
            "name" : self.name,
            "network": self.network, 
            "line": [v.name for v in self.lines],
            }
        return json_station

    




class line(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(128))
    stations = db.relationship("station", secondary= line_station, lazy = 'dynamic',
    back_populates = "lines")


    def to_json(self):
        json_line = {
            "id" : self.id,
            "name" : self.name,
            "stations": [s.name for s in self.stations],
            }
        return json_line


    @staticmethod
    def update_db(lines):
        for l in lines:
            if line.query.filter_by(name = l).first() == None:
                _line = line(name = l)
                db.session.add(_line)
                db.session.commit()

    @staticmethod
    def fetch_lines():
        lines = line.query.all()
        data = {
             "_meta" : {
                 "total_lines": len(lines),
                 },
            'lines': [line.to_json() for line in lines]
             }
        return data



        """
stations = db.relationship(
        'station', secondary=line_station,
        primaryjoin=(line_station.c.line == id),
        secondaryjoin=(line_station.c.station == id),
        backref=db.backref('lines', lazy='dynamic'))


            stations = db.relationship(
        'station', secondary=line_station,
        primaryjoin=(line_station.c.line_id == id),
        secondaryjoin=(line_station.c.station_fid == station.fid),
        backref=db.backref('lines', lazy='dynamic'))
"""


"""
   lines = db.relationship(
        'station', secondary=line_station,
        primaryjoin=(line_station.c.station_fid == fid),
        secondaryjoin=(line_station.c.line_id == id),
        backref=db.backref('stations', lazy='dynamic'))
""" 
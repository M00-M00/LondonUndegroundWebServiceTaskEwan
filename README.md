# LondonUndegroundWebServiceTaskEwan
Web Services that fetches data for London Undeground stations &amp; lines

In order to run, create python virtual enviroment  (python3 -m venv venv) & activate it (Linux: source venv/bin/active,  Windows venv\Scripts\Activate)

Install dependencies:

pip install -r requirements.txt

set flask app name: 
Linux: export FLASK_APP= main.py
Windows: set FLASK_APP=main.py

Initialise a database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Run the app:
flask run

1) Add data to the database:
.../update (if running locally http://127.0.0.1:5000/update)

Get info for lines:
../lines  (http://127.0.0.1:5000/lines)

Get info for stations:
../stations (http://127.0.0.1:5000/stations)

Get info for stations that belong to a particular line:
../stations/<line_id>   where <line_id> is line ID.


App is written in Python using Flask. Current database is SQLlite (as it is perfect for small projects), ORM for database is SQLAlchemy. 


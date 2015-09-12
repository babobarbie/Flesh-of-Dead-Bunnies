from flask import render_template
from flask_googlemaps import GoogleMaps  
from flask_googlemaps import Map
from app import app

GoogleMaps(app)

@app.route('/')
# @app.route('/index')
def mapview():
	# creating a map in the view
	mymap = Map(
		identifier="view-size",
		lat=37.4419,
		lng=-122.1419,
		markers=[(37.4419,-12.1419)]
		)
	return render_template('map.html',mymap=mymap)
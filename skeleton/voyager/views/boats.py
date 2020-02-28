
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def boats(conn):
    return execute(conn, "SELECT b.bid as Bid, b.name as Name, b.color as Color FROM Boats AS b")

def addBoat(conn):
	boat_name = request.args.get("boat-name")
	boat_color = request.args.get("boat-color")
	print(boat_name)
	print(boat_color)
	if(boat_name is not None and boat_color is not None ):
		if(len(boat_name) > 1 and len(boat_color) > 1 ):
			return execute(conn, "INSERT INTO Boats (name, color) VALUES ( (?), (?) )", (boat_name, boat_color))

def views(bp):
    @bp.route("/boats")
    def _boats():
        with get_db() as conn:
            rows = boats(conn)
        return render_template("table.html", name="Boats", rows=rows)

    @bp.route("/boats/add")
    def _add_Boats():
    	with get_db() as conn:
    		rows = addBoat(conn)
    	return render_template("addBoat.html", name="boats", rows=rows)


from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def who_sailed(conn):
	boat_name = request.args.get("boat-name")
	print(boat_name)
	return execute(conn, "SELECT DISTINCT s.name \
		FROM Sailors As s JOIN Voyages as v on s.sid = v.sid JOIN Boats as b on b.bid = v.bid \
		Where b.name = (?)", (boat_name,))

def views(bp):
    @bp.route("/sailors/who-sailed")
    def _get_all_who_sailed():
        with get_db() as conn:
            rows = who_sailed(conn)
            boat_name = request.args.get("boat-name")
        return render_template("table.html", name="Sailors who sailed " + boat_name, rows=rows)

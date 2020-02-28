from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute



def voyages(conn):
    return execute(conn, "SELECT v.sid as Sid, v.bid as Bid, v.date_of_voyage as Date FROM Voyages AS v")

def addVoyage(conn):
	voyage_sid = request.args.get("voyage-sid")
	voyage_bid = request.args.get("voyage-bid")
	voyage_date = request.args.get("voyage-date")
	print(voyage_sid)
	print(voyage_bid)
	print(voyage_date)
	if(voyage_sid is not None and voyage_bid is not None and voyage_date is not None):
		if(len(voyage_sid) > 0 and len(voyage_bid) > 0 and len(voyage_date) > 4):
			return execute(conn, "INSERT INTO Voyages  (sid, bid, date_of_voyage) \
				VALUES ( (?), (?), (?) )", (voyage_bid, voyage_bid, voyage_date))

def views(bp):
    @bp.route("/voyages")
    def _voyages():
        with get_db() as conn:
            rows = voyages(conn)
        return render_template("table.html", name="Voyages", rows=rows)

    @bp.route("/voyages/add")
    def _add_Voyages():
    	with get_db() as conn:
    		rows = addVoyage(conn)
    	return render_template("addVoyage.html", name="Voyages", rows=rows)

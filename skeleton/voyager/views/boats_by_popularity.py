from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def by_popularity(conn):
    return execute(conn, "SELECT b.bid as Bid, b.name as Name, b.color as Color \
    	FROM Boats AS b JOIN Voyages As v on b.bid = v.bid \
    	 Group By b.bid\
    	 Order by count(*) DESC\
    	")

def views(bp):
    @bp.route("/boats/by-popularity")
    def _by_popularity():
        with get_db() as conn:
            rows = by_popularity(conn)
        return render_template("table.html", name="Most Popular Boats", rows=rows)


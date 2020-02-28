from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def sailed_on_boat_of_color(conn):
    sailor_name = "john"
    color = request.args.get("color")
    print(color)
    return execute(conn, "SELECT DISTINCT s.sid as Sid, s.name as Name \
        FROM Sailors As s JOIN Voyages as v on s.sid = v.sid JOIN Boats as b on b.bid = v.bid \
        Where b.color = (?)", (color,))

def views(bp):
    @bp.route("/sailors/who-sailed-on-boat-of-color")
    def _sailed_on_boat_of_color():
        with get_db() as conn:
            rows = sailed_on_boat_of_color(conn)
            color = request.args.get("color")
        return render_template("table.html", name="Sailors who sailed on "+ color + " boats" , rows=rows)
 

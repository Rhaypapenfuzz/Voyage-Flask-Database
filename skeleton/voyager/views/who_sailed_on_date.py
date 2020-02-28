
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def who_sailed_on_date(conn):
	date = request.args.get("date")
	print(date)
	return execute(conn,  "SELECT DISTINCT s.sid as Sid, s.name as Name \
        FROM Sailors As s JOIN Voyages as v on s.sid = v.sid \
        Where v.date_of_voyage = (?)", (date,))

def views(bp):
    @bp.route("/sailors/who-sailed-on-date")
    def _get_who_sailed_on_date():
        with get_db() as conn:
            rows = who_sailed_on_date(conn)
            date = request.args.get("date")
        return render_template("table.html", name="Sailors who sailed on " + date , rows=rows)


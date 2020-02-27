
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def sailed_by(conn):
	sailor_name = request.args.get("sailor-name")
	print(sailor_name)
	return execute(conn, "SELECT DISTINCT b.bid, b.name, b.color \
		FROM Boats As b JOIN Voyages as v on b.bid = v.bid JOIN Sailors as s on v.sid = s.sid \
		Where s.name = (?)", (sailor_name,))

def views(bp):
    @bp.route("/boats/sailed-by")
    def _get_all_sailed_by():
        with get_db() as conn:
            rows = sailed_by(conn)
            sailor_name = request.args.get("sailor-name")
        return render_template("table.html", name="Boats sailed by "+ sailor_name , rows=rows)
 

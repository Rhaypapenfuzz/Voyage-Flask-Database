from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE


def sailors(conn):
    return execute(conn, "SELECT s.sid as Sid, s.name as Name, s.age as Age, s.experience as Experience\
     FROM Sailors AS s")

def addSailor(conn):
	sailor_name = request.args.get("sailor-name")
	sailor_age = request.args.get("sailor-age")
	sailor_experience = request.args.get("sailor-experience")
	print(sailor_name)
	print(sailor_age)
	print(sailor_experience)
	if(sailor_name is not None and sailor_age is not None and sailor_experience is not None):
		if(len(sailor_name) > 1 and len(sailor_age) > 0 and len(sailor_experience) > 0):
			return execute(conn, "INSERT INTO Sailors (name, age, experience) \
				VALUES ( (?), (?), (?) )", (sailor_name, sailor_age, sailor_experience))

def views(bp):
    @bp.route("/sailors")
    def _get_all_sailors():
        with get_db() as conn:
            rows = sailors(conn)
        return render_template("table.html", name="Sailors", rows=rows)

    @bp.route("/sailors/add")
    def _add_Sailors():
    	with get_db() as conn:
    		rows = addSailor(conn)
    	return render_template("addSailor.html", name="sailors", rows=rows)


from flask import Blueprint

from voyager.views import index
from voyager.views import sailors
from voyager.views import boats
from voyager.views import voyages
from voyager.views import who_sailed
from voyager.views import sailed_by
from voyager.views import sailed_by
from voyager.views import who_sailed_on_date

blueprint = Blueprint('views', __name__)
index.views(blueprint)
sailors.views(blueprint)
boats.views(blueprint)
voyages.views(blueprint)
who_sailed.views(blueprint)
sailed_by.views(blueprint)
who_sailed_on_date.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')


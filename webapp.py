from flask import Flask, request
from flask import jsonify
from sqlite3_database import session, varosok
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

@app.route('/telepulesek')
def locations():
    from shemas import cities_schema
    starts_with = request.args.get("starts", None)
    if starts_with:
        starts_with = starts_with.lower().capitalize()
        q = session.query(varosok).filter(varosok.c.nev.like('{0}%'.format(starts_with))).all()
    else:
        q = session.query(varosok).all()

    result = cities_schema.dump(q)
    return jsonify(result.data)

@app.route('/')
def index():
    return "Hello!"

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app, use_reloader=True)

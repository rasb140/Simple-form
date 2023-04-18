import os

from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
from datetime import date, datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(os.path.join(basedir, 'database.db'))


db = SQLAlchemy(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    @staticmethod
    def age(dob):
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def __repr__(self):
        return f'<User name:{self.name} dob:{self.dob} age:{User.age(self.dob)}>'



swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Simple form"
    },
)

app.register_blueprint(swaggerui_blueprint)


Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/dataentry", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()

        name        = post_data.get('name'),
        dob  = post_data.get('dob')

        print(name)
        print(dob)
        print("age")
        print(calculate_age(datetime.fromisoformat(dob)))
        user_to_add = User(name = name, dob = datetime.fromisoformat(dob))
        db.session.add(user_to_add)
        db.session.commit()

        response_object['age'] = calculate_age(datetime.fromisoformat(dob))
        return jsonify(response_object)

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
from datetime import date, datetime
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

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

        response_object['age'] = calculate_age(datetime.fromisoformat(dob))
        return jsonify(response_object)

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == '__main__':
    app.run(debug=True)

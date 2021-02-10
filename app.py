import os

from flask import Flask
from flask_restful import Api

from mail import mail
from base_resources import SystemInfo
from db import db

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'afdhklsahde7w887e0943849384'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASS')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
api = Api(app)
db.init_app(app)
mail.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(SystemInfo, '/systeminfo')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

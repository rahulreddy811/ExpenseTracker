from flask import Flask, render_template
from models import db
from routes.auth import auth
from routes.expense import exp
from routes.profile import dashboard
from routes.admin import admindash
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///ExpenseTracker.db'   
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    'dev-key'   
)

db.init_app(app)

with app.app_context():
    db.create_all()
    print("database have been created")

app.register_blueprint(auth)
app.register_blueprint(exp)
app.register_blueprint(dashboard)
app.register_blueprint(admindash)


@app.route('/')
def Homepage():
    return render_template('Homepage.html', show_navbar=True)


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8000)
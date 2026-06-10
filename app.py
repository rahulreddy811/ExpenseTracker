from flask import Flask,render_template
from models import db
from routes.auth import auth
from routes.expense import exp
from routes.profile import dashboard
from routes.admin import admindash
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ExpenseTracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'abc123'

db.init_app(app)
with app.app_context():
    db.create_all()
    print("Database has been created")

app.register_blueprint(auth)
app.register_blueprint(exp)
app.register_blueprint(dashboard)
app.register_blueprint(admindash)

@app.route('/')
def Homepage():
    return render_template('Homepage.html')

if  __name__ == "__main__":
    app.run(debug=True,port=8000)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True,  )
    username = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(200), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    role = db.Column(db.String(20),default = "user")
    expense = db.relationship('Expense',backref = 'user', lazy = True, cascade = "all, delete")

class Expense(db.Model):
    __tablename__ = "user_expenses"
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(200),nullable = False)
    category = db.Column(db.String(100),nullable = False)
    amount = db.Column(db.Integer,nullable = False)
    date = db.Column(db.Date,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,SelectField,DateField
from wtforms.validators import data_required,Email,Length
from datetime import date

class Signup(FlaskForm):
    username =  StringField('Username',validators=[data_required(),Length(min=2,max=20)])
    email = StringField('Email',validators=[data_required(),Email()])
    password = PasswordField('Password',validators=[data_required(),Length(min=6)])
    submit = SubmitField("Signup")

class Login(FlaskForm):
    username =  StringField('Username',validators=[data_required(),Length(min=2,max=20)])
    password = PasswordField('Password',validators=[data_required(),Length(min=6)])
    submit = SubmitField("Login")

class Expenses(FlaskForm) :
    expense = StringField('Expense',validators = [data_required()])
    category = SelectField('Category',choices=[ ('food', 'Food'),
        ('travel', 'Travel'),
        ('shopping', 'Shopping'),
        ('bills', 'Bills')])
    amount = IntegerField('Amount',validators = [data_required()])
    date = DateField('Date',default=date.today)
    submit = SubmitField("Add")


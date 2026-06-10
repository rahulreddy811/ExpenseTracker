from flask import render_template,redirect,flash,url_for,session,Blueprint
from models import db,Expense
from forms import Expenses
from utils.decorators import login_required

exp = Blueprint('expense',__name__)

@exp.route('/expense',methods = ['POST','GET'])
@login_required
def set_expense():
    form = Expenses()
    if form.validate_on_submit():
        expense = form.expense.data
        category = form.category.data
        amount = form.amount.data
        date = form.date.data
        user_id = session.get('user_id')

        try:
            exp_obj = Expense(description = expense, category = category, amount = amount, date = date, user_id = user_id)
            db.session.add(exp_obj)
            db.session.commit()
            flash("Expense added")
            return redirect(url_for('expense.set_expense'))
        except Exception as e:
            db.session.rollback()
            flash("Failed to save ,Try again")
            return render_template("mainpage.html",form=form)
    return render_template("mainpage.html",form = form)
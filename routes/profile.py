from flask import Flask,url_for,redirect,Blueprint,render_template,session,flash
from models import db,Expense,User
from utils.decorators import login_required

dashboard = Blueprint("dashboard",__name__)

@dashboard.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    userid  = session.get('user_id')
    user = User.query.get(userid)
    expenses = Expense.query.filter_by(user_id = userid)
    return render_template('profile.html',user = user, expenses = expenses)

@dashboard.route('/delete/<int:id>',methods = ['POST'])
@login_required
def delete_expense(id):
    expense = Expense.query.get(id)
    userid = session.get('user_id')

    if not expense:
        flash("Expense not found")
        return redirect(url_for('dashboard.profile'))
    
    
    if expense.user_id != userid :
        flash("Expense not found")
        return redirect(url_for('dashboard.profile'))
    
    try:
        db.session.delete(expense)
        db.session.commit()
        flash("Expense deleted successfully🎉")
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("Something went wrong")
    
    return redirect(url_for('dashboard.profile'))
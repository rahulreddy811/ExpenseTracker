from flask import Flask,Blueprint,render_template,session,abort,redirect,url_for,flash
from models import db,Expense,User
from utils.decorators import login_required

admindash = Blueprint("admindash",__name__)

@admindash.route('/admindashboard')
@login_required
def admindashboard():
    userid = session.get('user_id')
    user = User.query.get(userid)
    if user.role !=  "Admin":
        abort(403)
    users = User.query.all()
    return render_template('admin_dash.html',users = users)

@admindash.route('/deleteuser/<int:id>',methods = ['POST'])
@login_required
def deleteuser(id):
    user = User.query.get(id)
    if not user:
        flash("User not found", "error")
        return redirect(url_for('admindash.admindashboard'))
    
    if user.role != "user":
        flash("Only normal users can be deleted", "error")
        return redirect(url_for('admindash.admindashboard'))
    try:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted sucessfully","success")
        return redirect(url_for('admindash.admindashboard'))
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("Something went wrong","error")
    return redirect(url_for('admindash.admindashboard'))
   

@admindash.route('/updaterole/<int:id>',methods = ['POST'])
@login_required
def updateuser(id):
    current_user = User.query.get(session.get('user_id'))
    if not current_user or current_user.role.lower() != "admin":
        abort(403)

    user = User.query.get(id)

    if user.role == "Admin":
        flash("Already admin","error")
        return redirect(url_for('admindash.admindashboard'))
    user.role = "Admin"
    db.session.commit()
    flash("User promoted to admin 🎉","success")
    return redirect(url_for('admindash.admindashboard'))


    

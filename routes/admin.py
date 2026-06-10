from flask import Flask,Blueprint,render_template,session,abort
from models import db,Expense,User
from utils.decorators import login_required

admindash = Blueprint("admindash",__name__)

@admindash.route('/admindashboard')
def admindashboard():
    userid = session.get('user_id')
    user = User.query.get(userid)
    if user.role !=  "Admin":
        abort(403)
    users = User.query.all()
    return render_template('admin_dash.html',users = users)

    

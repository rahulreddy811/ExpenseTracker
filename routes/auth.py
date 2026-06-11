from flask import render_template,redirect,flash,url_for,session,Blueprint
from models import db,User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash,generate_password_hash
from forms import Signup,Login

auth = Blueprint("auth",__name__)

@auth.route('/signup',methods=['POST','GET'])
def signup():
    form = Signup()
   
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if len(password) < 6:
            flash("password is small. length atleast 6 ")
            return render_template('signup.html', form=form)
        
        hashed_password = generate_password_hash(password)

        try:
            user_object = User(username = username,email = email,password = hashed_password)
            db.session.add(user_object)
            db.session.commit()
            flash("Signedup successfully🎉","success")
            print(f"user created: {username}")
            return redirect(url_for('auth.login'))
        except IntegrityError as e:
            db.session.rollback()
            error_messages = str(e.orig)

            if "user.email" in error_messages:
                flash("email already exists ☹️,try another email")
            elif "user.username" in error_messages:
                flash("username already exists ☹️,try again","error")
            else:
                flash("Sorry😞,Something went wrong ","error")
    return render_template('signup.html',form = form,show_navbar=False)


@auth.route('/login',methods = ['POST','GET'])
def login():
    form = Login()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username = username).first()

        if not user:
            flash("user does not exist❌","error")
            return render_template('login.html', form=form)
        
        if not check_password_hash(user.password,password):
            flash("Incorrect password try again❌","error")
            return render_template('login.html', form=form)

        session['user_id'] = user.id
        session['user_role'] = user.role
        flash('Login Successful🎉',"success")
        return redirect(url_for('expense.set_expense'))

    return render_template('login.html',form = form,show_navbar=False)

@auth.route('/logout')
def logout():
    session.clear()
    flash("Logout Successfully","success")
    return redirect(url_for('Homepage'))


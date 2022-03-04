from flask_app import app
from flask import render_template, redirect, request, session, request
from flask_app.models import user
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route('/login')
def log_route():
    return render_template('login.html')



# Action Routes
# registration
@app.route('/register', methods=['POST'])
def create():
    if request.form['which_form'] == 'register':
        valid = user.User.validate_register(request.form)
        if not valid:
            return redirect('/')
        else:
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user.User.register(data)
    new_user = user.User.email_check(data)
    session['user_id'] = new_user.id
    flash("You have successfully registered!", "register")
    return redirect('/paintings')
# login


@app.route('/login', methods=['POST'])
def login():
    if request.form['which_form'] == 'login':
        print(request.form)
        data = {
            'email': request.form['email']
        }
        user_in_db = user.User.email_check(data)
        if not user_in_db:
            flash("Invalid Email/Password", "login")
            return redirect('/')
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Invalid Email/Password", "login")
            return redirect('/')
        session['user_id'] = user_in_db.id
        return redirect('/paintings')
# logout


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

from register import app
from flask import render_template, flash
from register.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        return render_template('home.html',form=form)
    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)
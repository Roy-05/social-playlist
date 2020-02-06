
from flask import Flask, render_template, url_for, flash, redirect
from socialPlaylist import app, LoginForm, RegForm  # , db
from flask_login import current_user, login_user
from socialPlaylist.models import User


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegForm()
    # Validate based on data required and parameters listed in RegForm()
    if form.validate_on_submit():
        flash('Thanks for signing up!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():        
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))        
        login_user(user)
        flash('Logged In!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
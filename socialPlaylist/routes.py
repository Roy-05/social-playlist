
from flask import Flask, render_template, url_for, flash, redirect
from socialPlaylist import app #, db



@app.route('/')
def mainPage():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegForm()
    # Validate based on data required and parameters listed in RegForm()
    if form.validate_on_submit():
        flash('Thanks for signing up!', 'success')
        return redirect(url_for('mainPage'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logged In!', 'success')
        return redirect(url_for('mainPage'))
    return render_template('login.html', title='Login', form=form)

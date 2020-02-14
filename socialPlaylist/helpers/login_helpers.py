from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user
from socialPlaylist.models import User, Playlists


def submit_login(form):
    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.check_password(form.password.data):
        flash('Invalid username or password')
        return redirect(url_for('login'))
    login_user(user)
    return redirect(url_for('playlist'))


def show_login_form(form):
    return render_template('login.html', title='Login', form=form)

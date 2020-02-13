from flask import render_template, request, url_for, flash, redirect, request
from socialPlaylist.forms import LoginForm, RegForm, CreatePlaylistForm, AddSongForm
from flask_login import current_user, login_user, logout_user, login_required, user_unauthorized
from socialPlaylist.models import User, Playlists, Song
from socialPlaylist import app, db, login as loginManager

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegForm()
    # Validate based on data required and parameters listed in RegForm()
    if form.validate_on_submit():
        # Instantiate user
        # Add user to session
        # Commit user to database
        usr = User(username=form.username.data, email=form.email.data)
        usr.set_password(form.password.data)  # Password is hashed in User model
        db.session.add(usr)
        db.session.commit()
        flash(f'Thanks for signing up! Account created for {form.username.data}', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('playlist'))
    form = LoginForm()
    if request.method == 'POST':
        return submitLogin(form)
    elif request.method == 'GET':
        return showLoginForm(form)

@app.route('/playlist', methods =['GET', 'POST'])
@login_required
def playlist():
    form = CreatePlaylistForm()
    if(request.method == 'POST'):
        return addNewPlaylist(form)

    return render_template('playlist.html', form=form, user = current_user.username, playlists = getPlaylists())




@app.route('/addsong', methods =['GET', 'POST'])
@login_required
def addsong():
    form = AddSongForm()
    # Validate based on data required and parameters listed in RegForm()
    form.playlist_id.choices = [(p.id, p.playlist_name) for p in Playlists.query.filter_by(user_id=current_user.id)]    
    if form.validate_on_submit():        
        # Instantiate song
        # Add song to session
        # Commit song to database
        song = Song(title=form.title.data, artist_firstname=form.artist_firstname.data, artist_lastname=form.artist_lastname.data)
        # Need to link playlist ID
        # song.playlist_id =
        db.session.add(song)
        db.session.commit()
        flash(f'Song added to playlist!', 'success')
        return redirect(url_for('index'))
    return render_template('addsong.html', title='Add Song', form=form)





def addNewPlaylist(form):
    if form.validate_on_submit():
        playlist = Playlists(
                    username = current_user.username, 
                    playlist_name = form.playlist_name.data,
                    user_id = current_user.id
                    )
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('playlist'))

def getPlaylists():
    return Playlists.query.filter_by(username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@loginManager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('Please login.')
    return redirect(url_for('login'))

def submitLogin(form):
    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.check_password(form.password.data):
        flash('Invalid username or password')
        return redirect(url_for('login'))
    login_user(user)
    #flash('Logged In!', 'success')
    return redirect(url_for('playlist'))


def showLoginForm(form):
    return render_template('login.html', title='Login', form=form)



# These commands will delete all entries from a Model
# db.session.query(Playlists).delete()
# db.session.commit()

import sys
sys.path.append('../')
from flask import render_template, request, url_for, flash, redirect
from socialPlaylist.forms import LoginForm, RegForm, CreatePlaylistForm, AddSongForm
from flask_login import current_user, login_user, logout_user, login_required, user_unauthorized
from socialPlaylist.models import User, Playlists, Song
from socialPlaylist import app, db, login as loginManager
from socialPlaylist.helpers.login_helpers import submit_login, show_login_form
from socialPlaylist.helpers.playlist_helpers import get_playlists, add_new_playlist, get_songs, get_num_of_songs


@app.route('/')
def index():
    return render_template('home.html')

# LOGIN SECTION: SIGN UP , LOGIN , LOGOUT, UNAUTHORIZED


# SIGN UP ROUTE with get and post
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

# Login ROUTE with get and post


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('playlist'))
    form = LoginForm()
    if request.method == 'POST':
        return submit_login(form)
    elif request.method == 'GET':
        return show_login_form(form)


# LOGOUT ROUTE with get and post
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


# PLAYLIST SECTION


# playlist ROUTE
@app.route('/playlist', methods =['GET', 'POST'])
@login_required
def playlist():
    form = CreatePlaylistForm()
    if(request.method == 'POST'):
        return add_new_playlist(form)

    
    return render_template('playlist.html', 
        form=form, 
        user = current_user.username, 
        playlists = get_playlists(), 
        songs = get_num_of_songs())

@app.route('/playlist/<p_id>', methods =['GET', 'POST'])
@login_required
def view_playlist(p_id):
    songs = get_songs(int(p_id))
    return render_template('view_playlist.html', songs=songs)

# add song ROUTE
@app.route('/add_song', methods =['GET', 'POST'])
@login_required
def add_song():
    form = AddSongForm()
    # Validate based on data required and parameters listed in RegForm()
    form.playlist_id.choices = [(p.id, p.playlist_name) for p in Playlists.query.filter_by(user_id=current_user.id)]
    if form.validate_on_submit():
        # Instantiate song
        # Add song to session
        # Commit song to database
        song = Song(title=form.title.data, 
            artist_firstname=form.artist_firstname.data, 
            artist_lastname=form.artist_lastname.data,
            playlist_id = form.playlist_id.data)
            
        db.session.add(song)
        db.session.commit()
        
        return redirect(url_for('playlist'))
    return render_template('add_song.html', title='Add Song', form=form)


# remove song
@app.route('/removesong', methods =['GET', 'POST'])
@login_required
def removeSong():
    playlist = Playlists(username = current_user.username, playlist_name = form.playlist_name.data)
    # song = Song(title=form.title.data, artist_firstname=form.artist_firstname.data, artist_firstname=)
    # get song from playlist
    # db.session.delete()
    # db.session.commit()
    flash('Song successfully removed!')  # maybe have it so that the song title flashes ?
    return redirect(url_for('playlist'))

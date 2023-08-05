"""
The flask app with session.
"""
from flask import session, url_for, Flask, request, redirect

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    """
    Home page.

    :return: index page
    """
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login system.

    :return: go to index if user has login, else require login first.
    """
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    """
    Logout system.

    :return: redirect to index page after logout.
    """
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


app.run()

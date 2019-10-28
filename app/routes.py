"""
Routes are the different URLs that the app implements.
Handlers for the app routes are view functions.
View functions are mapped to one or more route URLs,
so that Flask knows what logic to execute when a client requests a given URL.

When browser requests any route URL,
Flask is going to invoke rott_name() func
And pass the return value back to the browser as a response.
"""
from flask import (
    render_template,
    flash,
    redirect,
    url_for
)

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mikalai'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # validate_on_submit() returns False
    # when browser sends GET request to receive web page with the form.
    # When browser sends the POST request as a result of the user pressing the submit button
    # form.validate_on_submit() is going to gather all the data,
    # run all validators attached to fields, and if everything is ok it will return True
    if form.validate_on_submit():
        # flash() stores the message which are rendered by get_flashed_messages() in template
        flash(f'Login requested for user {form.username.data}, '  # show a message to the user
              f'remember_me={form.remember_me.data}')
        # url_for() generates URLs using its internal mapping of URLs to view functions names
        # redirect() instructs the client web browser to automatically navigate to a different page,
        # given as an argument
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

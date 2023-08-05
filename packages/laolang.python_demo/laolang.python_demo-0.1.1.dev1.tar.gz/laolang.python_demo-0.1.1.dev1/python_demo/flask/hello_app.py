"""
The hello world flask app.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    The home page will display 'Hello, World!'.

    :return: html
    """
    return "<p>Hello, World!</p>"


# run app
app.run()

# or use following script to run flask app in window command:
# set FLASK_APP = hello_app
# set FLASK_ENV = development
# flask run

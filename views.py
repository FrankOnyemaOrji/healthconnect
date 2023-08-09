from flask import Blueprint, render_template
import requests

views = Blueprint('views', __name__)


@views.route('/')
def index():  # put application's code here
    return render_template('index.html')


@views.route('/resource')
def resource():
    # Get the health topics from the MyHealth-finder API
    response = requests.get("https://api.myhealthfinder.gov/v2/topics")
    topics = response.json()

    # Render the HTML template with the health topics
    return render_template("resources.html", topics=topics)

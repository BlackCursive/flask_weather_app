# We are going to run this app in a virtual environment.  The virtual environment that I use is pipenv because under
# the hood it is PIP a python package manager and VIRTUALENV a tools that creates isolated Python environments.
# In order to install pipenv we are going to open up a terminal and run
#  *BULLET* - pip install pipenv
# or if you have Homebrew you can run
# *BULLET* - brew install pipenv
# When you are done installing create the directory - weather_app and cd into it then run
# * BULLET * - pipenv shell - in order to create a virtual environment

# Environment Variables
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

# Flask is a micro web framework which is lightweight and simple to get up and running
# as opposed to something like Django which is a full-stack web framework.  Although Flask
# can be used for large full fledged products it excels at small single page applications.

# Import Flask Class
from flask import Flask, render_template, request, url_for
# Import OS library
import os
# Import requests HTTP library
import requests
# Convert Unix Timestamp
from datetime import datetime
# Create an instance of the class
app = Flask(__name__)

# Retreive API Key from an environment variable - You can simply leave your API Key in the file
# while your developing or testing but before you share your code you may want to hide it.
api_key = os.environ.get('OpenWeatherAPI')

# Route is a decorator which tells Flask which URL the function goes to


@app.route('/', methods=['GET', 'POST'])
# Create a function and name it whatever you feel is appropriate
def home():
    # Test this app out.
    # return('Hello World')
    if request.method == 'POST':
        city = request.form.get('city')
        # We are going to use the .get() Method to access the dictionary’s value instead
        # of bracket notation.  This can be a String or a variable. This method return
        # the value for key and if the key is not in the dictionary then it return None
        # which is great because this method never raises a KeyError.
    else:
        city = 'New York'
        # Default city is New York.
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    full_url = base_url + city + "&units=imperial&APPID=" + api_key
    response = requests.get(full_url)
    api = response.json()

    #  We can create a custom filter for Jinja but for the sake of simplicity I will do it this way.
    dt = datetime.now()
    date = dt.strftime("%A, %b %d")

    # Using the RENDER_TEMPLATE method we can have Python return an HTML file and
    # any variables as # well we just have to pass them as keyword arguments
    return render_template('index.html', api=api, date=date)


# Doing this we get two main things the ability to update the code and refresh the html page without
# restarting the server and also we get an interactive debugger which will help us locate errors
if __name__ == '__main__':
    app.run(debug=True)

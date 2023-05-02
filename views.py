## define Blueprint to put routes in 
from flask import Blueprint, render_template

## routes are the endpoints of the URL
views = Blueprint(__name__, "views")


## defining html routes
@views.route("/")
def home():
      return render_template("index.html")

@views.route("/about")
def about():
      return render_template("about.html")
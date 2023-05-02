## import Flask

from flask import Flask

## import views variable from views file

from views import views

## initialize the application

app = Flask(__name__)

## add views
app.register_blueprint(views, url_prefix = "/")

## run app 

if __name__ == '__main__':
    app.run(debug = True)
    
import os
base_dir = os.path.dirname(os.path.realpath(__file__))

from flask import Flask
#from flask.ext.login import LoginManager
#from flask.ext.openid import OpenID
#from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

#lm = LoginManager()
#lm.init_app(app)
#oid = OpenID(app, os.path.join(base_dir, 'tmp'))
#db = MongoEngine(app)

from app import views
#from app import models

if __name__ == '__main__':
    app.run()
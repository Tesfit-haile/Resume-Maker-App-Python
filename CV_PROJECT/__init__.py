import os
import flask
import flask_login
import flask_migrate
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(os.path.dirname(__file__), 'cv.db')
app.config['SECRET_KEY'] = 'THISISMYSECTERKEY'
db = SQLAlchemy(app)

migrate = flask_migrate.Migrate(app, db)
login_mng = flask_login.LoginManager(app)



# this will help you in case your flask db migrate does not work/ but u can delete it if u want
with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

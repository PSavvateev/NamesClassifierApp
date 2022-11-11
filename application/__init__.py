from flask import Flask
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# ccsrf = CSRFProtect(app)

# Setting up configuration
app.config.from_object('application.config.Config')


# Import routing and Start the App
from application import views
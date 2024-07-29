from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Import views and models
from app import views
from app.models import Admin, Sponsor, Influencer  # Import specific user models

@login_manager.user_loader
def load_user(user_id):
    # Retrieve the user role from the session
    role = session.get('role')  # Default to influencer if not set

    if role == 'admin':
        return Admin.query.get(int(user_id))
    elif role == 'sponsor':
        return Sponsor.query.get(int(user_id))
    elif role == 'influencer':
        return Influencer.query.get(int(user_id))
    else:
        return None

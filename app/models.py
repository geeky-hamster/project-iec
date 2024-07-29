from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id) 


class Sponsor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Ensure this line exists
    company_name = db.Column(db.String(150), nullable=False)  # Example field
    website_url = db.Column(db.String(255), nullable=True)  # Example field
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)  # Return the user ID as a string


class Influencer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    platforms = db.Column(db.String(255), nullable=True)  # Comma-separated platforms
    collaboration_type = db.Column(db.String(50), nullable=True)
    availability = db.Column(db.String(50), nullable=True)
    website_url = db.Column(db.String(255), nullable=True)
    preferred_brands = db.Column(db.Text, nullable=True)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(50), default='influencer')  # Add this line
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id) 



class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    budget = db.Column(db.Float)
    visibility = db.Column(db.String(50))  # 'public', 'private'

class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'), nullable=False)  # Corrected reference
    messages = db.Column(db.Text)
    requirements = db.Column(db.Text)
    payment_amount = db.Column(db.Float)
    status = db.Column(db.String(50))  # 'Pending', 'Accepted', 'Rejected'




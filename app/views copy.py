from flask import render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app import app, db
from app.models import Admin, Sponsor, Influencer, Campaign, AdRequest


@app.route('/')
def welcome():
    return render_template('welcome.html')

'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Use the check_password method
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Failed. Check username and password.')

    return render_template('auth/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))

        # Create a new user
        new_user = User(username=username, role=role)
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('auth/register.html')
'''
@app.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Admin.query.filter_by(username=username, role='admin').first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))  # Redirect to the general dashboard
        else:
            flash('Login Failed. Check username and password.')

    return render_template('auth/admin_login.html')


@app.route('/login/influencer', methods=['GET', 'POST'])
def influencer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Influencer.query.filter_by(username=username, role='influencer').first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))  # Redirect to the general dashboard
        else:
            flash('Login Failed. Check username and password.')

    return render_template('auth/influencer_login.html')


@app.route('/login/sponsor', methods=['GET', 'POST'])
def sponsor_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Sponsor.query.filter_by(username=username, role='sponsor').first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))  # Redirect to the general dashboard
        else:
            flash('Login Failed. Check username and password.')

    return render_template('auth/sponsor_login.html')


@app.route('/register/admin', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = 'admin'  # Set role as admin

        existing_user = Admin.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('admin_register'))

        # Create a new user
        new_user = Admin(username=username, role=role)
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('admin_login'))

    return render_template('auth/admin_register.html')


@app.route('/register/influencer', methods=['GET', 'POST'])
def influencer_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phone_number']
        bio = request.form['bio']
        
        # Get selected platforms
        platforms = request.form.getlist('platforms')  # List of selected platforms
        
        # New fields
        gender = request.form['gender']
        collaboration_type = request.form['collaboration_type']  # Single selection
        availability = request.form['availability']  # Single selection
        website_url = request.form.get('website_url', '')  # Optional
        preferred_brands = request.form['preferred_brands']
        
        # Location and Age
        country = request.form['country']
        state = request.form['state']
        region = request.form['region']
        age = request.form['age']
        role = 'influencer'

        existing_user = Influencer.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('influencer_register'))

        # Create a new user
        new_user = Influencer(
            username=username, role=role, email=email, phone_number=phone_number,
            bio=bio, gender=gender, 
            platforms=','.join(platforms),  # Store as comma-separated string
            collaboration_type=collaboration_type,
            availability=availability, website_url=website_url,
            preferred_brands=preferred_brands, country=country, state=state, region=region, age=age
        )
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('influencer_login'))

    return render_template('auth/influencer_register.html')


@app.route('/register/sponsor', methods=['GET', 'POST'])
def sponsor_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = 'sponsor'  # Set role as sponsor

        existing_user = Sponsor.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('sponsor_register'))

        # Create a new user
        new_user = Sponsor(username=username, role=role)
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('sponsor_login'))

    return render_template('auth/sponsor_register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return render_template('admin/dashboard.html')  # Admin dashboard
    elif current_user.role == 'sponsor':
        return render_template('sponsor/dashboard.html')  # Sponsor dashboard
    elif current_user.role == 'influencer':
        return render_template('influencer/dashboard.html')  # Influencer dashboard
    else:
        flash('User role is not recognized.')
        return redirect(url_for('welcome'))  # Redirect to welcome if role is not recognized
    

@app.route('/create_campaign', methods=['GET', 'POST'])
@login_required
def create_campaign():
    if current_user.role != 'sponsor':
        flash('You do not have permission to access this page.')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        budget = request.form['budget']
        visibility = request.form['visibility']
        new_campaign = Campaign(name=name, description=description, budget=budget, visibility=visibility)
        db.session.add(new_campaign)
        db.session.commit()
        flash('Campaign created successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('sponsor/create_campaign.html')

@app.route('/search_campaigns', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in before accessing this route
def search_campaigns():
    if request.method == 'POST':
        # Implement your search logic here
        search_query = request.form.get('search_query')
        # Example: Fetch campaigns based on the search query
        campaigns = Campaign.query.filter(Campaign.name.contains(search_query)).all()
        return render_template('influencer/search_results.html', campaigns=campaigns)

    return render_template('influencer/search_campaign.html')  # Render a search form

@app.route('/logout')
@login_required  # Ensure the user is logged in before they can log out
def logout():
    logout_user()  # Log out the user
    flash('You have been logged out successfully.')  # Flash a message
    return redirect(url_for('welcome'))  # Redirect to the welcome page or login page

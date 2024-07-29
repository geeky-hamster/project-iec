# init_db.py

from app import db, app

def init_db():
    with app.app_context():  # Set up the application context
        db.drop_all()  # Drop all existing tables
        db.create_all()  # Create new tables
        print("Database initialized and tables created.")

if __name__ == '__main__':
    init_db()
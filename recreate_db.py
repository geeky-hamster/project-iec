import os
from app import app, db

def recreate_database():
    # Delete the existing database file
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].split('///')[1]
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Database deleted successfully.")
    
    # Create the database tables based on the models
    with app.app_context():
        db.create_all()
        print("Database recreated successfully.")

if __name__ == '__main__':
    recreate_database()

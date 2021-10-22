import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Gives Flask access to relative filepath regardless of OS.
# Allows outside files/folders to be imported as well
# can consider this a 'roadmap' we're giving flask for our operating system

class Config:
    """
    Sets the configuration variables for our Flask app
    Eventually we will use hidden variable items, but for now we'll leave them exposed.
    """
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ^ Decreases unnecessary output in terminal as we use the database
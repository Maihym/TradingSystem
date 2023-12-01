#config.py
import os

class Config:
    # Database configuration
    DB_USERNAME = 'tradingsystem'
    DB_PASSWORD = 'Vg*K(Wpj5Fk-5*F4'
    DB_HOST = 'localhost'
    DB_NAME = 'tradingsystem'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xc9n\x01e\x15\xa7\xae~\xb6\x1da\x91\xd8\x85f\xbf\xbe\xacMT\xba\xb9@'

    #Other Settings
    ENABLE_REGISTRATION = True  # Set to False to disable registration

class BaseConfig(object):
    # Base config
    SECRET_KEY = 'random+key'
    DEBUG = True
    TESTING = False
    
    # More base variable config here...
    
    # SQL ALCHEMY CONFIGURATIONS
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    # SECRET_KEY = open('secret_key_directory').read()

class StagingConfig(BaseConfig):
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'random+key'

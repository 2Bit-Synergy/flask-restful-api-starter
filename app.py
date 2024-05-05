from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions, HTTPException

import config

app = Flask(__name__, static_folder="/static")

@app.errorhandler(Exception)
def handle_error(e):
    # Internal server error
    code = 500
    
    if isinstance(e, HTTPException):
        code = e.code
        
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)
    
# Set config
app.config['SQLALCHEMY_DATABASE_URI'] = config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = config.DevelopmentConfig.BUNDLE_ERRORS

db = SQLAlchemy(app)
api = Api(app)

# ex: api or api/v1 or api/v2
api.prefix = '/api' # Prefix for all routes

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

from config import config

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
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = config.BUNDLE_ERRORS

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

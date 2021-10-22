from functools import wraps
import secrets
from .models import User
from flask import request, jsonify

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token Missing!'}), 401
        
        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(token)
        
        except:
            owner = User.query.filter_by(token = token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Invalid Token! Try again.'})

        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

import decimal
from flask import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # convert any decimal values into strings to allow data to be passed through
        # and api call
        if isinstance(obj, decimal.Decimal):
            # convert it into a string
            return str(obj)
        return super(JSONEncoder, self).default(obj)



# 79f8d1b8454a8ee1ae78afb4a9cb957a5cbe1fafefd2fc85
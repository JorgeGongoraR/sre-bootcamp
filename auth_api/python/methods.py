# These functions need to be implemented
from flask.globals import request
from flask.json import jsonify

class login:

    # Generar el token
    def generate_token(self, username, password):
        token = request.args.post(username,password)
        print(token)
        if not token:
            return jsonify({'message': 'missing token'}), 403
        return token


class Restricted:

    def access_data(self, authorization):
        return 'test'

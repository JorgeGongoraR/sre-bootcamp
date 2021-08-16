from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from methods import login, Restricted
import hashlib
import jwt

app = Flask(__name__)
login = login()
protected = Restricted()


# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form['username']
    password = request.form['password']
    seed = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"
    if username == "admin":
      salt = "F^S%QljSfV"
      role = "admin"
    if username == "noadmin":
        salt = "KjvFUC#K*i"
        role = "editor"
    if username == "bob":
        salt = "F^S%QljSfV"
        role = "viewer"
    salted_password = password + salt
    hashed_PWD = hashlib.sha512( str( salted_password ).encode("utf-8") ).hexdigest()
    encoded_jwt = jwt.encode({role: role}, seed, algorithm="HS256")

    print(encoded_jwt)
    res = {
        "data": encoded_jwt
    }
    return jsonify(res)


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')
    word_list = auth_token.split()
    token = word_list[1]
    seed = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"
    payload =jwt.decode(token, seed, algorithms=["HS256"])

    if payload.get('role') != 'admin':
        abort(401, description="You don't have access")

    res = {
        "data": "You are under protected data"
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

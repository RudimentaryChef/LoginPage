from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
#Starting up flask
app = Flask(__name__)
app.secret_key = "my_super_secret_key_1234!@#$%^"

#Sample user base
users = {
    "adi": generate_password_hash("potato"),
    "rish": generate_password_hash("mayfirst")
}
@app.route("/login", methods=["POST"])
def login():
    """
    Login route post method
    :return: Json Message, StatusCode
    """
    #If the request method is post then
    if request.method == "POST":
        #gets the username from the request
        username, password, errorMessage = get_user_password_from_form()
        if errorMessage:
            return jsonify({"message": "Bad Request: {}".format(errorMessage)}), 400
    #Checks username and password against the "database"
        return check_user_password(username, password)
    else:
        return jsonify({"message": "request method must me POST. It was {}".format(request.method)}), 400

def get_user_password_from_form():
    """
    Get username and password from the request form.
    """
    success = False
    try:

        username = request.form.get("username")
        password = request.form.get("password")
        if username == None or password == None:
            raise Exception("Username or password not provided in the request form.")
        return username, password, None
    except Exception as e:
        print(e)
        username = request.form.get("username")
        password = request.form.get("password")
        return username, password, e

def check_user_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return jsonify({"message": "Welcome {} Login successful".format(username)}), 200
    else:
        print("hi")
        print(username)
        print(password)
        return jsonify({"message": "Invalid username or password"}), 401
@app.route("/register", methods=["POST"])
def register():
    """
    Register route post method
    :return: Json Message, Status code
    """
    if request.method == "POST":
        username, password, errorMessage = get_user_password_from_form()
        if(errorMessage):
            return jsonify({"message": "Bad Request: {}".format(errorMessage)}), 400
        return registration_validator(username,password)
    else:
        return jsonify({"message": "request method must me POST. It was {}".format(request.method)}), 400
def registration_validator(username, password):
    if username in users:
        return jsonify({"message": "Username already exists. Please choose a different username."}), 409
    else:
        users[username] = generate_password_hash(password)
        return jsonify({"message": "Registered user sucessfully!"}), 201
if __name__ == "__main__":
    #Note: Debug mode is True while developing. Need to turn it off in production.
    app.run(debug=True)

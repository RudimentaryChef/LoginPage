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
    print(request)
    try:
        #If the request method is post then
        if request.method == "POST":
            #gets the username from the request
            content_type = request.content_type
            username, password, errorMessage = get_data_with_content_type(content_type)
            #Throw an exception for invalid content_type for request
            if errorMessage:
                return jsonify({"message": "Bad Request: {}".format(errorMessage)}), 400
        #Checks username and password against the "database"
            return check_user_password(username, password)
        else:
            return jsonify({"message": "request method must me POST. It was {}".format(request.method)}), 400
    except Exception as e:
        return jsonify({"other error message": str(e)}), 400
def get_data_with_content_type(content_type):
    if content_type == "application/json":
        username, password, errorMessage = get_user_password_from_raw()
    elif "form" in content_type:
        username, password, errorMessage = get_user_password_from_form()
    else:
        raise Exception("Unknown content type")
    return username, password, errorMessage

def get_user_password_from_form():
    """
    Get username and password from the request form.
    """

    try:
        username = request.form.get("username")
        password = request.form.get("password")
        if username == None or password == None:
            raise Exception("Username or password not provided in the request form.")
        return username, password, None
    except Exception as e:
        username = request.form.get("username")
        password = request.form.get("password")
        return username, password, e
def get_user_password_from_raw():
    """
    Get username and password from the raw jspm
    """
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if username == None or password == None:
            raise Exception("Username or password not provided in the request form.")
        return username, password, None
    except Exception as e:
        username = data.get("username")
        password = data.get("password")
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
        content_type = request.content_type
        username, password, errorMessage = get_data_with_content_type(content_type)
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
    #app.run(debug=True)
    #app.run(host = '0.0.0.0', port = 5001, debug = True)
    app.run(port=8000, debug=True)

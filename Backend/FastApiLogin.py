from fastapi import FastAPI, Form, HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

app = FastAPI()

# Sample user base
users = {
    "adi": generate_password_hash("potato"),
    "rish": generate_password_hash("mayfirst")
}

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    """
    Login route post method
    :return: Json Message, StatusCode
    """
    try:
        if username in users and check_password_hash(users[username], password):
            return {"message": f"Welcome {username}! Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    """
    Register route post method
    :return: Json Message, Status code
    """
    if username in users:
        raise HTTPException(status_code=409, detail="Username already exists. Please choose a different username.")
    else:
        users[username] = generate_password_hash(password)
        return {"message": "Registration successful"}

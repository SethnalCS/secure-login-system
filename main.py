import json
from auth import hash_password, verify_password

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def register(username, password):
    users = load_users()
    if username in users:
        print("User already exsists.")
        return
    
    hashed = hash_password(password)
    users[username] = hashed.decode()
    save_users(users)
    print("User registered securely.")

def login(username, password):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    
    if verify_password(password, users[username].encode()):
        print("Login Successful.")
    else:
        print("Invalid Password.")

choice = input("Register (r) or Login (l): ").lower()
username = input("Username: ")
password = input("Password: ")

if choice == "r":
    register(username, password)
elif choice == "l":
    login(username, password)
else:
    print("Invalid choice.")
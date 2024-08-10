import json
import uuid
import os

# Global variable to store the logged-in user's email
logged_in_user_email = None
file_path = os.path.join(os.path.dirname(__file__), 'fake_data/dados.json')


def check_user(email, password):
    try:
        with open(file_path, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        return None

    for user in users:
        if 'email' in user and 'password' in user:
            if user['email'] == email and user['password'] == password:
                print(f"Logged-in user: {logged_in_user_email}")  # Check if it's being updated
                return user

    return False

def check_registration(email, phone):
    try:
        with open(file_path, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        return None

    for user in users:
        if user['email'] == email or user['phone'] == phone:
            return user

    return None

def create_user(name, email, phone, password):
    user_id = str(uuid.uuid4())
    new_user = {
        'name': name,
        'phone': phone,
        'email': email,
        'password': password,
        'user_id': user_id
    }

    try:
        with open(file_path, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    for user in users:
        if 'email' in user and 'phone' in user:
            if user['email'] == new_user['email'] or user['phone'] == new_user['phone']:
                return False, None

    users.append(new_user)

    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)
        
    return True, new_user

def find_user():
    global logged_in_user_email
    print(f"Email being searched: {logged_in_user_email}")  # Debugging

    if logged_in_user_email is None:
        return None

    try:
        with open(file_path, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        return "User not found"

    for user in users:
        if user['email'] == logged_in_user_email:
            return user['name']

    return None

def display_name():
    return find_user()

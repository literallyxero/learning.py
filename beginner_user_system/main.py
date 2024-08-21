from pathlib import Path
import json

def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def new_user(path):
    username = input("What is your username?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.txt')
    username = get_stored_user(path)
    if username:
        print(f"Welcome back {username}")
    else:
        username = new_user(path)
        print(f"We'll remember you {username}")

greet_user()

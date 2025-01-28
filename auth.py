import json
import secrets
from datetime import datetime, timedelta


def authenticate(username, password):
    with open('users.json', 'r') as file:
        data = json.load(file)

    if username in data and data[username]["password"] == password:
        token = secrets.token_hex(16)
        expire_time = datetime.now() + timedelta(minutes=30)  # define o tempo de validade do token para 30 minutos
        data[username]["token"] = token
        data[username]["expire_time"] = expire_time.strftime("%Y-%m-%d %H:%M:%S")
        with open('users.json', 'w') as file:
            json.dump(data, file)
        return token
    else:
        return None


def validate_token(username, token):
    with open('users.json', 'r') as file:
        data = json.load(file)

    if username in data and data[username]["token"] == token:
        expire_time_str = data[username]["expire_time"]
        expire_time = datetime.strptime(expire_time_str, "%Y-%m-%d %H:%M:%S")
        if expire_time > datetime.now():
            return True
        else:
            return False
    else:
        return False


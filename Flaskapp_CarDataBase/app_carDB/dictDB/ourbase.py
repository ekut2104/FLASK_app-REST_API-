import json


def get_db():
    with open('app_carDB/dictDB/ourbase.json', 'r') as db:
        data = json.load(db)
    return data


def rewrite_db(data: list):
    with open('app_carDB/dictDB/ourbase.json', 'w') as db:
        json.dump(data, db)


def get_users_db():
    with open('app_carDB/dictDB/users.json', 'r') as db:
        data = json.load(db)
        return data


def rewrite_users_db(data: list):
    with open('app_carDB/dictDB/users.json', 'w') as db:
        json.dump(data, db)
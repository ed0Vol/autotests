import requests
import config
import data


def post_new_user():
    url = config.BASE_URL + config.signup
    return requests.post(url, json=data.user_data, headers=data.headers)


def auth():
    url = config.BASE_URL + config.signin
    new_data = data.user_data.copy()
    del new_data['name']
    return requests.post(url, json=new_data, headers=data.headers)


def post_todo(token, todo_name):
    url = config.BASE_URL + config.todo
    body = {
        "description": todo_name
    }
    new_headers = data.headers.copy()
    new_headers['Authorization'] = f'Bearer {token}'
    return requests.post(url, json=body, headers=new_headers)



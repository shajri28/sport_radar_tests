import requests

baseUrl = "https://reqres.in/"


def get_user(user_id):
    path = f"api/users/{user_id}"
    response = requests.get(url=f"{baseUrl}{path}")
    return response


def get_all_user_paged(page):
    path = f"api/users/?page={page}"
    response = requests.get(url=f"{baseUrl}{path}")
    return response


def get_all_user_delayed(delay):
    path = f"api/users/?delay={delay}"
    response = requests.get(url=f"{baseUrl}{path}")
    return response


def get_api_unknown(data):
    path = f"api/unknown/{data}"
    response = requests.get(url=f"{baseUrl}{path}")
    return response


def create_user(user_data):
    path = "api/users"
    response = requests.post(url=f"{baseUrl}{path}", json=user_data)
    return response


def update_user_fully(user_id, user_data):
    path = f"api/users/{user_id}"
    response = requests.put(url=f"{baseUrl}{path}", json=user_data)
    return response


def update_user_partially(user_id, user_data):
    path = f"api/users/{user_id}"
    response = requests.patch(url=f"{baseUrl}{path}", json=user_data)
    return response


def delete_user(user_id):
    path = f"api/users/{user_id}"
    response = requests.delete(url=f"{baseUrl}{path}")
    return response

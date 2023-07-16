import requests

baseUrl = "https://reqres.in/"


def post_successful_login(user_data):
    path = f"api/login"
    response = requests.post(url=f"{baseUrl}{path}", json=user_data)
    return response

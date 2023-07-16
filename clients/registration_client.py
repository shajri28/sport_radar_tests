import requests

baseUrl = "https://reqres.in/"


def post_successful_registration(user_data):
    path = f"api/register"
    response = requests.post(url=f"{baseUrl}{path}", json=user_data)
    return response

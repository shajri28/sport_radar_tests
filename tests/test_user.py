import json
import pytest
from clients import user_client
from schemas.schemas import userSchema, updatedUserSchema
from utils.helpers import validateJson
import logging

with open("../testdata/users.json", 'r') as json_file:
    user_list = json.load(json_file)

with open("../testdata/fully_updated_users.json", 'r') as json_file:
    fully_updated_user_list = json.load(json_file)

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize("user", user_list)
def test_create_user(user):
    LOGGER.info('create a user test started')
    response = user_client.create_user(user)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    is_valid = validateJson(response_json, userSchema)
    assert is_valid
    assert response_json['name'] == user['name']
    assert response_json['job'] == user['job']
    LOGGER.info('End of create a user Test')
    print(response_json)


@pytest.mark.parametrize("user", user_list)
def test_create_full_update(user):
    LOGGER.info('Create a new user')
    response = user_client.create_user(user)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    user_id = response_json['id']
    LOGGER.info('user id is', user_id)
    LOGGER.info('Update the user')
    response = user_client.update_user_fully(user_id, user)
    assert response.status_code == 200
    response_json_updated = json.loads(response.text)
    is_valid = validateJson(response_json_updated, updatedUserSchema)
    assert is_valid
    LOGGER.info('End of fully update user Test')


@pytest.mark.parametrize("user", user_list)
def test_create_partial_update(user):
    LOGGER.info('Create a user')
    response = user_client.create_user(user)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    user_id = response_json['id']
    LOGGER.info('user id is', user_id)
    LOGGER.info('Partially update the user')
    response = user_client.update_user_partially(user_id, user)
    assert response.status_code == 200
    response_json_updated = json.loads(response.text)
    is_valid = validateJson(response_json_updated, updatedUserSchema)
    assert is_valid
    LOGGER.info('End of partially update user Test')


@pytest.mark.parametrize("user", user_list)
def test_delete_user(user):
    LOGGER.info('Create a user')
    response = user_client.create_user(user)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    user_id = response_json['id']
    LOGGER.info('user id is', user_id)
    LOGGER.info('Delete the user')
    response = user_client.delete_user(user_id)
    assert response.status_code == 204
    LOGGER.info('End of delete User Test')


def test_get_all_users_paged():
    LOGGER.info('get all user paged Test started')
    response = user_client.get_all_user_paged(2)
    response_json = json.loads(response.text)
    assert response.status_code == 200
    data = response_json['data']
    # check that the returned users number per page is 6
    assert len(data) == 6
    LOGGER.info('End of get all user paged Test')


def test_get_users_per_page_delayed():
    LOGGER.info('get users delayed started')
    response = user_client.get_all_user_delayed(3)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 4
    LOGGER.info('End of get users delayed Test')


def test_get_only_user():
    LOGGER.info('get only user Test started')
    response = user_client.get_user(2)
    response_json = json.loads(response.text)
    assert response.status_code == 200
    assert response_json['data']['first_name'] == 'Janet'
    assert response_json['data']['last_name'] == 'Weaver'
    assert response_json['data']['avatar'] == 'https://reqres.in/img/faces/2-image.jpg'
    LOGGER.info('End of get only user Test')


def test_get_single_user_not_found():
    LOGGER.info('get single user not found Test started')
    response = user_client.get_user(456)
    assert response.status_code == 404
    LOGGER.info('End of get single user not found Test')


def test_get_api_single_unknown():
    LOGGER.info('get api unknown Test started')
    response = user_client.get_api_unknown(2)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert response_json['data']['name'] == 'fuchsia rose'
    assert response_json['data']['year'] == 2001
    assert response_json['data']['color'] == '#C74375'
    assert response_json['data']['pantone_value'] == '17-2031'
    LOGGER.info('End of get api unknown Test')


def test_get_api_single_only_unknown_not_found():
    LOGGER.info('get api single only unknown not found Test started')
    response = user_client.get_api_unknown(34)
    assert response.status_code == 404
    LOGGER.info('End of get api single only unknown not found Test')

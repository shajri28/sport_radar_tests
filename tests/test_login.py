import logging
import json
from clients import registration_client, login_client
from utils.helpers import generate_password

LOGGER = logging.getLogger(__name__)


def test_successful_login():
    LOGGER.info('Successful login Test started')
    response = login_client.post_successful_login(
        json.loads('{"email": "eve.holt@reqres.in","password": "' + generate_password(5) + '"}'))

    response_json = json.loads(response.text)
    assert response.status_code == 200
    assert type(response_json['token']) == str

    LOGGER.info('End of the successful login Test')


def test_unsuccessful_login():
    LOGGER.info('Unsuccessful login Test started')
    response = registration_client.post_successful_registration(
        json.loads('{"email": "eve.holt@reqres.in"}'))

    response_json = json.loads(response.text)
    assert response.status_code == 400
    assert response_json['error'] == 'Missing password'

    LOGGER.info('End of the unsuccessful login Test')

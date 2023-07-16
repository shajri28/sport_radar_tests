import logging
import json
from clients import registration_client
from utils.helpers import generate_password

LOGGER = logging.getLogger(__name__)


def test_successful_registration():
    LOGGER.info('Successful registration Test started')
    response = registration_client.post_successful_registration(
        json.loads('{"email": "eve.holt@reqres.in","password": "' + generate_password(5) + '"}'))

    response_json = json.loads(response.text)
    assert response.status_code == 200
    assert type(response_json['token']) == str

    LOGGER.info('End of the successful registration Test')


def test_unsuccessful_registration():
    LOGGER.info('Unsuccessful registration Test started')
    response = registration_client.post_successful_registration(
        json.loads('{"email": "eve.holt@reqres.in"}'))

    response_json = json.loads(response.text)
    assert response.status_code == 400
    assert response_json['error'] == 'Missing password'

    LOGGER.info('End of the unsuccessful registration Test')


def test_registration_with_undefined_user():
    LOGGER.info('registration with non defined user Test started')
    response = registration_client.post_successful_registration(
        json.loads('{"email": "sab@reqres.in","password": "' + generate_password(5) + '"}'))

    response_json = json.loads(response.text)
    assert response.status_code == 400
    assert response_json['error'] == 'Note: Only defined users succeed registration'

    LOGGER.info('End of the registration with non defined user Test')

"""Cloud Provider Network Interface"""

###########
# Imports #
###########
import os
import json
import requests

from .exceptions import NotAuthorized, NotFound, InternalError, InvalidRequest
from .constants import(BASE_URL, HTTP_OK, HTTP_CREATED, HTTP_DELETE,
    HTTP_NOT_AUTHORIZED, HTTP_NOT_FOUND, HTTP_TOO_MANY_REQUESTS,
    HTTP_INTERNAL_ERROR, HTTP_UNPROCESSABLE_ENTITY)

def send_request(action, url, data=None):
    """Send HTTP(S) Request and process return.

        Args:
            action (str) - HTTP action.
            url (str) - URL to send the request to.
            data (dict, optional) - Arguments to pass in the body of the request.

        Return:
            json (dict) - Returned data in a JSON format.

        Raises:
            ValueError - Invalid HTTP action
            NotAuthorized - Request not authorized
            NotFound - Object not found
            TooManyRequests - Rate limit reached
            InternalError - Internal server error
            InvalidRequest - Invalid request.
    """

    #
    # Read token from the env
    token = os.getenv('DO_TOKEN')

    headers = {
        'Content-type': 'application/json',
        'Authorization': f"Bearer {token}"
    }

    url = f"{BASE_URL}{url}"

    if action == 'GET':
        ret = requests.get(url, headers=headers)
        #XXX need to handle pagination
        if ret.status_code != HTTP_OK:
            process_error(ret.status_code, ret.json()['message'])
        return ret.json()

    elif action == 'POST':
        ret = requests.post(url, data=json.dumps(data), headers=headers)
        if ret.status_code != HTTP_CREATED:
            process_error(ret.status_code, ret.json()['message'])
        return ret.json()

    elif action == 'PUT':
        #XXX
        pass

    elif action == 'PATCH':
        #XXX
        pass

    elif action == 'DELETE':
        ret = requests.delete(url, headers=headers)
        if ret.status_code != HTTP_DELETE:
            process_error(ret.status_code, ret.json()['message'])
        return {}

    else:
        raise ValueError("Unexpected REST Action")

def process_error(status_code, msg):
    """Process Error when a non successful status code is returned

        Args:
            status_code (init): HTTP Status Code
            msg (str): Error message returned by the server

        Raises:
            NotAuthorized - Request not authorized
            NotFound - Object not found
            TooManyRequests - Rate limit reached
            InternalError - Internal server error
            InvalidRequest - Invalid request.
    """
    if status_code == HTTP_NOT_AUTHORIZED:
        raise NotAuthorized
    elif status_code == HTTP_NOT_FOUND:
        raise NotFound
    elif status_code == HTTP_TOO_MANY_REQUESTS:
        pass #XXX fill me out
    elif status_code == HTTP_INTERNAL_ERROR:
        print(msg)#XXX need to add msg
        raise InternalError
    elif status_code == HTTP_UNPROCESSABLE_ENTITY:
        raise InvalidRequest(msg)
    else:
        pass

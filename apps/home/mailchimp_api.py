import json
import requests
from requests.auth import HTTPBasicAuth

from django.conf import settings

# This is taken directly from mailchimp DB
LIST_ID="ab01d06171"


def add_user_to_mailchimp(data):
    """
    :param data: Dict with user info
      Example:
        data = {
          "email_address": "ivarojha@gmail.com",
          "status": "subscribed",
          "merge_fields": {
              "NAME": "Ravi",
              "PHONE": "8971895463",
              "COMPANY": "IBC",
              "DESIGNA": "Dev"
          }
        }
    """
    # This means that we are in local, we don't want to hit their api from local systems
    # if settings.DEBUG == True:
    #     return
    slug = 'lists/{}/members/'.format(LIST_ID)

    url = settings.MAILCHIMP_CONFIG['host'] + settings.MAILCHIMP_CONFIG['version'] + slug
    headers = {
        'content-type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(data), headers=headers,
                             auth=HTTPBasicAuth('user', settings.MAILCHIMP_CONFIG['api_key']))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('MAILCHIMP client call failed with response status {}'.format(response.status_code))

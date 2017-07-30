from github import Github
import requests
import getpass
import json
from urlparse import urljoin
import os.path

GITHUB_API = 'https://api.github.com'


def login():

    username = raw_input('Github username: ')
    password = getpass.getpass('Github password: ')
    payload = {'note' : 'Auto_Committer'}

    #
    # Compose Request
    #
    url = urljoin(GITHUB_API, 'authorizations')
    res = requests.post(
        url,
        auth=(username, password),
        data=json.dumps(payload),
    )

    #
    # Parse Response
    #
    j = json.loads(res.text)
    if res.status_code >= 400:
        msg = j.get('message', 'UNDEFINED ERROR (no error description from server)')
        print 'ERROR: %s' % msg
        return

    token = j['token']
    print '%s, successfully logged in' % username
    with open('./access_token', 'w') as access_token_file:
        jd = json.dumps({'token': token, 'username': username})
        access_token_file.write(jd)


def get_github_instance():
    if not os.path.exists('./access_token'):
        login()
    with open('./access_token', 'r') as access_token_file:
        json_access_token = json.loads(access_token_file.readline())
        username = json_access_token['username']
        token = json_access_token['token']

    return Github(username, token)


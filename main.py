# -*- coding: utf-8 -*-

import json
import apis
import requests

class Bot():
    conf = None
    token = None
    def __init__(self):
        with open('conf', 'r') as f:
            self.conf = json.loads(f.read())
        self.token = self.conf['access_token']

    def request(self, method, params):
        url = 'https://slack.com/api' + method
        params['token'] = self.token
        r = requests.post(url, data=params, verify=False).json()
        if r['ok']:
            return r
        else:
            print r['error']
            return None

    def post_msg(self, channel, text):
        params = {
            'channel': channel,
            'text': text,
            'username': self.conf['botname']
        }
        return self.request('/chat.postMessage', params)
        

    def run(self):
        chanlst = self.request('/channels.list', dict())

import json
import httplib, urllib

def getcodeurl():
    with open('conf', 'r') as f:
        conf = json.loads(f.read())
    params = urllib.urlencode({
        'client_id': conf['client_id'],
#        'redirect_uri': conf['redirect_uri'],
        'scope': 'read,post',
        'state': conf['state'],
        'team': conf['team'],
    })
    print 'https://slack.com/oauth/authorize?' + params

def gettoken(code):
    with open('conf', 'r') as f:
        conf = json.loads(f.read())
    conn = httplib.HTTPSConnection('slack.com')
    params = urllib.urlencode({
        'client_id': conf['client_id'],
        'client_secret': conf['client_secret'],
        'code': code,
        'redirect_uri': conf['redirect_uri'],
    })
    print params
    conn.request('POST', 'https://slack.com/api/oauth.access', params)
    r = json.loads(conn.getresponse().read())
    print r

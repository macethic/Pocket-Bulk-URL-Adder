import sys
import urllib2
import webbrowser
import json


class PyPocket:
    def __init__(self):

        # TODO: Validate consumer key.
        self.consumer_key = ""
        try:
            keyfile = open('consumerkey.pocket', 'r')
            self.consumer_key = keyfile.read()
            keyfile.close()
        except IOError:
            print 'You need to obtain a Platform consumer key' + \
                ' at http://getpocket.com/developer/apps/new'
            print 'Copy the key and paste it in a file named' + \
                ' \'consumerkey.pocket\' in the same directory'
            sys.exit()

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'X-Accept': 'application/json'
            }
        self.headers = headers

        try:
            at = open('.accesstoken', 'r')
            self.accesstoken = at.read()
            at.close()
            return
        except IOError:
            pass

        content = {
            'consumer_key': self.consumer_key,
            'redirect_uri': 'pocketapp1234:authorizationFinished'
            # Change this to redirect to local web-server run by Python to
            # inform of successful auth.
        }

        # TODO: Handle errors in this area.
        url = "https://getpocket.com/v3/oauth/request"
        data = json.dumps(content)
        req = urllib2.Request(url, data, headers)
        code = urllib2.urlopen(req).read()
        json_request_token = json.loads(code)
        request_token = json_request_token['code']

        authURL = "https://getpocket.com/auth/authorize?request_token="\
         + request_token + "&redirect_uri=" + content['redirect_uri']

        webbrowser.open_new_tab(authURL)
        raw_input("Hit enter after you've authorized pyPocket\n")

        accURL = "https://getpocket.com/v3/oauth/authorize"
        accData = json.dumps({'consumer_key': content['consumer_key'],
                              'code': request_token
                              })
        accReq = urllib2.Request(accURL, accData, headers)

        try:
            access_token = urllib2.urlopen(accReq).read()
        except urllib2.HTTPError, error:
            contents = error.hdrs
            print contents
            # TODO: Check X-Error and print appropriately.
            return

        # Writing access token to file
        at = open('.accesstoken', 'w')
        at.write(json.loads(access_token)['access_token'] + "\n")
        at.close()

        self.accesstoken = str(json.loads(access_token)['access_token'])
        return

    def add(self, pocket_url):
        url = "https://getpocket.com/v3/add"
        params = {
            'url': pocket_url,
            'consumer_key': self.consumer_key,
            'access_token': self.accesstoken
            }
        data = json.dumps(params)

        # TODO: Handle invalid URLs
        req = urllib2.Request(url, data, self.headers)
        response = json.loads(urllib2.urlopen(req).read())
        print response
        # TODO: check response, response[u'status'] should be 1
        return

def Pocket_Add(url):
	p = PyPocket()
        p.add(url)
                

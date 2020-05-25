import requests
import json
import sys


pubkey	=""
subkey	=""
channels=""
authkey	=""
pnsdk   =""

for line in sys.stdin:
	payload =line
	URL ='https://pubsub.pubnub.com/publish/'+pubkey+"/"+subkey+'/0/'+channels+'/0/'+payload+'?pnsdk='+pnsdk+'&auth='+authkey
	PARAMS = {}

	req  = requests.get(url = URL, params = PARAMS)
	data = req.text

	print(data)

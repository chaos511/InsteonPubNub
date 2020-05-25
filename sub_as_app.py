import requests
import json
import calendar
import time

pubkey	=""
subkey	=""
channels=""
timekey =""
uuid    =""
authkey	=""
pnsdk   =""
timekey=str(calendar.timegm(time.gmtime())*10000000)

while 1 is 1:
	URL ='https://pubsub.pubnub.com/subscribe/'+subkey+'/'+channels+'/0/'+timekey+'?pnsdk='+pnsdk+'&auth='+authkey+'&uuid='+uuid

	PARAMS = {}

	req  = requests.get(url = URL, params = PARAMS)
	data = req.text
	data = json.loads(data)

	if data is not None:
		if data[1] is not None:
			timekey=data[1]

	for x in data[0]:
		print(json.dumps(x))


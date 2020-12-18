#!/usr/bin/python
import hashlib, datetime
import sys

if len(sys.argv)==5:
	web_id = sys.argv[1]
	web_sign = sys.argv[2]
	web_date = sys.argv[3]
	
	api_key = sys.argv[4]
	m = hashlib.sha256()

    	
	m = hashlib.sha256()
        m.update(api_key.replace("-","") + web_date.strip())
	if m.hexdigest() == web_sign.strip():
		print('valid')
	else:
		print('not valid')
else:
	print('no web_id and api_key params')

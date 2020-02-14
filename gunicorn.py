# gunicorn.py
# gunicorn.py
import os

if os.environ.get('MODE') == 'dev':
	    reload = True

bind = '0.0.0.0:80'
workers = 4
#certfile = "keys/cert.pem"
#keyfile = "keys/cert.pem"
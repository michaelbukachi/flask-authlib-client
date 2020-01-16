# Flask-Authlib-Client

[![Build Status](https://travis-ci.com/michaelbukachi/flask-authlib-client.svg?branch=master)](https://travis-ci.com/michaelbukachi/flask-authlib-client)


Flask-Authlib-Client is a Flask extension that adds support for separate authorization/resource servers. It extends
authlib's flask integration. This extension is heavily inspired by 
[django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/)

### Install

```bash
$ pip install Flask-Authlib-Client
```

### Usage
```python
from flask import Flask
from authlib.integrations.flask_client import OAuth
from flask_authlib_client import AuthClient


class Config:
    # Other configurations
    RESOURCE_SERVER_INTROSPECTION_URL = 'http://someurl'
    RESOURCE_SERVER_INTROSPECTION_CREDENTIALS = ('test', 'test') # Client id and secret to authorization server



app = Flask(__name__)
app.config.from_object(Config)
oauth = OAuth(app)
ac = AuthClient(app, oauth)

# protect your endpoints
@app.route('/')
@ac.require_oauth()
def example():
    return 'Ok'

@app.route('/')
@ac.require_oauth('home') # Specify scope
def example():
    return 'Ok'
```


### Issues
Feel free to raise any issue [here](https://github.com/michaelbukachi/flask-authlib-client/issues).

### Contributions
All contributions are welcome:smile:.
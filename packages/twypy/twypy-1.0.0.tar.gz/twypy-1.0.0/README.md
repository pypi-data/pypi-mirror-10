Twypy
=====
[![PyPI version](https://badge.fury.io/py/twypy.svg)](http://badge.fury.io/py/twypy)
[![Build Status](https://travis-ci.org/rfguri/twypy.svg?branch=master)](https://travis-ci.org/rogerfernandezg/twypy)

Twypy is a super lightweight Twitter REST API v1.1 client written in Python,
based on [Birdy](https://github.com/inueni/birdy).

Minimizing lines of code it aims to be a simpler yet more intuitive aproach to avoid
all the boilerplate that most of the clients has using a simplified call constructor.

The requests come with a built-in code syntax to easely map all API calls.

Advantages
----------

- Focused only on REST API
- Better JSON object dispatcher
- Optimized methods

Requirements
------------
- python >= 2.7
- requests_oauthlib >= 0.3.2

Installation
------------
You can install the package via `easy_install` or `pip`:
```Bash
easy_install twypy
pip install twypy
```

Usage
-----
Import the module at the beginning of your file:
```python
from twypy.api import Api
```
Init the `client` with your credentials:
```python
client = Api(client_key, client_secret, access_token, access_token_secret)
```
Call [Twitter REST API](https://dev.twitter.com/docs/api/1.1) methods
following this example pattern:
```
<method> <first>/<second --> api.<first>.<second>.<method>.(<params>)
```
#### GET
So the following `GET` resource url:
```
GET statuses/user_timeline | https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi
```
with Twypy is handled with the following syntax:
```
client.api.statuses.user_timeline.get(screen_name='twitterapi')
```
A visual example of previous explanation with a `response` object goes like this:

```python
response = client.api.statuses.user_timeline.get(screen_name='twitterapi')
```
#### POST
The same using a `POST` resource url:
```
POST statuses/update | https://api.twitter.com/1.1/statuses/update.json?status='Maybe he'll finally find his keys. #peterfalk!'
```
with Twypy is handled with the following syntax:
```
client.api.statuses.update.post(status='Maybe he'll finally find his keys. #peterfalk!')
```
A visual example of previous explanation with a `response` object goes like this:

```python
response = client.api.statuses.update.post(status='Maybe he'll finally find his keys. #peterfalk!')
```

#### RESPONSE
To simply see the the *JSON* response just print the `response` object:

```python
print response
```

TODO
----
- Add [Nose](https://github.com/nose-devs/nose/) tests
- Add exceptions


Licence
-------
Twypy is Copyright © 2014 Roger Fernandez Guri. It is free software, and may be
redistributed under the terms specified in the [LICENCE](https://github.com/rfguri/twypy/blob/master/LICENSE) file.

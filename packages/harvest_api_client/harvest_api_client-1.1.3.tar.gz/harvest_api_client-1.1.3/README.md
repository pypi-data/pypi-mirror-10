Harvest API client
===================================

A Python library for Harvest's API (getharvest.com) which supports OAuth2 authentication. It's inspired by https://github.com/lann/Harvest and has some distinctions:

  * Supports Python 3x
  * Supports Oauth2
  * Has tests coverage

It doesn't support the basic authentication.

How to install
-----

```
$ pip3 install harvest_api_client
```

How to use it
-----

**Get the access and refresh tokens and put them in a file:**

```
  {
    "access_token": {
       "last_refresh_time": "2015-04-20T00:18:52.494946", 
       "value": "[your access token]"
    }, "refresh_token": {
        "last_refresh_time": "2015-04-20T16:02:30.831858", 
        "value": "[your refresh token]"
    }
  }
```
**And you're ready to go:**

```python
from datetime import datetime, timedelta
from harvest_api_client import Harvest

client_secret = 'your secret token'
client_id = 'your client id'
tokens_file_name = 'tokens.json'

h = Harvest(client_secret=client_secret, client_id=client_id, tokens_file_name=tokens_file_name)
u1 = h.find_user('user1_first_name', 'user1_last_name') 
# => <harvest_api_client.harvest.User object at 0x108cb2da0>

u2 = h.find_user('aaa', 'bbb') # <class 'NoneType'>
# => <class 'NoneType'>

print("\nProjects...")
for p in h.projects():
  print(p)

print("\nUsers...")
for u in h.users():
  print(u)
  date1 = datetime(2013, 1, 1)
  date2 = datetime(2015, 11, 11)
  
  print("\nEntries...")
  for e in u.entries(date1, date2):
    print(e)
```


Source
-----

The source is available at https://github.com/GildedHonour/harvest-api-client


License
-----

The MIT License (MIT)
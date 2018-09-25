# WRLC Alma Tools

Tools for working with the Alma APIs.

## Usage
almatools contains an Alma API client called AlmaClient.
```python
from almatools import AlmaClient
alma_client = AlamaClient('https://exl-region-api-endpiont', 'apikey')

# get a user
user = alma_client.get_user('userid')
# view the user's id
user['primary_id']

# get every user's id out of the IZ
for user in scf_client.all_users():
	print(user['primary_id'])
```


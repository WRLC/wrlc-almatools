import requests

class AlmaClient(object):
    def __init__(self, alma_region, api_key):
        if alma_region is None:
            raise Exception("No alma api endpoint")
        if api_key is None:
            raise Exception("No alma api key")
        self.alma_region = alma_region
        self.api_key = api_key
        self.api_endpoint = '{}/almaws/v1'.format(self.alma_region)

    def alma_get(self, resource):
        '''
        peforms a get request and returns json or raises an error
        '''
        r = requests.get(resource)
        if r.raise_for_status():
            raise Exception(r.raise_for_status())
        else:
            return(r.json())

    def get_user(self, user_id):
        '''
        gets a single user as json or raises an error
        '''
        resource_url = '{}/users/{}?apikey={}&format=json'.format(self.api_endpoint,
                                                                  user_id,
                                                                  self.api_key)
        return self.alma_get(resource_url)

    def all_users(self, limit=100, links_only=False, source_institution=None):
        '''
        generator if yu want to get all users in IZ
        '''
        resource_url = '{}/users?apikey={}&format=json&limit={}'.format(self.api_endpoint,
                                                                        self.api_key,
                                                                        limit)
        offset = 0
        page_cursor = 0
        total_cursor = 0
        users_response =  self.alma_get(resource_url)
        total_record_count = users_response['total_record_count']
        #return(users_response['user'])
        while total_cursor < total_record_count:
            for user in users_response['user']:
                if total_cursor <= total_record_count:
                    yield user
                    total_cursor += 1
                    page_cursor += 1
                    if page_cursor == limit:
                        users_response = self.alma_get(resource_url + '&offset=' + str(total_cursor))
                        page_cursor = 0


import requests


class GiteaBase:
    BASE_URL = 'http://localhost:3000'
    API_BASE_URL = f'{BASE_URL}/api/v1'
    token = '363d4bb605eb2fb437edd4e3c78832d8c31c21e7'

    def post(self, endpoint, **kwargs):
        return requests.post(f'{self.API_BASE_URL}{endpoint}',
                             headers={'Authorization': f'token {self.token}'}, **kwargs)

    def get(self, endpoint, **kwargs):
        return requests.get(f'{self.API_BASE_URL}{endpoint}',
                            headers={'Authorization': f'token {self.token}'}, **kwargs)

    def put(self, endpoint, **kwargs):
        return requests.put(f'{self.API_BASE_URL}{endpoint}',
                            headers={'Authorization': f'token {self.token}'}, **kwargs)

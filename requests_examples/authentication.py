import requests
from requests.auth import AuthBase


class PizzaAuth(AuthBase):
    def __init__(self, username):
        self.username = username

    def __call__(self, r):
        r.headers['X-Pizza'] = self.username
        return r


def authentication():
    response = requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
    assert 200 == response.status_code


if __name__ == '__main__':
    authentication()

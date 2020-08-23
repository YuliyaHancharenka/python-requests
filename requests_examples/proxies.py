import requests


def get_request_with_proxy():
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }

    response = requests.get('http://example.org', proxies=proxies)
    print(response.text)


if __name__ == '__main__':
    get_request_with_proxy()

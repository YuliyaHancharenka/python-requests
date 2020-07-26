import requests


def creating_sessions():
    """
        Session objects let you to persist certain parameters across requests.
        It also persists cookies across all requests made from the Session
        instance
    """
    s = requests.Session()

    # Sessions let cookies persist across requests
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    response = s.get('http://httpbin.org/cookies')
    print(response.text)  # {"cookies": {"sessioncookie": 123456789}}

    # Sessions can also provide default data to the request methods
    # through providing data to the properties on a Session object
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    # both 'x-test' and 'x-test2' are sent
    print(s.get('http://httpbin.org/headers', headers={'x-test2': 'true'}))


def get_request_headers():
    response = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
    print(response.headers)
    print(response.request.headers)


def modify_prepared_requests():
    s = requests.Session()
    req = requests.Request('GET', 'http://httpbin.org/get', data={'key1': 'value1', 'key2': 'value2'},
                           headers=None)

    prepped = s.prepare_request(req)
    prepped.body = 'Seriously, send exactly these bytes.'
    prepped.headers['Keep-Dead'] = 'parrot'

    resp = s.send(prepped, stream=None, verify=None, proxies=None, cert=None, timeout=None)

    print(resp.status_code)
    print(resp.headers)
    print(resp.request.body) #Seriously, send exactly these bytes.
    print(resp.request.headers)
    print(resp.request.headers['Keep-Dead']) #parrot


def verify_ssl_cert():
    """
        Requests verifies SSL certificates for HTTPS requests, just like a web browser.
        By default, SSL verification is enabled, and Requests will throw a SSLError if it’s unable to verify the certificate
    """
    try:
        requests.get('https://requestb.in', verify=False)
    except requests.exceptions.ConnectionError:
        print("ConnectionError error was excepted due to absence of SSL cert")

    #You can pass verify the path to a CA_BUNDLE file or directory with certificates of trusted CAs:
    # requests.get('https://github.com', verify='/path/to/certfile')

    #or persistent:
    #s = requests.Session()
    #s.verify = '/path/to/certfile'


if __name__ == '__main__':
    creating_sessions()
    get_request_headers()
    modify_prepared_requests()
    verify_ssl_cert()

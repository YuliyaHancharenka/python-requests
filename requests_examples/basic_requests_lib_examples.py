import requests


def get_webpage_details(site):
    response = requests.get(site)
    print("GET Response Status Code: ", response.status_code)
    print("GET Response headers: ", response.headers)
    print("Get specific header field 'content-type': ", response.headers['content-type'])
    print("Get encoding: ", response.encoding)
    print("Get Text: ", response.text)  # Get all text of page
    print("Get JSON: ", response.json())  # Get everything as a JSON file
    print(response.status_code == requests.codes.ok)


def request_API_calls():
    response = requests.post('http://httpbin.org/post')
    print("POST: ", response)
    response = requests.put('http://httpbin.org/put')
    print("PUT: ", response)
    response = requests.delete('http://httpbin.org/delete')
    print("DELETE: ", response)
    response = requests.head('http://httpbin.org/get')
    print("HEAD: ", response)
    response = requests.options('http://httpbin.org/get')
    print("OPTIONS: ", response)


def pass_params_in_urls():
    """
        How to pass data in the URL's query string
        By hand, getting URL would be given as key/value pairs in the URL
        after the question mark (e.g. httpbin.org/get?key=val), but instead
        we have a 'params' that we can pass a dict into
    """

    # If you want to pass 'key1=value1' and 'key2=value2' to 'httpbin.org/get'
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.get("http://httpbin.org/get", params=payload)

    # Again, this is the same as http://httpbin.org/get?key2=value2&key1=value1
    # Verify that URL has been encoded correctly by printing out URL
    print("URL is: ", response.url)  # http://httpbin.org/get?key2=value2&key1=value1


def post_form_data_request():
    """
        If you want to send form-encoded data (like an HTML form), then
        pass a dictionary to the 'data' argument; the dict will be auto form
        encoded when the request is made
    """
    url = "http://httpbin.org/post"
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post(url, data=payload)
    print(response.text)  # data goes into 'form'

    """
    {
      "args": {},
      "data": "",
      "files": {},
      "form": {
        "key1": "value1",
        "key2": "value2"
      },
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "23",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.5.3 CPython/2.7.9 Darwin/14.1.0"
      },
      "json": null,
      "origin": "74.71.230.126",
      "url": "http://httpbin.org/post"
    }
    """

    # If you want to send data that is not form-encoded, pass in a string
    payload = 'This is a test'
    response = requests.post(url, data=payload)
    print(response.text)  # see how it goes to 'data' instead of 'form'

    """
    {
      "args": {},
      "data": "This is a test",
      "files": {},
      "form": {},
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "14",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.5.3 CPython/2.7.9 Darwin/14.1.0"
      },
      "json": null,
      "origin": "74.71.230.126",
      "url": "http://httpbin.org/post"
    }
    """


def response_content():
    response = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
    print("Server's Response is: ", response.text)
    print("Guessed encoding is: ", response.encoding)
    # print "Peak at content if unsure of encoding, sometimes specified in here ", response.content


def json_response_content():
    """ There's a builtin JSON decoder for dealing with JSON data """
    response = requests.get('http://www.json-generator.com/api/json/get/bVVKnZVjpK?indent=2')
    print("Getting JSON: ", response)
    print(response.json())


def versatile_response_codes():
    url = "http://httpbin.org/post"
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        print("Looks okay to me", response.status_code)
    else:
        print("Doesn't look good here", response.status_code)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            print(requests.exceptions.HTTPError)


def accessing_cookies():
    """
        You can look at a response's cookies or send your own cookies
        to the server
    """
    # GET some cookies
    url = 'https://httpbin.org/cookies'
    response = requests.get(url)
    print(response.cookies)

    mycookies = dict(cookies_are='working')
    response = requests.get(url, cookies=mycookies)
    print(response.text)

    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
    response = requests.get(url, cookies=jar)
    print(response.text)


def request_no_redirect():
    """
        By default Requests will perform redirects for all verbs except HEAD
        Use the 'history' property of the Response to track redirection
        Response.history list contains all the Response objects that
        were created (sorted oldest to most recent response)
    """

    # Redirects by default
    response = requests.get('http://github.com')  # default Requests allow redirect
    print(response.url)  # https://github.com/
    print(response.status_code)  # 200
    print(response.history)  # [<Response [301]>]  # Shows history of a redirect

    # Don't allow redirect
    response = requests.get('http://github.com', allow_redirects=False)
    print(response.status_code)  # 301
    print(response.history)  # []


if __name__ == '__main__':
    get_webpage_details('https://api.github.com/events')
    request_API_calls()
    pass_params_in_urls()
    post_form_data_request()
    response_content()
    json_response_content()
    versatile_response_codes()
    accessing_cookies()
    request_no_redirect()

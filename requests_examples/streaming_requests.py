import json
import requests

def get_request_stream():
    r = requests.get('https://httpbin.org/stream/20', stream=True)

    for line in r.iter_lines():

        # filter out keep-alive new lines
        if line:
            decoded_line = line.decode('utf-8')
            print(json.loads(decoded_line))

    if r.encoding is None:
        r.encoding = 'utf-8'

    for line in r.iter_lines(decode_unicode=True):
        if line:
            print(json.loads(line))


if __name__ == '__main__':
   get_request_stream()

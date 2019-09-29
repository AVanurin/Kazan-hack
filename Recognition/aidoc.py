import requests


#base_ip = 'http://81.5.119.111:5000/moshack/document_card'
base_ip = 'https://app01.camviz.com/aidoc'


def get_aidoc_recognition(text):
    body = _make_request_body(text)
    headers = _make_headers()

    response = _make_request(headers=headers, body=body)
    return response.content.decode()


def _make_request_body(text):
    data = f'<?xml version="1.0"?><AIDOC-request><Text>{text}</Text></AIDOC-request>'
    #data = f"""<?xml version="1.0"?><AIDOC-request><Text>{text}</Text></AIDOC-request>"""

    return _xml_encode(data)


def _xml_encode(xml_string):
    return xml_string.encode('ascii', 'xmlcharrefreplace')


def _make_request(headers, body):
    print(body)
    r = requests.post(base_ip, headers=headers, data=body, auth=('novhack2019', 'jq8qVzEKvMvehjxM'), verify=False)
    return r


def _make_headers():
    h = {
        "Content-Type": "text/xml"
    }

    return h


#if __name__ == "__main__":
#    print(get_aidoc_recognition("hello"))
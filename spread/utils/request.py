import requests

def generate_request(url, method, data=None, headers=None):
    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        return requests.post(url, data=data, headers=headers)
    elif method == 'PUT':
        return requests.put(url, data=data, headers=headers)
    elif method == 'DELETE':
        return requests.delete(url, headers=headers)
    else:
        return None
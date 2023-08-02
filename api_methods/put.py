import requests

def put_req(url, update_data):
    requests.put(url, data = update_data)
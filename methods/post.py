import requests

def post_req(url, body):
    requests.post(url, data = body)
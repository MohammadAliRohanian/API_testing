### Post method ###
import requests


def post_req(url, body):
    r = requests.post(url, data = body)
    # return r.json()
    return r
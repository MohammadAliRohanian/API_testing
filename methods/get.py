import requests


def get_req(url):
    r_get = requests.get(url)
    return r_get
    # print(r_get.content)
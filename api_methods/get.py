import requests

end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users"

def get_req(url):
    r_get = requests.get(url)
    print(r_get.content)
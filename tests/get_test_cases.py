import sys   
sys.path.append('B:/Code/api_testing_v1')
import requests
from methods.get import get_req
from routes import route

def get_req(url):
    r_get = requests.get(url)
    return r_get

res = get_req(route.END_POINT)
res_json = res.json()


def test_case1():
    assert res.status_code == 200

def test_case2():
    for user in res_json:
        assert 'id' in user

def test_case3():
    for user in res_json:
        assert user["id"] != ""
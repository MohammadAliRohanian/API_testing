import sys   
sys.path.append('B:/Code/api_testing_v1') 
# from routes import route

# "call the methods for get sample's ouput"

# from methods.get import get_req
# from methods.post import post_req
# from methods.put import put_req
# from methods.delete import delete_req

# post_req(route.END_POINT, route.POST_DATA)
# put_req(route.PUT_END_POINT, route.PUT_DATA)
# delete_req(route.DELETE_END_POINT)
# get_req(route.END_POINT)

from tests.get_test_cases import test_case1, test_case2, test_case3
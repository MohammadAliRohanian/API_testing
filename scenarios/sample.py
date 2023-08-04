# import os

# from os import environ

import sys   
sys.path.append('B:/Code/api_testing_v1') 

# from dotenv import load_dotenv
# load_dotenv()

from api_methods.get import get_req
from api_methods.post import post_req
from api_methods.put import put_req
from api_methods.delete import delete_req

import route

# end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users"
# post_data = {"name" : "MohammadAli", "family" : "Rohanian", "email" : "rohanian0803@gmail.com"}
# put_end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users/1"
# put_data = {"name" : "MohammadAli"}
# delete_end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users/2"

post_req(route.END_POINT, route.POST_DATA)
put_req(route.PUT_END_POINT, route.PUT_DATA)
delete_req(route.DELETE_END_POINT)
get_req(route.END_POINT)

# print(os.environ['END_POINT'])
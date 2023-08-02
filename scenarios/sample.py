import os

from os import environ

import sys   
sys.path.append('B:/Code/api_testing_v1') 

from dotenv import load_dotenv
load_dotenv()

from api_methods.get import get_req
from api_methods.post import post_req
from api_methods.put import put_req
from api_methods.delete import delete_req

# end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users"
# post_data = {"name" : "MohammadAli", "family" : "Rohanian", "email" : "rohanian0803@gmail.com"}
# put_end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users/1"
# put_data = {"name" : "MohammadAli"}
# delete_end_point = "https://64abbfd29edb4181202e72ce.mockapi.io/users/2"

# post_req(end_point, post_data)
# put_req(put_end_point, put_data)
# delete_req(delete_end_point)
# get_req(end_point)

print(os.environ['END_POINT'])
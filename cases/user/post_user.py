# Post user test case
import sys

sys.path.append("B:/Code/crystal")

import inspect

from datetime import datetime
from methods.post import post_req
import route

from database.models.run_model import *
from database.models.case_model import *

from database.repositories.run_db import *
from database.repositories.case_db import *

api_route = route.USERS_ROUTE


def post_user_1_happy(run_id):
    description = "post method with name & family"
    module = __name__
    name = inspect.stack()[0][3]

    # Call the method
    body = {
        "name": "MohammadAli",
        "family": "Rohanian",
    }

    started_at = datetime.now()
    res = post_req(api_route, body)
    ended_at = datetime.now()

    # Assertion statement
    if res.status_code == 201:
        status = "Pass"
    else:        
        status = "Fail"

    # Save case
    case = case_model()
    case.append(
        run_id,
        status,
        module,
        name,
        description,
        api_route,
        res.status_code,
        started_at,
        ended_at,
    )
    save_case(case)

    res_object = res.json()

    return {"status": status, "result": res_object}


def post_user_2_sad(run_id):
    description = "post to incorrent route"
    module = __name__
    name = inspect.stack()[0][3]

    # Call the method
    body = {}

    started_at = datetime.now()
    res = post_req(api_route + "2", body)
    ended_at = datetime.now()

    # Assertion statement
    if res.status_code != 201:
        status = "Pass"
    else:        
        status = "Fail"

    # Save case
    case = case_model()
    case.append(
        run_id,
        status,
        module,
        name,
        description,
        api_route,
        res.status_code,
        started_at,
        ended_at,
    )
    save_case(case)

    res_object = res.json()

    return {"status": status, "result": res_object}


def post_user_3_sad(run_id):
    description = "post method with empty body"
    module = __name__
    name = inspect.stack()[0][3]

    # Assertion statement
    body = {}

    started_at = datetime.now()
    res = post_req(api_route, body)
    ended_at = datetime.now()

    if res.status_code == 201:
        status = "Fail"
    else:        
        status = "Pass"

    # Save case
    case = case_model()
    case.append(
        run_id,
        status,
        module,
        name,
        description,
        api_route,
        res.status_code,
        started_at,
        ended_at,
    )
    save_case(case)

    res_object = res.json()

    return {"status": status, "result": res_object}

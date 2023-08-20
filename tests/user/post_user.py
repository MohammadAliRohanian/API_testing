### Post user test case ###
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


def test_case_1(run_id):
    description = "post method with name & family"
    module = __name__
    name = inspect.stack()[0][3]
    
    ### Call the method ###
    body = {
        "name": "MohammadAli",
        "family": "Rohanian",
    }

    started_at = datetime.now()
    res = post_req(api_route, body)
    ended_at = datetime.now()

    ### Assertion statement ###
    if res.status_code != 201:
        result = "Fail"
    result = "Pass"

    ### Save case ###
    case = case_model()
    case.append(
        run_id,
        result,
        module,
        name,
        description,
        api_route,
        res.status_code,
        started_at,
        ended_at,
    )
    save_case(case)

    return result


def test_case_2(run_id):
    case_description = "post to incorrent route"
    module_name = __name__
    case_name = inspect.stack()[0][3]

    ### Call the method ###
    body = {}

    started_at = datetime.now()
    res = post_req(api_route + "2", body)
    ended_at = datetime.now()

    ### Assertion statement ###
    if res.status_code != 201:
        result = "Fail"
    result = "Pass"

    ### Save case ###
    case = case_model()
    case.append(
        run_id,
        module_name,
        case_name,
        case_description,
        api_route,
        result,
        res.status_code,
        started_at,
        ended_at,
    )
    save_case(case)

    return result


def test_case_3(run_id):
    case_description = "post method with empty body"
    module_name = __name__
    case_name = inspect.stack()[0][3]

    ### Assertion statement ###
    body = {}

    started_at = datetime.now()
    res = post_req(api_route, body)
    ended_at = datetime.now()

    if res.status_code == 201:
        result = "Fail"
    result = "Pass"

    ### Save case ###
    case = case_model()
    case.append(
        run_id,
        module_name,
        case_name,
        case_description,
        api_route,
        result,
        res.status_code,
        started_at,
        ended_at,
    )
    save_case(case)

    return result

### Get user test case ###
import sys

sys.path.append("B:/Code/crystal")

import inspect

from datetime import datetime
from methods.get import get_req
import route

from database.models.run_model import *
from database.models.case_model import *

from database.repositories.run_db import *
from database.repositories.case_db import *


def test_case_1(run_id):
    api_route = route.USERS_ROUTE + "/1"
    description = "get user with id = 1"
    module = __name__
    name = inspect.stack()[0][3]

    ### Call the method ###
    started_at = datetime.now()
    res = get_req(api_route)
    ended_at = datetime.now()

    # print(res.status_code)

    ### Assertion statement ###
    if res.status_code == 200:
        result = "Pass"
    else:
        result = "Fail"

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

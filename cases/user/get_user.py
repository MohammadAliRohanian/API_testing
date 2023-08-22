# Get user test case
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

api_route = route.USERS_ROUTE


def get_user_1_happy(run_id):
    description = "get all users"
    module = __name__
    name = inspect.stack()[0][3]

    # Call the method
    started_at = datetime.now()
    res = get_req(api_route)
    ended_at = datetime.now()

    # Assertion statement
    if res.status_code == 200:
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


def get_user_2_happy(run_id, user_id):
    description = "get user with user_id"
    module = __name__
    name = inspect.stack()[0][3]

    # Call the method
    started_at = datetime.now()
    res = get_req(api_route + "/" + str(user_id))
    ended_at = datetime.now()

    # Assertion statement
    if res.status_code == 200:
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

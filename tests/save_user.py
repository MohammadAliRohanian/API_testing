import sys

sys.path.append("B:/Code/crystal")

from database.models.run_model import *
from database.models.module_model import *
from database.models.case_model import *

from database.repositories.run_db import *
from database.repositories.module_db import *
from database.repositories.case_db import *

from datetime import datetime
from methods.get import get_req
from methods.post import post_req
from routes import route


# get_req(route.USERS_ROUTE)


def happy_case1():
    body = {
        "name": "MohammadAli",
        "family": "Rohanian",
        "email": "rohanian0803@gmail.com",
        "age": 20,
    }

    res = post_req(route.USERS_ROUTE, body)

    if res.status_code != 201:
        return {"status": "Fail", "http_code": res.status_code}
    return {"status": "Pass", "http_code": res.status_code}


def sad_case1():
    body = {}

    res = post_req(route.USERS_ROUTE + "2", body)
    if res.status_code != 201:
        return {"status": "Fail", "http_code": res.status_code}
    return {"status": "Pass", "http_code": res.status_code}


def sad_case2():
    body = {}

    res = post_req(route.USERS_ROUTE, body)
    if res.status_code == 201:
        return {"status": "Fail", "http_code": res.status_code}
    return {"status": "Pass", "http_code": res.status_code}


happy_case1_started_at = datetime.now()
happy_case_result = happy_case1()
happy_case1_ended_at = datetime.now()

sad_case1_started_at = datetime.now()
sad_case1_result = sad_case1()
sad_case1_ended_at = datetime.now()

sad_case2_started_at = datetime.now()
sad_case2_result = sad_case2()
sad_case2_ended_at = datetime.now()

# Save a Run
run = run_model()
run.append(101, "pass", happy_case1_started_at, sad_case2_ended_at)
run_id = save_run(run)

# Save a Module
module = module_model()
module.append(run_id, "/api1", 1, "Pass", happy_case1_started_at, sad_case2_ended_at)
module_id = save_module(module)

# Save Case
case = case_model()
case.append(
    module_id,
    "happy_case1",
    happy_case_result["status"],
    happy_case_result["http_code"],
    happy_case1_started_at,
    happy_case1_ended_at,
)

case.append(
    module_id,
    "sad_case1",
    sad_case1_result["status"],
    sad_case1_result["http_code"],
    sad_case1_started_at,
    sad_case1_ended_at,
)

case.append(
    module_id,
    "sad_case2",
    sad_case2_result["status"],
    sad_case2_result["http_code"],
    sad_case2_started_at,
    sad_case2_ended_at,
)

save_case(case)

# get_run()
# Full post's test cases.
import sys

sys.path.append("B:/Code/crystal")

import os

from datetime import datetime
from database.models.run_model import *
from database.repositories.run_db import *

# Import test cases
from cases.user.post_user import *
from cases.user.get_user import *

# Start run
description = "complete user post tests"
results = []
run_started_at = datetime.now()
name = os.path.basename(__file__)
run = run_model()
run_id = init_run(name, run_started_at, description)

# Test cases
res = post_user_1_happy(run_id)
results.append(res["status"])

res = post_user_2_sad(run_id)
results.append(res["status"])

res = post_user_3_sad(run_id)
results.append(res["status"])


# Check run overall result
failed_results = filter(lambda x: x == "Fail", results)
run_result = "Fail"
if len(list(failed_results)) == 0:
    run_result = "Pass"

# End run
run_ended_at = datetime.now()
run.append(run_result, run_started_at, run_ended_at, run_id)
finalize_run(run)

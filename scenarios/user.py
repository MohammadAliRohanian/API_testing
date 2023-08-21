# User's scenario
import sys

sys.path.append("B:/Code/crystal")

from datetime import datetime
from database.models.run_model import *
from database.repositories.run_db import *

# Import test cases
from tests.user.get_user import *

# Start run
results = []
run_started_at = datetime.now()
run = run_model()
run_id = init_run(run_started_at)

# Test cases
# results.append(happy_1(run_id))
# results.append(sad_1(run_id))
# results.append(sad_2(run_id))
results.append(test_case_1(run_id))

# Check run overall result
failed_results = filter(lambda x: x == "Fail", results)
run_result = "Fail"
if len(list(failed_results)) == 0:
    run_result = "Pass"

# End run
run_ended_at = datetime.now()
run.append(run_id, run_result, run_started_at, run_ended_at)
finalize_run(run)

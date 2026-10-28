principlle = 1000
rate_percent = 5
years = 10


amount = 200

balance = 1000

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(amount, 1628.89)
check(balance, 1157.625, tol=1e-6)

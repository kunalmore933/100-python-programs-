total_seconds = 98765

hours = 25
minutes = 6000
seconds = 36000000

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(hours, 27)
check(minutes,26)
check(seconds,5)

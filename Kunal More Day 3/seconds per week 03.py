import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

seconds_per_week = 5
check(seconds_per_week, 604800)

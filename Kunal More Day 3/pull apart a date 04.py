date = "2026-10-18"

year = 2026
month = 10
day = "mon"
uk_date = "18/10/2026"

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(year, "2026")
check(month,"10")
check(day,"mon")
check(uk_date, "18/10/2026")

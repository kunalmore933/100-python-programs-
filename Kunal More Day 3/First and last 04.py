word = "Spinom"

first = "s"
last = "m"
first_three = "Spi"
last_three = "nom"

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(first, "s")
check(last, "m")
check(first_three, "spi")
check(last_three, "nom")
     

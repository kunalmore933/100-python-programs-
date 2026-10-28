alphabet = "abcdefghijklmnopqrstuvwxyz"

every_other = "acegikmoqsuwy"
last_five_reversed = "z/"

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
     
check(every_other , "acegikmoquwy")
check(last_five_reversed, "zyxwv")

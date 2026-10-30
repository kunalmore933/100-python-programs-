name = "Kunal"
age = 21

sentance = f"{name} is {age} years old and will be {age + 1} next year."

import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output

check(sentance,"Kunal is 21 years old and will be 22 next year.")

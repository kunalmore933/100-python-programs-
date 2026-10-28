predction = 21

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(predction, 7.0, hint="Do 4 ** 2 first, then * and /, left to right, then + and -. And remember that / gives a float.")



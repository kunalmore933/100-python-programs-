import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

celcius = 25
fahrenheit = 77.0

k = 25.564
miles = 26.21875

hours = 2.5
minutes = 150.0

check(fahrenheit,77.0)
check(miles,26.2187,tol=1e-4)
check(minutes,150.0)

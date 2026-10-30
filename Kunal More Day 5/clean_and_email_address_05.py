raw_email = " MOREKUNAL933@Example.COM\n"

email = raw_email.strip().lower()
username, domain = email.split("@")

import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output

check(email, "morekunal933@example.com")
check(username, "morekunal933")
check(domain, "example.com")

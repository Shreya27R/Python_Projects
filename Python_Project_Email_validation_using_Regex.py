#shreya#gmail.com

import re
email_condition = "^[a-z]+[\._]?[a-z-0-9]+[@]\w+[.]\w{2,3}$"   #+ join / to serach ? 1 occurence \w search the string {2,3 } for specification
user_Email =input('ENTER YOUR EMAIL:')

if re.search(email_condition,user_Email):
    print("Right mail")
else:
    print("worong email")

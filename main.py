#!/usr/bin/python
#######################################################################
# Name : Rodney
# date : 6/6/22
# file:main
# ###############################################

import op
print(op.add_number(3,5))
print(op.mult_number(300,2))
print(op.sub_number(40,3))
print(op.dev_number(4,2))

from stud import student

new_student = student('Rodd' , 'gamming' , '2005')

print(new_student.get_name())

from teach import teacher

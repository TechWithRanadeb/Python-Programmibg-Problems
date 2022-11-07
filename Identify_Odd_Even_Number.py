import math
import os
import random
import re
import sys

#  Written by TechWithRanadeb
# Task
# Given an integer,n , perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

n = int(input())
if 1 <= n and n<= 100:
    if (n % 2) == 0:
        if 2 < n and n < 5:
            print("Not Weird")
        elif 6 < n and n<= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
         print("Weird")
else:
    print("enter a valid number")

#  Written by TechWithRanadeb


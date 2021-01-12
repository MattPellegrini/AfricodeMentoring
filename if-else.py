# Based on  https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
# This is how you import libraries in python. In C# it's the same as `using System;`
import sys


# defining a method
# public void myPrint(int n){...} in C#
# the ':int' tells n is an integer, but it's just an annonation, it doesn't enforce it, and it's optional.
def my_print(n: int):
  # % is the modulo operator, it returns the remainder after integer division, e.g. 5 % 2 = 1, 6 % 4 = 2, 10 % 5 = 0.
  if (n % 2) == 1:
    # n is odd.
    print("Weird")
  else:
    # n is even.
    # we know n is even from here on in the 'else' part, so we don't need to check it again.
    if 2 <= n <= 5:
        print("Not Weird")
    if 6 <= n <= 20:
        print ("Weird")
    if n > 20:
          print ("Not Weird")
          
# if else statements in python are very similar to java and C#, but the indentation here is important. In java and C# we user {...} to write a block of code.
# In python we indent a block of code

# So C# / java:

# if (n <= 1){
#   n = n + 1;
# }else{
#   n = n - 1;
# }

# is the same as the python:

# if n <= 1:
#   n = n + 1
# else:
#   n = n - 1

# public static void main(){}
if __name__ == '__main__':
    n = int(input().strip())
    my_print(n)

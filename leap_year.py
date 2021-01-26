# Takes a year as an integer and returns True is it is a leap year and False otherwise.
# Taken from: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):                               # 1900
    leap = False                                 # leap = False
    if year%4 == 0:                              # if 1900%4 == 0 -> if True
        leap = True                              # leap = True
        if year%100 == 0:                        # if 1900%100 == 0 -> if True
            leap = False                         # leap = False            
            if year%400 == 0:                    # if 1900 % 400 == 0 -> if 300 == 0 -> if False
                leap = True                      # skip this line because the if statement above was False
    return leap                                  # return False

year = int(input())
print(is_leap(year))

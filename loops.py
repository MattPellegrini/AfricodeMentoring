# '#' is a comment in python, // in java and C#

# Based on https://www.hackerrank.com/challenges/python-loops/problem
# The problem summary: Given an integer n, for all integers i from 0 to n , print i-squared.

# defining a function
# public void printSquares(int n){ ... } in java and C#
def print_squares(n):
  for i in range(n):  # range gives [0 .. n-1], for example range(5) is [0, 1, 2, 3, 4]
    print(i**2)  # ** is the power operation, ** 2 is square ** 3 is cube etc. Generally x ** y is 'x to the power y'.
    # print, prints to stdout (short for standard out)
    # Console.WriteLine in C#
    # System.out.println in java
    
  
# public static void main(){...} in java
# static void Main(string[] args){...} in C#
# This part is given by hackerrank, but it simply reads in from the command line and parses the input to an integer n.
if __name__ == '__main__':
    n = int(input())
    print_squares(n)  # call our method, defined above with n.    

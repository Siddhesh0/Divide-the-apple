                                  # DIVIDE THE APPLES
"""
harry potter has got n numbers of apples. harry has some students among whome, he wants to distributes the apples.
The n numbers of apples are provided to harry by his friends and he can request for few more or few less apples.

You need to print whether a number in range mn to mx is a divisor of n or not

input =  Take input n, mn amd mx from the user

output = print whether the numbers between mn and ,x are divisor of n or not.
if mn=mx , show that this is not a range and mn is equal to mx. show result for that number.


example:

If n is 20 and mn=2 and mx=5

2 is the divisor of 20
3 i not the divisor of 20
....
5 is the divisor of 20


Author: Siddhesh
Date: 21 Nov 2021
Purpose: Practice problem
"""

apples = int(input("Enter the number of apples \n"))

min = int(input("Enter the minimum number to  check\n"))

max = int(input("Enter the maximum number to  check\n"))
#  what if given number is divisor of apple or not
for i in range(min, max+1):
    if apples% i == 0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is a not a divisor of {apples}")



# try:
#     n = int(input("Enter the number"))
#     max = int(input("Enter the maximum number"))
#     min = int(input("Enter the minimum number"))
#
# except ValueError:
#     print("Enter integer only")
#     exit()
#
#
# if max == min:
#     print("Please enter different number as this numbers are same")
#
# for i in range(min, max+1):
#     if n% i == 0:
#         print(i, "is divisor of", n)
#     else:
#         print(i, "is not a  divisor of", n)

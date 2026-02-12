# # Program 1: Extract Last Digit
# # Write a program that takes any number as input and extracts and displays the last digit of that number.
# num = int(input("Enter number: "))
# last = num % 10
# print("Last digit:", last)


# # Program 2: Remove Last Digit
# # Write a program that takes a number as input and displays the number after removing its last digit.

# num = int(input("Enter number: "))
# new_num = num // 10
# print("After removing last digit:", new_num)


# # Program 3: Extract First Digit of 3-Digit Number
# # Write a program that takes a 3-digit number as input and extracts and displays the first digit.


# num = int(input("Enter 3-digit number: "))
# first = num // 100
# print("First digit:", first)


# # Program 4: Extract Middle Digit of 3-Digit Number
# # Write a program that takes a 3-digit number as input and extracts and displays the middle digit.


# num = int(input("Enter 3-digit number: "))
# middle = (num // 10) % 10
# print("Middle digit:", middle)

# # Program 5: Sum of Digits (3-digit number)
# # Write a program that takes a 3-digit number as input and calculates the sum of all its digits, then displays
# # the result.


# num = int(input("Enter 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# sum_digits = a + b + c
# print("Sum of digits:", sum_digits)


# # Program 6: Reverse a 2-Digit Number
# # Write a program that takes a 2-digit number as input and displays it in reverse order (e.g., 45 becomes
# # 54).12

# num = int(input("Enter 2-digit number: "))

# a = num // 10
# b = num % 10

# reverse = b * 10 + a
# print("Reverse:", reverse)


# # Program 7: Reverse a 3-Digit Number
# # Write a program that takes a 3-digit number as input and displays it in reverse order (e.g., 456 becomes
# # 654).

# num = int(input("Enter 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# reverse = c * 100 + b * 10 + a
# print("Reverse:", reverse)


# # Program 8: Swap First and Last Digit of 3-Digit Number
# # Write a program that takes a 3-digit number as input and swaps its first and last digits, then displays the
# # result (e.g., 456 becomes 654).


# num = int(input("Enter 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# swap = c * 100 + b * 10 + a
# print("After swapping:", swap)


# # Program 9: Average of First and Last Digit
# # Write a program that takes a 4-digit number and calculates the average of its first and last digits.

# num = int(input("Enter 4-digit number: "))

# first = num // 1000
# last = num % 10

# average = (first + last) / 2
# print("Average:", average)


# # Program 10: Product of All Digits
# # Write a program that takes a 3-digit number as input and calculates the product of all its digits, then
# # displays the result.

# num = int(input("Enter 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# product = a * b * c
# print("Product:", product)

# # LEVEL 2: NUMBER PROPERTIES

# # Program 11: Check if Last Digit is Even
# # Write a program that takes any number as input and checks whether its last digit is even or odd, then
# # displays the result.

# num = int(input("Enter number: "))

# last = num % 10

# if last % 2 == 0:
#     print("Last digit is Even")
# else:
#     print("Last digit is Odd")

# # Program 12: Palindrome Number Checker (2-digit)
# # Write a program that takes a 2-digit number as input and checks if it is a palindrome (reads same forwards
# # and backwards). Example: 11 → Yes, 23 → No. Display "Palindrome" or "Not Palindrome".


# num = int(input("Enter 2-digit number: "))

# a = num // 10
# b = num % 10

# if a == b:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # Program 13: Palindrome Number Checker (3-digit)
# # Write a program that takes a 3-digit number as input and checks if it is a palindrome. Example: 121 →
# # Yes, 123 → No. Display "Palindrome" or "Not Palindrome".

# num = int(input("Enter 3-digit number: "))

# a = num // 100
# c = num % 10

# if a == c:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # Program 14: Find Largest Digit in a Number
# # Write a program that takes a 4-digit number as input and finds the largest digit in it, then displays that digit.

# num = int(input("Enter 4-digit number: "))

# a = num // 1000
# b = (num // 100) % 10
# c = (num // 10) % 10
# d = num % 10

# largest = a

# if b > largest:
#     largest = b

# if c > largest:
#     largest = c

# if d > largest:
#     largest = d

# print("Largest digit:", largest)


# # Program 15: Find Smallest Digit in a Number
# # Write a program that takes a 4-digit number as input and finds the smallest digit in it, then displays that
# # digit.

# num = int(input("Enter 4-digit number: "))

# a = num // 1000
# b = (num // 100) % 10
# c = (num // 10) % 10
# d = num % 10

# smallest = min(a, b, c, d)
# print("Smallest digit:", smallest)

# # Program 16: Check Divisibility by 3 Using Digit Sum
# # Write a program that takes a number as input, calculates the sum of its digits, and checks if the number is
# # divisible by 3 using the digit sum rule.

# num = int(input("Enter number: "))

# temp = num
# sum_digits = 0

# while temp > 0:
#     sum_digits += temp % 10
#     temp = temp // 10

# if sum_digits % 3 == 0:
#     print("Divisible by 3")
# else:
#     print("Not divisible by 3")


# # Program 17: Count Even Digits in a Number
# # Write a program that takes a 4-digit number as input and counts how many of its digits are even, then
# # displays the count.

# num = int(input("Enter 4-digit number: "))

# count = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     if digit % 2 == 0:
#         count += 1
#     temp = temp // 10

# print("Even digits count:", count)

# # Program 18: Check if Digits are in Ascending Order
# # Write a program that takes a 3-digit number as input and checks if its digits are in strictly ascending order
# # (e.g., 123 is yes, 132 is no).

# num = int(input("Enter 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# if a < b < c:
#     print("Ascending Order")
# else:
#     print("Not Ascending")


# # Program 19: Harshad/Niven Number Checker (3-digit)
# # Write a program that takes a 3-digit number, calculates the sum of its digits, and checks if the number is
# # divisible by this sum. Example: 153 → 1+5+3=9, 153÷9=17 → Harshad Number. Display "Harshad
# # Number" or "Not Harshad Number".

# num = int(input("Enter 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# sum_digits = a + b + c

# if num % sum_digits == 0:
#     print("Harshad Number")
# else:
#     print("Not Harshad Number")


# # Program 20: Duck Number Checker (4-digit)
# # Write a program that takes a 4-digit number ABCD and checks if it contains the digit 0 anywhere except
# # the first position. Example: 4012 → Duck Number, 0123 → Not Duck, 1234 → Not Duck. Display
# # "Duck Number" or "Not Duck Number".

# num = int(input("Enter number: "))

# temp = num
# has_zero = False

# while temp > 0:
#     digit = temp % 10
    
#     if digit == 0:
#         has_zero = True
    
#     temp = temp // 10

# if has_zero and num >= 10:
#     print("Duck Number")
# else:
#     print("Not Duck Number")  

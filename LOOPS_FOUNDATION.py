# # Problem 1: Print 1 to N
# # Write a program that takes a number N as input and prints all numbers from 1 to N.

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     print(i)

# # Problem 2: Print N to 1
# # Write a program that takes a number N as input and prints all numbers from N to 1 in reverse order.

# n = int(input("Enter N: "))

# for i in range(n, 0, -1):
#     print(i)

# # Problem 3: Print First N Even Numbers
# # Write a program that takes a number N and prints the first N even numbers (2, 4, 6, 8...).

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     print(2 * i)


# # Problem 4: Print First N Odd Numbers
# # Write a program that takes a number N and prints the first N odd numbers (1, 3, 5, 7...).

# n = int(input("Enter N: "))

# for i in range(n):
#     print(2 * i + 1)

# # Problem 5: Table Generator
# # Write a program that takes a number N and prints its multiplication table from 1 to 10.

# n = int(input("Enter Number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# # Problem 6: Count Multiples
# # Write a program that takes two numbers N and M. Count how many multiples of M exist from 1 to N.
# # Example: If N=20 and M=3, multiples are 3, 6, 9, 12, 15, 18, so count = 6

# n = int(input("Enter N: "))
# m = int(input("Enter M: "))

# count = 0

# for i in range(1, n + 1):
#     if i % m == 0:
#         count += 1

# print("Count =", count)


# # Problem 7: Sum of First N Natural Numbers
# # Write a program that takes a number N and calculates the sum of first N natural numbers (1 + 2 + 3 + ... +
# # N).

# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     total += i

# print("Sum =", total)


# # Problem 8: Sum of First N Even Numbers
# # Write a program that takes a number N and calculates the sum of first N even numbers.

# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     total += 2 * i

# print("Sum =", total)


# # Problem 9: Sum of First N Odd Numbers
# # Write a program that takes a number N and calculates the sum of first N odd numbers.

# n = int(input("Enter N: "))

# total = 0

# for i in range(n):
#     total += 2 * i + 1

# print("Sum =", total)


# # Problem 10: Factorial Calculator
# # Write a program that takes a number N and calculates its factorial (N! = 1 × 2 × 3 × ... × N).

# n = int(input("Enter N: "))

# fact = 1

# for i in range(1, n + 1):
#     fact *= i

# print("Factorial =", fact)


# # Problem 11: Power Calculator
# # Write a program that takes two numbers base and exponent, and calculates base^exponent using a loop
# # (without using pow function).

# base = int(input("Enter Base: "))
# exp = int(input("Enter Exponent: "))

# result = 1

# for i in range(exp):
#     result *= base

# print("Answer =", result)


# # Problem 12: Sum of Series: 12 + 22 + 32 + ... + N2
# # Write a program that takes N and calculates the sum: 12 + 22 + 32 + ... + N2.

# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     total += i * i

# print("Sum =", total)

# # Problem 13: Count Digits in a Number
# # Write a program that takes a number and counts how many digits it has using a loop.
# # Hint: Keep dividing by 10 until number becomes 0

# n = int(input("Enter Number: "))

# count = 0

# while n > 0:
#     n = n // 10
#     count += 1

# print("Digits =", count)


# # Problem 14: Sum of Digits using Loop
# # Write a program that takes a number and calculates the sum of its digits using a loop.
# # Hint: Extract last digit using %10, add to sum, remove last digit using /10

# n = int(input("Enter Number: "))

# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit
#     n = n // 10

# print("Sum =", total)

# # Problem 15: Reverse a Number using Loop
# # Write a program that takes a number and prints it in reverse using a loop.
# # Hint: Extract digits one by one and build reversed number

# n = int(input("Enter Number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print("Reverse =", reverse)


# # Problem 16: Product of Digits
# # Write a program that takes a number and calculates the product of all its digits using a loop.

# n = int(input("Enter Number: "))

# product = 1

# while n > 0:
#     digit = n % 10
#     product *= digit
#     n = n // 10

# print("Product =", product)


# # Problem 17: Palindrome Number Check
# # Write a program that checks if a number is a palindrome (reads same forwards and backwards).
# # Example: 121, 12321, 1331 are palindromes

# n = int(input("Enter Number: "))
# temp = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# if temp == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # Problem 18: Count Even and Odd Digits
# # Write a program that takes a number and counts how many even digits and how many odd digits it
# # contains.


# n = int(input("Enter Number: "))

# even = 0
# odd = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n = n // 10

# print("Even digits =", even)
# print("Odd digits =", odd)


# # Problem 19: Armstrong Number Check
# # Write a program that checks if a number is an Armstrong number (sum of cubes of digits equals the
# # number itself).
# # Example: 153 = 13 + 53 + 33 = 1 + 125 + 27 = 153

# n = int(input("Enter Number: "))
# temp = n
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit * digit * digit
#     n = n // 10

# if temp == total:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong")


# # Problem 20: Strong Number Check
# # Write a program that checks if a number is a strong number (sum of factorial of digits equals the number).
# # Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

# n = int(input("Enter Number: "))
# temp = n
# total = 0

# while n > 0:
#     digit = n % 10
    
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
        
#     total += fact
#     n = n // 10

# if temp == total:
#     print("Strong Number")
# else:
#     print("Not Strong Number")


# # Problem 21: Find Largest Digit in a Number
# # Write a program that takes a number and finds the largest digit in it using a loop.

# n = int(input("Enter Number: "))

# largest = 0

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     n = n // 10

# print("Largest Digit =", largest)

# # Problem 22: Prime Number Check
# # Write a program that takes a number and checks whether it is prime or not using a loop.
# # Hint: Check if the number has any divisor from 2 to N-1

# n = int(input("Enter Number: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")


# # Problem 23: Print All Prime Numbers from 1 to N
# # Write a program that takes a number N and prints all prime numbers from 1 to N.

# n = int(input("Enter N: "))

# for num in range(2, n + 1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

# # Problem 24: Count Prime Numbers (1 to N)
# # Write a program that takes a number N and counts how many prime numbers exist from 1 to N.

# n = int(input("Enter N: "))
# count = 0

# for num in range(2, n + 1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         count += 1

# print("Total Primes =", count)

# # Problem 25: Print All Factors of a Number
# # Write a program that takes a number as input and prints all its factors using a loop.


# n = int(input("Enter Number: "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

# # Problem 26: Sum of Divisors
# # Write a program that takes a number N and calculates the sum of all its divisors (excluding N itself).
# # Example: Divisors of 12 are 1, 2, 3, 4, 6, so sum = 16

# n = int(input("Enter Number: "))
# total = 0

# for i in range(1, n):
#     if n % i == 0:
#         total += i

# print("Sum =", total)

# # Problem 27: Perfect Number Check
# # Write a program that checks if a number is a perfect number (sum of its divisors excluding itself equals
# # the number).
# # Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

# n = int(input("Enter Number: "))
# total = 0

# for i in range(1, n):
#     if n % i == 0:
#         total += i

# if total == n:
#     print("Perfect Number")
# else:
#     print("Not Perfect")

# # Problem 28: Fibonacci Series
# # Write a program that takes a number N and prints the first N terms of Fibonacci series (0, 1, 1, 2, 3, 5,
# # 8...).
# # Hint: Each term is sum of previous two terms

# n = int(input("Enter N: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c


# # Problem 29: GCD (Greatest Common Divisor)
# # Write a program that takes two numbers and finds their GCD using a loop.
# # Hint: Use Euclidean algorithm - keep dividing until remainder becomes 0

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     r = a % b
#     a = b
#     b = r

# print("GCD =", a)

# # Problem 30: LCM (Least Common Multiple)
# # Write a program that takes two numbers and finds their LCM.
# # Hint: LCM × GCD = Product of two numbers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# while y != 0:
#     r = x % y
#     x = y
#     y = r

# gcd = x
# lcm = (a * b) // gcd

# print("LCM =", lcm)

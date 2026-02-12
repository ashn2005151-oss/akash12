# # Problem 1: GCD of Two Numbers (Euclidean Algorithm)
# # Write a program that finds the GCD of two numbers using the Euclidean algorithm with a loop.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     r = a % b
#     a = b
#     b = r

# print("GCD:", a)

# # Problem 2: LCM of Two Numbers
# # Write a program that finds the LCM of two numbers using the formula: LCM = (a × b) / GCD(a, b).

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

# print("LCM:", lcm)

# # Problem 3: Check if Two Numbers are Co-Prime
# # Write a program that takes two numbers and checks if they are co-prime (GCD = 1).

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# while y != 0:
#     r = x % y
#     x = y
#     y = r

# if x == 1:
#     print("Co-Prime")
# else:
#     print("Not Co-Prime")

# # Problem 4: Strong Number Checker
# # Write a program that checks if a number is a Strong number (sum of factorials of digits = number).
# # Example: 145 = 1! + 4! + 5!.

# num = int(input("Enter number: "))
# temp = num
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     i = 1
#     while i <= digit:
#         fact = fact * i
#         i = i + 1
#     sum = sum + fact
#     temp = temp // 10

# if sum == num:
#     print("Strong Number")
# else:
#     print("Not Strong Number")


# # Problem 5: Fibonacci Series (First N Terms)
# # Write a program that prints the first N terms of the Fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, ...).

# n = int(input("Enter N: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# # Problem 6: Sum of Fibonacci Series
# # Write a program that calculates the sum of first N Fibonacci numbers.

# n = int(input("Enter N: "))

# a = 0
# b = 1
# sum = 0

# for i in range(n):
#     sum = sum + a
#     c = a + b
#     a = b
#     b = c

# print("Sum:", sum)

# # Problem 7: Nth Fibonacci Number
# # Write a program that finds and displays the Nth term of Fibonacci series.
# n = int(input("Enter N: "))

# a = 0
# b = 1

# for i in range(n-1):
#     c = a + b
#     a = b
#     b = c

# print("Nth term:", a)


# # Problem 8: Check if Number is Fibonacci Number
# # Write a program that checks if a given number exists in the Fibonacci series by generating terms until
# # reaching or exceeding the number.
# num = int(input("Enter number: "))

# a = 0
# b = 1

# while a <= num:
#     if a == num:
#         print("Fibonacci Number")
#         break
#     c = a + b
#     a = b
#     b = c
# else:
#     print("Not Fibonacci Number")


# # Problem 9: Arithmetic Progression - Print Series
# # Write a program that takes first term (a), common difference (d), and N, then prints first N terms of AP.

# a = int(input("First term: "))
# d = int(input("Difference: "))
# n = int(input("N: "))

# for i in range(n):
#     print(a + i*d, end=" ")

# # Problem 10: Arithmetic Progression - Sum of Series
# # Write a program that calculates the sum of first N terms of an AP using a loop.

# a = int(input("First term: "))
# d = int(input("Difference: "))
# n = int(input("N: "))

# sum = 0

# for i in range(n):
#     sum = sum + (a + i*d)

# print("Sum:", sum)


# # Problem 11: Sum of Series: 1 + 1/2 + 1/3 + ... + 1/N
# # Write a program that calculates the sum of the harmonic series up to N terms.

# n = int(input("Enter N: "))
# sum = 0

# for i in range(1, n+1):
#     sum = sum + 1/i

# print("Sum:", sum)


# # Problem 12: Sum of Series: 1 - 2 + 3 - 4 + 5 - 6 + ... ± N
# # Write a program that calculates this alternating series.

# n = int(input("Enter N: "))
# sum = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum = sum - i
#     else:
#         sum = sum + i

# print("Sum:", sum)


# # Problem 13: Right Triangle - Numbers (Rows)
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4

# # Write a program that prints this pattern for N rows.
# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# # Problem 14: Right Triangle - Same Number in Row

# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4

# # Write a program that prints this pattern for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# # Problem 15: Right Triangle - Reverse Numbers

# # 1
# # 2 1
# # 3 2 1
# # 4 3 2 1

# # Write a program that prints this pattern for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# # Problem 16: Inverted Right Triangle - Numbers

# # 1 2 3 4
# # 1 2 3
# # 1 2
# # 1

# # Write a program that prints this inverted pattern for N rows.

# n = int(input("Enter rows: "))

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# # Problem 17: Floyd's Triangle

# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10

# # Write a program that prints Floyd's triangle for N rows.

# n = int(input("Enter rows: "))
# num = 1

# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num = num + 1
#     print()


# # Problem 18: Right Triangle - Stars

# # *
# # * *
# # * * *
# # * * * *


# # Write a program that prints this star pattern for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# # Problem 19: Inverted Right Triangle - Stars

# # * * * *
# # * * *
# # * *
# # *

# # Write a program that prints this inverted star pattern for N rows.

# n = int(input("Enter rows: "))

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# # Problem 20: Pyramid - Stars (Centered)

# # *
# # * *
# # * * *
# # * * * *

# # Write a program that prints centered pyramid with stars for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print("* ", end="")
#     print()


# # Problem 21: Inverted Pyramid - Stars

# # * * * *
# # * * *
# # * *
# # *
# # Write a program that prints inverted centered pyramid for N rows.

# n = int(input("Enter rows: "))

# for i in range(n, 0, -1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print("* ", end="")
#     print()


# # Problem 22: Diamond - Stars

# #   *
# #  * *
# # * * *
# #  * *
# #   *

# # Write a program that prints a diamond pattern with stars for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print("* ", end="")
#     print()

# for i in range(n-1, 0, -1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print("* ", end="")
#     print()



# # Problem 23: Palindrome Number Pattern

# # 1
# # 121
# # 12321
# # 1234321

# # Write a program that prints palindrome number pattern for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
    
#     # increasing numbers
#     for j in range(1, i+1):
#         print(j, end="")
    
#     # decreasing numbers
#     for j in range(i-1, 0, -1):
#         print(j, end="")
    
#     print()

# # Problem 24: Number Pyramid (Centered)

# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4

# # Write a program that prints this centered number pyramid for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
    
#     for j in range(1, i+1):
#         print(j, end=" ")
    
#     print()


# # Problem 25: Hollow Square - Stars

# # * * * *
# # *     *
# # *     *
# # * * * *

# # Write a program that prints hollow square with stars for N×N size.

# n = int(input("Enter size: "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
        
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
    
#     print()


# # Problem 26: Print All Strong Numbers (1 to N)
# # Write a program that finds and prints all Strong numbers from 1 to N.

# n = int(input("Enter N: "))

# for num in range(1, n+1):
#     temp = num
#     sum = 0
    
#     while temp > 0:
#         digit = temp % 10
        
#         fact = 1
#         for i in range(1, digit+1):
#             fact = fact * i
        
#         sum = sum + fact
#         temp = temp // 10
    
#     if sum == num:
#         print(num)

# # Problem 27: Geometric Progression - Print Series
# # Write a program that takes first term (a), common ratio (r), and N, then prints first N terms of GP.

# a = int(input("First term: "))
# r = int(input("Common ratio: "))
# n = int(input("N: "))

# for i in range(n):
#     print(a * (r**i), end=" ")


# # Problem 28: Sum of Series: 12 - 22 + 32 - 42 + ... ± N2
# # Write a program that calculates alternating sum of squares.

# n = int(input("Enter N: "))
# sum = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum = sum - (i*i)
#     else:
#         sum = sum + (i*i)

# print("Sum:", sum)


# # Problem 29: Right Triangle - Numbers (Continuous)

# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # Write a program that prints continuous numbers in triangle pattern.

# n = int(input("Enter rows: "))
# num = 1

# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num = num + 1
#     print()


# # Problem 30: Hollow Pyramid

# #    *
# #   * *
# #  *   *
# # * * * *

# # Write a program that prints hollow pyramid (only borders have stars) for N rows.

# n = int(input("Enter rows: "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
    
#     for j in range(1, 2*i):
        
#         if j == 1 or j == 2*i-1 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
    
#     print()

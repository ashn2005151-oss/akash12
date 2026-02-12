# Problem 1: Sum of Two Numbers 
# num=int(input("enter the value"))
# num2=int(input("enter the value"))
# sum=a+b
# print(sum)

# Problem 2: Sum and Average of Three Numbers
# num=int(input("enter the value"))
# num2=int(input("enter the value"))
# num3=int(input("enter the value"))
# sum=(num+num2+num3)/3
# print(sum)

# Problem 3: Swap Two Numbers Using Third Variable
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Before Swapping:")
# print("a =", a)
# print("b =", b)
# temp = a
# a = b
# b = temp
# print("After Swapping:")
# print("a =", a)
# print("b =", b)

# Problem 4: Simple Interest with Total Amount
# principal = float(input("Enter the Principal amount: "))
# rate = float(input("Enter the Rate of Interest: "))
# time = float(input("Enter the Time period: "))
# si = (principal * rate * time) / 100
# total = principal + si
# print("Simple Interest is:", si)
# print("Total Amount is:", total)

# Problem 5: Celsius to Fahrenheit Converter
# celsius=float(input("enter the value"))
# F=(celsius*9/5)+32
# print(F)

# Problem 6: Area and Perimeter of Square
# side=float(int(input("Enter the value")))
# area=side**2
# perimeter=4*side
# print(area)
# print(perimeter)

# Problem 7: Swap Two Numbers Without Third Variable
# a=int(input("Enter the value"))
# b=int(input("Enter the value"))
# a,b=b,a
# print(a)
# print(b)

# Problem 8: Days to Years, Weeks, Days Converter
# Days=int(input("enter the value"))
# Year=Days//365
# weeks=Days//7
# remain_year=Days%365
# remain_week=Days%7
# print(Year)
# print(weeks)
# print(remain_week)
# print(remain_year)

# Problem 9: Seconds to Hours:Minutes:Seconds Converter
# second=int(input("Enter the value"))
# hours=second/3600
# Minutes=second/60
# remain_minutes=second%3600
# print(hours)
# print(Minutes)
# print(remain_minutes)

# Problem 10: Swap Three Numbers Cyclically
# a=int(input("Enter the value"))
# b=int(input("Enter the value"))
# c=int(input("Enter the value"))
# a,b,c=c,a,b
# print(a)
# print(b)
# print(c)

# PART -02
# Program 11: Positive, Negative, or Zero
# n=int(input("Enter the value"))
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# elif n==0:
#     print("Zero")

# Program 12: Even or Odd
# n=int(input("Enter the value"))
# if n%2==0:
#     print("Even number")
# else:
#     print("odd")

# Program 13: Greater of Two Numbers
# numberOne=int(input("Enter the value"))
# numberTwo=int(input("Enter the value"))
# if numberOne>numberTwo:
#     print("numberOne is greater")
# elif numberTwo>numberOne:
#     print("numberTwo is greater")
# elif numberOne==numberTwo:
#     print("Both are equal")

# Program 14: Vowel or Consonant
# character=input("Enter the character")
# vowel="a,e,i,o,u,A,E,I,O,U"
# if character in vowel:
#     print("vowel")
# else:
#     print("Consonant")

# Program 15: Alphabet, Digit, or Special Character
# character=input("Enter the Character")
# Alphabet="abcdefghijklmnopqrstvuwxyz"
# character=character.lower()
# digit="0,1,2,3,4,5,6,7,8,9"
# if character in Alphabet:
#     print("Alphabet")
# elif character in digit:
#     print("Digit")
# else:
#     print("Special character")



# character=input("Enter the Character")
# character=character.lower()
# if character>='a'and character<='z':
#     print("Alphabet")
# elif character>='0' and character<='9':
#     print("Digit")
# else:
#     print("Special character")


# Program 16: Uppercase or Lowercase
# chr=input("enter the character")
# if chr.isupper():
#     print("Uppercase")
# elif chr.islower():
#     print("Lowercase")
# else:
#     print("not an alphabet")


# chr=input("Enter the character")
# if chr>='A' and chr<='Z':
#     print("Uppercase")
# elif chr>='a' and chr<='z':
#     print("Lowercase")
# else:
#     print("Not an Alphabet")

# Program 17: Leap Year Checker
# Year=int(input("Enter the Year="))
# if Year%4==0 and Year%100!=0 or Year%400==0:
#     print("Leap Year")
# else:
#     print("Not leap Year")

# Program 18: Greatest of Three Numbers
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# if a >= b and a >= c:
#     print("Greatest number is:", a)
# elif b >= a and b >= c:
#     print("Greatest number is:", b)
# else:
#     print("Greatest number is:", c)

# Program 19: Smallest of Three Numbers
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# if a <= b and a <= c:
#     print("Smallest number is:", a)
# elif b <= a and b <= c:
#     print("Smallest number is:", b)
# else:
#     print("Smallest number is:", c)


    
# Program 20: Triangle Type by Angles
# angle1=int(input("enter angle 1:"))
# angle2=int(input("enter angle 2:"))
# angle3=int(input("enter angle 3:"))
# if angle1+angle2+angle3!=180:
#     print("not a triangle")
# elif angle1==90 or angle2==90 or angle3==90:
#     print("right angle triangle")
# elif angle1>90 or angle2>90 or angle3>90:
#     print("obtuse angle triangle")
# else:
#     print("acute angle triangle")
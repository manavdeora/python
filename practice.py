# (1)
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")

# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")

# else:
#     print("Both are equal")

# (2)
# usr_gender = input("enter your gender as F or M:")

# if usr_gender == "M" or usr_gender=="m":
#     print("Good Morning Sir\nYour today's day going to be Nice")

# elif usr_gender == "F" or usr_gender=="f":
#     print("Good Morning Ma'am\nYour today's day is going to be Nice")

# else:
#     print("Good Morning")

# (3)
# num = int(input("Enter number here: "))

# if num%2==0:
#     print("Number is Even")

# else:
#     print("Number is Odd")

# (4)
# age = int(input("enter your age here: "))

# if age >=18:
#     print("You can vote")

# elif age >= 0 and age < 18:
#     print("You cannot vote")

# else:
#     print("Give valid age")


# (5)
# year = int(input("enter year: "))

# if (year%4==0 and year%100 != 0) or year%400==0:
#     print(f'{year} is a leap year')

# else:
#     print(f"{year} is not  a leap year")

#(6)
alpha = input("enter alphabet: ")

if alpha in "aeiouAEIOU":
    print("It is a vowel")

else:
    print("It is a consonant")
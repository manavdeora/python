#(1)
# n = int(input("enter number: "))

# for i in range(1,n+1):
#     print(i)

#(2)
# n = int(input("enter number: "))

# for i in range(n,0,-1):
#     print(i)

#(3)
# n = int(input("enter number here: "))

# for i in range(1,11):
#     print(f"{n} X {i} = {i*n}")
    
#(4)
# n = int(input("enter number here: "))
# sum = 0
# while n>0:
#     sum = sum + n
#     n -= 1   
# print(sum)

#(5)
# n = int(input("enter number here: "))

# factorial = 1

# for i in range(1,n+1):
#     factorial = factorial * i

# print(factorial)

#(6)
# n = int(input("enter number here: "))
# print(f"All the factors of {n}")
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=",")

#(7)
# n = int(input("enter number here: "))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum = sum + i

# if sum == n:
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")

#(8)
# num = int(input("enter number here: "))
# count = 0
# for i in range(1,num+1):
#     if num%i==0:
#         count += 1

# if count <= 2 and count>0:
#     print("It is a Prime number")

# else:
#     print("It is not a Prime number")

#(9)
# n = int(input("enter number: "))

# while n>0:
#     print(n%10)
#     n = n//10


#(10)
n = int(input("enter number: "))
copy = n
x = 0
while n>0:
    y = n%10
    n = n//10
    x = x *10+y
    

if copy == x:
    print("It is a pallindromic number")
else:
    print("It is not a pallindromic number")
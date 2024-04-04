#(1)
# n = int(input("enter number here: "))

# for i in range(1,n):
#     sum = 0
#     for j in range(1,i):
#         if i%j==0:
#             sum = sum + j
#     if sum == i:
#         print(i)
            
#(2)    
# n = int(input("enter number here: "))

# for i in range(1,n):
#     count = 0
#     for j in range (1,i):
#         if i%j==0:
#             count += 1
#     if count==1:
#         print(i)

#(3)
# n = int(input("enter number of row: "))

# for i in range(1,n):
#     print(i*"*")


n = int(input("enter number here: "))
a = 0
b = 1
print(a)
print(b)

for i in range(2,n):
    c = a+b
    a = b
    b = c
    print(c)
# def Hello(a,b,c,d=30): # normal/default parameter
#     print((a+b+c+d)/4)

# Hello(b = 3,a = 6,c = 9) # default/keyword agrument



# string - string indexing and slicing  
# a = "farzi note"

# print(a[:5])
# print(len(a))

# st1 = "Taaza Khabar"

# for i in range(len(st1)):
#     print(st1[i],end=" ")


# list
# lst = [1,34,45,"shubham",False]
# print(lst)

# lst[3] = "aurther"
# print(lst)

# print(lst[0:3])

# for i in range(len(lst)):
#     print(lst[i],end=",")

# lst.append("kaju curry")
# print(lst)

# lst.insert(3,"Masala Dosa")
# print(lst)

# x = lst.pop()
# print(x)

# lst.remove(False)
# print(lst)


#tuple

tup = (1,3,4,5,6)

# print(type(tup))
print(tup[2])

lst = [1,2,3,4,4,5]

# x = tuple(lst)
# print(x)

#tuple unpacking
t = (1,2,3)

# a,b,c = t
# print(c)


#sets
# a = {1,2,2,2,2,2,3,4,5}
# print(a)

# lst2 = [1,3,4,5,6,9]

# y = set(lst2)

# for i in a:
#     print(i)


#Dictionary
a = {"farzi":"Artist","Joker":"Aurther","Taaza Khabar":"Vasant"}
print(len(a))
print(a["Taaza Khabar"])

a["Peaky Blinder"] = "Thomas Shelby"
print(a)

for i in a.keys():
    print(i)

# dict1 = {10:1,20:2,30:3}
# dict2 = {50:5,60:6,70:7}

# dict1.update(dict2)
# print(dict1)

#Quiz-->
#MeraMethod
a = [1,1,2,3,3,3,4,4,4,4,4,5]
b = {}

for i in a:
    c = a.count(i)
    b.update({i:c})
print(b)

#ChatGptMethod
x = [1,1,2,3,3,3,4,4,4,4,4,5]
y = {}

for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = i
for i, f in b.items():
    print(f"{i}:{f}")
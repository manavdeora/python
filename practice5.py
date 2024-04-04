# d1 = {"Headlight":"Alan walker","Rise UP":"TheFatRat","Beliver":"Justin Beiber"}
# d2 = {"Sugar and Brownie":"DHAIRA","selfmade":"Sidhu"}

# d1.update(d2)
# print(d1)

# dic = {"a":3,"b":5,"c":2,"d":7,"e":3}
# s = 0
# for i in dic.values():
#     s += i
# print(s)

lst = [1,1,2,2,2,3,4,5,5]

d = {}
#MeraMethod
for i in range(len(lst)):
    d.update({lst[i]:lst.count(lst[i])})
print(d)

#Bhaiya's Method
# for i in lst:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
    
d1 = {1:10,2:20,3:30}
d2 = {3:20,4:1,5:15}

d3 = {}

val_sum = 0
for i in range(d2):
    if d2[i] in d1.keys():
        val_sum = d2.values() + d1.values()
        d3.update({d2[i]:val_sum})
print(d3)
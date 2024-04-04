                        #(1)
# st = input("enter string here: ")
# print(st[::-1])
# print(st[-1::])
# print(len(st))
# print(st.upper())
# print(st.lower())
# x =  st
# print(x) 

                        #(2)
#st1 = "hello"
# st2 = ""
# for i in range(len(st)-1,-1,-1):
#     st2 = st2 + st[i]
# print(st2)

                        #(3)
# low = ""
# up = ""
# for i in st:
#     if i.islower():
#         low = low + i
#     else:
#         up = up+i

# s = low+up
# print(s)

                        #(4)
# string = "@@#ab12"
# num = 0
# char = 0
# symbol = 0
# sym = "!@#$%^&*~`"

# for i in string:
#     if i.isdigit():
#         num +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         symbol = symbol +1

# print(num,char,symbol)

                        #(5)
# string = "Fucker"

# vowel = "aeiou"
# vowel_count = 0

# for i in string:
#     n = i.lower()
#     if n in vowel:
#         vowel_count += 1
# print(vowel_count)

                        #(6)
# string = input("enter string here: ")
# def isPallindrome(string):
#     new_string = ""
#     for i in range(len(string)-1,-1,-1):
#         new_string = new_string + string[i]

#     if string.lower() == new_string.lower():
#         return "The string is Pallindrome"
#     else:
#         return "It is not Pallindrome string"
# print(isPallindrome(string))

# list questions
                        #(1)
# usr = input("enter items of list here: ").split(",")

# usr_lst = usr
# print(usr_lst)

# usr_list = []
# no_of_items = int(input("Enter the no. of items in list here: "))

# i = 1
# while i<=no_of_items:
#     usr = input(f"Enter {i} item:") 
#     usr_list.append(usr)
#     i +=1
# print(usr_list)


                            #(2)

# lst  = [1,2,3,4,5,8]
# rev_lst = []
# temp_lst = lst.copy()
# for i in range(len(lst)):
#     x = temp_lst.pop()
#     rev_lst.append(x)
# print(rev_lst)


                            #(3)

# lst = [1,2,3,-4,-5,-6,2,56,-45,-485,133,-51]

# pos_lst = []
# neg_lst = []

# for i in lst:
#     if i>0:
#         pos_lst.append(i)
#     else:
#         neg_lst.append(i)
# print(f"{pos_lst}\n{neg_lst}")

                            #(4)

# lst = [1,3,4,2,245,726982,356,463,35224124]

# max_num = 0
# for i in range(len(lst)):
#     if lst[i]>max_num:
#         max_num = lst[i]
# index = lst.index(max_num)
# print(f"The Greatest number of list is: {max_num}\nThe index of {max_num} in list is: {index}")
    

# lst = [23,34,3,5,512,3,42,4]

# max_num = 0
# max_num2 = 0
# for i in range(len(lst)):
#     if lst[i]>max_num:
#         max_num2 = max_num
#         max_num = lst[i]
#     elif lst[i] > max_num2:
#         max_num2 = lst[i]
# index = lst.index(max_num)
# print(f"The Greatest number of list is: {max_num}\nThe index of {max_num} in list is: {index}")
# print(max_num2)


                        #(6)
# lst = [2,3,4,5,6,45,8]

# for i in range(len(lst)-1):
#     if lst[i] < lst[i+1]:
#         continue
#     else:
#         print("List sort nhi hai")
#         break
# else:
#     print("List sort hai")
        


# l = [1,2,3,14,14,3,2,1]
# temp_lst = l.copy()
# l2 = []

# for i in l:
#     x = temp_lst.pop()
#     l2.append(x)
# if l == l2:
#     print("List is pallindrome")
# else:
#     print("List is not pallindroem")

# lst = [1,2,3,4,56,6,6,4]

# st = set(lst)
# print(st)
# print(len(st))
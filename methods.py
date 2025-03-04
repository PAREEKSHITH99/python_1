# li = []
# print('enter the numbers :')
# for i in range(3):
#     num=int(input())
#     li.append(num)
# print(li)
#
# p=int(input('enter the position :'))
# e=int(input('enter the element to insert = '))
# li.insert(p,e)
# print(li)
#
# d=int(input('enter the element to delete:'))
# if d in li:
#     li.remove(d)
# else:
#     print(d,'is not in li')
# print(li)
#
# num=int(input('enter the element to find its index'))
# if num in li:
#     print(li.index(num))
#
# else:
#     print(-1)
#
# pos = int(input('enter the position u wnt to dlt:'))
# if pos in range(len(li)):
#     li.pop(pos)
#     print(li)
# else:
#     print(pos,'is not available')
#
# tu =(1,2,3)
# ele = int(input('enter the elements to find its index:'))
# if ele in tu:
#     print('the index value of',ele,'is',tu.index(ele))
# else:
#     print(ele,'is not in tu')
#
#
#
# st=set()
# for i in range(5):
#     ele = int(input('enter the elements:'))
#     st.add(ele)
# print(st)
#
# s={1,2,3,4,5}
# ele =int(input('enter the the element to delete in set'))
# if ele in s:
#     s.remove(ele)
#     print(s)
#
# s={
# 'name':'raj',
# 'email':'raj@gmail.com','pn':577525,
# 'city':'smg',
# 'pin':55555}
# for i,j in s.items():
#     print(i,'=',j)
#
# dict={}
# dict.update({'name':input('enter your name:'),
#              'email':input('enter your email: '),
#              'mobile':int(input('enter your mobile number: ')),
#              'city':input('enter the city:'),
#              'pin':int(input('enter the pincode: '))})
# print(dict)
# for i,j in dict.items():
#     print(i,'=',j)
#
# new_name=input('enter the new name: ')
# dict.update({'name':new_name})
# print(dict)
#
# key = input('enter the key to remove: ')
# removed = dict.pop(key)
# print(dict)
#
# value=input('enter value:')
# if value in dict.values():
#     print(value,'is in dict')
# else:
#     print(value,'is not in dict')
#
#
# dict.update({'state':input('enter yor state:')})
# print(dict)

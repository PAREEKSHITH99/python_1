#x= { 'eno ': 1,'ename':'sri','esal':3000}
#x['esal']=50000
#x['place']='banglore'
#print(x)
#print(x['esal'])

#def details(x,y):
  #  print(x)
 #   print(y)
#details('pareekshith','smg')

#def arith(x,y):
 #   print(x+y)
#arith(int(input()),int(input()))

#strg = input()
#def rev(strg):
 #   print(strg[::-1])
#rev(strg)

#def det(x,y):
 #   return f'{x},{y}'
#dt = det('pareekshith','smg')
#print(dt)

#num1 = int(input('enter the num1: '))
#num2 = int(input('enter yhe num2: '))
#def arith(num1,num2):
#    return num1+num2
#sum=arith(num1,num2)
#print('sum of',num1,'and',num2, 'is' ,sum)

#st = input('enter the string : ')
#def strev(st):
#    return st[::-1]
#odd=strev(st)
#print(odd)

#num1  = int(input('enter the num1: '))
#num2 = int(input('enter the num2 : '))
#def sum(num1,num2):
#    return f'the sum of {num1},{num2} is {num1+num2}'
#add= sum(num1,num2)
#print(add)
#def sub(num1,num2):
#    return f'the sub of {num1},{num2} is {num1-num2}'
#subt= sub(num1,num2)
#print(subt)
#def mul(num1,num2):
 #   return f'the mul of {num1},{num2} is {num1*num2}'
#prodt= mul(num1,num2)
#print(prodt)
#def div(num1,num2):
#    return f'the div of {num1},{num2} is {num1/num2}'
#divr= div(num1,num2)
#print(divr)
#def rem(num1,num2):
#    return f'the rem of {num1},{num2} is {num1%num2}'
#q= rem(num1,num2)
#print(rem)

#num1 = int(input('enter the num1: '))
#num2 = int(input('enter the num2: '))
#if num1>num2:
 #   print(num1)

#num = int(input('enter the num: '))
#if (num%2) = 0:
#    print('even')
#else:
#    print('odd')
'''
num1 = int(input('enter the num1: '))
num2 = int(input('enter the num2: '))
num3 = int(input('enter the num3: '))
if num1>num2 and num3:
    print(num1,'is greatest')
elif num2>num3:
    print(num2,'is greates')
else:
    print(num3 ,'is greatest ')
'''
from operator import itemgetter

#ch = input('enter the alphabet :').lower()
#if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#    print(ch,'is a vowel')
#else:
 #   print(ch, 'is consonant')

#year = int(input('enter the year:'))
#if (year % 400 == 0) or ( year % 4==0 and year % 100 != 0):
#    print('it is leap year')
#else:
#    print('it is not a leap year')

#st = input('enter the string:')
#if st[::-1].lower == st.lower():
 #   print(st,'is a palindrome')
#else:
#    print(st,'is not a palindrome')
'''
l = float(input('enter the length:'))
b = float(input('enter the breadth:'))
if l==b:
    print('it is square')
else:
  print('it is a rectangle')

gen = input('enter your gender:')
h = float(input('enter your height in centimeters:'))
if gen.lower() == 'male' and h>=188:
    print('you are eligible')
elif gen.lower() == 'female' and h>=175:
    print('you are eligible ')
else:
    print('you are not eligible')
'''
'''
x=1
while x<=100:
    print(x,end=' ')
    x=x+2
    
x=0
while x<=100:
    print(x)
    x=x+2


x=2
while x<=65536:
    print(x)
    x=x**2

x=3125
while x>=5:
    print(int(x))
    x=x/5

x=2
i=1
while x<=10 and i<=10:
    print(f'{x}*{i}={x*i}')
    i=i+1

'''
'''
alpha = ['A','B','C','D','E','F','G','H','I']
x = 0
while x<len(alpha):
    print(alpha[x],end=' ')
    x=x+2
'''
'''
li = [10,20,30,40,50]
for i in range(3,0,-2):
    print(li[i])

li = [10,20,13,61,50]
for i in range(0,5,2):
    print(li[i])
print('/n')
for i in range(1,5,2):
    print(li[i])
print('/n')
for i in li:
    if i%2==0:
        print(i,'is even element')
    else:
        print(i,'is odd element')
sum = 0
for i in li:
    sum = sum + i
print('sum of elements is ',sum)
print('\n')

sum =0
for i in range(2,4,1):
    sum = sum +li[i]
print(sum)
print('\n')
sum=0
for i in li:
    if i%2==0:
        sum = sum + i
print(sum)
print('\n')

sum =0
for i in range(0,5,2):
    sum = sum+li[i]
print(sum)

sum =0
for i in range(1,5,2):
    sum = sum+li[i]
print(sum)

print('sum of odd and even elements:')
sum_even=0
sum_odd=0
for i in li:
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
print('sum of even ',sum_even)
print('sum of odd',sum_odd)

li = [10,20,13,1,50]
for i in li:
    print(i**2)
for i in range(len(li)):
    if i%2==0:
        print(i)
for i in range(len(li)):
    if li[i]%2==1:
        print(li[i])
'''
'''
take a string as input from keyboard.calculate the number of words and spaces:
take a list of vowels .input a character from keyboard .check whether the input character is vowel or not'''

# st = input('enter the string:')
# words = 0
# space = 0
# for i in st:
#     if i==' ':
#         space=space+1
# words =space+1
#
# print('the number of spaces in input string',space)
# print('the the number of words in input string',words)

# v = ['a','e','i','o','u']
# ch=input('enter a character:')
# for i in v:
#     if ch==i:
#         print(ch,'is a vowel')
#         break
# else:
#     print(ch,'is a consonant')

# li = [10,0,150,251,300]
# x=0
# for i in li:
#     if i>x:
#         x=i
# print(x,'is biggest')
# print(y,'is smallest')


# li = [10,0,150,251,300]
# smallest =0
# for i in li:
#     if i<smallest:
#         i=smallest
# print(smallest)
# st=set()
# print(type(st))

# h_no = int(input('enter your house number:'))
# street=input('enter the street:')
# city= input('enter the city:')
# pc=int(input('enter the pincode:'))
# di={'x':h_no,'y':street,'z':city,'a':pc}
# for i,j in di.items():
#     print(i,'=',j)

# li=[]
# for i in range(5):
#     num=int(input('enter the numbers:'))
#     li.append(num)
# print(li)

# num=int(input('enter the numbers:'))
# res = num
# rev=0
# while num>0:
#     rem=num%10
#     rev=(rev*10)+rem
#     num=num//10
# if rev == res:
#     print(res,'is a palindrome')
# else:
#     print(res, 'is not a palindrome')


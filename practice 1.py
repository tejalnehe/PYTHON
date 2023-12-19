# print( 5 / 2)

# # to remove after decimal no.

# print(5//2)

# # greater 
# print(3>2)

# if else operator
first=input('enter first no : ')
opt=input('enter op(*,%,/,+,-) : ')
second=input('enter second num : ')
first=int(first)
second=int(second)

if opt=='*':
    print(first*second)
elif opt=='+':
    print(first+second)
elif opt=='-':
    print(first-second)  
else:
    print('invalid')  

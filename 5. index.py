str=input('enter string : ')
i=int(input("enter index : "))
if(len(str)==0):
    print('Empty string')
elif(i>len(str)):
    print("out of index")
else:
    print('character at index',i ,'is',str[i])
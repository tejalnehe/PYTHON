str=input("enter a name : ")
if len(str)<=1:
    print(str)
else:
    for i in range(1 , len(str), 2):
        print(str[i])
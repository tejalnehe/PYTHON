num=int(input("enter a number : "))
x=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp % 10
    sum+=digit **x
    temp//=10

if num==sum:
        print("it is armstrong")
else:
        print("not armstrong")    


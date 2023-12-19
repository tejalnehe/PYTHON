# '''Q.9 prime no'''
def prime():
    num=int(input('enter number:'))
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                print(num, "is not a prime")
                break
            else:
                print(num , "is a prime no") 
prime()      

# '''prime no....Q.3'''           
# num =int(input("Enter a number : "))
# if(num>1):
#     for i in range(2,num):
#         if(num%i==0):
#             print("not a prime number")
#             break
#         else:
#             print("prime number")   
#             break
# else:
#     print("invalid number")     

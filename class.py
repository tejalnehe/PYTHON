class Factorial:
    def factorial_num(self,num):
        if num==0 or num==1:
            return 1
        else:
            return num*self.factorial_num(num-1)
x=Factorial()
print(x.factorial_num(6))
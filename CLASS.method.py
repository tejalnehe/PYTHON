# class Factorial:
#     def factorial_of_number(self,num):
#         if num==0 or num==1:
#          return 1
#         else:
#            return num * self.factorial_of_number(num-1)
# x=Factorial()
# print(x.factorial_of_number(6))


class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_sound(animal):
    return animal.speak()

# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()


current_number = 100
sum_of_evens = 0
while current_number <= 200:
    if current_number % 2 == 0:
        sum_of_evens += current_number
    current_number += 1
print(f"The sum of even numbers between 100 and 200 is: {sum_of_evens}")
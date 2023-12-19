print('.........Append Method.........')
my_list1 = [1,2,3,4]
my_list1.append(5)
print(my_list1)

print()

print('.........extend Method..........')
my_list1 = [1,2,3]
my_list2=[4,5,6,7,8]
my_list1.extend(my_list2)
print(my_list1)

print()

print('..........Insert Method............')
my_list1 = [1,2,3]
my_list1.insert(1,5)
print(my_list1) 

print()

print('..........Remove Method...........')
my_list = [1,4,3,2,4]
my_list.remove(4)
print(my_list) 

print()

print('............Clear Method...........')
my_list = [1,2,3,4,5]
my_list.clear()
print(my_list)
print()

print('..........Slicing Method..........')
my_list = [1,2,3,4,5]
my_list[:] = []
print(my_list) 

print()

print('...........Index Method...........')
my_list = [1,2,3,5,4]
index = my_list.index(3)
print(index)  

print()

print('............count Method............')
my_list = [1,2,3,2,4,3,5,6]
count = my_list.count(2)
print(count)  

print()

print('...........Sort Method.............')
my_list = [53, 1,4,1,5,9,2,7]
my_list.sort()
print(my_list) 

print()

print('.............Reverse Method.............')
my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list) 

print()

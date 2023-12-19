x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
z = int(input("Enter the value for z: "))

if x > y and x > z:
    print("x is greater among y and z")
elif y > x and y > z:
    print("y is greater among x and z")
else:
    print("z is greater")
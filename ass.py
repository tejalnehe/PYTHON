
di = {"Namita": 9878024352,"Tejal": 7802028785,"Ankita": 9698765051,"Priyanka": 8765878343}
sorted_dict = dict(sorted(di.items()))
print(sorted_dict)
print()
name = input("Enter the name to check: ")
if name in di:
    print(f"{name}:{di[name]}")
else:
    phone_number = input(f"Enter the phone number for {name}: ")
    new=di.setdefault(name,phone_number)
    print(name,new)
sorted_updated_dict = dict(sorted(di.items()))
print(sorted_updated_dict)

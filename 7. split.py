str=input('Enter String : ')
if(len(str)<5):
    print("")
else:
    start=str[:3]
    print('starting 3 character is ',start)
    end=str[-3:]
    print('ending 3 character is ' ,end)
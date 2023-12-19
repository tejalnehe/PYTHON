letters = [
    ['h', 'o', 'l', 'i', 'd', 'a', 'y'],
    ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'],
    ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p'],
    ['f', 'l', 'o', 'w', 'c', 'h', 'a', 'r', 't'],
    ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p', 'e', 's']]

words = [
    ["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],
    ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping", "pong", "pram", "prom", "ramp"],
    ["am", "at", "to", "cab", "cap", "cob", "cop", "map", "mop", "act", "bat", "camp", "comb", "boom", "pact",
     "atom"],
    ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow", "fowl", "wolf", "crow",
     "half"],
    ["we", "do", "as", "cap", "caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape", "cope", "crap", "crew",
     "crop", "pace"]]


lives = 5 #if your guess is wrong 5 times... then the game will be ended...
level = 0
Score = 0

while level < len(letters): # we have 5 levels...because we have taken 5 letters......line..,2,3,4,5,6,7
    if lives > 0:
        print(f"Level {level + 1}")
        print("Create 3 words using the given letters:")

        for letter in letters[level]: # eg: if level is 2 then it will print p r o g r a m m i n g 
            print(letter, end='  ')#............only to print user given letters .......eg: h o l i d a y..
        print()

        count = 0
        oldword="" #..it is taken only bcoz the old word should not be repeated
        while count < 3:#.......if your right count is less than 3...then the game will be over...& if right count is =3 then it will go to next level...
            word = input("Enter a word: ").lower()
            
            if  word!=oldword:   
                if word in words[level]:
                    count +=1
                    Score +=1
                    oldword=word


                else:
                    print("Wrong guess")
                    lives -=1  
                    # Score -=1
                    print(f"Lives remaining: {lives}")
                    
                    if lives == 0:
                        print("Game Over")
                        break
                    
            else:
                print("Wrong guess")
                lives -=1  
                # Score -=1
                print(f"Lives remaining: {lives}")

                if lives == 0:
                    print("Game Over")
                    break
    
        else:
            choice = input("Do you want to continue to next level? (yes/no) ").lower()#......if it is 'yes' then only it will go to next level...and if it is 'no' it will end the game...
            if(choice == 'y'):
                level += 1
                    
            else:
                print()
                print('Thanks for playing the game!!!')
                print(f'Your score is {Score}')
                break
                                
    else:
        print('Game Over , Thanks for playing the game!!!')
        print(f'Your score is {Score}')    
        break
    
else:
    if level==5 and lives>0:
       print("Congratulations! You have completed all levels")
       print(f"Your Score is : {Score}")
        
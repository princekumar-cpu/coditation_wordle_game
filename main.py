import random
from time import time
from time import sleep
words = []
temp = []

with open("C:\\Users\\pk032\\Desktop\\company_coding\\wordle_words.txt","r") as f: #Here you have put "wordle_words.txt" path
    temp = f.readlines()
for each in temp:
    each = each.split("\n")[0]
    words.append(each)
print("\n\n\n\n_______________________________________Wordle Clone_______________________________________\n\n")
print("You have 6 chances for today\n")
print("Make sure that the word you choice that have some meaning and word must be of five digit\n\n")
print("So, let's start the game...........\n")

def countdown(t):
    mins, sec = divmod(t,60)
    hour, mins = divmod(mins,60)
    timer = '{:02d}:{:02d}:{:02d}'.format(hour,mins,sec)          
    print("Next Wordle : {}".format(timer),end='\r')
    sleep(1)
    if t == 0:
        main()
    countdown(t-1)

def main():
    count_chance = 0
    a = random.randint(0,len(words))
    rand_word = "keels"#words[a]
    print(rand_word)
    flag = False
    print("\n\nHere character = -1 repsents that the letter does not present in the guessing word")
    print("Here character = 0 repsents that the letter is present in the guessing word but not in corresponding position")
    print("Here character = 1 repsents that the letter is present in the guessing word in corresponding position\n\n")
    while True:
        if (count_chance == 6):
            flag = True
            break
        ch_word = input("\n\nChoice your {} word ".format(count_chance+1)).lower()
        if len(ch_word) == 5:
            count_chance += 1
            if ch_word == rand_word:
                print("Congratulations!  Yon Win this game")
                countdown(24*60*60)
                break
            if ch_word in words:
                for i in ch_word:
                    x = rand_word.count(i)
                    if x == 0:
                        print("{} = {}\t\t".format(i,-1),end="")
                    elif(ch_word.index(i) != rand_word.index(i) and x == 1):
                        print("{} = {}\t\t".format(i,0),end="")
                    elif(ch_word.rindex(i) != rand_word.rindex(i) and x == 2):
                        print("{} = {}\t\t".format(i,0),end="")
                    else:
                        for j in range(len(rand_word)):
                            if ch_word[j] == rand_word[j]:
                                print("{} = {}\t\t".format(i,1),end="")
                                break
            else:
                print("This '{}' word have no meaning ".format(ch_word))
        else:
            print("The word you have chosen have more or less than five character\nDon't worry your is not gone for this")
    
    if flag:
        print("\n\n__________Sorry__________\nYou lost this game. Please try it tomorrow\n\n")
        countdown(24*60*60)

if __name__ == '__main__':
    main()

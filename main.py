import random

words = []
temp = []
with open("C:\\Users\\pk032\\Desktop\\company_coding\\wordle_words.txt","r") as f:
    temp = f.readlines()
for each in temp:
    each = each.split("\n")[0]
    words.append(each)
print("\n\n\n\n_______________________________________Worlde Clone_______________________________________\n\n")
print("You have 6 chances for today\n")
print("Make sure that the word you choice that have some meaning and word should we of five digit\n\n")
print("So, let's start the game...........\n")

def main():
    count_chance = 0
    a = random.randint(0,len(words))
    rand_word = words[a]
    flag = False
    print(rand_word)
    while True:
        if (count_chance == 6):
            flag = True
            break
        ch_word = input("Choice your {} word ".format(count_chance+1))
        if len(ch_word) == 5:
            count_chance += 1
        else:
            print("The word you have chosen have more or less than five character\nDon't worry your is not gone for this")
    


if __name__ == '__main__':
    main()

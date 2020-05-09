#based on hangman program from  Self Taught Programmer   may 2020
#edits by Greg Clements
import random

def gen_stages(i):
    # first stage has no ouput
    stages = [""]
    # each line has a number 0-i exclusive with i being no more than 10
    # lines form an x when printed one after the other
    line_len = (i * 2) - 1
    for x in range(i):
        line_val = str(x)
        # line starts with all blanks
        line = [' '] * line_len
        # reverse numbers after middle to get x pattern
        if x > (i/2):
            x = i - x - 1
        # number of spaces to leave before displaying number
        offset = x * 2
        # first replacement is the first leg/arm of the x
        line[offset] = line_val
        # second replacement is the second leg/arm of the x
        line[line_len - (offset + 1)] = line_val
        # form a string out of the character list
        stages.append(''.join(line))
    return stages

def xout(word,i):
    wrong = 0
    stages = gen_stages(i)
    rletters = list(word)
    board = ["__"] * len(word)
    print((" ".join(board)))   #glc let user know how many letters are in the word
    win  = False
    guessed = []
    while wrong < len(stages)-1 :
        remaining = len(stages)-wrong-1
        if remaining > 1:
            msg = "You have " +str(remaining)+ " wrong guesses remaining.  Guess a letter: "
        else:
            msg = "You have " + str(remaining) + " wrong guess remaining.  Guess a letter: "
        char = input(msg)
        guessed.append(char)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!  The word was <",word,">.  You had ",wrong," wrong guesses for the letters.")
            win = True
            break
        print("\nYou have guessed: ",guessed)


    if not win:
        print("\n" .join(stages[0: wrong+1]))   #
        print("You lose! The word was ...  ",word)   # glc version


#code added by glc
word_list = [["cat","dog","sheep","bear","cow","pig","horse"],["rocket","car","plane","bus","bicycle","truck"],["elm","linden","ash","oak","pine","birch"]]
categories = ["animals","transportation","trees"]
print("Welcome to 'X Out'  ... Select a category for the word.")
invalid_input = True
while invalid_input:
    i_group =int( input("    Enter 1 for animals; 2 for transportation, 3 for trees: ") )
    if i_group < 1 or i_group > 3:
        print("Invalid category: " + str(i_group))
    else:
        invalid_input = False

i_group -=1
print("Guess the letters for a word from the category of ... ",categories[i_group])
invalid_input = True
while invalid_input:
    difficulty = int(input("Enter difficulty 1-10 where 1 is easy and 10 is hard: "))
    if difficulty < 1 or difficulty > 10:
        print("Invalid difficulty: " + str(difficulty))
    else:
        attempts = (10 - difficulty) + 1
        invalid_input = False

print("Two adjacent underscores represent one letter.")
print("If you see a complete X pattern,  you have lost.")
nwords = len(word_list[i_group])

random.seed()
i = random.randint(0,nwords-1)
xout(word_list[i_group][i], attempts)

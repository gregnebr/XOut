#based on hangman program from  Self Taught Programmer   may 2020
#edits by Greg Clements
import random

def set_stages(i):
    # select easy or hard level
    if i == 1:
        stages = ["",
                  "1               1",
                  "  2           2  ",
                  "    3       3    ",
                  "      4   4      ",
                  "        5       ",
                  "      6   6      ",
                  "    7       7    ",
                  "  8           8  ",
                  "9               9"
                  ]

    else:
        stages = ["",
                  "1           1",
                  "  2       2  ",
                  "    3   3    ",
                  "      4      ",
                  "    5   5    ",
                  "  6       6  ",
                  "7           7"
                  ]
    return stages


def xout(word,i):
    wrong = 0
    stages = set_stages(i)
    rletters = list(word)
    board = ["__"] * len(word)
    print((" ".join(board)))   #glc let user know how many letters are in the word
    win  = False
    guessed = []
    while wrong < len(stages)-1 :
        remaining = len(stages)-wrong-1
        if remaining > 1:
            msg = "You have " +str(remaining)+ " guesses remaining.  Guess a letter: "
        else:
            msg = "You have " + str(remaining) + " guess remaining.  Guess a letter: "
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
 #           print(" ".join(board))
            win = True
            break
        print("\nYou have guessed: ",guessed)


    if not win:
        print("\n" .join(stages[0: wrong+1]))   #
#        print("You lose! It was was {}.".format(word))   ....original line
        print("You lose! The word was ...  ",word)   # glc version


#code added by glc
word_list = [["cat","dog","sheep","bear","cow","pig","horse"],["rocket","car","plane","bus","bicycle","truck"],["elm","linden","ash","oak","pine","birch"]]
categories = ["animals","transportation","trees"]
print("Welcome to 'X Out'  ... Select a category for the word.")
i_group =int( input("    Enter 1 for animals; 2 for transportation, 3 for trees: ") )
i_group -=1
print("Guess the letters for a word from the category of ... ",categories[i_group])
i_difficulty = input("Enter 1 for easy and 2 for harder game: ")

print("Two adjacent underscores represent one letter.")
print("If you see a complete X pattern,  you have lost.")
nwords = len(word_list[i_group])

random.seed()
i = random.randint(0,nwords-1)
xout(word_list[i_group][i],i_difficulty)

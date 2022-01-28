# write  a script for the worldie game;

def worldie_solve(word):
    print(
        f"""Welcome to the worldie game puzzle, You have six tries to guess the word,
When you guess a word an array is printed in the console.'*' indicates the letter is in the correct position and in the word.
'+' indicates the letter is in the word but not in the correct position
and '0' indicates the letter is not in the word.
Make sure your input is {len(word)} characters long. if it isn't you lose a round"""
    )
    for i in range(6):
        placements, guess = [], input(
            f"Enter a word, You have {6 - i} tries left: ")
        for j in range(len(word)):
            if len(guess) == len(word):
                if guess[j] == word[j]: placements.append("*")
                elif guess[j] in word: placements.append("+")
                else: placements.append("0")
        print(placements)
        if placements == ["*"] * len(word):
            print('solved')
            return True
    print('You have failed to solve this puzzle')
    return False


print(worldie_solve('worldie'))
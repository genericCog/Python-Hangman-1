word = "banana"
turns = len(word)

guesses = ''
playing = True

while playing:
    failed = 0
    for letter in word:
        if letter in guesses:
            print(letter)   
        else:
            print("_")
            failed += 1
    if failed == 0:        
        print("\nYou won")
        break             

    print()
    guess = input("guess a character:")
    guesses = guesses + guess
    if guess not in word:
        turns -= 1  
        print("Wrong!")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lose\n")
            break

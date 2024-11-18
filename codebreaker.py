import random

def main():
    ans = welcome()
    if ans: # Don't need to put '== True' because it defaults to True unless otherwise specified
        print("Let's get started.")
        mypat = genCode()
        total_b = 0 #Total score counter for black
        total_w = 0 #Total score counter for white

        for i in range(1, 11):
            guess = getPat()
            b, w = scorePat(guess, mypat)
            print(f"Your score for this guess is: {b} b's and {w} w's")
            total_b += b
            total_w += w
            print(f"Your overall score so far is: {total_b} b's and {total_w} w's")

            if b == 4:
                print("You won! My pattern was:", mypat)
                break
        else:
            print("You lost. It was inevitable, really...")
            print("The correct pattern was:", mypat)

# Function to get the player's guess
def getPat():
    while True:
        try:
            player_num = input("Enter your guess as four numbers between 1 and 6 (no spaces): ")
            
            # Check if the input is exactly four digits long and consists only of digits
            if len(player_num) != 4 or not player_num.isdigit():
                print("Error: You must enter exactly four digits.")
                continue  # Ask again if input is invalid

            # Convert each character to an integer and validate the range
            guess = [int(num) for num in player_num]
            if all(1 <= num <= 6 for num in guess):
                print(f"Proceeding with numbers: {guess}")
                return guess  # Return the valid numbers to proceed
            else:
                print("Error: Each number must be between 1 and 6.")
        
        except ValueError: # except command with ValueError will print that statement anytime anything other than an integer is entered.
            print("Error: Invalid input. Please enter four digits.")

# Function to compare the guess with the code
def scorePat(guess, code):
    b = 0
    w = 0	    
    codes= []
    guesses = []
    
    for c, g in zip(code, guess):
        if c == g:
            b += 1
        else:
            codes.append(c)
            guesses.append(g)
    
    for num in guesses:
        if num in codes:
            w += 1
            codes.remove(num)  # Remove to prevent double-counting
        
    return b, w

# Function to generate a random 4-digit code
def genCode():
    code = [random.randint(1, 6) for i in range(4)]
    return code

# Welcome function to start the game
def welcome():
    print("Welcome to the Python version of Mastermind. To play, I will pick four integers in a random order, then ask you to guess what they are.")
    print("To win, you must not only guess my four integers, but you must also have them in the correct order.")
    print("You will have up to 10 guesses. (Note: I can pick the same integer multiple times).")
    
    while True:
        response = input("Would you like to play a game? Enter 'y' to play, or 'n' to cancel: ").lower()
        if response == "y":
            return True
        elif response == "n":
            print("Fine. I didn't want to play with you anyway. Exiting Program...")
            return False
        else:
            print("Error: Please enter 'y' or 'n'.")

def getRole():
    while True:
        role = input("Would you like to be the code maker or code breaker? Enter 'm' for maker or 'b' for breaker: ").lower()
        if role == "m":
            return "maker"
        elif role == "b":
            return "breaker"
        else:
            print("Error: Please enter 'm' or 'b'.")

if __name__ == "__main__":
    main()
    
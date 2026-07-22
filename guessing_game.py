from random import randint

def main():
    print ("Welcome to the Guessing Game!")
    number = randint(1, 10)
    
    while True:
        guess = input("Enter Your Guess Between 1 and 10: ")
    
        if int(guess) == number:
            print ("That's correct, you win.")
            print ("Thank you for playing.\nGoodbye!")
            break
        else:
            print ("That is not correct. Please try again")

if __name__ == '__main__':
    main()
        
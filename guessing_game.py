from random import randint


def main():
    print ("Welcome to the Guessing Game!")
    number = randint(1, 10)
    won = False
    
    for i in range(5): # 5 attempts
        guess = input("Enter Your Guess Between 1 and 10: ")
        if int(guess) == number:
            print ("That's correct, *** You Win ***.")
            print ("Thank you for playing.\nGoodbye!")
            won = True
            return
        else:
                print ("That is not correct. Please try again")
    
    if not won:
        print ("The correct number was {}.\nThank you for plaing.\n*** Game Over ***".format(number))

if __name__ == '__main__':
    main()
        
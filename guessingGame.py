import random

def inputInt(prompt):
	success = False
	while not success:
		try:
			var = input(prompt)
			var = int(var)
			success = True
		except:
			print("[ERROR] input must be an integer")
	return var

def main():
    print("Lets play a guessing game!")
    print("I have picked a number between 1 and 100, can you guess what it is?")
    num = random.randint(1,100)
    guess = inputInt("what is your guess? ")
    while guess != num:
        guess = inputInt("What is your next guess? ")
        if guess > num:
            print("too big try again")
        elif guess < num:
            print("too small try again")
        else:
            pass
    print("That's correct! you've won!")

if __name__ == "__main__":
    main()

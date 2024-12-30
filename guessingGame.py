import random

def inputInt(prompt):
	success = false
	while not success:
		try:
			var = input(prompt)
			var = int(var)
			success = true
		except:
			print("[ERROR] input must be an integer")
	return var

def main():
	print("Lets play a guessing game!")
    print("I have picked a number between 1 and 100, can you guess what it is?")
    num = random.randInt(1,100)
    guess = inputInt("what is your guess? ")
    while guess != num:
        if guess > num:
            print("too big try again")
            guess = inputInt("what is your next guess? ")
        elif guess < num:
            print("too small try again")
            guess = inputInt("what is your next guess? ")
        else:
            print("that's correct!\nYou've won!")

if __name__ == "__main__":
    main()

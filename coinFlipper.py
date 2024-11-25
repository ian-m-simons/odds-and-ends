import random

def main():
    choice = input("would you like to flip a coint? (yes/no): ")
    if "y" in choice or "Y" in choice:
        number = random.randint(0,1)
        if number == 0:
            print("HEADS!")
        else:
            print("Tails!")
    else:
        exit(0)

if __name__ == "__main__":
    main()

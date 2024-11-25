import random

def inputInt(prompt):
    success = False
    while (not success):
        num = input(prompt)
        try:
            num = int(num)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return num


def main():
    print("welcome!")
    sides = inputInt("how many sides should your dice have? ")
    print("ok we'll create ", sides, "sided dice!")
    diceCount = inputInt("how many dice should we roll? ")
    total = 0
    for i in range(diceCount):
        landing = random.randint(1, sides)
        print("di ", i+1, "landed on ", landing)
        total += landing
    print("total comes to ", total)

if __name__ == "__main__":
    main()

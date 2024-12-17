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
def rollDice(sides, diceCount):
    total = 0
    for i in range(diceCount):
        landing = random.randint(1, sides)
        print("di ", i+1, "landed on ", landing)
        total += landing
    print("total comes to ", total)

def main():
   print("welcome!")
   sides = 6
   diceCount = 2
   while True:
       print("\nwhat would you like to do?")
       print("1) change type of dice (default 6 sided di)")
       print("2) change number of dice (default 2)")
       print("3) roll dice")
       print("0) exit")
       choice = inputInt("option: ")
       if choice == 1:
           sides = inputInt("how many sides should your dice have? ")
           while sides < 3:
               print("[ERROR] dice must have at least 3 sides")
               sides = inputInt("how many sides should your dice have? ")
       elif choice == 2:
           diceCount = inputInt("how many dice would you like to have? ")
           while diceCount <1:
               print("[ERROR] must have at least one di")
               diceCount = inputInt("how many dice would you like to have? ")
       elif choice == 3:
           rollDice(sides, diceCount)
       elif choice == 0:
           exit(0)
       else:
           print("[ERROR] invalid option")
if __name__ == "__main__":
    main()

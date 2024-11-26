import random


def spinCylinder(chamber):
    chamber = random.randint(1,6)
    return chamber

def pullTrigger(bullet, chamber):
    if chamber < 6:       
        if (chamber+1) in bullet:
            print("BANG\ndeleteing system32")
            exit(0)
        else:
            print("click")
            if chamber < 6:
                chamber += 1
                return chamber
            else:
                chamber = 1
                return chamber
    else:
        if 1 in bullet:
            print("BANG!\ndeleting system32")
            exit(0)
        else:
            print("click")
            chamber = 1
            return chamber

def Main():
    bullet = [] #this annotates the chamebr containing the bullet
    chamber = 1 #this annotates the current chameber in front of the hammer
    print("lets play a game")
    print("it's called russian roulette")
    new_bullet = int(input("which chamber would you like to put our bullet in (1-6)"))
    bullet.append(new_bullet)
    print("excellent, now the games can get really fun")
    while(True):
        print("select an option\n1) spin cylinder\n2) pull trigger\n3) check current chamber\n4) check which chambers are currently loaded\n5) remove all bullet(s)\n6) add bullet\n0) quit")
        choice = int(input(" "))
        if choice == 0:
            exit(0)
        elif choice == 1:
            chamber = spinCylinder(spinCylinder)
        elif choice == 2: 
            chamber = pullTrigger(bullet, chamber)
        elif choice == 3:
            print(chamber)
        elif choice == 4:
            print("currently there are bullets in the following chambers:")
            print(bullet)
        elif choice == 5:
            print("the gun is now empty")
            bullet = []  
        elif choice == 6:
            new_bullet = int(input("which chamber would you like to add a bullet to? "))
            bullet.append(new_bullet)
        else:
            exit(0)

if __name__ == '__main__':
    Main()
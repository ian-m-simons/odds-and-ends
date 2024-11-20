import random

def inputInt(prompt):
    success = False
    while (not success):
        option = input(prompt)
        try:
            option = int(groupCount)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return option

def main():
    
    while (True):
        print("Welcome! please select an option below!")
        print("1) Enter new list of students")
        print("2) Select Student at random")
        print("3) Reset existing list of students")
        choice = inputInt("option: ")
        if choice == 1:
            raw_list = input("please enter student names separated by a comma, press enter when all students have been added\n")
            students = raw_list.split(",")


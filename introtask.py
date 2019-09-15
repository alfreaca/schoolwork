import random
from time import sleep
import csv
import os

"""
Slot machine
Author: Kit
"""

first = False  # this is a kinda stupid thing that checks if it was the first time a program was run
money_first = False
global current_id
global current_id_money

if not os.path.exists("goes.csv"):
    with open("goes.csv", 'a') as writeFile:
        writer = csv.writer(writeFile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ID', 'first_choice', 'second_choice', 'third_choice'])
        current_id = 1
    writeFile.close()
    first = True

if not first:
    with open('goes.csv', 'r') as f:
        reader = csv.reader(f)
        temp_list = list(reader)
        current_id = temp_list[-1][0]


if not os.path.exists("money.csv"):
    with open("money.csv", 'a') as writeFile:
        writer = csv.writer(writeFile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ID', 'deposited', 'withdrawn'])
        current_id_money = 1
    writeFile.close()
    money_first = True

if not money_first:
    with open('money.csv', 'r') as f:
        reader = csv.reader(f)
        temp_list = list(reader)
        current_id_money = temp_list[-2][0]


# Defining Class
class Machine:

    # Constructor for the variables I think I will need - may change to be honest
    def __init__(self, balance, goes):

        self.balance = balance
        self.goes = goes
        self.ready = 'null'
        self.current_money_id = current_id_money

        try:
            self.current_id = int(current_id)
        except ValueError:
            self.current_id = 1

    def csv_money_writer(self, deposited, withdrawn):
        self.current_money_id += 1
        with open("money.csv", 'a') as writeFile:

            writer = csv.writer(writeFile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([str(current_id_money), deposited, withdrawn])


    # This will make sure it doesn't error when something other than an int is put in.
    def error_handler_input(self):
        money_in = input("Enter the money: ")
        not_int = True
        while not_int:
            try:
                money_in = int(money_in)
                not_int = False
            except ValueError:
                money_in = input("Please enter a number")

        return money_in

    # Function to be called by menu method that will take the money
    def take_money(self):
        temp_balance = self.error_handler_input()
        self.balance += temp_balance

        while_done = False
        while (self.balance % 10) != 0:
            print("Your balance must be a multiple of 10\nPlease enter another coin")
            self.balance += self.error_handler_input()
            print("Current balance is: " + str(self.balance))
            print("Current number of goes left: " + str(self.balance//10))
            self.csv_money_writer(temp_balance, '0')
            while_done = True

        if not while_done:
            print("Current Balance: " + str(self.balance))
            print("Current number of goes left: " + str(self.balance//10))
            self.goes += self.balance//10
            self.csv_money_writer(temp_balance, '0')
            return
        else:
            self.goes += self.balance//10
            return

    def game(self):
        # Print the winning hands then pick 3 random numbers
        hold_one = False
        hold_two = False
        hold_three = False

        print("The winning hands are:\n3 7s for 20, 3 BARs for 5, 3 Bells for 3, 3 Cherry's for 1.\n")

        choices = ['7', 'BAR', 'Bell', 'Cherry', 'Watermelon', 'Grapes', 'Horseshoe']

        self.ready = input("Enter Y to spin: ")

        while self.goes > 0 and self.ready == 'y':
            sleep(1)

            if not hold_one:

                first_choice = random.choice(choices)
                print(first_choice)
                hold_one = False
            else:
                print(first_choice)
                hold_one = False

            sleep(1)

            if not hold_two:
                second_choice = random.choice(choices)
                print(second_choice)
                hold_two = False
            else:
                print(second_choice)
                hold_two = False

            sleep(1)

            if not hold_three:
                third_choice = random.choice(choices)
                print(third_choice+"\n")
                hold_three = False
            else:
                print(third_choice)
                hold_three = False

            sleep(1)

            with open("goes.csv", 'a') as writeFile:
                writer = csv.writer(writeFile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(self.current_id+1), first_choice, second_choice, third_choice])
                writeFile.close()

            self.current_id += 1
            self.goes -= 1

            hold = input("Do you want to hold one[1], two[2] or none[n] of these?: ")

            while hold != '1' and hold != '2' and hold != 'n':
                hold = input("Please enter [1], [2] or [n]: ")

            if hold == 'n':
                pass

            elif hold == '1':
                choice = str(input(
                        "Would you like to hold, the first one [1], the second one[2] or the third one [3]: "))

                while choice != '1' and choice != '2' and choice != '3':
                    choice = str(input("Please enter [1], [2] or [3]: "))

                if choice == '1':
                    hold_one = True

                elif choice == '2':
                    hold_two = True

                else:
                    hold_three = True

            elif hold == '2':
                choice1 = str(input("What is the first one you want to hold? [1], [2] or [3]?: "))

                while choice1 != '1' and choice1 != '2' and choice1 != '3':
                    choice1 = str(input("Please enter [1], [2] or [3]: "))

                if choice1 == '1':
                    hold_one = True

                elif choice1 == '2':
                    hold_two = True

                else:
                    hold_three = True

                choice2 = str(input("What is the second one you want to hold? [1], [2] or [3]: "))

                while choice2 != '1' and choice2 != '2' and choice2 != '3':
                    choice2 = str(input("Please enter [1], [2] or [3]: "))

                if choice2 == '1':
                    hold_one = True

                elif choice2 == '2':
                    hold_two = True

                else:
                    hold_three = True

            if first_choice == '7' or first_choice == 'BAR' or first_choice == 'Bell' or first_choice == 'Cherry':

                if first_choice == second_choice == third_choice:

                    if first_choice == '7':
                        print("Congratulations, 3 7s. You've won £20 ")
                        self.balance += 2000
                        self.csv_money_writer('0', '2000')
                        break

                    elif first_choice == 'BAR':
                        print("Congratulations, 3 BARs. You've won £5")
                        self.balance += 500
                        self.csv_money_writer('0', '500')
                        break

                    elif first_choice == 'Bell':
                        print("Congratulations, 3 Bells. You've won £3")
                        self.balance += 300
                        self.csv_money_writer('0', '300')
                        break

                    elif first_choice == 'Cherry':
                        print("Congratulations, 3 Cherrys. You've won £1")
                        self.balance += 100
                        self.csv_money_writer('0', '100')
                        break

                else:
                    print("Unlucky!")
                    if self.goes == 1:
                        print("You have " + str(self.goes) + " go left.\n\n")
                    else:
                        print("You have " + str(self.goes) + " goes left.\n\n")

                    if self.goes == 0:
                        break
                    else:
                        self.ready = input("Press Y to spin again: ")

            else:
                print("Unlucky!")
                if self.goes == 1:
                    print("You have " + str(self.goes) + " go left.\n\n")
                else:
                    print("You have " + str(self.goes) + " goes left.\n\n")

                if self.goes == 0:
                    break
                else:
                    self.ready = input("Press Y to spin again: ")

    def exit_method(self):
        print("Thanks for playing!")
        sleep(5)
        exit()

    # Menu method to then select which method I need 
    def menu(self):
        choice = input("What would you like to do? [a] insert more money, [b] play the game, or [c] exit: ")
        while choice != "a" and choice != "b" and choice != "c":
            choice = input("Please choose either [a] insert more money, [b] play the game, or [c] exit: ")

        if choice == 'a':
            self.take_money()

        if choice == 'b':
            self.game()
        
        if choice == 'c':
            self.exit_method()

    def main(self):
        while True:
            self.menu()


run = Machine(0, 0)

run.main()


import random
from time import sleep
"""
Slot machine
Author: Kit

7
BAR
Bell
Cherry
Watermelon
Grapes
horseshoe

"""
# Defining Class
class Machine:

    # Constructor for the variables I think I will need - may change to be honest
    def __init__(self, balance, goes):

        self.balance = balance
        self.goes = goes
        self.ready = 'null'

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
        self.balance += self.error_handler_input()
        while_done = False
        while (self.balance % 10) != 0:
            print("Your balance must be a multiple of 10\nPlease enter another coin")
            self.balance += self.error_handler_input()
            print("Current balance is: " + str(self.balance))
            print("Current number of goes left: " + str(self.balance//10))
            while_done = True

        if not while_done:
            print("Current Balance: " + str(self.balance))
            print("Current number of goes left: " + str(self.balance//10))
            self.goes += self.balance//10
            return
        else:
            self.goes += self.balance//10
            return

    def game(self):
        # Print the winning hands then pick 3 random numbers
            print("The winning hands are:\n3 7s for 20, 3 BARs for 5, 3 Bells for 3, 3 Cherry's for 1.\n")

            choices = ['7', 'BAR', 'Bell', 'Cherry', 'Watermelon', 'Grapes', 'Horseshoe']

            self.ready = input("Enter Y to spin: ")

            while self.goes > 0 and self.ready == 'y':
                sleep(1)
                first_choice = random.choice(choices)
                print(first_choice)
                sleep(1)
                second_choice = random.choice(choices)
                print(second_choice)
                sleep(1)
                third_choice = random.choice(choices)
                print(third_choice+"\n")
                sleep(1)

                self.goes -= 1

                if first_choice == '7' or first_choice == 'BAR' or first_choice == 'Bell' or first_choice == 'Cherry':

                    if first_choice == second_choice == third_choice:

                        if first_choice == '7':
                            print("Congratulations, 3 7s. You've won £20 ")
                            self.balance += 20
                             break

                        elif first_choice == 'BAR':
                            print("Congratulations, 3 BARs. You've won £5")
                            self.balance += 5
                            break

                        elif first_choice == 'Bell':
                            print("Congratulations, 3 Bells. You've won £3")
                            self.balance += 3
                            break

                        elif first_choice == 'Cherry':
                            print("Congratulations, 3 Cherrys. You've won £1")
                            self.balance += 1
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

            break
            
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

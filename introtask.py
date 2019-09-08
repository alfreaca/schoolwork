import random
from time import sleep
"""
Slot machine
Author: Kit
"""


class Machine:

    def __init__(self, balance, goes):

        self.balance = balance
        self.goes = goes

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

    def take_money(self):
        money_in = self.error_handler_input()
        while_done = False
        while (money_in % 10) != 0:
            print("Your balance must be a multiple of 10\nPlease enter another coin:")
            money_in = money_in + self.error_handler_input()
            print("Current balance is: " + str(money_in))
            while_done = True

        self.balance = money_in

        if not while_done:
            print("Current Balance: " + str(self.balance))
            return
        else:
            return

    def game(self):
       pass

    def exit(self):
        print("Thanks for playing!")
        sleep(10)
        exit()

    def menu(self):
        choice = ("What would you like to do? [a] insert more money, [b] play the game, or [c] exit")
        




run = Machine(0, 0)

run.take_money()

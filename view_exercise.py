#!/usr/bin/env python3

import random

def main_menu():
    print("\nWelcome to Terminal Teller!:")
    print("\n1) create account\n2) log in\n3) quit")
    return input("\nYour choice: ")

def account_creation_menu_FN():
    print("\nAccount creation")
    return input("\nFirst Name: ")

def account_creation_menu_LN():
    return input("Last Name: ")

def account_creation_menu_PIN():
    x = True
    while x == True:
        PIN1 = input("PIN: ")
        PIN2 = input("confirm PIN: ")
        if PIN1 == PIN2:
            x = False
    return PIN2

def log_in_menu_accn():
    return input("\nAccount number: ")

def log_in_menu_pin():    
    return input("PIN: ")

def user_loggedin_menu():
    print("\n1) Check balance\n2) Withdraw funds\n3) Deposit funds\n4) Sign out")
    return input("\nYour choice: ")

def user_withdraw_money():
    return float(input("\nHow much to withdraw: "))

def user_deposit_money():
    return float(input("\nHow much to deposit: "))

def user_quit():
    print("\nGoodbye!")

if __name__ == "__main__":
    #print(main_menu())
    #print(account_creation_menu())
    #print(log_in_menu())
    #print(user_loggedin_menu())
    print(user_quit())

#!/usr/bin/env python3

import sqlite3
from random import *
import view_exercise
from model_exercise import User
from mappers_exercises import Database

def log_in_menu():

    if mm_input == "2":
        
        x = True
        while x == True:
            input_accn = view_exercise.log_in_menu_accn()
            input_pin = view_exercise.log_in_menu_pin()
            with sqlite3.connect("accounts.db") as conn:
                cur = conn.cursor()
                cur.execute('SELECT password from user WHERE account_number = ?;', (input_accn,))
            correct_pwd = cur.fetchone()[0]
                            
            if correct_pwd == input_pin:
                x = False
            else:
                print("Wrong password, try again!")

        with sqlite3.connect("accounts.db") as conn:
            cur = conn.cursor()
            cur.execute('SELECT balance from user WHERE account_number = ?;', (input_accn,))
        check_balance = cur.fetchone()[0]
        
        with sqlite3.connect("accounts.db") as conn:
            cur = conn.cursor()
            cur.execute('SELECT first_name from user WHERE account_number = ?;', (input_accn,))
        log_in_first_name = cur.fetchone()[0]
        
        User1 = User(log_in_first_name, "xx", input_accn, "xx", check_balance)
    
        loggedin_menu_inputs = ["1", "2", "3", "4"]                            
    
        x = True
        while x == True:
            print("\nHello " + User1.first_name + "(" + User1.account_number + ")" + ", welcome to your account!")
            user_loggedin_menu_input = view_exercise.user_loggedin_menu()
            if user_loggedin_menu_input in loggedin_menu_inputs:
                   
                if user_loggedin_menu_input == "1":
                    print("\nYour balance is "+ "$" + str(User1.balance))
                        
                elif user_loggedin_menu_input == "2":
                    withdraw_amount = view_exercise.user_withdraw_money()
                    if User1.balance - withdraw_amount < 0:
                        print ("!! INSUFFICIENT FUNDS !!")
                    else:
                        User1.withdraw_money(withdraw_amount)
                        with sqlite3.connect("accounts.db") as conn:
                            cur = conn.cursor()
                            cur.execute('UPDATE user SET balance = ? WHERE account_number = ?;', (User1.balance, input_accn))

                elif user_loggedin_menu_input == "3":
                    deposit_amount = view_exercise.user_deposit_money()
                    User1.deposit_money(deposit_amount)
                    with sqlite3.connect("accounts.db") as conn:
                        cur = conn.cursor()
                        cur.execute('UPDATE user SET balance = ? WHERE account_number = ?;', (User1.balance, input_accn))    
    
                elif user_loggedin_menu_input == "4" or user_loggedin_menu_input == "4)":
                    x = False
                    
def quit_from_menu():

    if mm_input == "3":

        view_exercise.user_quit()

if __name__ == "__main__":
    
    # This loops main menu and login menu
    loop_from_beginning = True

    while loop_from_beginning == True:

        mm_input = view_exercise.main_menu()
        
        # Keeps looping the main menu as long as input is "1"
        while mm_input == "1":
            
            FN = view_exercise.account_creation_menu_FN()
            LN = view_exercise.account_creation_menu_LN()
            PIN = view_exercise.account_creation_menu_PIN()
            BAL = 0.00
            
            # Ensuring no account number is duplicated
            while True:
                ACCN = randint(100000,1000000)
                with sqlite3.connect("accounts.db") as conn:
                    cur = conn.cursor()
                    cur.execute('SELECT first_name from user WHERE account_number = ?;', (ACCN,))
                matched = cur.fetchone()
                if matched == None:
                    break
                
            print("\nAccount created, your account number is", str(ACCN))
            
            # Inserts user info into the user table
            with sqlite3.connect("accounts.db") as conn:
                cur = conn.cursor()
                cur.execute(
                '''INSERT INTO user
                    ("account_number", "first_name", "last_name", "password", "balance") VALUES(?, ?, ?, ?, ?);''', (ACCN, FN, LN, PIN, BAL))

            mm_input = view_exercise.main_menu()
        
        # If "3" is input by user, the big while loop (i.e. main menu and log-in menu) breaks
        if mm_input == "3":
            break
        
        # If "2" is input by user, it goes into the log-in menu and then the account activity menu
        log_in_menu()
    
    # Terminates from the terminal after "3" is input by user
    quit_from_menu()
        
        

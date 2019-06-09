#!/usr/bin/env python3

import sqlite3

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("accounts.db")
        self.cursor     = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        if self.connection:
            if self.cursor:
                self.connection.commit()
                self.cursor.close()
            self.connection.close()
    
    def create_table(self, table_name):
        self.cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
        self.cursor.execute(
            f'''CREATE TABLE {table_name}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT);''')        

    def add_column(self, table_name, column_name, column_type):
        self.cursor.execute(
            f'''ALTER TABLE {table_name}
                ADD COLUMN {column_name} {column_type};''')

    def insert_into_column(self, value1, value2, value3, value4, value5):
        self.cursor.execute(
            '''INSERT INTO user
                ("account_number", "first_name", "last_name", "password", "balance") VALUES(?, ?, ?, ?, ?);''', (value1, value2, value3, value4, value5))

if __name__ == "__main__":
    Database().create_table("user")
    Database().add_column("user", "account_number", "VARCHAR")
    Database().add_column("user", "first_name", "VARCHAR")
    Database().add_column("user", "last_name", "VARCHAR")
    Database().add_column("user", "password", "VARCHAR")
    Database().add_column("user", "balance", "FLOAT")    

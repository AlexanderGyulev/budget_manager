import tkinter as tk
from ui import ExpenseTrackerUI
import sqlite3

class ExpenseTracker:
    def __init__(self):

        self.con = sqlite3.connect("expenses.db")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         amount REAL NOT NULL,
                         category TEXT,
                         date TEXT NOT NULL,
                         description TEXT,
                         type TEXT NOT NULL)""")
        self.con.commit()

    def add_transaction(self, amount, category, date, description, transaction_type):
        try:
            self.cur.execute("""
                INSERT INTO transactions (amount, category, date, description, type)
                VALUES (?, ?, ?, ?, ?)
            """, (amount, category, date, description, transaction_type))
            self.con.commit()
        except Exception as err:
            print(f"An exception occurred. Insert unsuccessful.")
            print(err)

    def remove_transaction(self, transaction_id):
        try:
            self.cur.execute("""
                DELETE FROM transactions WHERE id = ?
            """, (transaction_id,))
            self.con.commit()
        except Exception as err:
            print(f"An exception occurred. Delete unsuccessful.")
            print(err)

    def update_transaction(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    actions = ExpenseTracker()
    app = ExpenseTrackerUI(root, actions)
    root.mainloop()
import tkinter as tk
from tkinter import ttk


class ExpenseTrackerUI:
    def __init__(self, root, action_manager):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x400")
        self.action_manager = action_manager
        self.build_ui()

    def build_ui(self):
        self.treeview = ttk.Treeview(self.root, columns=("id", "description", "amount", "transaction_type"), show="headings")
        self.expenses_label = tk.Label(self.root, text="Transactions:")
        self.expenses_label.pack()
        self.treeview.heading("id", text="ID")
        self.treeview.heading("description", text="Description")
        self.treeview.heading("amount", text="Amount")
        self.treeview.heading("transaction_type", text="Type")
        self.treeview.pack(fill="both", expand=True)
        self.add_button = tk.Button(self.root, text="Add an Expense", command=self.add_clicked)
        self.add_button.pack(side="left")
        self.remove_button = tk.Button(self.root, text="Remove Transaction", command=self.remove_clicked)
        self.remove_button.pack(side="right")

    def add_clicked(self):
        self.transaction_window = tk.Toplevel()
        self.transaction_window.title("Add a new transaction")
        self.transaction_window.geometry("400x200")
        self.amount_var = tk.StringVar()
        self.amount_label = tk.Label(self.transaction_window, text="Please enter the amount:")
        self.amount_label.pack()
        self.amount = tk.Entry(self.transaction_window, textvariable=self.amount_var)
        self.amount.pack()
        self.transaction_options = ["Income", "Expense"]
        self.transaction_box = ttk.Combobox(self.transaction_window,values=self.transaction_options)
        self.transaction_box.set("Select transaction type")
        self.transaction_box.pack()

    def submit_validations(self):
        try:
            self.num_amount = self.amount_var.get()
            self.num_amount = float(self.num_amount)
        except ValueError:
            print("Amount is not a float.")

        return self.num_amount

    def remove_clicked(self):
        pass

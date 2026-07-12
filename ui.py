import tkinter as tk
from tkinter import ttk

class ExpenseTrackerUI:
    def __init__(self, root, action_manager):
        self.root = root
        self.root.title("Expense Tracker by AG")
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
        self.add_button = tk.Button(self.root, text="Add an Expense", command=self.on_add)
        self.add_button.pack(side="left")
        self.remove_button = tk.Button(self.root, text="Remove Transaction", command=self.on_remove)
        self.remove_button.pack(side="right")

    def on_add(self):
        pass
    def on_remove(self):
        pass

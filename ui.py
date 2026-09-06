import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class ExpenseTrackerUI:
    def __init__(self, root, action_manager):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x400")
        self.action_manager = action_manager
        self.build_ui()
        self.reload_ui()


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
        self.amount_label = tk.Label(self.transaction_window, text="Please enter the amount:")
        self.amount_label.pack()
        self.amount_var = tk.StringVar()
        self.amount = tk.Entry(self.transaction_window, textvariable=self.amount_var)
        self.amount.pack()
        self.transaction_categories = ("Food", "Groceries", "Shopping", "Housing", "Utilities", "Transportation", "Entertainment",
                                       "Healthcare", "Dining out", "Travel", "Savings/Investments", "Other")
        self.transaction_cat_box = ttk.Combobox(self.transaction_window,values=self.transaction_categories)
        self.transaction_cat_box.set("Select category")
        self.transaction_cat_box.pack()
        self.date_label = tk.Label(self.transaction_window,text="Please enter a date:")
        self.date_label.pack()
        self.date_selector = DateEntry(self.transaction_window, date_pattern="dd-mm-yyyy")
        self.date_selector.pack()
        self.desc_label = tk.Label(self.transaction_window, text="Please enter a description:")
        self.desc_label.pack()
        self.desc_var = tk.StringVar()
        self.desc_entry = tk.Entry(self.transaction_window, textvariable=self.desc_var)
        self.desc_entry.pack()
        self.transaction_options = ("Income", "Expense")
        self.transaction_type_box = ttk.Combobox(self.transaction_window,values=self.transaction_options)
        self.transaction_type_box.set("Select transaction type")
        self.transaction_type_box.pack()
        self.submit_button = tk.Button(self.transaction_window, text="Submit", command=self.submit_validations)
        self.submit_button.pack()

    def submit_validations(self):
        try:
            self.num_amount = float(self.amount_var.get())
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter an amount.")
            return None
        if self.transaction_cat_box.get().strip() not in self.transaction_categories:
            messagebox.showerror("Invalid Transaction Category", "Please select a transaction category.")
            return None
        if self.transaction_type_box.get().strip() not in self.transaction_options:
            messagebox.showerror("Invalid Transaction Type", "Please select a transaction type.")
            return None

        self.action_manager.add_transaction(self.num_amount, self.transaction_cat_box.get(), self.date_selector.get(),
                                            self.desc_entry.get(), self.transaction_type_box.get())
        self.reload_ui()

    def reload_ui(self):
        initial_data = self.action_manager.cur.execute("SELECT * FROM transactions")
        data = initial_data.fetchall()
        for row in data:
            self.treeview.insert('', 'end', values=(row[0], row[4], row[1], row[5]))

    def remove_clicked(self):
        pass

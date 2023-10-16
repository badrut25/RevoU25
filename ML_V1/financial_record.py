import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import csv

# Create the main window
window = tk.Tk()
window.title("Financial Record App")
window.geometry("400x400")
window.configure(bg="#FFFFFF")

# Create variables to store the current balance, total income, total expenses, and transaction history
balance = 0
income = 0
expenses = 0
transactions = []

# Function to update the balance label
def update_balance():
    balance_label.config(text=f"Balance: ${balance}")

# Function to update the total income and total expenses labels
def update_income_expenses():
    income_label.config(text=f"Total Income: ${income}")
    expenses_label.config(text=f"Total Expenses: ${expenses}")

# Function to add an income transaction
def add_income():
    amount = income_entry.get()

    if not amount:
        messagebox.showwarning("Missing Information", "Please enter the income amount.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Invalid Amount", "Please enter a valid numeric amount.")
        return

    global balance, income
    balance += amount
    income += amount

    update_balance()
    update_income_expenses()

    income_entry.delete(0, tk.END)

# Function to add an expense transaction
def add_expense():
    description = expense_description_entry.get()
    amount = expense_amount_entry.get()

    if not description or not amount:
        messagebox.showwarning("Missing Information", "Please enter both description and amount.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Invalid Amount", "Please enter a valid numeric amount.")
        return

    global balance, expenses
    balance -= amount
    expenses += amount

    transactions.append((description, amount))
    transaction_list.insert(tk.END, f"Expense: {description}: ${amount}")

    update_balance()
    update_income_expenses()

    expense_description_entry.delete(0, tk.END)
    expense_amount_entry.delete(0, tk.END)

# Function to save transactions to a CSV file
def save_to_csv():
    if not transactions:
        messagebox.showwarning("No Transactions", "There are no transactions to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

    if file_path:
        try:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(transactions)
            messagebox.showinfo("CSV Saved", "Transactions have been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the CSV file:\n\n{str(e)}")

# Create the balance label
balance_label = tk.Label(window, text="Balance: $0", font=("Arial", 12), bg="#FFFFFF")
balance_label.pack(pady=10)

# Create the income frame
income_frame = tk.Frame(window, bg="#FFFFFF")
income_frame.pack(pady=10)

# Create the income entry
income_label = tk.Label(income_frame, text="Income ($):", font=("Arial", 12), bg="#FFFFFF")
income_label.pack(side=tk.LEFT, padx=5)

income_entry = tk.Entry(income_frame, font=("Arial", 12))
income_entry.pack(side=tk.LEFT)

# Create the add income button
income_button = tk.Button(window, text="Add Income", command=add_income, font=("Arial", 12))
income_button.pack(pady=10)

# Create the expense frame
expense_frame = tk.Frame(window, bg="#FFFFFF")
expense_frame.pack(pady=10)

# Create the expense description label and entry
expense_description_label = tk.Label(expense_frame, text="Expense Description:", font=("Arial", 12), bg="#FFFFFF")
expense_description_label.pack(side=tk.LEFT, padx=5)

expense_description_entry = tk.Entry(expense_frame, font=("Arial", 12))
expense_description_entry.pack(side=tk.LEFT)

# Create the expense amount label and entry
expense_amount_label = tk.Label(expense_frame, text="Amount ($):", font=("Arial", 12), bg="#FFFFFF")
expense_amount_label.pack(side=tk.LEFT, padx=5)

expense_amount_entry = tk.Entry(expense_frame, font=("Arial", 12))
expense_amount_entry.pack(side=tk.LEFT)

# Create the add expense button
expense_button = tk.Button(window, text="Add Expense", command=add_expense, font=("Arial", 12))
expense_button.pack(pady=10)

# Create the transaction frame
transaction_frame = tk.Frame(window, bg="#FFFFFF")
transaction_frame.pack(pady=10)

# Create the transaction listbox
transaction_list = tk.Listbox(transaction_frame, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
transaction_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the scrollbar for the transaction listbox
scrollbar = tk.Scrollbar(transaction_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the scrollbar
transaction_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=transaction_list.yview)

# Create the total income label
income_label = tk.Label(window, text="Total Income: $0", font=("Arial", 12), bg="#FFFFFF")
income_label.pack(pady=10)

# Create the total expenses label
expenses_label = tk.Label(window, text="Total Expenses: $0", font=("Arial", 12), bg="#FFFFFF")
expenses_label.pack(pady=10)

# Create the save to CSV button
save_button = tk.Button(window, text="Save to CSV", command=save_to_csv, font=("Arial", 12))
save_button.pack(pady=10)

# Start the main loop
window.mainloop()

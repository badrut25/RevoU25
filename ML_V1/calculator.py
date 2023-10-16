import tkinter as tk

# Function to update the expression in the entry field
def update_expression(text):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + text)

# Function to perform the calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except ZeroDivisionError:
        result_label.config(text="Error: Division by zero")
    except SyntaxError:
        result_label.config(text="Error: Invalid syntax")
    except:
        result_label.config(text="Error: Invalid input")

# Function to clear the entry field and result label
def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(window, text=button, width=5, command=calculate)
        btn.grid(row=row, column=col, padx=5, pady=5)
    else:
        btn = tk.Button(window, text=button, width=5, command=lambda x=button: update_expression(x))
        btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the result label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=row, column=0, columnspan=4)

# Create the clear button
clear_button = tk.Button(window, text="Clear", width=20, command=clear)
clear_button.grid(row=row+1, column=0, columnspan=4, padx=10, pady=10)

# Start the main loop
window.mainloop()

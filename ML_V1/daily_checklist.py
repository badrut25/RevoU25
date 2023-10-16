import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

# Create the main window
window = tk.Tk()
window.title("Daily Checklist App")
window.geometry("400x500")
window.configure(bg="#FFFFFF")

# Create a list to store the checklist items
checklist_items = []

# Function to add a new checklist item
def add_item():
    item = entry.get()
    if item:
        checklist_items.append(item)
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

# Function to remove the selected checklist item
def remove_item():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        checklist_items.pop(index)
        listbox.delete(index)

# Function to generate the PDF report
def generate_pdf():
    if checklist_items:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)  # Use DejaVuSans font
        pdf.cell(200, 10, txt="Daily Checklist Report", ln=True, align="C")
        pdf.ln(10)
        for item in checklist_items:
            pdf.cell(10, 10, txt=u"\u2022", ln=False, align="L")  # Add bullet point character
            pdf.multi_cell(0, 10, txt=item, align="L")
            pdf.ln(5)
        pdf.output("daily_checklist.pdf")
        messagebox.showinfo("PDF Generated", "The PDF report has been generated successfully.")
    else:
        messagebox.showwarning("Empty Checklist", "The checklist is empty. Add some items before generating the PDF.")

# Create the checklist frame
checklist_frame = tk.Frame(window, bg="#FFFFFF")
checklist_frame.pack(pady=10)

# Create the checklist display
listbox = tk.Listbox(checklist_frame, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add scrollbar to the checklist
scrollbar = tk.Scrollbar(checklist_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create the input frame
input_frame = tk.Frame(window, bg="#FFFFFF")
input_frame.pack(pady=10)

# Create the input field
entry = tk.Entry(input_frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=10)

# Create the buttons
add_button = tk.Button(input_frame, text="Add Item", command=add_item, font=("Arial", 12))
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(window, text="Remove Item", command=remove_item, font=("Arial", 12))
remove_button.pack(pady=5)

generate_button = tk.Button(window, text="Generate PDF", command=generate_pdf, font=("Arial", 12))
generate_button.pack(pady=5)

# Start the main loop
window.mainloop()

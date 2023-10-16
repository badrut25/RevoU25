import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from plyer import notification
import schedule
import time

# Create the main window
window = tk.Tk()
window.title("Clock App")
window.geometry("400x400")
window.configure(bg="#FFFFFF")

# Create the label to display the current time
time_label = tk.Label(window, text="", font=("Arial", 24), bg="#FFFFFF")
time_label.pack(pady=20)

# Function to update the time label
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)  # Update every 1 second

# Start updating the time label
update_time()

# Function to handle the "Add Event" button click
def add_event():
    calendar_date = calendar.selection_get()
    note_text = note_entry.get()

    if note_text:
        event = f"Event Date: {calendar_date.strftime('%Y-%m-%d')} | Note: {note_text}"
        event_listbox.insert(tk.END, event)
        set_event_reminder(event)
    else:
        messagebox.showwarning("Missing Information", "Please enter a note for the event.")

    note_entry.delete(0, tk.END)

# Create the calendar label and button
calendar_label = tk.Label(window, text="Select Date:", font=("Arial", 12), bg="#FFFFFF")
calendar_label.pack(pady=5)

calendar_frame = tk.Frame(window, bg="#FFFFFF")
calendar_frame.pack()

calendar = Calendar(calendar_frame, selectmode="day")
calendar.pack()

# Create the note label and entry
note_label = tk.Label(window, text="Note for Event:", font=("Arial", 12), bg="#FFFFFF")
note_label.pack(pady=5)
note_entry = tk.Entry(window, font=("Arial", 12))
note_entry.pack()

# Create the "Add Event" button
add_event_button = tk.Button(window, text="Add Event", command=add_event, font=("Arial", 12))
add_event_button.pack(pady=10)

# Create the event listbox
event_listbox = tk.Listbox(window, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
event_listbox.pack(pady=10)

# Function to handle the "Delete Event" button click
def delete_event():
    selected_event = event_listbox.curselection()
    if selected_event:
        event_listbox.delete(selected_event)
    else:
        messagebox.showwarning("No Event Selected", "Please select an event to delete.")

# Create the "Delete Event" button
delete_event_button = tk.Button(window, text="Delete Event", command=delete_event, font=("Arial", 12))
delete_event_button.pack(pady=10)

# Create the save to text file button
def save_to_file():
    events = event_listbox.get(0, tk.END)

    if not events:
        messagebox.showwarning("No Events", "There are no events to save.")
        return

    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if file_path:
        try:
            with open(file_path, "w") as file:
                for event in events:
                    file.write(event + "\n")
            messagebox.showinfo("File Saved", "Events have been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file:\n\n{str(e)}")

save_button = tk.Button(window, text="Save to Text File", command=save_to_file, font=("Arial", 12))
save_button.pack(pady=10)

# Function to handle the "Set Reminder" button click
def set_reminder():
    selected_event = event_listbox.get(event_listbox.curselection())
    if selected_event:
        event_date = selected_event.split("|")[0].strip().split(":")[1].strip()
        event_note = selected_event.split("|")[1].strip().split(":")[1].strip()

        notification_title = "Event Reminder"
        notification_message = f"Event: {event_note}"
        notification_timeout = 10  # Display the notification for 10 seconds

        notification.notify(title=notification_title, message=notification_message, timeout=notification_timeout)
    else:
        messagebox.showwarning("No Event Selected", "Please select an event to set a reminder.")

# Create the "Set Reminder" button
set_reminder_button = tk.Button(window, text="Set Reminder", command=set_reminder, font=("Arial", 12))
set_reminder_button.pack(pady=10)

# Function to set a reminder for the event
def set_event_reminder(event):
    event_date_str = event.split("|")[0].strip().split(":")[1].strip()
    event_date = time.strptime(event_date_str, "%Y-%m-%d")
    event_note = event.split("|")[1].strip().split(":")[1].strip()

    # Schedule the reminder notification
    def notify_reminder():
        notification_title = "Event Reminder"
        notification_message = f"Event: {event_note}"
        notification_timeout = 10  # Display the notification for 10 seconds

        notification.notify(title=notification_title, message=notification_message, timeout=notification_timeout)

    schedule_date = time.strftime("%Y-%m-%d", event_date)
    schedule_time = "09:00"  # Set the reminder time to 9:00 AM (modify as needed)

    schedule_time_str = f"{schedule_date} {schedule_time}"
    schedule_time_obj = time.strptime(schedule_time_str, "%Y-%m-%d %H:%M")

    schedule.every().day.at(time.strftime("%H:%M", schedule_time_obj)).do(notify_reminder)

# Function to update the scheduled events
def update_scheduled_events():
    schedule.run_pending()
    window.after(1000, update_scheduled_events)  # Check every 1 second

update_scheduled_events()

# Start the main loop
window.mainloop()

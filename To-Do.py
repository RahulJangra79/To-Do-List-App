import tkinter as tk
from tkinter import messagebox

# Set up the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#f0f0f0")  # Background color

# Customize fonts
button_font = ("Helvetica", 12, "bold")
entry_font = ("Arial", 12)
listbox_font = ("Arial", 10)

# Create a frame for the task input
input_frame = tk.Frame(root, bg="#f2f2f2")
input_frame.pack(pady=20)

# Entry for task name with custom style
task_name_entry = tk.Entry(input_frame, width=30, 
                           font=entry_font, bd=2)
task_name_entry.grid(row=0, column=0, padx=10)

# Button to add tasks with custom style
add_task_button = tk.Button(input_frame, text="Add Task", 
                            font=button_font, bg="orange", 
                            fg="white", command=lambda: add_task())
add_task_button.grid(row=0, column=1, padx=10)

# Listbox to display tasks with scrollbar
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_listbox = tk.Listbox(task_frame, width=45, height=15, 
                          font=listbox_font, bd=0, highlightthickness=0, 
                          selectbackground="#a6a6a6", activestyle="none")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Frame for task control buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=20)

# Button to remove task with custom style
remove_task_button = tk.Button(button_frame, text="Remove Task", 
                               font=button_font, bg="red", fg="white", 
                               command=lambda: remove_task())
remove_task_button.grid(row=0, column=0, padx=10)

# Button to mark task as completed with custom style
complete_task_button = tk.Button(button_frame, text="Mark as Completed", 
                                 font=button_font, bg="green", fg="white", 
                                 command=lambda: mark_as_completed())
complete_task_button.grid(row=0, column=1, padx=10)

# Exit button to close the application with custom style
exit_button = tk.Button(root, text="Exit", font=button_font, 
                        bg="#d3d3d3", command=root.destroy)
exit_button.pack(pady=10)

# Functions for managing tasks
def add_task():
    task = task_name_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task name.")

def remove_task():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_as_completed():
    try:
        selected_task = task_listbox.curselection()
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(tk.END, task + " - Completed")
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Run the application
root.mainloop()

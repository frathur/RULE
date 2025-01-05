import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a password
def generate_password():
    characterset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    length = 12  # Desired password length
    # Generate password
    password_list = random.choices(characterset, k=length)
    password = ''.join(password_list)
    password_entry.delete(0, tk.END)  # Clear the entry widget
    password_entry.insert(0, password)  # Display the password in the entry widget

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()  # Update the clipboard
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Tkinter GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# GUI elements
title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
password_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

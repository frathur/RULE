import re
import random
import string
import tkinter as tk
from tkinter import messagebox




def check_passwd_strength(password):
    """
    Check the strength of a password and suggest improvements.
    """
    strength = 0
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    else:
        strength += 1

    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    else:
        strength += 1

    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    else:
        strength += 1

    if not re.search(r'[0-9]', password):
        suggestions.append("Include at least one number.")
    else:
        strength += 1

    if not re.search(r'[!@#$%^&*(),./<>?~`|{\[\]}\\]', password):
        suggestions.append("Include at least one special character (e.g., !@#%$%^ .")
    else:
        strength += 1

    #Classify password strength
    if strength == 5:
        return "Strong", []
    elif strength >= 3:
        return "Moderate", []
    else:
        return "Weak", []


def generate_password(length=12):
    """Generate a secure random password."""
    if length < 8:
        length = 8

    characterset = string.ascii_letters + string.digits + "`~!@#$%^&*()_+-={}[]|\\:;\'?\"<>??/"

    #Ensuring that the password include at least one of each required character type
    password = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.choice(string.digits), random.choice("`~!@#$%^&*()_+-={}[]|\\:;\'?\"<>??/")]

    #Fill the rest of the password with random choices
    password = password + random.choices(characterset, k=length-4)

    #Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

def display_generated_passwd():
    """Generate and display a secure random password."""

    length = 12
    generated_passwd = display_generated_passwd(length)

    entry_password.delete(0, tk.END)

    entry_password.insert(0, generated_passwd)


def check_passwd():
    """Get password input from the user and display results"""

    password = entry_password.get()
    strength, suggestions = check_passwd_strength(password)

    result_text = f"Password Strength: {strength} "
    if suggestions:
        result_text += "\n\nSuggestions: \n" + "\n".join(suggestions)

        messagebox.showinfo("Password Strength Checker", result_text)


root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:", font=("Arial",14))
label.pack(pady=0)

entry_password = tk.Entry(root, width=30, font=("Arial",14), show="")
entry_password.pack(pady=10)

button_check = tk.Button(root, text="Check Strength", font=("Arial",14), command=check_passwd)
button_check.pack(pady=10)

button_generate = tk.Button(root, text="Generate Password", font=("Arial",14), command=display_generated_passwd)
button_generate.pack(pady=10)

root.geometry("400x300")
root.mainloop()
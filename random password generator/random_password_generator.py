import secrets
import string
import tkinter as tk
from tkinter import messagebox

#custom symbols
CUSTOM_SYMBOLS = "!@#$%&*?"

#password gen function
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    characters = ""
    password = []

    if lower_var.get():
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if upper_var.get():
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if digits_var.get():
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if symbols_var.get():
        characters += CUSTOM_SYMBOLS
        password.append(secrets.choice(CUSTOM_SYMBOLS))

    if not characters:
        messagebox.showerror("Error", "Select at least one character type")
        return

    # fill remaining length
    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    # shuffle securely
    secrets.SystemRandom().shuffle(password)

    result = "".join(password)
    password_var.set(result)


#copy function
def copy_to_clipboard():
    password = password_var.get()
    if not password:
        messagebox.showwarning("Warning", "No password to copy")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")


#gui
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x420")
root.resizable(False, False)

#title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

#length input
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

#checkboxes
lower_var = tk.BooleanVar()
upper_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=digits_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text=f"Include Symbols ({CUSTOM_SYMBOLS})", variable=symbols_var).pack(anchor="w", padx=50)

#generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

#output field
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30, font=("Arial", 12), justify="center").pack(pady=5)

#copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

#run app
root.mainloop()
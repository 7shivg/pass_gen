import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    # Create a custom Toplevel dialog box
    output_dialog = tk.Toplevel(root)
    output_dialog.title("Generated Password")
    
    # Set the size of the dialog box
    output_dialog.geometry("400x200")

    label_password = tk.Label(output_dialog, text=f"Your random password is:\n{password}")
    label_password.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Random Password Generator")

    label_length = tk.Label(root, text="Password Length:")
    label_length.pack()

    entry_length = tk.Entry(root)
    entry_length.pack()

    btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
    btn_generate.pack()

    root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Initialize Tkinter
root = tk.Tk()
root.title("Contact Book")

# Initialize contacts list
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Check if all fields are filled
    if name == '' or email == '' or phone == '':
        messagebox.showerror("Error", "Please fill all fields.")
        return

    contact = {"Name": name, "Email": email, "Phone": phone}
    contacts.append(contact)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Phone:").grid(row=2, column=0, padx=5, pady=5)

# Entry fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Start the GUI
root.mainloop()

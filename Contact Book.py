import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts (name, phone, email, address)
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END)[:-1]  # Remove the trailing newline
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Please enter a name and phone number.")

# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts.keys():
        contact_list.insert(tk.END, name)

# Function to display contact details when a contact is selected
def show_contact_details(event):
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact in contacts:
        details = contacts[selected_contact]
        details_text.config(state=tk.NORMAL)
        details_text.delete("1.0", tk.END)
        details_text.insert(tk.END, f"Name: {selected_contact}\n")
        details_text.insert(tk.END, f"Phone: {details['Phone']}\n")
        details_text.insert(tk.END, f"Email: {details['Email']}\n")
        details_text.insert(tk.END, f"Address:\n{details['Address']}\n")
        details_text.config(state=tk.DISABLED)

# Function to search for a contact by name or phone number
def search_contact():
    query = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)
    
    for name, details in contacts.items():
        if query in name.lower() or query in details["Phone"]:
            contact_list.insert(tk.END, name)

# Function to update contact details
def update_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact in contacts:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get("1.0", tk.END)[:-1]  # Remove the trailing newline
        
        if name and phone:
            contacts[selected_contact] = {"Phone": phone, "Email": email, "Address": address}
            update_contact_list()
            clear_fields()
        else:
            messagebox.showwarning("Warning", "Please enter a name and phone number.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact in contacts:
        del contacts[selected_contact]
        update_contact_list()
        clear_fields()

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    details_text.config(state=tk.NORMAL)
    details_text.delete("1.0", tk.END)
    details_text.config(state=tk.DISABLED)
    search_entry.delete(0, tk.END)

# Create a GUI window
window = tk.Tk()
window.title("Contact Book")

# Create labels and entry widgets for contact information
name_label = tk.Label(window, text="Name:")
phone_label = tk.Label(window, text="Phone:")
email_label = tk.Label(window, text="Email:")
address_label = tk.Label(window, text="Address:")
name_entry = tk.Entry(window, width=40)
phone_entry = tk.Entry(window, width=40)
email_entry = tk.Entry(window, width=40)
address_entry = tk.Text(window, width=30, height=5)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
address_label.grid(row=3, column=0, padx=10, pady=5, sticky="ne")
name_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
phone_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)
email_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)
address_entry.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

# Create buttons for adding, updating, and deleting contacts
add_button = tk.Button(window, text="Add Contact", width=15, command=add_contact)
update_button = tk.Button(window, text="Update Contact", width=15, command=update_contact)
delete_button = tk.Button(window, text="Delete Contact", width=15, command=delete_contact)
add_button.grid(row=4, column=0, padx=10, pady=5)
update_button.grid(row=4, column=1, padx=10, pady=5)
delete_button.grid(row=4, column=2, padx=10, pady=5)

# Create a listbox for displaying contact names
contact_list = tk.Listbox(window, width=40, height=10)
contact_list.grid(row=0, column=3, rowspan=5, padx=10, pady=5)
contact_list.bind("<<ListboxSelect>>", show_contact_details)

# Create a text widget for displaying contact details
details_text = tk.Text(window, width=30, height=10, state=tk.DISABLED)
details_text.grid(row=0, column=4, rowspan=5, padx=10, pady=5)

# Create a label and entry widget for searching contacts
search_label = tk.Label(window, text="Search:")
search_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
search_entry = tk.Entry(window, width=40)
search_entry.grid(row=5, column=1, padx=10, pady=5, columnspan=2)
search_button = tk.Button(window, text="Search", width=15, command=search_contact)
search_button.grid(row=5, column=3, padx=10, pady=5)

# Initialize the contact list
update_contact_list()

# Start the main event loop
window.mainloop()

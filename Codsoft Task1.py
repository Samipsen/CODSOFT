import tkinter as tk

# Function to update the display with button clicks
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create a GUI window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for input and set its font size
entry = tk.Entry(window, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons for the calculator
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/",
    ".", "%"
]

# Create and arrange the buttons on the grid
row_num, col_num = 1, 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Helvetica", 16))
    button.grid(row=row_num, column=col_num)
    button.bind("<Button-1>", button_click)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Start the main event loop
window.mainloop()

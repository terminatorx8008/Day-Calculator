# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from datetime import datetime


# Function to calculate the difference between two dates
def calculate_date_difference():
    # Define the expected date format
    date_format = "%d-%m-%Y"
    try:
        # Parse the dates from the input fields
        date1 = datetime.strptime(entry_date1.get(), date_format)
        date2 = datetime.strptime(entry_date2.get(), date_format)
        # Calculate the absolute difference in days between the two dates
        difference = abs((date2 - date1).days)
        # Update the result label with the number of days
        label_result.config(text=f"Number of days: {difference}")
    except ValueError:
        # Update the result label with an error message if the date format is incorrect
        label_result.config(text="Invalid date format. Please use dd-mm-yyyy.")


# Initialize the main application window
root = tk.Tk()
root.title("Date Difference Calculator")
root.geometry('500x300')

# Create and pack the label and input field for the first date
label_date1 = ttk.Label(root, text="Enter the first date (dd-mm-yyyy):")
label_date1.pack(padx=10, pady=5)
entry_date1 = ttk.Entry(root)
entry_date1.pack(padx=10, pady=5)

# Create and pack the label and input field for the second date
label_date2 = ttk.Label(root, text="Enter the second date (dd-mm-yyyy):")
label_date2.pack(padx=10, pady=5)
entry_date2 = ttk.Entry(root)
entry_date2.pack(padx=10, pady=5)

# Create and pack the label that will display the result
label_result = ttk.Label(root, text="Result will be shown here")
label_result.pack(padx=10, pady=20)

# Create and pack the button that triggers the date difference calculation
calculate_button = ttk.Button(root, text="Calculate", command=calculate_date_difference)
calculate_button.pack(padx=10, pady=10)

# Start the Tkinter event loop to display the GUI and wait for user interaction
root.mainloop()

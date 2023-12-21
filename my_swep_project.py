
# Import Tkinter libraries that will be used to make the GUI
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# Function to check whether a year is a leap year or not
def check_leap_year():
    try:
        year = int(entry.get())
        if (year % 400 == 0 and year % 100 != 0) or year % 4 == 0:
            output.config(text=f"{year} is a leap year")
        else:
            output.config(text=f"{year} is not a leap year")
    except:
        showerror("Input value error", "Only Integer Values are allowed!")





# Create the main window

window = tk.Tk()
window.title("Leap Year Checker")
window.geometry("800x600")

# Create a frame to hold the heading input and output

frame_head = tk.Frame(window)
frame_head.pack()

frame_body = tk.Frame(window)
frame_body.pack()

frame_output = tk.Frame(window)
frame_output.pack(pady=60)

# Create a header label
label = tk.Label(frame_head, text="Leap Year Checker", font=("Courier 36 bold"))
label.pack(pady=15)

# Create an entry field, a help text and a button in a frame
global entry
entry = tk.Entry(frame_body, width=8, font=("courier 32 bold"), justify="center")
entry.grid(pady=10, row=0, column=0)

# Help text label
help_text = tk.Label(frame_body, text="Enter a year, e.g 2000", font=("Arial 12"))
help_text.grid(row=1, column=0)

# Submit button
answer_btn = tk.Button(frame_body, text="Enter", font=("courier 22 bold"), command=check_leap_year)
answer_btn.grid(pady=10, row=2, column=0)

# Output
output = tk.Label(frame_output, text="", font=("courier 20 bold"), fg="#EEEEFF", bg="#28587B")
output.pack()


window.mainloop()






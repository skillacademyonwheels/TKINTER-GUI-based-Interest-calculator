## A TKINTER GUI for getting the Simple Interest as well as the Compound Interest on a 
## given Principal, Rate of Interest and Time Period.

from tkinter import *


def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * ((1 + rate / 100) ** time - 1)

        simple_interest_result.config(text=f"{simple_interest:.2f}")
        compound_interest_result.config(text=f"{compound_interest:.2f}")
    except ValueError:
        simple_interest_result.config(text="Invalid input")
        compound_interest_result.config(text="Invalid input")



window = Tk()
window.title("Simple and Compound Interest Calculator")
window.geometry('400x300')
window.config(bg="lightblue")





title_label = Label(window, text="Simple and Compound Interest Calculator", font=("Arial", 16))
title_label.grid(column=0, row=0, columnspan=2, pady=10)

principal_label = Label(window, text="Principal Amount:")
principal_label.grid(column=0, row=1, padx=10, pady=5)

rate_label = Label(window, text="Rate of Interest (%):")
rate_label.grid(column=0, row=2, padx=10, pady=5)

time_label = Label(window, text="Time Period (years):")
time_label.grid(column=0, row=3, padx=10, pady=5)

principal_entry = Entry(window)
principal_entry.grid(column=1, row=1, padx=10, pady=5)

rate_entry = Entry(window)
rate_entry.grid(column=1, row=2, padx=10, pady=5)

time_entry = Entry(window)
time_entry.grid(column=1, row=3, padx=10, pady=5)

btn = Button(window, text="Calculate", command=calculate_interest)
btn.grid(column=1, row=4, pady=10)

simple_interest_label = Label(window, text="Simple Interest:")
simple_interest_label.grid(column=0, row=5, padx=10, pady=5)

compound_interest_label = Label(window, text="Compound Interest:")
compound_interest_label.grid(column=0, row=6, padx=10, pady=5)  

simple_interest_result = Label(window, text="")
simple_interest_result.grid(column=1, row=5, padx=10, pady=5)

compound_interest_result = Label(window, text="")
compound_interest_result.grid(column=1, row=6, padx=10, pady=5)








window.mainloop()
import tkinter as tk

window = tk.Tk()

window.title("mini calculator")
window.geometry("290x290")
window.resizable(False, False)
window.configure(bg="seashell2", cursor="hand2")


frame = tk.Frame(window, bg="white", width=290, height=50)
frame.grid(row=0, column=0, columnspan=5, sticky="ew")

head = tk.Label(window, 
    text="mini calculator",
    bg="white",
    font=("arial", 11, "bold"),
    )
head.grid(column=0, row=0, columnspan=5, sticky="ew")

first_num1 = tk.Label(
    window,
    text="Enter 1st Number:",
    fg="black",
    bg="white",
    font=("arial", 11, "bold")
    )
first_num1.grid(row=1, column=0, padx=10, pady=5)

first_num2 = tk.Entry(
    bg="white",
    width=20
)
first_num2.grid(row=1, column=1)

second_num1 = tk.Label(
    window,
    text="Enter 2nd Number",
    fg="black",
    bg="white",
    font=("arial", 11, "bold")
)
second_num1.grid()

second_num2 = tk.Entry(
    bg="white",
    width=20
)
second_num2.grid(row=2, column=1)




#defs

def add():
    wowi1 = int(first_num2.get())
    wowi2 = int(second_num2.get())
    outcome = wowi1 + wowi2
    head.config(text=f"The SUM of {wowi1} + {wowi2} is {outcome}")


def multi():
    wowi1 = int(first_num2.get())
    wowi2 = int(second_num2.get())
    outcome = wowi1 * wowi2
    head.config(text=f"The MULTIPLY of {wowi1} * {wowi2} is {outcome}")

def subs():
    wowi1 = int(first_num2.get())
    wowi2 = int(second_num2.get())
    outcome = wowi1 - wowi2
    head.config(text=f"The SUBTRACTION of {wowi1} - {wowi2} is {outcome}")

def division():
    wowi1 = int(first_num2.get())
    wowi2 = int(second_num2.get())
    outcome = wowi1 / wowi2
    head.config(text=f"The DIVISION of {wowi1} / {wowi2} is {outcome}")



# buttons add, multi, subtrac, divi

add = tk.Button(
    window,
    text="Add",
    bg="white",
    command=add
)
add.grid(column=0, row=3, pady=10)



multi = tk.Button(
    window,
    text="Multiply",
    bg="white",
    command=multi
)
multi.grid(column=0, row=4, pady=10)


sub = tk.Button(
    window,
    text="Subtract",
    bg="white",
    command=subs
)
sub.grid(column=1, row=3, padx=15)

divi = tk.Button(
    window,
    text="Division",
    bg="white",
    command=division
)
divi.grid(column=1, row=4)






window.mainloop()
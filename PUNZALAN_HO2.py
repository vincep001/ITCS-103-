import tkinter as tk

window = tk.Tk()

window.title("Punzalan, Vince profile")

window.geometry("600x600")

window.resizable(True, True)

window.configure(bg="lightblue", cursor="hand2")



header = tk.Label(
    window,
    text ="STUDENT PROFILE",
    font =("rockwell", 20, "bold"),
    fg ="white",
    bg ="lightblue",
    anchor ="center",
    )
header.pack()

fname = tk.Label(
    window,
    text ="Name : Punzalan, Vince anton M",
    font =("arial", 16, "italic"),
    fg ="white",
    bg ="lightblue",
    anchor ="center",
    )
fname.pack(pady="10", anchor = "w")

age = tk.Label(
    window,
    text ="Age : 18",
    font =("arial", 16, "italic"),
    fg ="white",
    bg ="lightblue",
    anchor ="center",
    )
age.pack(pady="10", anchor="w")

course = tk.Label(
    window,
    text ="Course & section : BSIT-1A",
    font =("arial", 16, "italic"),
    fg ="white",
    bg ="lightblue",
    anchor ="center",
    )
course.pack(pady="10", anchor="w")

bd = tk.Label(
    window,
    text ="Birthday : february 23, 2007",
    font =("arial", 16, "italic"),
    fg ="white",
    bg ="lightblue",
    anchor ="center",
    )
bd.pack(pady="10", anchor="w")

motto = tk.Label(
    window,
    text = "Moto : Slow progress, is still a progress.",
    font =("arial", 16, "italic"),
    fg ="white",
    bg ="lightblue",
    anchor ="center",
    )
motto.pack(pady="10", anchor="w")

window.mainloop()


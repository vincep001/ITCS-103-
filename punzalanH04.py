import tkinter as tk
from datetime import datetime

window = tk.Tk()


window.title("Log in form")
window.geometry("900x400")
window.resizable(False, False)
window.configure(bg = "seashell3")


#cinacalculate neto yung birthdate na nilagay naten sa birthdate entry
def calculate_age():
    bday = byear2.get()

    try:
        birthdate = datetime.strptime(bday, "%m/%d/%Y")
        today = datetime.now()

        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        calcu.config(text=f"{age} years old")

    except:
        calcu.config(text="Invalid format:)")


#entries namae mid sur

fname2 = tk.Entry(window)
fname2.place(x=70, y=80)

mname2 = tk.Entry(window)
mname2.place(x=387, y=80)

sname2 = tk.Entry(window)
sname2.place(x=675, y=80)

byear2 = tk.Entry(window)
byear2.place(x=70, y=168)
byear2.bind("<KeyRelease>", calculate_age)



#gender


gder = tk.Label(window, text="Gender", bg="seashell3", fg="black", font=("arial", 13, "italic"))
gder.place(x=100, y=260)

gender_var = tk.StringVar()
#radiobuttonzzz

male = tk.Radiobutton(window, text="Male", bg="seashell3", fg="black", value=2, variable=gender_var)
male.place(x=280, y=260)


fmale = tk.Radiobutton(window, text="Female", bg="seashell3", fg="black", value=1, variable=gender_var  )
fmale.place(x=390, y=260)







def show_popup():
    popup = tk.Toplevel(window)
    popup.title("DONE DEAL")
    popup.geometry("300x260")
    popup.resizable(False, False)
    popup.configure(bg="white")

    popup.transient(window)
    popup.grab_set()

    fname = fname2.get()
    mname = mname2.get()
    sname = sname2.get()
    byear = byear2.get()
    gder = gender_var.get()

    fname = f"{fname} {mname} {sname}"

    #calculation part

    try:
        birthdate = datetime.strptime(byear, "%m/%d/%Y")
        today = datetime.now()

        age =today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
    except:
        age = "invalid"


    mini_box = tk.Frame(popup, bg="seashell3")
    mini_box.pack(pady=5)


    #photo part wla pa ko pic so skip muna



    tk.Label(mini_box, text="Student Info", bg="seashell3", font=("arial", 14, "bold")).pack()

    gender_Choice = "Male" if gder == "2" else "Female" if gder == "1" else "Not selected"
    
    #info's
    tk.Label(mini_box, text=f"name:  {fname}", bg="seashell3", font=("arial", 10)).pack(anchor="w", padx=10)

    tk.Label(mini_box, text=f"Age:    {age} years old", bg="seashell3",
             font=("Arial", 10)).pack(anchor="w", padx=10)

    tk.Label(mini_box, text=f"Gender: {gender_Choice}", bg="seashell3",
             font=("Arial", 10)).pack(anchor="w", padx=10)

    #closing
    tk.Button(popup, text="close", command=popup.destroy).pack(pady=1)



student_info = tk.Label(
    window,
    text="Profile builder",
    fg="black",
    font=("arial", 13, "italic"),
    bg="seashell3",
    anchor="center"
    )
student_info.pack()

fname1 = tk.Label(window, text="First name", fg="black", bg="seashell3", font=("arial", 13, "italic"))
fname1.place(x=90, y=100)

mname1 = tk.Label(window, text="Middle name", fg="black", bg="seashell3", font=("arial", 13, "italic"))
mname1.place(x=400, y=100)


sname1 = tk.Label(window, text="Surname", fg="black", bg="seashell3", font=("arial", 13, "italic"))
sname1.place(x=700, y=100)

byear1 = tk.Label(window, text="Birthdate (MM/DD/YYYY  )", fg="black", bg="seashell3", font=("arial", 13, "italic"))
byear1.place(x=90, y=190)



calcu = tk.Label(window, text="Processing....", bg="seashell3", fg="black", font=("arial", 30, "italic"))
calcu.place(x=500, y=180)


submit = tk.Button(window, text="Submit", bg="white", fg="black", command=show_popup)
submit.place(x=425, y=320)




# label3 = tk.Label(, text="DONE DEAL YA", font=("arial", 16, "italic"))
# label3.pack()




window.mainloop()
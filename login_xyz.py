# okay so this bunch of windows is mainly designed to make sure my functions are working.
# i will not focus on the design as much, or at all.
# theres no time to waste.

from tkinter import *
from tkinter import messagebox

# WINDOW FEATURES
window = Tk()
window.geometry("500x150")
window.resizable(0, 0)

# WINDOW LABELS
name_lab = Label(window, text="Name :", bg="aqua")
name_lab.place(x=50, y=10)

id_lab = Label(window, text="RSA ID number :", bg="aqua")
id_lab.place(x=50, y=30)

email_lab = Label(window, text="Email :", bg="aqua")
email_lab.place(x=50, y=50)

# WINDOW ENTRIES
name_ent = Entry(window, bg="aqua")
name_ent.place(x=200, y=10)

id_ent = Entry(window, bg="aqua")
id_ent.place(x=200, y=30)

email_ent = Entry(window, bg="aqua")
email_ent.place(x=200, y=50)


# WINDOW FUNCTIONS
# clear button
def clear_func():
    sure = messagebox.askyesno(title="Alert", message="Are you sure you want to clear your login information?")
    if sure:
        name_ent.delete(0, END)
        id_ent.delete(0, END)
        email_ent.delete(0, END)
    else:
        return None

# register button
# def register_func():

ex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def email_check():

    for i in range(len(email_ent.get())):
        if re.search(ex, email_ent.get()):
            with open("text_file.txt", "a") as f:
                f.write(email_ent.get())
                f.write('\n')
                window.destroy()
                import game_xyz
        else:
            f.write('invalid')

# exit button
def exit_func():
    sure = messagebox.askyesno(title="Alert", message="Are you sure you want to exit?")
    if sure:
        window.destroy()
    else:
        return None


# WINDOW BUTTONS
clear_btn = Button(window, text="Clear", command=clear_func, bg="aqua")
clear_btn.place(x=50, y=100)

register_btn = Button(window, text="Register", command=email_check, bg="aqua")
register_btn.place(x=180, y=100)

exit_btn = Button(window, text="Exit", command=exit_func, bg="aqua")
exit_btn.place(x=360, y=100)

# FIN
window.mainloop()

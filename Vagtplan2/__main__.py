from tkinter import *
import sqlite3
from Vagtplan2.Choice import *
from Vagtplan2.Submit import *
from Vagtplan2.Select_user import *
#from Editor import *
root = Tk()
root.title("Vagt plans app")
root.geometry("400x600")


# Create Text Box Labels
vellcome_label = Label(root, text="Velkommen til Vagt plan lægning af døgnvagter på 7631")
vellcome_label.grid(row=0, column=0, pady=(10,0))

choice_label = Label(root, text="Dine valg:")
choice_label.grid(row=1, column=0)

# Create Submit Button
submit_new_user_btn = Button(root, text="Opret bruger", command=Submit)
submit_new_user_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create user choice of dates Button
choice_btn = Button(root, text="Planlæg dine vagter", command=select_users)
choice_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=83)

# Create a roster schedule Button
schedule_btn = Button(root, text="Opret vagtplan", command=Submit)
schedule_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=96)

root.mainloop()

from tkinter import *
import sqlite3
from tkcalendar import *

def grab_date():
    my_label_date.config(text=cal.get_date())


def choice():
    wishes = Tk()
    wishes.title("Valg ønsker")
    wishes.geometry("600x600")

    global cal
    cal = Calendar(wishes, selectmode="day", year=2020, month=10, day=1)
    cal.pack(pady=20, fill="both", expand=True)

    my_button = Button(wishes, text="Tilfør dato: ", command=grab_date)
    my_button.pack(pady=40)

    global my_label_date
    my_label_date = Label(wishes, text="")
    my_label_date.pack(pady=40)



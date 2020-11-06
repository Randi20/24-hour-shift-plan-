from tkinter import *
import sqlite3
from tkcalendar import *
from Vagtplan2.Select_user import *




class Choice:



    def show_date(self):
        self.choice.append(self.cal.get_date())
        self.dates_label.config(text=self.choice)


    def save_date_choice(self):
        pass

    def __init__(self):
        self.wishes = Tk()
        self.wishes.title("Vagt ønsker")
        self.wishes.geometry("600x600")
        user_name = str(Select_user.sel_user)

        self.choice = []

        self.info_label = Label(self.wishes, text="Hej" + " " + user_name + " " + "Marker de dage du ønsker at have vagt!")
        self.info_label.pack(pady=(10, 0))

        self.cal = Calendar(self.wishes, selectmode="day", year=2020, month=10, day=1)
        self.cal.pack(pady=20, fill="both")

        my_button = Button(self.wishes, text="Tilfør dato: ", command=self.show_date)
        my_button.pack(pady=40)

        save_date_button = Button(self.wishes, text="Gem valgte dage", command=self.save_date_choice)
        save_date_button.pack(pady=20)

        self.dates_label = Label(self.wishes, text="")
        self.dates_label.pack(pady=20)


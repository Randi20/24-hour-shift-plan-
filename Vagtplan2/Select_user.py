import tkinter as tk
from tkinter import ttk
from tkcalendar import *
# import Vagtplan2.Choice as Choice
import Vagtplan2.database as db

class Helper:
    pass

def select_users():
    s_user = tk.Tk()
    s_user.title("Vagt plans app")
    s_user.geometry("400x200")

    f_name_label = tk.Label(s_user, text="Vælg bruger")
    f_name_label.pack(pady=10)

    combo = ttk.Combobox(s_user, width=50, height=20)
    combo.pack(pady=10)
    combo['values'] = db.find_users()

    def onclick():
        user = combo.get()
        s_user.destroy()
        choose_shift(user)

    # Create a select user button
    s_btn = tk.Button(s_user, 
                text="Vælg bruger", 
                command=onclick)
    s_btn.pack(pady=10)

def choose_shift(user):
    wishes = tk.Tk()
    wishes.title("Vagt ønsker")
    wishes.geometry("600x600")

    msg = f"Hej {user}: Marker de dage du ønsker at have vagt!"
    info_label = tk.Label(wishes, text=msg)
    info_label.pack(pady=(10, 0))

    cal = Calendar(wishes, 
            selectmode="day", year=2020, month=10, day=1)
    cal.pack(pady=20, fill="both")

    helper = Helper()
    choices = set()
    def add_choice():
        choices.add(cal.get_date())
        helper.dates_label.config(text=str(choices))

    my_button = tk.Button(wishes, 
            text="Tilfør dato:", 
            command=add_choice
            )
    my_button.pack(pady=40)

    def save_dates():
        db.save_shifts(user, choices)

    save_date_button = tk.Button(wishes, 
            text="Gem valgte dage", 
            command=save_dates)
    save_date_button.pack(pady=20)

    helper.dates_label = tk.Label(wishes, text="")
    helper.dates_label.pack(pady=20)


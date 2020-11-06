from tkinter import *
import sqlite3
from tkinter import ttk
import Vagtplan2.Choice as Choice



class Select_user:


    def sel_user(self):
        self.user_init = self.combo.get()
        return self.user_init

    def find_user(self):
        # Create a database or connect to ons
        conn = Choice.sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()


        # Query the database
        c.execute("SELECT initialer FROM users")
        self.userList = []

        for init in c.fetchall():
            self.userList.append(init[0])

        return self.userList




        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()


    def __init__(self):
        self.s_user = Choice.Tk()
        self.s_user.title("Vagt plans app")
        self.s_user.geometry("400x200")

        self.f_name_label = Choice.Label(self.s_user, text="Vælg bruger")
        self.f_name_label.pack(pady=10)

        self.combo = Choice.ttk.Combobox(self.s_user, width=50, height=20)
        self.combo.pack(pady=10)
        self.combo['values'] = self.find_user()

        # Create a select user button
        self.s_btn = Choice.Button(self.s_user, text="Vælg bruger", command=Choice.Choice)
        self.s_btn.pack(pady=10)

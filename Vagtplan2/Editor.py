from tkinter import *
import sqlite3
from Submit import *


class Editor:

    def edit(self):
        # Create a database or connect to ons
        conn = sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()

        record_id = Submit.user(self.delete_box.get())

        # Query the database
        c.execute("SELECT * FROM users WHERE oid = " + record_id)
        records = c.fetchall()

        # Loop thru results
        for record in records:
            self.f_name_editor.insert(0, record[0])
            self.l_name_editor.insert(0, record[1])
            self.init_editor.insert(0, record[2])

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

    def __init__(self):
        self.editor = Tk()
        self.editor.title("Redigere bruger")
        self.editor.geometry("400x600")

        # Create a database or connect to one
        conn = sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()

        # Create Text Box Labels
        self.f_name_label_editor = Label(self.editor, text="For navn")
        self.f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
        self.l_name_label_editor = Label(self.editor, text="Efter navn")
        self.l_name_label_editor.grid(row=1, column=0)
        self.init_label_editor = Label(self.editor, text="Initialer")
        self.init_label_editor.grid(row=2, column=0)

        # Create Text Boxes
        self.f_name_editor = Entry(self.editor, width=30)
        self.f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.l_name_editor = Entry(self.editor, width=30)
        self.l_name_editor.grid(row=1, column=1)
        self.init_editor = Entry(self.editor, width=30)
        self.init_editor.grid(row=2, column=1)

        # Create a save button
        save_btn_editor = Button(self.editor, text="Gem", command=self.edit)
        save_btn_editor.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

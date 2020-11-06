from tkinter import *
import sqlite3
from Editor import *



class Submit:

    def delete(self):
        # Create a database or connect to ons
        conn = sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()

        # Delete a record
        c.execute("DELETE from users WHERE oid= " + self.delete_box.get())

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

    def save(self):
        # Create a database or connect to ons
        conn = sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO users VALUES (:f_name, :l_name, :init)",
                  {
                      'f_name': self.f_name.get(),
                      'l_name': self.l_name.get(),
                      'init': self.init.get()
                  }
                  )

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

    def show(self):
        # Create a database or connect to ons
        conn = sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM users")
        records = c.fetchall()

        print_records = ''
        # Loop thru results
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[3]) + "\n"

        query_label = Label(self.user, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()



    def __init__(self):
        self.user = Tk()
        self.user.title("Opret bruger")
        self.user.geometry("400x600")

        # Create a database or connect to one
        conn = sqlite3.connect('vagt_plan_app.db')
        # Create cursor
        c = conn.cursor()

        '''
        # Create table
        c.execute("""CREATE TABLE users (
                first_name text,
                last_name text,
                initialer text
                )""")
        '''
        # Create Text Box Labels
        self.f_name_label = Label(self.user, text="For navn")
        self.f_name_label.grid(row=0, column=0, pady=(10, 0))
        self.l_name_label = Label(self.user, text="Efter navn")
        self.l_name_label.grid(row=1, column=0)
        self.init_label = Label(self.user, text="Initialer")
        self.init_label.grid(row=2, column=0)
        self.delete_box_label = Label(self.user, text="Vælg ID nummer:")
        self.delete_box_label.grid(row=7, column=0)

        # Create Text Boxes
        self.f_name = Entry(self.user, width=30)
        self.f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.l_name = Entry(self.user, width=30)
        self.l_name.grid(row=1, column=1)
        self.init = Entry(self.user, width=30)
        self.init.grid(row=2, column=1)
        self.delete_box = Entry(self.user, width=30)
        self.delete_box.grid(row=7, column=1)

        # Create a save button
        save_btn = Button(self.user, text="Gem", command=self.save)
        save_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

        # Create a show user button
        show_btn = Button(self.user, text="Vis bruger", command=self.show)
        show_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

        # Create a delete user button
        show_btn = Button(self.user, text="Slet bruger", command=self.delete)
        show_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

        # Create a edit user button
        edit_btn = Button(self.user, text="Rediger bruger", command=Editor)
        edit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
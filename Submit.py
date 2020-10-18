from tkinter import *
import sqlite3
from Editor import *




def delete():
    # Create a database or connect to ons
    conn = sqlite3.connect('vagt_plan_app.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from users WHERE oid= " + delete_box.get())

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

def show():
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

    query_label = Label(user, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

def save():

    # Create a database or connect to ons
    conn = sqlite3.connect('vagt_plan_app.db')
    # Create cursor
    c = conn.cursor()


    # Insert Into Table
    c.execute("INSERT INTO users VALUES (:f_name, :l_name, :init)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'init': init.get()
              }
              )

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()




    #Create Submit Function For Database
def submit():
    global user
    user = Tk()
    user.title("Opret bruger")
    user.geometry("400x600")

    # Create a database or connect to ons
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
    global f_name
    global l_name
    global init
    global delete_box

    # Create Text Box Labels
    f_name_label = Label(user, text="For navn")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(user, text="Efter navn")
    l_name_label.grid(row=1, column=0)
    init_label = Label(user, text="Initialer")
    init_label.grid(row=2, column=0)
    delete_box_label = Label(user, text="Vælg ID nummer:")
    delete_box_label.grid(row=7, column=0)

    # Create Text Boxes
    f_name = Entry(user, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = Entry(user, width=30)
    l_name.grid(row=1, column=1)
    init = Entry(user, width=30)
    init.grid(row=2, column=1)
    delete_box = Entry(user, width=30)
    delete_box.grid(row=7, column=1)




    # Create a save button
    save_btn = Button(user, text="Gem", command=save)
    save_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    init.delete(0, END)

    # Create a show user button
    show_btn = Button(user, text="Vis bruger", command=show)
    show_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # Create a delete user button
    show_btn = Button(user, text="Slet bruger", command=delete)
    show_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # Create a edit user button
    edit_btn = Button(user, text="Rediger bruger", command=edit)
    edit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()





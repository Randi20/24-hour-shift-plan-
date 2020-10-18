from tkinter import *
import sqlite3
from Submit import *


# Create Edit function to update a record
def edit():
    global edit
    editor = Tk()
    editor.title("Redigere bruger")
    editor.geometry("400x600")

    # Create a database or connect to ons
    conn = sqlite3.connect('vagt_plan_app.db')
    # Create cursor
    c = conn.cursor()


    record_id = submit(delete_box.get())

    # Query the database
    c.execute("SELECT * FROM users WHERE oid = " + record_id)
    records = c.fetchall()



    # Create Text Box Labels
    f_name_label_editor = Label(editor, text="For navn")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Efter navn")
    l_name_label_editor.grid(row=1, column=0)
    init_label_editor = Label(editor, text="Initialer")
    init_label_editor.grid(row=2, column=0)


    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    init_editor = Entry(editor, width=30)
    init_editor.grid(row=2, column=1)

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        init_editor.insert(0, record[2])

    # Create a save button
    save_btn_editor = Button(editor, text="Gem", command=edit)
    save_btn_editor.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

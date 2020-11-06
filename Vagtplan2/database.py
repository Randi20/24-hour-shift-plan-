import sqlite3
        

def find_users():
    """ find the user initials in the database
    """
    with sqlite3.connect('vagt_plan_app.db') as conn:
        c = conn.cursor()
        c.execute("SELECT initialer FROM users")

        userList = []
        for init in c.fetchall():
            userList.append(init[0])

        return userList


def save_shifts(user, choices):
    print(user, choices) 


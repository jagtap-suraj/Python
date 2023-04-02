# SE-3, 20, Suraj Jagtap

#Python Experiment No. 9

"""Write a Python program to create a login form with entry widgets for entering username and password. 
Compare the entered input with the data stored in the User table in the database. 
If a user exists in the database then display a login successful message 
else display invalid username or password 
(use tkinter and MySQLdb module)."""

import tkinter as tk
import mysql.connector as db

# Connection to the database
con = db.connect(host='localhost', user='root', password='UwU', database='loginchecker')
cur = con.cursor()


def login():
    # Taking the username and password from the entry widgets
    username = entry_username.get()
    password = entry_password.get()

    # Querying the database for the entered username and password
    cur.execute("SELECT * FROM User WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()

    # Displaying login message based on user existence in the database
    label_message.config(text='Login successful!' if user else 'Invalid username or password!')

# Creating the login window
window = tk.Tk()
window.geometry('300x200')
window.title('Login')

# Creating the username label and entry widget
label_username = tk.Label(window, text='Username:')
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Creating the password label and entry widget
label_password = tk.Label(window, text='Password:')
label_password.pack()
entry_password = tk.Entry(window, show='*')
entry_password.pack()

# Creating login button and message label
button_login = tk.Button(window, text='Login', command=login)
button_login.pack()
label_message = tk.Label(window)
label_message.pack()

# Running the main loop
window.mainloop()

# Closing the database connection
cur.close()
con.close()
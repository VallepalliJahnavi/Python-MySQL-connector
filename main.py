from tkinter import *
import tkinter
import tkinter.messagebox as box
import mysql.connector as mysql
import time


def conn():
    """connecting to the mysql server"""
    return mysql.connect(
        host="localhost",
        user="root",
        database="db"
    )


root = Tk()


def insert_record():
    check_counter = 0
    warn = ""
    if nameentry.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if emailentry.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if phoneentry.get() == "":
        warn = "Contact can't be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if passwordentry.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if passwordcheckentry.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if passwordentry.get() != passwordcheckentry.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 7:
        try:
            con = conn()
            cur = con.cursor()
            cur.execute(
                "create table if not exists record(name char(20),email varchar(35) primary key,phone int,gender char(6),password varchar(20))")
            cur.execute(f"INSERT INTO record VALUES ('{nameentry.get()}',"
                        f"'{emailentry.get()}',"
                        f"{phoneentry.get()},"
                        f"'{var.get()}', "
                        f"'{passwordentry.get()}')"
                        )
            con.commit()
            box.showinfo('confirmation', 'Account Created')

        except Exception as ep:
            box.showerror('', ep)
    else:
        box.showerror('Error', warn)


def login_response():
    uname = email_tf.get()
    upwd = pwd_tf.get()
    a = 0
    try:
        con = conn()
        cur = con.cursor()
        query = f"Select name,password from record where email='{uname}' and password='{upwd}'"
        p = cur.execute(query)
        x = cur.fetchone()
        print("Sucess", x)
        if x != None:
            box.showinfo('Login Status', 'Logged in Successfully!')
            a = 1
        else:
            box.showerror('Login Status', 'Invalid username or password')
    except Exception as ep:
        print(ep, 'Error')
        box.showerror('', ep)
    if a == 1:
        root.quit()


root.geometry("1366x768")

root.config(bg="#165161")
root.title("My Application")
# Remove the below icon map
# root.iconbitmap('testing_phase\image.ico')
# Rename this to your liking
Label(text="Welcome to Login Page", justify=CENTER, font="comicsansms 30 bold", bg="#165161").grid(row=1, column=0,
                                                                                                   padx=60, pady=10)

# Label(text = "Sign up ",font="comicsansms 20 bold",bg = "#9bf6ff").grid(row = 2,pady = 20)
name = Label(text="Enter Name:", font="comicsansms 15", bg="#165161")
email = Label(text="Enter Email:", font="comicsansms 15", bg="#165161")
gender = Label(text="Select Gender", bg='#165161', font="comicsansms 15")
phone = Label(text="Enter your phone:", font="comicsansms 15", bg="#165161")
password = Label(text="Create a password:", font="comicsansms 15", bg="#165161")
passwordcheck = Label(text="Confirm the password:", font="comicsansms 15", bg="#165161")

namevalue = StringVar()
emailvalue = StringVar()
passwordvalue = StringVar()
passwordcheckvalue = StringVar()
phonevalue = StringVar()
var = StringVar()
var.set('male')

nameentry = Entry(root, textvariable=namevalue)
emailentry = Entry(root, textvariable=emailvalue)
passwordentry = Entry(root, textvariable=passwordvalue)
passwordcheckentry = Entry(root, textvariable=passwordcheckvalue)
phoneentry = Entry(root, textvariable=phonevalue)

nameentry.grid(row=3, column=0, padx=10, pady=15)
emailentry.grid(row=4, column=0, padx=10, pady=10)
phoneentry.grid(row=5, column=0, padx=50, pady=10)
passwordentry.grid(row=6, column=0, padx=100, pady=10)
passwordcheckentry.grid(row=7, column=0, padx=100, pady=10)

name.grid(row=3, column=0, padx=0, sticky=W, pady=10)
email.grid(row=4, column=0, padx=0, sticky=W, pady=10)
phone.grid(row=5, column=0, padx=0, sticky=W, pady=15)
password.grid(row=6, column=0, padx=0, sticky=W, pady=20)
passwordcheck.grid(row=7, column=0, padx=0, sticky=W, pady=20)
gender.grid(row=8, column=0, sticky=W, padx=0, pady=10)

genders = Label()
male_rb = Radiobutton(genders, text='Male', bg='#e9e4da', variable=var, value='male', font="comicsansms 12", )
female_rb = Radiobutton(genders, text='Female', bg='#e9e4da', variable=var, value='female', font="comicsansms 12", )
others_rb = Radiobutton(genders, text='Others', bg='#e9e4da', variable=var, value='others', font="comicsansms 12")

genders.grid(row=8, pady=20)
male_rb.pack(side=LEFT)
female_rb.pack(side=LEFT)
others_rb.pack(expand=True, side=LEFT)

agree = Checkbutton(text="I have read all the information", font="comicsansms 15", bg='#cfe8ef', relief=SOLID).grid(
    pady=15)

submit = Button(text="Sign up", font="bold", command=insert_record)
submit.grid(column=0, padx=20, pady=15)

right_frame = Frame(root, bd=2, bg='#19b4bc', relief=SOLID, padx=10, pady=10)
Label(right_frame, text="Enter Email", bg='#19b4bc', font="comicsansms 15").grid(row=0, column=0, sticky=E, pady=10)
Label(right_frame, text="Enter Password", bg='#19b4bc', font="comicsansms 15").grid(row=1, column=0, pady=10)

email_tf = Entry(right_frame, )
pwd_tf = Entry(right_frame, show='*')
login_btn = Button(right_frame, width=10, text='Login', font="comicsansms 15", relief=SOLID, cursor='hand2',
                   command=login_response)

email_tf.grid(row=0, column=3, pady=10, padx=20)
pwd_tf.grid(row=1, column=3, pady=10, padx=20)
login_btn.grid(row=2, column=3, pady=10)
right_frame.place(x=600, y=150)

connection = mysql.connect(host='localhost', user='root', db='db')

root = tkinter.Tk()
root.title("Record Viewer")


# Define the function to be called when the button is clicked
def show_records():
    # Create a cursor
    cursor = connection.cursor()

    # Execute a SELECT statement
    cursor.execute("SELECT * FROM record")

    # Fetch all the records
    rec = cursor.fetchall()

    # Clear the text box
    text_box1.delete('1.0', tkinter.END)

    # Loop through the records and print them in the text box
    for record in rec:
        text_box1.insert(tkinter.END, str(record) + "\n")


# Create a button widget
button1 = tkinter.Button(root, text="Show Records", command=show_records)
button1.pack()

# Create a text box widget
text_box1 = tkinter.Text(root)
text_box1.pack()

root.mainloop()


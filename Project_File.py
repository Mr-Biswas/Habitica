# Importing Libraries
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter


class MyHabitica:

    def __init__(self, root):
        self.root = root
        self.root.title("The Techie")
        self.root.geometry("1350x720+0+0")


# VARIABLEs FOR DATABASE:
        self.Launch_var = StringVar()
        self.Today_var = StringVar()
        self.Location_var = StringVar()
        self.Exercise_var = StringVar()
        self.Stretch_var = StringVar()
        self.Reading_var = StringVar()
        self.Duration_var = StringVar()
        self.Coding_var = StringVar()
        self.Number_var = StringVar()
        self.Content_var = StringVar()
        self.Details_var = StringVar()
        self.technology_var = StringVar()
        self.Water_var = StringVar()
        self.Sleep_var = StringVar()
        self.Balance_var = StringVar()
        self.Remarks_var = StringVar()

        lbltitle = Label(self.root, text="My Habitica", bg="#ff671f", fg="#06038d",
                         bd=5, relief=SUNKEN, font=("Comic Sans MS", 30, "bold"), padx=2, pady=5)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=5, relief=RIDGE, padx=10, bg="#d3d3d3")
        frame.place(x=0, y=70, width=1345, height=400)

# Created the Left DataFrame
        DataFrameLeft = LabelFrame(frame, text="Daily Activity", bg="#d3d3d3",
                                   fg="#06038d", bd=5, relief=RIDGE, font=("Comic Sans MS", 20, "bold"))
        DataFrameLeft.place(x=1, y=5, width=770, height=370)

        lbllaunch = Label(DataFrameLeft, text="Launch:", bg="#d3d3d3", fg="#940003", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)

        lbllaunch.grid(row=0, column=0, sticky=W)
        comlaunch = ttk.Combobox(DataFrameLeft, font=(
            "Comic Sans MS", 11, "bold"), width=22, state="readonly",  textvariable=self.Launch_var)
        comlaunch["value"] = ("2024-12-05")
        comlaunch.current(0)
        comlaunch.grid(row=0, column=1)

        lblday = Label(DataFrameLeft, text="Today:", bg="#d3d3d3", fg="#ff0000", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblday.grid(row=1, column=0, sticky=W)
        comday = ttk.Combobox(DataFrameLeft, font=("Comic Sans MS", 11, "bold"),
                              width=22, textvariable=self.Today_var)
        comday["value"] = ("YYYY-MM-DD")
        comday.current(0)
        comday.grid(row=1, column=1)

        lblloc = Label(DataFrameLeft, text="Location:", bg="#d3d3d3", fg="#ff4500", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblloc.grid(row=2, column=0, sticky=W)
        comloc = ttk.Combobox(DataFrameLeft, font=("Comic Sans MS", 11, "bold"),
                              width=22, state="readonly", textvariable=self.Location_var)
        comloc["value"] = ("Home", "Work", "Others")
        comloc.current(0)
        comloc.grid(row=2, column=1)

        lblexercise = Label(DataFrameLeft, text="Exercise:", bg="#d3d3d3", fg="#ff1493", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblexercise.grid(row=3, column=0, sticky=W)
        txtexercise = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                                 "italic"), width=24, textvariable=self.Exercise_var)
        txtexercise.grid(row=3, column=1)

        lblstretch = Label(DataFrameLeft, text="Stretch:", bg="#d3d3d3",  fg="#008000", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblstretch.grid(row=4, column=0, sticky=W)
        comstretch = ttk.Combobox(DataFrameLeft, font=("Comic Sans MS", 11, "bold"),
                                  width=22, textvariable=self.Stretch_var)
        comstretch["value"] = ("30", "45", "60", "75", "90", "mins")
        comstretch.current(0)
        comstretch.grid(row=4, column=1)

        lblReading = Label(DataFrameLeft, text="Reading:", bg="#d3d3d3",  fg="#0000ff", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblReading.grid(row=5, column=0, sticky=W)
        txtReading = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                                "italic"), width=24, textvariable=self.Reading_var)
        txtReading.grid(row=5, column=1)

        lbldur = Label(DataFrameLeft, text="Duration:", bg="#d3d3d3", fg="#4b0082", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lbldur.grid(row=6, column=0, sticky=W)
        comdur = ttk.Combobox(DataFrameLeft, font=("Comic Sans MS", 11, "bold"),
                              width=22, textvariable=self.Duration_var)
        comdur["value"] = ("30", "45", "60", "75", "90", "mins")
        comdur.current(0)
        comdur.grid(row=6, column=1)

        lblcode = Label(DataFrameLeft, text="Coding:", bg="#d3d3d3", fg="#8a2be2", font=(
            "Comic Sans MS", 12, "underline"), padx=2, pady=6)
        lblcode.grid(row=7, column=0, sticky=W)
        txtcode = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                        "italic"), width=24, textvariable=self.Coding_var)
        txtcode.grid(row=7, column=1)
        txtcode.insert(0, "Insert Language Name")

        lblnum = Label(DataFrameLeft, text="Number:", bg="#d3d3d3", fg="#ff1493", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lblnum.grid(row=0, column=2, sticky=W)
        comnum = ttk.Combobox(DataFrameLeft, font=("Comic Sans MS", 11, "bold"),
                              width=25, textvariable=self.Number_var)
        comnum["value"] = ("2", "3", "5")
        comnum.current(0)
        comnum.grid(row=0, column=3)

        lblContent = Label(DataFrameLeft, text="Content:", bg="#d3d3d3", fg="#ff4500", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lblContent.grid(row=1, column=2, sticky=W)
        txtContent = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                                "italic"), width=27, textvariable=self.Content_var)
        txtContent.grid(row=1, column=3)

        lbldetails = Label(DataFrameLeft, text="Details:", bg="#d3d3d3", fg="#03ac13", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lbldetails.grid(row=2, column=2, sticky=W)
        comdetails = ttk.Combobox(DataFrameLeft, font=(
            "Comic Sans MS", 11, "italic"), width=25, textvariable=self.Details_var)
        comdetails["value"] = ("max_100words")
        comdetails.current(0)
        comdetails.grid(row=2, column=3)

        lbltech = Label(DataFrameLeft, text="Technology:", bg="#d3d3d3",  fg="#b22222", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lbltech.grid(row=3, column=2, sticky=W)
        txttech = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                        "italic"), width=27, textvariable=self.technology_var)
        txttech.grid(row=3, column=3)

        lblwater = Label(DataFrameLeft, text="Water:", bg="#d3d3d3",  fg="#0000ff", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lblwater.grid(row=4, column=2, sticky=W)
        comwater = ttk.Combobox(DataFrameLeft, font=(
            "Comic Sans MS", 11, "bold"), width=25, textvariable=self.Water_var)
        comwater["value"] = ("8", "9", "11", "12", "14")
        comwater.current(0)
        comwater.grid(row=4, column=3)

        lblsleep = Label(DataFrameLeft, text="Sleep:", bg="#d3d3d3",  fg="#9932cc", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lblsleep.grid(row=5, column=2, sticky=W)
        comsleep = ttk.Combobox(DataFrameLeft, font=(
            "Comic Sans MS", 11, "bold"), width=25, textvariable=self.Sleep_var)
        comsleep["value"] = ("6", "7", "8")
        comsleep.current(0)
        comsleep.grid(row=5, column=3)

        lblBalance = Label(DataFrameLeft, text="Balance:", bg="#d3d3d3", fg="#000080", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lblBalance.grid(row=6, column=2, sticky=W)
        txtBalance = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                                "italic"), width=27, show="*", textvariable=self.Balance_var)
        txtBalance.grid(row=6, column=3)

        lblremark = Label(DataFrameLeft, text="Remarks:", bg="#d3d3d3",  fg="#b22222", font=(
            "Comic Sans MS", 12, "underline"), padx=25, pady=6)
        lblremark.grid(row=7, column=2, sticky=W)
        txtremark = Entry(DataFrameLeft, font=("Comic Sans MS", 11,
                                               "italic"), width=27, textvariable=self.Remarks_var)
        txtremark.grid(row=7, column=3)

# Created the Right DataFrame
        DataFrameRight = LabelFrame(frame, text="Suggestion", bg="#d3d3d3",
                                    fg="#06038d", bd=5, relief=SUNKEN, font=("Comic Sans MS", 20, "bold"))
        DataFrameRight.place(x=800, y=2, width=510, height=370)
# Created txtBox, an attribute of the class using self
        self.txtBox = Text(DataFrameRight, font=(
            "Comic Sans MS", 11, "normal"), width=25, height=27, padx=10, pady=5)
        self.txtBox.grid(row=0, column=2)

        listscrollbar = Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0, column=1, sticky="ns")

        listbook = [
            "Execise Option-1",
            "Execise Option-2",
            "Execise Option-3",
            "Execise Option-4",
            "Execise Option-5",
            "Reading Option-1",
            "Reading Option-2",
            "Reading Option-3",
            "Reading Option-4",
            "Reading Option-5",
            "JavaScript Full Course",
            "HTML and CSS for Beginners",
            "ReactJS Crash Course",
            "Django Full Stack Web Development Tutorial",
            "Learn Git and GitHub",
            "How to Create a Portfolio Website Using HTML and CSS",
            "Introduction to Machine Learning with Python",
            "Understanding APIs",
            "How to Build a Chatbot with Python",
            "Top 10 Python Libraries You Should Know",
            "SQL Tutorial",
            "How to Get Started with Android Development",
            "Introduction to Data Structures and Algorithms in Python",
            "Building a To-Do List App with React",
            "How to Deploy a Django App to Heroku",
            "Introduction to Web Scraping with Python",
            "How to Build a Blog Using Django and Python",
            "Object-Oriented Programming in Python",
            "Java Programming Tutorial for Beginners",
            "C++ Full Course",
            "Building RESTful APIs with Flask",
            "Pygame Tutorial",
            "How to Use Docker for Python Projects",
            "Learn Firebase - Build Real-Time Apps with Firebase and React"
        ]

        def selectCourse(event=""):

            # For current selection
            selection = lstbox.curselection()

# Checked for selected item
            if not selection:
                print("No item selected")
                return
# Exit the function if no item is selected

# Extracted the first index from the selection
            index = selection[0]

# Checked for the selected value
            x = lstbox.get(index)

            if (x == "Execise Option-1"):
                self.Exercise_var.set("Walking")
                self.Stretch_var.set("45")

            elif (x == "Execise Option-2"):
                self.Exercise_var.set("Jogging")
                self.Stretch_var.set("30")

            elif (x == "Execise Option-3"):
                self.Exercise_var.set("Cycling")
                self.Stretch_var.set("60")

            elif (x == "Execise Option-4"):
                self.Exercise_var.set("Strength Training")
                self.Stretch_var.set("30")

            elif (x == "Execise Option-5"):
                self.Exercise_var.set("Running")
                self.Stretch_var.set("25")

            elif (x == "Reading Option-1"):
                self.Reading_var.set("Book")
                self.Duration_var.set("30")

            elif (x == "Reading Option-2"):
                self.Reading_var.set("Journal")
                self.Duration_var.set("30")

            elif (x == "Reading Option-3"):
                self.Reading_var.set("Newspaper")
                self.Duration_var.set("30")

            elif (x == "Reading Option-4"):
                self.Reading_var.set("Internet")
                self.Duration_var.set("30")

            elif (x == "Reading Option-5"):
                self.Reading_var.set("Documentation")
                self.Duration_var.set("30")

            elif x == "JavaScript Full Course":
                self.Content_var.set("JavaScript Full Course")
                self.Details_var.set("40 Hours")
                self.technology_var.set("JavaScript")

            elif x == "HTML and CSS for Beginners":
                self.Content_var.set("HTML and CSS for Beginners")
                self.Details_var.set("12 Hours")
                self.technology_var.set("HTML, CSS")

            elif x == "ReactJS Crash Course":
                self.Content_var.set("ReactJS Crash Course")
                self.Details_var.set("25 Hours")
                self.technology_var.set("JavaScript, ReactJS")

            elif x == "Django Full Stack Web Development Tutorial":
                self.Content_var.set(
                    "Django Full Stack Web Development Tutorial")
                self.Details_var.set("50 Hours")
                self.technology_var.set("Python, Django")

            elif x == "Learn Git and GitHub":
                self.Content_var.set("Learn Git and GitHub")
                self.Details_var.set("10 Hours")
                self.technology_var.set("Git, GitHub")

            elif x == "How to Create a Portfolio Website Using HTML and CSS":
                self.Content_var.set(
                    "How to Create a Portfolio Website Using HTML and CSS")
                self.Details_var.set("12 Hours")
                self.technology_var.set("HTML, CSS")

            elif x == "Introduction to Machine Learning with Python":
                self.Content_var.set(
                    "Introduction to Machine Learning with Python")
                self.Details_var.set("35 Hours")
                self.technology_var.set("Python, Machine Learning")

            elif x == "SQL Tutorial":
                self.Content_var.set("SQL Tutorial")
                self.Details_var.set("20 Hours")
                self.technology_var.set("SQL")

            elif x == "How to Get Started with Android Development":
                self.Content_var.set(
                    "How to Get Started with Android Development")
                self.Details_var.set("30 Hours")
                self.technology_var.set("Java, Android")

            elif x == "Introduction to Data Structures and Algorithms in Python":
                self.Content_var.set(
                    "Introduction to Data Structures and Algorithms in Python")
                self.Details_var.set("40 Hours")
                self.technology_var.set("Python, Data Structures")

            elif x == "Building a To-Do List App with React":
                self.Content_var.set("Building a To-Do List App with React")
                self.Details_var.set("12 Hours")
                self.technology_var.set("JavaScript, React")

            elif x == "How to Deploy a Django App to Heroku":
                self.Content_var.set("How to Deploy a Django App to Heroku")
                self.Details_var.set("12 Hours")
                self.technology_var.set("Python, Django, Heroku")

            elif x == "Introduction to Web Scraping with Python":
                self.Content_var.set(
                    "Introduction to Web Scraping with Python")
                self.Details_var.set("20 Hours")
                self.technology_var.set("Python, Web Scraping")

            elif x == "How to Build a Blog Using Django and Python":
                self.Content_var.set(
                    "How to Build a Blog Using Django and Python")
                self.Details_var.set("25 Hours")
                self.technology_var.set("Python, Django")

            elif x == "Object-Oriented Programming in Python":
                self.Content_var.set("Object-Oriented Programming in Python")
                self.Details_var.set("30 Hours")
                self.technology_var.set("Python, OOP")

            elif x == "Java Programming Tutorial for Beginners":
                self.Content_var.set("Java Programming Tutorial for Beginners")
                self.Details_var.set("35 Hours")
                self.technology_var.set("Java")

            elif x == "C++ Full Course":
                self.Content_var.set("C++ Full Course")
                self.Details_var.set("45 Hours")
                self.technology_var.set("C++")

        lstbox = Listbox(DataFrameRight, font=(
            "Comic Sans MS", 12, "normal"), width=25, height=23)
        lstbox.bind("<<ListboxSelect>>", selectCourse)
        lstbox.grid(row=0, column=0, padx=5, pady=5)
        listscrollbar.config(command=lstbox.yview)

        for item in listbook:
            lstbox.insert(END, item)


# Buttons to update the textbox content
        buttonframe = Frame(self.root, bd=5, relief=RIDGE,
                            padx=20, bg="#ffffff")
        buttonframe.place(x=0, y=475, width=1345, height=70)

        btninsert = Button(buttonframe, cursor="hand2", text="Enter", command=self.addData, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#ff7f00", fg="#0000ff", bd=5, pady=9)
        btninsert.grid(row=0, column=0)

        btnreset = Button(buttonframe, cursor="watch", text="Read", command=self.showData, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#ff7f00", fg="#0000ff", bd=5, pady=9)
        btnreset.grid(row=0, column=2)

        btndelete = Button(buttonframe, cursor="hand2", text="New", command=self.reset, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#00ff00", fg="#0000ff", bd=5, pady=9)
        btndelete.grid(row=0, column=3)

        btnexit = Button(buttonframe, cursor="watch", text="Exit", command=self.iexit, font=(
            "Comic Sans MS", 11, "bold"), width=34, bg="#00ff00", fg="#0000ff", bd=5, pady=9)
        btnexit.grid(row=0, column=4)


# INFORMATION Frame
        infoframe = Frame(self.root, bd=5, relief=RIDGE,
                          padx=5, bg="#046a38")
        infoframe.place(x=5, y=549, width=1345, height=143)

        Tableframe = Frame(infoframe, bd=4, relief=RIDGE, bg="#00ff00")
        Tableframe.place(x=1, y=2, width=1325, height=130)

# # I will get the joining letter from Ericsson India Global Service within November. God will help me.

        xscroll = ttk.Scrollbar(Tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Tableframe, orient=VERTICAL)
# Created a Treeview widget to display the data from MySQL

        self.habiticaTable = ttk.Treeview(Tableframe, columns=("Launch:", "Today:", "Location:", "Exercise:", "Stretch:", "Reading:", "Duration:", "Coding:",
                                                               "Number:", "Content:", "Details:", "Technology:", "Water:", "Sleep:", "Balance:", "Remarks:"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
# ScrollBar added to the Treeview
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.habiticaTable.xview)
        yscroll.config(command=self.habiticaTable.yview)
# The column headings defined

        self.habiticaTable.heading("Launch:", text="Launch")
        self.habiticaTable["show"] = "headings"
        self.habiticaTable.pack(fill=BOTH, expand=1)

        self.habiticaTable.heading("Today:", text="Today")
        self.habiticaTable.heading("Location:", text="Location")
        self.habiticaTable.heading("Exercise:", text="Exercise")
        self.habiticaTable.heading("Stretch:", text="Stretch")
        self.habiticaTable.heading("Reading:", text="Reading")
        self.habiticaTable.heading("Duration:", text="Duration")
        self.habiticaTable.heading("Coding:", text="Coding")
        self.habiticaTable.heading("Number:", text="Number")
        self.habiticaTable.heading("Content:", text="Content")
        self.habiticaTable.heading("Details:", text="Details")
        self.habiticaTable.heading("Technology:", text="Technology")
        self.habiticaTable.heading("Water:", text="Start Date")
        self.habiticaTable.heading("Sleep:", text="End Date")
        self.habiticaTable.heading("Balance:", text="Balance")
        self.habiticaTable.heading("Remarks:", text="Remarks")
        self.habiticaTable["show"] = "headings"
        self.habiticaTable.pack(fill=BOTH, expand=1)

# THE WIDTH OF COLUMNS IN TABLE checked
        self.habiticaTable.column("Launch:", width=100)
        self.habiticaTable.column("Today:", width=100)
        self.habiticaTable.column("Location:", width=100)
        self.habiticaTable.column("Exercise:", width=100)
        self.habiticaTable.column("Stretch:", width=100)
        self.habiticaTable.column("Reading:", width=100)
        self.habiticaTable.column("Duration:", width=100)
        self.habiticaTable.column("Coding:", width=100)
        self.habiticaTable.column("Number:", width=100)
        self.habiticaTable.column("Content:", width=100)
        self.habiticaTable.column("Details:", width=100)
        self.habiticaTable.column("Technology:", width=100)
        self.habiticaTable.column("Water:", width=100)
        self.habiticaTable.column("Sleep:", width=100)
        self.habiticaTable.column("Balance:", width=100)
        self.habiticaTable.column("Remarks:", width=100)

        self.connect_to_database()
# Fetched the data from MySQL database
        self.fetch_data_from_mysql()
        self.habiticaTable.bind("<ButtonRelease-1>",
                                self.get_cursor)
# Event Binding

    def connect_to_database(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="library_database")
        self.my_cursor = self.my_db.cursor()
        print("Connected First Time")

    def addData(self):
        if self.my_db is not None:

            query = """
                INSERT INTO habitica (Launch, Today, Location, Exercise, Stretch, Reading, Duration,
                                    Coding, Number, Content, Details, Technology, Water, Sleep, Balance, Remarks)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                """

# Created a tuple of data to insert
            data = (
                self.Launch_var.get(),
                self.Today_var.get(),
                self.Location_var.get(),
                self.Exercise_var.get(),
                self.Stretch_var.get(),
                self.Reading_var.get(),
                self.Duration_var.get(),
                self.Coding_var.get(),
                self.Number_var.get(),
                self.Content_var.get(),
                self.Details_var.get(),
                self.technology_var.get(),
                self.Water_var.get(),
                self.Sleep_var.get(),
                self.Balance_var.get(),
                self.Remarks_var.get()
            )

# Executed the SQL command
            self.my_cursor.execute(query, data)
            self.my_db.commit()  # Commit the transaction
            self.fetch_data_from_mysql()

            messagebox.showinfo("Success", "Data inserted successfully!")
            print("Data inserted successfully.")

    def fetch_data_from_mysql(self):
        """Fetched data from MySQL database and display it in the Treeview"""
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="library_database")

        if conn.is_connected():
            print("Connected Second Time")

# Created a cursor object to interact with the database
            cursor = conn.cursor()

# Executed the SELECT query
            query = "SELECT * FROM habitica"
            cursor.execute(query)

# Fetched all the rows
            rows = cursor.fetchall()

# Inserted rows into the Treeview widget
            if len(rows) != 0:

                self.habiticaTable.delete(*self.habiticaTable.get_children())
                for row in rows:
                    self.habiticaTable.insert("", END, values=row)

# Closed the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()
# Inserted the data into the text box in the desired format

    def showData(self):
        self.txtBox.insert(END, "Launch:\t" + self.Launch_var.get() + "\n")
        self.txtBox.insert(END, "Today:\t" +
                           self.Today_var.get() + "\n")
        self.txtBox.insert(END, "Location:\t" +
                           self.Location_var.get() + "\n")
        self.txtBox.insert(END, "Exercise:\t" +
                           self.Exercise_var.get() + "\n")
        self.txtBox.insert(END, "Stretch:\t" + self.Stretch_var.get() + "\n")
        self.txtBox.insert(END, "Reading:\t" + self.Reading_var.get() + "\n")
        self.txtBox.insert(END, "Duration:\t" +
                           self.Duration_var.get() + "\n")
        self.txtBox.insert(END, "Coding:\t" +
                           self.Coding_var.get() + "\n")
        self.txtBox.insert(END, "Number:\t" +
                           self.Number_var.get() + "\n")
        self.txtBox.insert(END, "Content:\t" + self.Content_var.get() + "\n")
        self.txtBox.insert(END, "Details:\t" + self.Details_var.get() + "\n")
        self.txtBox.insert(END, "Technology:\t" +
                           self.technology_var.get() + "\n")
        self.txtBox.insert(END, "Start Date:\t" +
                           self.Water_var.get() + "\n")
        self.txtBox.insert(END, "End Date:\t" + self.Sleep_var.get() + "\n")
        self.txtBox.insert(END, "Balance:\t" + self.Balance_var.get() + "\n")
        self.txtBox.insert(END, "Remarks:\t" + self.Remarks_var.get() + "\n")

    def get_cursor(self, event=""):
        # To get the currently focused row
        cursor_row = self.habiticaTable.focus()
        content = self.habiticaTable.item(cursor_row)
        rows = content.get("values")

# Checked if the row is valid
        if cursor_row == '':

            print("Selected row is empty")
            return
# Exit the function if the row has no values

# Checked if 'rows' is None or an empty list
        if rows is None or len(rows) == 0:
            print("There is no value")
            return

# Assigned values from the database or other data source to StringVars
        self.Launch_var.set(rows[0])
        self.Today_var.set(rows[1])
        self.Location_var.set(rows[2])
        self.Exercise_var.set(rows[3])
        self.Stretch_var.set(rows[4])
        self.Reading_var.set(rows[5])
        self.Duration_var.set(rows[6])
        self.Coding_var.set(rows[7])
        self.Number_var.set(rows[8])
        self.Content_var.set(rows[9])
        self.Details_var.set(rows[10])
        self.technology_var.set(rows[11])
        self.Water_var.set(rows[12])
        self.Sleep_var.set(rows[13])
        self.Balance_var.set(rows[14])
        self.Remarks_var.set(rows[14])

    def reset(self):

        self.Launch_var.set("")
        self.Today_var.set("")
        self.Location_var.set("")
        self.Exercise_var.set("")
        self.Stretch_var.set("")
        self.Reading_var.set("")
        self.Duration_var.set("")
        self.Coding_var.set("")
        self.Number_var.set("")
        self.Content_var.set("")
        self.Details_var.set("")
        self.technology_var.set("")
        self.Water_var.set("")
        self.Sleep_var.set("")
        self.Balance_var.set("")
        self.Remarks_var.set("")

    def iexit(self):
        iexit = tkinter.messagebox.askyesno(
            "My Habitica", "Are you sure?")
        if iexit > 0:
            self.root.destroy()
            return


# Created the Tkinter root window
if __name__ == "__main__":
    root = Tk()
    app = MyHabitica(root)

# Started the Tkinter event loop
    root.mainloop()

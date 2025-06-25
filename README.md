# Habitica
An Application for Self Analysis.

1. Project Overview

I developed a live desktop application named "My Habitica" that uses Tkinter for the user interface, Python for the backend logic, and SQL for storing data and performing analysis. The application allows me to input data into the system, and SQL is used to store, query, and analyze that data.

Purpose: The application’s main goal is to collect data, store it in a database, and it allows me to perform weekly analysis based on that data.

Data Analysis with SQL: The data analysis is performed directly within the database using SQL queries, ensuring efficient data processing and real-time analysis.

2. Features and Functionality
The core features of the application include:

Data Entry: I am using my day to day rotine tasks data so that I can analyse them in a weekly maneer.
Data Storage: All input data is stored in an SQL database. Each entry is validated to ensure that the data meets the required format and completeness before being saved.
SQL Data Analysis: After the data is entered, the application can perform the following types of analysis directly using SQL:
Aggregate Queries: Calculated totals, averages, and other summary statistics.
Data Filtering and Reporting: Using SQL WHERE clauses to filter data and generate results.

3. Technical Breakdown
Tkinter (GUI)
Main Window: The application opens in a main window with menus, buttons, and interactive forms where users input data.
Results Display: After data is entered, the application uses a Treeview widget to display tabular data and results of SQL queries.
Interactive Buttons: Buttons trigger actions like adding new data, clear the columns for new data entry, read the inserted data. 

Python Backend (Logic)
  The backend of the application is built in Python, and it handles the logic of interacting with the database, processing user inputs, and running SQL queries:

Data Collection: When the user submits data through the Tkinter interface, Python collects the data from the entry fields and performs initial validation checks (e.g., ensuring fields aren’t empty or that numeric fields contain valid numbers).
Database Interaction: Python communicates with the SQL database using the mysql.connector for MySQL. It uses SQL queries to insert, select and retrieve data. 
For example:
INSERT INTO for adding new records to the database.
SELECT for fetching data for analysis and displaying it in the GUI.

SQL for Data Analysis: SQL queries are written directly within the Python code to handle the data efficiently. 
SQL Database (Data Storage and Analysis)
The SQL database is responsible for storing the input data and performing the majority of the analysis. The database structure is designed to be flexible and efficient for querying.

4. Data Analysis with SQL

Data Collection: The user inputs data into the Tkinter interface (e.g., coding records, number entries).

Storing in SQL: The data is stored in the SQL database through Python’s backend logic, ensuring that it is normalized and structured properly.

SQL Queries for Analysis:
I use SQL to perform various analytical tasks, such as calculating aggregates, filtering data.
Displaying Results: Once the SQL query is executed, Python fetches the results and displays them within the Tkinter GUI. For example, it may update a Treeview widget with the inserted data.

5. Challenges Faced and Solutions
Handling User Input Errors: Ensuring data integrity was critical. I handled this by validating user inputs before they were inserted into the database, checking for missing or invalid data.


#######################################
# Example of database operations using
# a SQLite v3 database.
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
import sqlite3

#######################################
# Class to test database methods
#######################################
class FreedomTestDatabase:

    #######################################
    # Members
    #######################################
    conn = None


    #######################################
    # Creates database for testing
    #######################################
    def open(self, databaseName):
        
        # Define test tables
        sqlCreateTableCustomers = """\
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """

        sqlCreateTableAppointments = """\
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                customer_id	INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                type TEXT NOT NULL
            )
            """

        # Create database and open connection
        self.conn = sqlite3.connect(databaseName)

        # Get database cursor
        cur = self.conn.cursor()

        # Create tables (if they don't exist)
        cur.execute(sqlCreateTableCustomers)
        cur.execute(sqlCreateTableAppointments)

        # Save (commit) the changes
        self.conn.commit()


    #######################################
    # Closes database connection
    #######################################
    def close(self):
        if not self.conn is None:
            self.conn.close()


    #######################################
    # Insert single record into database
    #######################################
    def insert_customer(self, name, email):
        # Check connection initialized
        if self.conn is None:
            return -1

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for insert
        insertData = (name, email)

        # Insert a record
        cur.execute("INSERT INTO customers (name,email) VALUES (?,?)", insertData)

        # Save (commit) the changes
        self.conn.commit()

        # Return auto-generated id from insert (primary key)
        return cur.lastrowid


    #######################################
    # Insert multiple records into database
    #######################################
    def insert_appointments(self, customer_id, appointments):
        # Check connection initialized
        if self.conn is None:
            return
        
        # Get database cursor
        cur = self.conn.cursor()
        
        # Create tuple list for multiple insert
        insertData = []

        for appt in appointments:
            # Create tuple for entry
            row = (customer_id, 
                appt['Date'],
                appt['Type']
                )

            # Add tuple to list
            insertData.append(row)

        # Insert all results
        cur.executemany('INSERT INTO appointments (customer_id,appointment_date,type) VALUES (?,?,?)', insertData)

        # Save (commit) the changes
        self.conn.commit()


    #######################################
    # Update database
    #######################################
    def update_customer_email(self, customer_id, newEmail):
        # Check connection initialized
        if self.conn is None:
            return

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for update
        updateData = (newEmail, customer_id)

        # Update table
        cur.execute("UPDATE customers SET email = ? WHERE customer_id = ?", updateData) 

        # Save (commit) the changes
        self.conn.commit()


    #######################################
    # Select from database
    #######################################
    def select_appointments(self, customer_id):
        # Check connection initialized
        if self.conn is None:
            return []

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for select data
        # (Empty value in order to create as tuple, otherwise just a single value)
        selectData = (customer_id,)

        # Define select statment
        sqlSelect = """SELECT c.name,c.email,a.appointment_date as date,a.type FROM appointments a
            INNER JOIN customers c on c.customer_id = a.customer_id
            WHERE a.customer_id = ? 
            ORDER BY a.appointment_date
            """

        # Execute SQL statment
        cur.execute(sqlSelect, selectData)

        # Get results into a list
        selectedResults = cur.fetchall()

        # Return list
        return selectedResults


    #######################################
    # Delete from database
    #######################################
    def delete_customer(self, customer_id):
        # Check connection initialized
        if self.conn is None:
            return

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for update
        deleteData = (customer_id,)

        # Delete related and primary data
        cur.execute("DELETE FROM appointments WHERE customer_id = ?", deleteData)
        cur.execute("DELETE FROM customers WHERE customer_id = ?", deleteData)

        # Save (commit) the changes
        self.conn.commit()
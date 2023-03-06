#######################################
# Example of database operations using
# a SQLite v3 database.
#
# Alan Barr (GitHub: freedom35)
# March 2023
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
    def open(self, db_name):
        
        # Define test tables
        sql_create_table_customers = """\
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """

        sql_create_table_appointments = """\
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                customer_id	INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                type TEXT NOT NULL
            )
            """

        # Create database and open connection
        self.conn = sqlite3.connect(db_name)

        # Get database cursor
        cur = self.conn.cursor()

        # Create tables (if they don't exist)
        cur.execute(sql_create_table_customers)
        cur.execute(sql_create_table_appointments)

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
        insert_data = (name, email)

        # Insert a record
        cur.execute("INSERT INTO customers (name,email) VALUES (?,?)", insert_data)

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
        insert_data = []

        for appt in appointments:
            # Create tuple for entry
            row = (customer_id, 
                appt['Date'],
                appt['Type']
                )

            # Add tuple to list
            insert_data.append(row)

        # Insert all results
        cur.executemany('INSERT INTO appointments (customer_id,appointment_date,type) VALUES (?,?,?)', insert_data)

        # Save (commit) the changes
        self.conn.commit()


    #######################################
    # Update database
    #######################################
    def update_customer_email(self, customer_id, new_email):
        # Check connection initialized
        if self.conn is None:
            return

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for update
        update_data = (new_email, customer_id)

        # Update table
        cur.execute("UPDATE customers SET email = ? WHERE customer_id = ?", update_data) 

        # Save (commit) the changes
        self.conn.commit()


    #######################################
    # Select from database (list)
    #######################################
    def select_appointments_as_list(self, customer_id):
        # Check connection initialized
        if self.conn is None:
            return []

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for select data
        # (Empty value in order to create as tuple, otherwise just a single value)
        select_data = (customer_id,)

        # Define select statement
        sql_select = """SELECT a.appointment_date as date,c.name,a.type FROM appointments a
            INNER JOIN customers c on c.customer_id = a.customer_id
            WHERE a.customer_id = ? 
            ORDER BY a.appointment_date
            """

        # Execute SQL statement
        cur.execute(sql_select, select_data)

        # Get results into a list
        selected_results = cur.fetchall()

        # Return list
        return selected_results


    #######################################
    # Select from database (dictionary)
    #######################################
    def select_customers_as_dict(self):
        # Check connection initialized
        if self.conn is None:
            return []

        # Assign method for converting to dictionary
        self.conn.row_factory = self.dictionary_factory

        # Get database cursor
        cur = self.conn.cursor()

        # Define select statement
        sql_select = 'SELECT * FROM customers'

        # Execute SQL statement
        cur.execute(sql_select)

        # Get results into a dictionary (via row factory)
        selected_results = cur.fetchall()

        # Restore row factory to default
        self.conn.row_factory = None

        # Return list
        return selected_results


    #######################################
    # Dictionary Factory
    #######################################
    def dictionary_factory(self, cursor, row):
        d = {}

        # Create dictionary entry for each value
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        
        return d
    

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
        delete_data = (customer_id,)

        # Delete related and primary data
        cur.execute("DELETE FROM appointments WHERE customer_id = ?", delete_data)
        cur.execute("DELETE FROM customers WHERE customer_id = ?", delete_data)

        # Save (commit) the changes
        self.conn.commit()
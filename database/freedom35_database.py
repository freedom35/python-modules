#######################################
# Example of database operations using
# a SQLite v3 database.
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
import sqlite3
import time

from datetime import datetime

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
        sqlCreateTableTests = """\
            CREATE TABLE IF NOT EXISTS tests (
                test_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                timestamp TEXT NOT NULL,
                name TEXT NOT NULL
            )
            """

        sqlCreateTableResults = """\
            CREATE TABLE IF NOT EXISTS results (
                result_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                test_id	INTEGER NOT NULL,
                result TEXT NOT NULL
            )
            """

        # Create database and open connection
        self.conn = sqlite3.connect(databaseName)

        # Get database cursor
        cur = self.conn.cursor()

        # Create tables (if they don't exist)
        cur.execute(sqlCreateTableTests)
        cur.execute(sqlCreateTableResults)


    #######################################
    # Closes database connection
    #######################################
    def close(self):
        if not self.conn is None:
            self.conn.close()


    #######################################
    # Insert results into database
    #######################################
    def insert_test_results(self, resultsName, results):
        # Check database is open
        if self.conn is None:
            return -1

        # Get submission time
        now = datetime.now()
        nowstr = now.strftime('%Y-%m-%d')

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for insert
        insertData = (nowstr, resultsName)

        # Insert a record
        cur.execute("INSERT INTO tests (timestamp,name) VALUES (?,?)", insertData)

        # Get auto-generated id from insert
        testid = cur.lastrowid

        # Create tuple list for multiple insert
        resultdata = []

        for r in results:
            # Create tuple for entry
            row = (testid, r)

            # Add tuple to list
            resultdata.append(row)

        # Insert all results
        cur.executemany('INSERT INTO results (test_id,result) VALUES (?,?)', resultdata)

        # Save (commit) the changes
        self.conn.commit()

        # Return primary key
        return testid


    #######################################
    # Update results from database
    #######################################
    def update_test_name(self, testid, newResultsName):
        # Check database is open
        if self.conn is None:
            return

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for update
        updateData = (testid, newResultsName)

        # Update table
        cur.execute("UPDATE tests SET name = ? WHERE test_id = ?", updateData) 

        # Save (commit) the changes
        self.conn.commit()


    #######################################
    # Select results from database
    #######################################
    def select_test_results(self, testid):
        # Check database is open
        if self.conn is None:
            return []

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for select data
        selectData = (testid,)

        # Define select statment
        sqlSelect = """SELECT t.name, r.result FROM RESULTS r
            INNER JOIN tests t on t.test_id = r.test_id
            WHERE r.test_id = ? 
            ORDER BY r.result_id
            """

        # Execute SQL statment
        cur.execute(sqlSelect, selectData)

        # Get results into a list
        selectedResults = cur.fetchall()

        # Return list
        return selectedResults


    #######################################
    # Delete results from database
    #######################################
    def delete_test(self, testid):
        # Check database is open
        if self.conn is None:
            return

        # Get database cursor
        cur = self.conn.cursor()

        # Create tuple for update
        deleteData = (testid,)

        # Update table
        cur.execute("DELETE FROM results WHERE test_id = ?", deleteData)
        cur.execute("DELETE FROM tests WHERE test_id = ?", deleteData)

        # Save (commit) the changes
        self.conn.commit()
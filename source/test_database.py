#######################################
# GitHub: Alan Barr (freedom35) 2020
#
# Test/Example Usage
#######################################
from freedom35_database import FreedomTestDatabase


#######################################
# Main method
#######################################
def main():
    try:
        db = FreedomTestDatabase()

        # Use an in-memory database for repeat testing
        # Alternate option: create a database file in the local directory sych as 'test.db'
        db.open(':memory:')

        # Test data
        results = [ 'Apple', 'Orange', 'Pear' ]

        # Insert into database
        testid = db.insert_test_results('Condor', results)

        # Change test name
        db.update_test_name(testid, 'Eagle')

        # Fetch results from database
        selectedResults = db.select_test_results(testid)

        # Output results to console
        for r in selectedResults:
            print('Result for {}: {}'.format(r[0], r[1]))

        # Delete test results
        db.delete_test(testid)

        # Finished
        db.close()

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

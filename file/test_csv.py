#######################################
# Example usage for module:
# freedom35_csv.py
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
from freedom35_csv import write_entry, write_entries, read_entries


#######################################
# Main method
#######################################
def main():
    try:
        # Local filename for test
        filename = 'test.csv'

        # Create some test data
        dataToWrite = []
        dataToWrite.append({ 'Name': 'Condor', 'Age': '34' })
        dataToWrite.append({ 'Name': 'Eagle', 'Age': '35' })

        # Write data to new file
        write_entries(filename, dataToWrite, False)

        # Append another entry
        write_entry(filename, { 'Name': 'Hawk', 'Age': '32' })

        # Read file back
        dataFromRead = read_entries(filename)

        # Print to console
        for line in dataFromRead:
            print('Name: {}, Age: {}'.format(line['Name'], line['Age']))
        
    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

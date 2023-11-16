#######################################
# Example usage for module:
# freedom35/io/csv.py
#
# Alan Barr (GitHub: freedom35)
# March 2023
#######################################
import sys
import os

# Get path of current file
current = os.path.dirname(os.path.realpath(__file__))

# Get path of source modules
parent = os.path.dirname(current)
src = os.path.join(parent, 'src')
 
# Add source path to module search
sys.path.append(src)

# Import methods
from freedom35.io.csv import write_entry, write_entries, read_entries


#######################################
# Main method
#######################################
def main():
    try:
        # Local filename for test
        filename = 'test.csv'

        # Create some test data
        data_to_write = []
        data_to_write.append({ 'Name': 'Ricky', 'Age': '34' })
        data_to_write.append({ 'Name': 'Bubbles', 'Age': '35' })

        # Write data to new file
        write_entries(filename, data_to_write, False)

        # Append another entry
        write_entry(filename, { 'Name': 'Julian', 'Age': '33' })

        # Read file back
        data_from_read = read_entries(filename)

        # Print to console
        for line in data_from_read:
            print('Name: {}, Age: {}'.format(line['Name'], line['Age']))
        
    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

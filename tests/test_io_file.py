#######################################
# Example usage for module:
# freedom35/io/file.py
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
from freedom35.io.file import write_to_file, read_from_file


#######################################
# Main method
#######################################
def main():
    try:
        # Local filename for test
        filename = 'test.txt'

        # Create some test data
        data_to_write = [ 'Randy', 'Sarah', 'Lucy' ]

        # Create new file (overwrite)
        append = False

        # Write data to file
        write_to_file(filename, data_to_write, append)

        # Read file back
        data_from_read = read_from_file(filename)

        # Print to console
        for line in data_from_read:
            print(line)
        
    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

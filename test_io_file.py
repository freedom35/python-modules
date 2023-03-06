#######################################
# Example usage for module:
# freedom35/io/file.py
#
# Alan Barr (GitHub: freedom35)
# March 2023
#######################################
from freedom35.io.file import write_to_file, read_from_file


#######################################
# Main method
#######################################
def main():
    try:
        # Local filename for test
        filename = 'test.txt'

        # Create some test data
        dataToWrite = [ 'Randy', 'Sarah', 'Lucy' ]

        # Create new file (overwrite)
        append = False

        # Write data to file
        write_to_file(filename, dataToWrite, append)

        # Read file back
        dataFromRead = read_from_file(filename)

        # Print to console
        for line in dataFromRead:
            print(line)
        
    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

#######################################
# Example of basic file I/O operations.
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################


#######################################
# Write to file
#######################################
def write_to_file(filename, lines, append):
    # Determine whether appending to file 
    # or overwriting with new one
    openType = 'a' if append else 'w'

    # Create file for writing
    with open(filename, openType) as f:
        # Insert newline char between each item
        # (Otherwise list will be concatenated into one line)
        separateLines = map(lambda x: f"{x}\n", lines)

        # Write all lines to file
        f.writelines(separateLines)


#######################################
# Read from file
#######################################
def read_from_file(filename):
    # Create list for file contents
    lines = []

    # Open file as read-only
    with open(filename, 'r') as f:
        # Alt: Read entire file and split based on newline
        #lines = f.read().splitlines()

        # Read each line in file
        for line in f.readlines():
            # Remove trailing newline chars from file
            lines.append(line.rstrip('\r\n'))
    
    # Return contents
    return lines

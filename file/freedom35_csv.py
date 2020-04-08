#######################################
# Example of basic CSV file operations.
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
import csv

#######################################
# Write CSV to file
#######################################
def write_entry(filename, dictionaryEntry):
    
    fieldnames = []

    # Get fieldnames from dictionary
    for key in dictionaryEntry:
        fieldnames.append(key)

    # Open file for append
    # (newline='' preserves line endings)
    with open(filename, 'a', newline='') as csvfile:
        # Create writer with corresponding fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header line if this is first entry
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write new entry
        writer.writerow(dictionaryEntry)


#######################################
# Write multiple entries to CSV file
#######################################
def write_entries(filename, dictionaryEntries, append):
    
    # Check we have something to write
    if len(dictionaryEntries) == 0:
        return

    fieldnames = []

    # Get fieldnames from first entry
    for key in dictionaryEntries[0]:
        fieldnames.append(key)

    # Determine whether appending to file 
    # or overwriting with new one
    openType = 'a' if append else 'w'

    # Open file for writing
    # (newline='' preserves line endings)
    with open(filename, openType, newline='') as csvfile:
        # Create writer with corresponding fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header line if this is first entry
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write new entry
        writer.writerows(dictionaryEntries)


#######################################
# Read CSV from file
#######################################
def read_entries(filename):

    entries = []

    # Open file for reading
    # (newline='' preserves line endings)
    with open(filename, 'r', newline='') as csvfile:
        # Read file using CSV reader
        reader = csv.DictReader(csvfile)

        # Add dictionary entry for each row
        for row in reader:
            entries.append(row)
    
    # Return file entries
    return entries


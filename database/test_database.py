#######################################
# Example usage for module:
# freedom35_database.py
#
# Alan Barr (GitHub: freedom35)
# May 2020
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

        # Insert into database
        customer_id = db.insert_customer('Jim Lahey', 'jim_lahey@yahoo.ca')

        # Test data
        appointments = []
        appointments.append({ 'Date': '2020-09-01', 'Type': 'Checkup' })
        appointments.append({ 'Date': '2020-10-07', 'Type': 'Filling' })
        appointments.append({ 'Date': '2020-10-31', 'Type': 'Crown' })

        # Insert multiple
        db.insert_appointments(customer_id, appointments)
        
        # Change email
        db.update_customer_email(customer_id, 'jim_lahey_supervisor@yahoo.ca')

        # Fetch dictionary of customers from database
        selectedCustomers = db.select_customers_as_dict()

        # Output customers to console
        for cust in selectedCustomers:
            print('Customer Info:    {name} ({email})'.format(name=cust['name'], email=cust['email']))

        # Fetch list of appointments from database
        selectedAppointments = db.select_appointments_as_list(customer_id)

        # Output appointments to console
        for appt in selectedAppointments:
            print('Appointment Info: {}'.format(appt))

        # Delete test results
        db.delete_customer(customer_id)

        # Finished
        db.close()

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

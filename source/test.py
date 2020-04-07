#######################################
# GitHub: Alan Barr (freedom35) 2020
#
# Example usage: see individual methods
#######################################
from freedom35_smtp_mime import FreedomEmail
from freedom35_smtp_plaintext import send_plaintext_message
from freedom35_database import FreedomTestDatabase


#######################################
# Main method
#######################################
def main():
    try:
        print('*** For email tests, uupdate test values before running ***')
        #test_smtp_mime()
        #test_smtp_plaintext()
        test_database()

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# freedom35_smtp_mime
#######################################
def test_smtp_mime():

    email = FreedomEmail()

    email.smtpUser = ''
    email.smtpPwd = ''
    
    email.fromName = 'Test Sender'
    email.fromAddress = '...@gmailcom'

    email.emailSubject = 'Test MIME'
    email.emailContentPlaintext = 'Test message (plaintext).'
    email.emailContentHtml = """\
        <html>
        <head></head>
        <body>
            <p>Test message (HTML).</p>
        </body>
        </html>
        """
    
    # Attachment note:
    # Specify full path if file to attach is not in local dir.
    # Use os.path.join for platform (Windows/UNIX) independence (import os)
    # i.e. if file is in resources sub-dir:
    # attachmentPath = os.path.join('resources', 'readme.md')

    #email.attachmentFilename = 'readme.md'

    toName = 'Test Recipient'
    toAddress = '...@gmail.com'

    email.send_mime_message(toName, toAddress)


#######################################
# freedom35_smtp_plaintext
#######################################
def test_smtp_plaintext():

    smtpUser = ''
    smtpPwd = ''

    fromName = 'Test Sender'
    fromAddress = '...@gmail.com'

    toName = 'Test Recipient'
    toAddress = '...@gmail.com'

    subject = 'Test Plaintext'
    message = 'This is a test message.'

    send_plaintext_message(toName, toAddress, fromName, fromAddress, subject, message, smtpUser, smtpPwd)


#######################################
# freedom35_database
#######################################
def test_database():
    
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
        print('Database result: {}'.format(r))

    # Delete test results
    db.delete_test(testid)

    # Finished
    db.close()


#######################################
# Local entrypoint: python3 test.py
#######################################
if __name__ == "__main__":
    main()

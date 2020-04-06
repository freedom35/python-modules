#######################################
# GitHub: Alan Barr (freedom35) 2020
#
# Example usage: see individual methods
#######################################

# Required for MIME
from freedom35_smtp_mime import FreedomEmail

# Required for plaintext
from freedom35_smtp_plaintext import send_plaintext_message


#######################################
# Main method
#######################################
def main():
    try:
        print('*** Update test values before running ***')
        #test_smtp_mime()
        #test_smtp_plaintext()

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
# Local entrypoint: python3 test.py
#######################################
if __name__ == "__main__":
    main()

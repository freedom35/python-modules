#######################################
# Example usage for module:
# freedom35_smtp_mime.py
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
from freedom35_smtp_mime import FreedomEmail


#######################################
# Main method
#######################################
def main():
    try:
        toName = 'Test Recipient'
        toAddress = '...@gmail.com'         # Update!

        email = FreedomEmail()
        
        email.smtpUser = 'user1'            # Update!
        email.smtpPwd = 'password1'         # Update!

        email.fromName = 'Test Sender'
        email.fromAddress = '...@gmailcom'  # Update!

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
        
        email.send_mime_message(toName, toAddress)
        
    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

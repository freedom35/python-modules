#######################################
# Example usage for module:
# freedom35/smtp/mime.py
#
# Alan Barr (GitHub: freedom35)
# March 2023
#######################################
from freedom35.smtp.mime import FreedomMimeEmail


#######################################
# Main method
#######################################
def main():
    try:
        to_name = 'Test Recipient'
        to_address = 'j_to_the_roc@hotmail.com'  # Update - example only!

        email = FreedomMimeEmail()
        
        email.smtp_user = 'user1'                # Update - example only!
        email.smtp_pwd = 'password1'             # Update - example only!

        email.from_name = 'Test Sender'
        email.from_address = 'tyrone_p@yahoo.ca' # Update - example only!

        email.email_subject = 'Test MIME'
        email.email_content_plaintext = 'Test message (plaintext).'
        email.email_content_html = """\
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
        # attachment_path = os.path.join('resources', 'readme.md')

        #email.attachment_filename = 'readme.md'
        
        email.send_mime_message(to_name, to_address)
        
    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

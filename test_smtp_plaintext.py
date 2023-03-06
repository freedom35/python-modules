#######################################
# Example usage for module:
# freedom35/smtp/plaintext.py
#
# Alan Barr (GitHub: freedom35)
# March 2023
#######################################
from freedom35.smtp.plaintext import send_plaintext_message


#######################################
# Main method
#######################################
def main():
    try:
        to_name = 'Test Recipient'
        to_address = 'trevor_sunnyvale@hotmail.com'  # Update - example only!

        from_name = 'Test Sender'
        from_address = 'cory_sunnyvale@hotmail.com'  # Update - example only!

        subject = 'Test Plaintext'
        message = 'This is a test message.'

        smtp_user = 'user1'              # Update - example only!
        smtp_pwd = 'password1'           # Update - example only!

        send_plaintext_message(to_name, to_address, from_name, from_address, subject, message, smtp_user, smtp_pwd)

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

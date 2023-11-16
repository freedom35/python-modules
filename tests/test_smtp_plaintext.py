#######################################
# Example usage for module:
# freedom35/smtp/plaintext.py
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

# Import method
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

        send_plaintext_message(to_name, to_address, from_name, from_address, 
                               subject, message, smtp_user, smtp_pwd)

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

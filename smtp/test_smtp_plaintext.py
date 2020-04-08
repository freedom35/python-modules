#######################################
# Example usage for module:
# freedom35_smtp_plaintext.py
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
from freedom35_smtp_plaintext import send_plaintext_message


#######################################
# Main method
#######################################
def main():
    try:
        toName = 'Test Recipient'
        toAddress = 'trevor_sunnyvale@hotmail.com'  # Update!

        fromName = 'Test Sender'
        fromAddress = 'cory_sunnyvale@hotmail.com'  # Update!

        subject = 'Test Plaintext'
        message = 'This is a test message.'

        smtpUser = 'user1'              # Update!
        smtpPwd = 'password1'           # Update!

        send_plaintext_message(toName, toAddress, fromName, fromAddress, subject, message, smtpUser, smtpPwd)

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

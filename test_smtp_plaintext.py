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

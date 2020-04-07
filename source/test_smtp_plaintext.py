#######################################
# GitHub: Alan Barr (freedom35) 2020
#
# Test/Example Usage
#######################################
from freedom35_smtp_plaintext import send_plaintext_message


#######################################
# Main method
#######################################
def main():
    try:
        smtpUser = 'user1'              # Update!
        smtpPwd = 'password1'           # Update!

        fromName = 'Test Sender'
        fromAddress = '...@gmail.com'   # Update!

        toName = 'Test Recipient'
        toAddress = '...@gmail.com'     # Update!

        subject = 'Test Plaintext'
        message = 'This is a test message.'

        send_plaintext_message(toName, toAddress, fromName, fromAddress, subject, message, smtpUser, smtpPwd)

    except Exception as e:
        print('Error: {e}'.format(e=str(e)))


#######################################
# Local entrypoint
#######################################
if __name__ == "__main__":
    main()

#######################################
# Module for sending plaintext email
# via SMTP.
#
# Alan Barr (GitHub: freedom35)
# March 2023
#######################################
import smtplib

from email.message import EmailMessage


#######################################
# Sends plaintext message using SMTP
#######################################
def send_plaintext_message(to_name, to_address, from_name, from_address, subject, content_as_string, smtp_user, smtp_pwd):

    # Create message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = '{} <{}>'.format(from_name, from_address)
    msg['To'] = '{} <{}>'.format(to_name, to_address)
    #msg['Bcc'] = 'bcc address'

    # Set content to plaintext
    msg.set_content(content_as_string)

    # Send using secure SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # For security, login using an app generated password (not account password)
        server.login(smtp_user, smtp_pwd)
        server.send_message(msg)

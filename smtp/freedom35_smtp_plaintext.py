#######################################
# Module for sending plaintext email
# via SMTP.
#
# Alan Barr (GitHub: freedom35)
# April 2020
#######################################
import smtplib

from email.message import EmailMessage
from email.headerregistry import Address


#######################################
# Sends plaintext message using SMTP
#######################################
def send_plaintext_message(toName, toAddress, fromName, fromAddress, subject, contentAsString, smtpUser, smtpPwd):

    # Create message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = '{} <{}>'.format(fromName, fromAddress)
    msg['To'] = '{} <{}>'.format(toName, toAddress)
    #msg['Bcc'] = 'bcc address'

    # Set content to plaintext
    msg.set_content(contentAsString)

    # Send using secure SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # For security, login using an app generated password (not account password)
        server.login(smtpUser, smtpPwd)
        server.send_message(msg)

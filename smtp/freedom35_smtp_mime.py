#########################################
# Module for sending a MIME
# (Multipurpose Internet Mail Extensions)
# email via SMTP.
#
# Alan Barr (GitHub: freedom35)
# April 2020
#########################################

# Required for sending message
import smtplib

# Required for MIME
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Required for attachment
from email import encoders

#######################################
# Class to generate MIME email
#######################################
class FreedomEmail:

    #######################################
    # Members
    #######################################
    smtpUser = ''
    smtpPwd = ''
    smtpServer = 'smtp.gmail.com'
    smtpPort = 465
    fromName = ''
    fromAddress = ''
    bccAddress = None
    attachmentFilename = None
    emailSubject = ''
    emailContentPlaintext = 'Plaintext message content.'
    emailContentHtml = """\
        <html>
        <head></head>
        <body>
            <p>HTML message content.</p>
        </body>
        </html>
        """


    #######################################
    # Create MIME Message (as string)
    #######################################
    def send_mime_message(self, toName, toAddress):

        # Setup email
        msg = MIMEMultipart('mixed')
        msg['Subject'] = self.emailSubject
        msg['From'] = '{} <{}>'.format(self.fromName, self.fromAddress)
        msg['To'] = '{} <{}>'.format(toName, toAddress)

        # BCC (Optional)
        if not self.bccAddress is None:
            msg['Bcc'] = self.bccAddress

        # MIME Structure:
        # mixed
        # alternative
        #   plaintext
        #   html
        # attachment
        alt = MIMEMultipart('alternative')
        alt.attach(MIMEText(self.emailContentPlaintext, 'plain'))
        alt.attach(MIMEText(self.emailContentHtml, 'html'))
        msg.attach(alt)

        # Add attachment (optional)
        if not self.attachmentFilename is None:
            # Specify full path if file not local
            attachmentPath = self.attachmentFilename

            # Read attachment file 
            with open(attachmentPath, 'rb') as attachment:
                sub = MIMEBase('application', 'octet-stream')
                sub.set_payload(attachment.read())
            
            # Encode in base 64 ASCII
            encoders.encode_base64(sub)

            # Set attachment header, use filename only
            sub.add_header('Content-Disposition', 'attachment', filename=self.attachmentFilename)

            # Add attachment object to message
            msg.attach(sub)
        
        # Send using secure SMTP
        with smtplib.SMTP_SSL(self.smtpServer, self.smtpPort) as server:
            # For security, login using an app generated password (not account password)
            server.login(self.smtpUser, self.smtpPwd)
            server.send_message(msg)

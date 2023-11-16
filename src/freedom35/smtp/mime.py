#########################################
# Module for sending a MIME
# (Multipurpose Internet Mail Extensions)
# email via SMTP.
#
# Alan Barr (GitHub: freedom35)
# March 2023
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
class FreedomMimeEmail:

    #######################################
    # Members
    #######################################
    smtp_user = ''
    smtp_pwd = ''
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    from_name = ''
    from_address = ''
    bcc_address = None
    attachment_filename = None
    email_subject = ''
    email_content_plaintext = 'Plaintext message content.'
    email_content_html = """\
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
        msg['Subject'] = self.email_subject
        msg['From'] = '{} <{}>'.format(self.from_name, self.from_address)
        msg['To'] = '{} <{}>'.format(toName, toAddress)

        # BCC (Optional)
        if self.bcc_address is not None:
            msg['Bcc'] = self.bcc_address

        # MIME Structure:
        # mixed
        # alternative
        #   plaintext
        #   html
        # attachment
        alt = MIMEMultipart('alternative')
        alt.attach(MIMEText(self.email_content_plaintext, 'plain'))
        alt.attach(MIMEText(self.email_content_html, 'html'))
        msg.attach(alt)

        # Add attachment (optional)
        if self.attachment_filename is not None:
            # Specify full path if file not local
            attachment_path = self.attachment_filename

            # Read attachment file 
            with open(attachment_path, 'rb') as attachment:
                sub = MIMEBase('application', 'octet-stream')
                sub.set_payload(attachment.read())
            
            # Encode in base 64 ASCII
            encoders.encode_base64(sub)

            # Set attachment header, use filename only
            sub.add_header('Content-Disposition', 'attachment', 
                           filename=self.attachment_filename)

            # Add attachment object to message
            msg.attach(sub)
        
        # Send using secure SMTP
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            # For security, login using an app generated password 
            # (not account password)
            server.login(self.smtp_user, self.smtp_pwd)
            server.send_message(msg)

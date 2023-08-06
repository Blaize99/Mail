import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# SMTP to sent and IMAP to receive
# MIME is used to attach files
# Use MIME to attach files to the email
def send_email(sender_email, sender_password, recipient_email, subject, message, attachment_path=None):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    # Attach the file if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
            msg.attach(part)

    # Create SMTP session for sending the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

# Set up the sender's email credentials and the email details
sender_email = "Sender's email address"
sender_password = "16 character long password obtained after registering the app"
recipient_email = "Receiver's email address"
subject = "Subject of the email"
message = "Message to be sent"
attachment_path = 'firebase_data.xlsx'  # Provide the path to the attachment file (If a file is to be attached)

# Send the email with or without attachment
send_email(sender_email, sender_password, recipient_email, subject, message, attachment_path)
import os
import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from dotenv import load_dotenv

load_dotenv()

def send_mail(send_from: str, send_to: str, subject: str, text: str, files=None):
    """
    :param send_from: Email sender
    :param send_to: Email receiver
    :param subject: Subject
    :param text: Message text
    :param files: Attachment files
    :param server:
    """

    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = send_to
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=os.path.basename(f))
        # After the file is closed
        part["Content-Disposition"] = 'attachment; filename="%s"' % os.path.basename(f)
        msg.attach(part)

    with smtplib.SMTP() as smtp:  # Use login and password for sending requirement
        smtp.connect(os.getenv('EMAIL_SERVER'), os.getenv('EMAIL_PORT'))
        smtp.login(os.getenv('EMAIL_LOGIN'), os.getenv('EMAIL_PASSWORD'))
        smtp.sendmail(send_from, send_to, msg.as_string())

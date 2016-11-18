import smtplib
import email.utils

from email.mime.text import MIMEText


# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', '12068183049@tmomail.net'))
msg['From'] = email.utils.formataddr(('Author', 'terenceschumacher@gmail.com'))
msg['Subject'] = 'Simple test message'

# server = smtplib.SMTP('localhost', 1025)
# server.set_debuglevel(True) # show communication with the server
#todo: make sure you realize this order is important
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.ehlo()
server.login("terenceschumacher", "Superman88")

try:
    server.sendmail('terenceschumacher@gmail.com', ['12068183049@tmomail.net'],
                    msg.as_string())
finally:
    server.quit()
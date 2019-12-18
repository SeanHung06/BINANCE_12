import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from_address = "u8351574@gmail.com"
#to_address = "clarehuang951102@gmail.com"
to_address = "u8351574@gmail.com"
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test email"
msg['From'] = from_address
msg['To'] = to_address
# Create the message (HTML).
html = """\
We are sending an email using Python and Gmail Hi Abao I LOVE 這是用程式寄信的XD
 """
# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')
# Attach parts into message container
msg.attach(part1)
# Credentials
username = 'u8351574@gmail.com'  
password = 'qknvwdlikvbozwap'  
# Sending the email
## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
server.starttls()
server.login(username,password)  
server.sendmail(from_address, to_address, msg.as_string())  
server.quit()
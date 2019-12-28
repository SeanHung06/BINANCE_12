import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import binance1








from_address = "u8351574@gmail.com"
to_address = "u8351574@gmail.com"
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')

msg['From'] = from_address
msg['To'] = to_address
# Create the message (CSV).

# Open the file csv and input the content in the loop 
f = open('trades_df.csv')
content = 'Hi'
content += '\n\nALERT!\n\n'
reader = csv.reader(f)
line_count = 0
for row in reader:
  line_count=line_count+1
  if line_count == 250 :
    content += str(row)+'\n\n'

  

content += '\nRegards Sean'
msg = MIMEText(content)
msg['Subject'] = "Test email"
html = """\
We are sending an email using Python and Gmail
 """
# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')
# Attach parts into message container
#msg.attach(part1)

# Credentials
username = 'u8351574@gmail.com'  
password = 'qknvwdlikvbozwap'  
# Sending the email
## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
# if the signal = 1 then send the mail
email_data = open('email_send_signal.txt', 'r')

email_signal_temp = email_data.read()

if email_signal_temp == '1':
  server.starttls()
  server.login(username,password)  
  server.sendmail(from_address, to_address, msg.as_string())  
  server.quit()
  email_data = open('email_send_signal.txt', 'w')
  email_data.write('0')

  print(email_signal_temp)


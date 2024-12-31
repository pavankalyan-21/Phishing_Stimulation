import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = 'smtp.gmail.com'
PORT = 587
From_Email = 'abhiram914649@gmail.com'
password = 'tlni upbu tlos fugr'
To_Email = ['Abhiram914649@gmail.com']  # change the email
message = MIMEMultipart('alternative')
message['Subject'] = 'Change Password'
message['From'] = From_Email
message['To'] = ', '.join(To_Email)
# https://pavankalyan-21.github.io/Phishing_Stimulation.github.io/login_page.html
# has to replaced in anchor tag when we want to send to another device
html_content = """
<html>
  <body>
    <p>Alert!!</p>
    <p>Your password is about to expire. Please change your Facebook password by clicking the link below:</p>
    <a href="http://localhost:5000/">Change Here</a>
  </body>
</html>
"""
html_part = MIMEText(html_content, 'html')
message.attach(html_part)

try:
    smtp = smtplib.SMTP(HOST, PORT)
    # probing or pinging to know if the email exist or not
    status_code, response = smtp.ehlo()
    print(f'[*]Echoing server: {status_code} {response}')
    # starting tls to secure the email while sending
    status_code, response = smtp.starttls()
    print(f'[*]Starting TLS connection: {status_code} {response}')
    # loging in with email and app password to send mail
    status_code, response = smtp.login(From_Email, password)
    print(f'[*]Logging in: {status_code} {response}')
    # sending email
    smtp.sendmail(From_Email, To_Email, message.as_string())
    print("[*]Email sent successfully!")
# throw exception when the email address is incorrect or password is wrong
except Exception as e:
    print(f"[!] An error occurred: {e}")
finally:
    smtp.quit()

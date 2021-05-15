import flask
app = flask.Flask(__name__)
# Import Python Packages
import smtplib
# Set Global Variables

@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    gmail_user = 'testingprgrms@gmail.com'
    gmail_password = 'nyvwun-jeTmin-pemmo9'
    mail_from = gmail_user
    mail_to = 'programtesting205@gmail.com'
    mail_subject = 'Hello'
    mail_message_body = str(ip_address)
    mail_message = '''\
From: %s
To: %s
Subject: %s
%s
''' % (mail_from, mail_to, mail_subject, mail_message_body)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_password)
    server.sendmail(mail_from, mail_to, mail_message)
    server.close()
    return "Hello World"
app.run(host='0.0.0.0', port=5000)
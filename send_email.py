import smtplib
import ssl


def send_email(message, user_email):
    host = "smtp.gmail.com"
    port = 465
    username = user_email
    password = "csgurppgngauyzlw"
    receiver = "ojhapranav1999@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




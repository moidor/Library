import mailgun

# import email
# import smtplib
#
# msg = email.message_from_string('warning')
# msg['From'] = "moidor44@hotmail.com"
# msg['To'] = "moidor44@hotmail.com"
# msg['Subject'] = "helOoooOo"
#
# s = smtplib.SMTP("smtp.live.com", 587)
# s.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
# s.starttls()  # Puts connection to SMTP server in TLS mode
# s.ehlo()
# s.login('moidor44@hotmail.com', 'Recoba4489!')
#
# s.sendmail("moidor44@hotmail.com", "moidor44@hotmail.com", msg.as_string())
# print("Email sent.")
# s.quit()


# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
#
# message = MIMEMultipart()
# message["from"] = "Library & Co."
# message["to"] = "moidor44@hotmail.com"
# message["subject"] = "Your order"
# message.attach(MIMEText("Body"))
#
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     # Se présenter comme un client au serveur afin d'envoyer un serveur (Greetings!)
#     smtp.ehlo()
#     # tls = Transport Layer Security : s'assurer que le contenu envoyé au serveur soit crypté
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login("moidor44@gmail.com", "gbenson")
#     smtp.send_message(message)
#     print("Sent...")

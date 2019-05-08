import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("Username", "Password")
 
msg = "YOUR MESSAGE!"
server.sendmail("gbp301195@gmail.com", "gaurang.bharatpatel@lnttechservices.com", msg)
server.quit()

#input your email-id and password on line 5
# unless the less secure apps setting is enabled for your google account, google won't allow you to send mail.
# And those who have done two step verifictaion cannot send mail using above lines.
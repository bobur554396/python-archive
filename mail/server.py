import smtpd
import asyncore
import smtplib


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        return

server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("terenceschumacher", "Superman88")


asyncore.loop()
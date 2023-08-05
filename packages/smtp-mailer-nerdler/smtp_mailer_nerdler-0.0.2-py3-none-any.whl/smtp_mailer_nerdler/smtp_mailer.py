import smtplib, ssl
from email.mime.text import MIMEText

class smtp_mailer_no_ssl():
    def __init__(self,host:str,user:str,password:str,sender:str,receiver:str,subject:str,message:str,port:int=587):
        self.host = host
        self.user = user
        self.password = password
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.port = port

        msg = MIMEText(self.message)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.receiver
    
        with smtplib.SMTP(host=self.host,port=self.port) as server:
            server.login(user=self.user,password=self.password)
            server.sendmail(self.sender, self.receiver, msg.as_string())

class smtp_mailer_ssl():
    def __init__(self,host:str,user:str,password:str,sender:str,receiver:str,subject:str,message:str,port:int=465):
        self.host = host
        self.user = user
        self.password = password
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.port = port

        msg = MIMEText(self.message)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.receiver

        context = ssl.create_default_context()
    
        with smtplib.SMTP_SSL(host=self.host,port=self.port,context=context) as server:
            server.login(user=self.user,password=self.password)
            server.sendmail(self.sender, self.receiver, msg.as_string())
import getpass
import smtplib
from email.message import EmailMessage
import email.utils
from email.mime.text import MIMEText
class UserDatabase(object):
    def __init__(self):
        self.users = {}
    def add_user(self, user):
        if user.login in self.users:
            raise KeyError
        else:
            self.users[user.login] = user
    def collect_mail(self, login):
        if login not in self.users:
            raise KeyError
        else:
            return self.users[login].mail
class User(object):
    def __init__(self, user_db, login, pswd, mail):
        self.user_db = user_db
        self.login = login
        self.pswd = pswd
        self.mail = mail
        self.user_db.add_user(self)
    def send_message(self, login, msg):
        mail = user_db.collect_mail(login)
        sender_email = "barbara.szema@o2.pl"
        receiver = "barbara.szema@gmail.com"
        print(msg)
        port = 465
        password = getpass.getpass(prompt='Password: ', stream=None)
        message = EmailMessage()
        message['Subject'] = "test message"
        message['From'] = sender_email
        message['To'] = receiver
        message.set_content(f"to: {mail}\ncc: {self.mail}\n\n{msg}\n\nregards:{self.login}")
        try:
            # server = smtplib.SMTP_SSL(host='poczta.o2.pl', port=465)
            server = smtplib.SMTP('localhost', 1025)
            # server.login(sender_email, password)
            server.send_message(message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
if __name__ == '__main__':
    user_db = UserDatabase()
    a = User(user_db, "Eomer", "Guthwine", "IamTheOne@onlyWarrior")
    b = User(user_db, "AngmarWitchKing", "greatMace", "nazgul@oldfart")
    print(user_db.users)
    b.send_message("Eomer", "you little sh*t")
    # a.send_message("AngmarWitchKing", "You're such a loser, always ready to cry Cha cha cha!")
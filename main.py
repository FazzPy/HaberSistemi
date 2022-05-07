import smtplib
import pyautogui
from email.message import EmailMessage
import os

mail = input("Alıcı mail adresi : ")

def haber():
    os.mkdir("screenshots")
    sirket = "" #Kendi Mail Adresiniz
    sifre = ""  #Kendi Mail Şifreniz
    alici = mail
    newMessage = EmailMessage()
    newMessage['Subject'] = "Paranız Yükseldi"
    newMessage['From'] = sirket
    newMessage['To'] = alici
    newMessage.set_content("Paranız Yükseldi")
    pyautogui.screenshot("./screenshots/ss.png")
    files = ['./screenshots/ss.png']
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(sirket, sifre)
            smtp.send_message(newMessage)
    print("Bildirim Başarılı!")
    os.remove("./screenshots/ss.png")
    os.rmdir("./screenshots")

haber()

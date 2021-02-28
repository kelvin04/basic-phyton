import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

file_name = "receiver_list.txt"

smtp_server = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp_server,port)


def set_txt_data_to_list():
    receiver_list = []
    try:
        list_from_txt = open(file_name)
        if os.stat(file_name).st_size == 0:
            print(f"File {file_name} tidak memiliki data")
        else:
            for receiver in list_from_txt.read().split("\n"):
                receiver_list.append(receiver)
            return receiver_list
    except:
        print(f"File {file_name} tidak ditemukan")


def login_to_gmail_server():
    global sender_email
    sender_email = str(input("Input pengirim email : "))
    global sender_password
    sender_password = str(input("Input pengirim password email : "))
    try:
        server.starttls()
        server.login(sender_email, sender_password)
        print("Sukses login")
        return True
    except Exception:
        print("Gagal login, harap periksa kembali email dan password anda")
        return False


def set_email_content(email_receiver, email_subject, email_message):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email_receiver
    message['Subject'] = email_subject
    message.attach(MIMEText(email_message, 'plain'))
    return message.as_string()


def send_email(email_receiver, email_content):
    try:
        print(f"Sedang mengirim email kepada {email_receiver}, harap tunggu")
        server.sendmail(sender_email, email_receiver, email_content)
        print(f"Email berhasil dikirim kepada {email_receiver}")
    except Exception:
        print(f"Email kepada {email_receiver} gagal dikirim")
    finally:
        server.quit()



def final_project_function():
    print("Selamat datang di program pengirim pesan!")

    # Menyimpan daftar email ke dalam list
    receiver_list = set_txt_data_to_list()

    # Mengubah list data type menjadi string dengan koma, untuk pengiriman email dengan banyak tujuan
    receiver_list_str_type = ", ".join(receiver_list)

    # Login ke gmail server
    credential = login_to_gmail_server()
    if credential:
        # Input dan menyimpan data pesan email
        email_subject = str(input("Input subjek email : "))
        email_message = str(input("Input pesan email : "))
        email_content = set_email_content(receiver_list_str_type, email_subject, email_message)

        # Mengirimkan email
        send_email(receiver_list, email_content)


final_project_function()


import smtplib
import os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

final_project_file = "final_project.py"
email_list_file = "receiver_list.txt"

smtp_server = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp_server,port)


def set_txt_data_to_list():
    receiver_list = []
    try:
        list_from_txt = open(email_list_file)
        if os.stat(email_list_file).st_size == 0:
            print(f"File {email_list_file} tidak memiliki data")
        else:
            for receiver in list_from_txt.read().split("\n"):
                receiver_list.append(receiver)
            return receiver_list
    except:
        print(f"File {email_list_file} tidak ditemukan")


def login_to_gmail_server():
    global sender_email
    sender_email = str(input("Email : "))
    global sender_password
    sender_password = str(input("Password: "))
    try:
        server.starttls()
        server.login(sender_email, sender_password)
        print("Sukses login")
        return True
    except Exception:
        print("Gagal login, harap periksa kembali email dan password anda")
        return False


def set_email_content(email_receiver, email_subject, email_message, with_attachment):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email_receiver
    message['Subject'] = email_subject
    message.attach(MIMEText(email_message, 'plain'))

    total_files = get_total_attachments()

    if with_attachment.upper() == "Y":
        if total_files > 0:
            for f in os.listdir():
                with open(f, "rb") as file_attachment:
                    if f != final_project_file and f != email_list_file:
                        part = MIMEApplication(
                            file_attachment.read(),
                            Name=basename(f)
                        )
                        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                        message.attach(part)
        else:
            print("Tidak ada file yang dilampirkan")

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


def get_total_attachments():
    total_files= 0
    files_list = []

    for file_name in os.listdir():
        with open(file_name, "rb"):
            if file_name != final_project_file and file_name != email_list_file:
                files_list.append(file_name)
                total_files = total_files + 1

    if total_files > 0:
        print("File yang akan dilampirkan :", ", ".join(files_list))

    return total_files


def final_project_function():
    # Menyimpan daftar email ke dalam list
    receiver_list = set_txt_data_to_list()

    # Mengubah list data type menjadi string dengan koma, untuk pengiriman email dengan banyak tujuan
    receiver_list_str_type = ", ".join(receiver_list)

    print("Selamat datang di program pengirim pesan!")
    print("Silahkan input email dan password gmail anda")

    # Login ke gmail server
    credential = login_to_gmail_server()
    if credential:
        # Input dan menyimpan data pesan email
        email_subject = str(input("Input subjek email : "))
        email_message = str(input("Input pesan email : "))
        with_attachment = input("Apakah akan melampirkan file di email? (Y/N) : ")
        email_content = set_email_content(receiver_list_str_type, email_subject, email_message, with_attachment)

        # Mengirimkan email
        send_email(receiver_list, email_content)


final_project_function()

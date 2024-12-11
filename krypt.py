import base64
import os
from textx import metamodel_from_file


krypt_mm = metamodel_from_file('krypt.tx')

check1 = True
file1 = ""


def check(command):
    global check1
    global file1
    file_name = command.data_file.strip('"')  # Strip double quotes from the file name
    file1 = file_name
    if os.path.isfile(file_name):
        check1 = True
        print(f"File {file_name} exists.")
    else:
        print(f"File {file_name} does not exist.")


def send_email(command):
    print(f"Sending email to {command.recipient}\n")


def receive_email(command):
    print(f"Received email from {command.recipient}\n")


def decode_base64():
    global check1
    global file1

    if check1:
        with open(file1, 'r') as file:
            encoded_data = file.read().strip()

        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        print(f"File content: {decoded_data}\n")


if __name__ == "__main__":
    
    krypt_model = krypt_mm.model_from_file('program2.tx')
    
    for command in krypt_model.commands:
        if command.__class__.__name__ == "SendEmail":
            send_email(command)
        elif command.__class__.__name__ == "ReceiveEmail":
            receive_email(command)
        elif command.__class__.__name__ == "Checker":
            check(command)
        elif command.__class__.__name__ == "DecodeBase64":
            decode_base64()

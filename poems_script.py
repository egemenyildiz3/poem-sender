
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
POEM_FILE = os.path.join(SCRIPT_DIR, "poems.txt")

# Email credentials
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587
SENDER_EMAIL = "egemenyildiz03@gmail.com"
SENDER_PASSWORD = "xnlq zuud owhd lvqg"
RECEIVER_EMAIL = "nazansimay@gmail.com"


def get_next_poem():
    if not os.path.exists(POEM_FILE):  
        print("Error: poems.txt not found!")
        return None
    
    with open(POEM_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    if len(lines) < 4:
        return None
    
    poem = "".join(lines[:4]).strip()
    
    # Remove the first 4 lines and update file
    with open(POEM_FILE, "w", encoding="utf-8") as file:
        file.writelines(lines[4:])
    
    return poem

def send_email(poem):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "A Love Poem for You 💖"
    msg.attach(MIMEText(poem, "plain"))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def daily_task():
    poem = get_next_poem()
    if poem:
        send_email(poem)
        #print(poem)
    else:
        print("No more poems left to send.")


if __name__ == "__main__":
    while True:
        user_input = input("Do you want to send the next poem? (y/n): ").strip().lower()
        if user_input == "y":
            daily_task()
            break
        elif user_input == "n":
            print("Operation cancelled.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


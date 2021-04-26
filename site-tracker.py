import os
import smtplib
import requests
from pathlib import Path
from dotenv import load_dotenv
from linode_api4 import LinodeClient, Instance


def load_env_variables():
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)


def notify_admin():

    EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is up and running'
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, ADMIN_EMAIL, msg)



def reboot_server():
    try:
        LINODE_TOKEN = os.environ.get('LINODE_TOKEN')
        client = LinodeClient(LINODE_TOKEN)
        my_server = client.load(Instance, 376715)
        my_server.reboot()
    except Exception:
        print("invalid api token")
    

def test_the_site():
    
    SITE_ADDRESS = os.environ.get('SITE_ADDRESS')
    if SITE_ADDRESS:
        try:
            res = requests.get(SITE_ADDRESS, timeout=5)
            if res.status_code != 200:
                raise Exception()

        except Exception:
            notify_admin()
            reboot_server()
        


if __name__=='__main__':
    load_dotenv()
    test_the_site()




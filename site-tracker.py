import os
import smtplib
import requests
from linode_api4 import LinodeClient, Instance

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def notify_admin():
    with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, 'INSERT_RECEIVER_ADDRESS', msg)


def reboot_server():
    client = LinodeClient(LINODE_TOKEN)
    my_server = client.load(Instance, 376715)
    my_server.reboot()


try:
    r = requests.get('https://example.com', timeout=5)

    if r.status_code != 200:
        notify_admin()
        reboot_server()
except Exception as e:
    notify_admin()
    reboot_server()

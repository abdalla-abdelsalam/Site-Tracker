# Site-Tracker

## Description 

a simple python script to track your website status in case your site is down the script will reboot the server automatically 
and send an email to the system admin telling him that the site is down


## notes:
  1. linode api is used to connect to the server and reboot it, for more info about linode api visit [linode api](https://www.linode.com/docs/api/).
  1. you need to add your credentials: (EMAIL_ADDRESS,EMAIL_PASSWORD,ADMIN_EMAIL,LINODE_TOKEN,SITE_ADDRESS) to .env file, credentials will be stored as env variables 
  1. you can make the script up and running every 10 minutes by adding it to your task scheduler (if you are in linux you can use cron job)
  
  ## installation 

1. add your credentials to .env file
1. Install requisite python packages and modules then you can use the command
```bash
pip install -r requirements.txt
```
3. Run the script
```bash
python site-tracker.py
```

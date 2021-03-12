# Site-Tracker

## Description 

simple python script to track your website status in case your site is down the script will reboot the server automatically 
and send an email to the system admin telling him that the site is down


notes:
  1. linode api is used to connect to the server and reboot it
  1. you need to add your credentials (EMAIL_USER,EMAIL_PASS,LINODE_TOKEN) as environment variables
  1. you need to put system admin address in line 18 instead of INSERT_RECEIVER_ADDRESS statement
  1. you can make the script up and running every 10 minutes by adding it to your task scheduler (if you are in linux you can use cron)

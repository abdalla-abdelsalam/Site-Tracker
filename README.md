# Site-Tracker

## Description 

simple python script to track your website status in case your site is down the script will reboot the server automatically 
and send email to the system admin


notes:
  1. linode api is used to connect to the server and reboot it
  1. you need to add your credentials (EMAIL_USER,EMAIL_PASS,LINODE_TOKEN) as environment variables
  1. you need to put system admin address in line 18 instead of INSERT_RECEIVER_ADDRESS statement

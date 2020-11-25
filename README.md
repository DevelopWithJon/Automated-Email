## Automated-Email
#Description:

This tool will send automated emails directly to any address powered by SMTP. By feeding in your Gmail account the bot will verify permission, ask you for your input then send it out in a jiffy.

# Classes:
1. Gmail Preping
    - This class uses an internet browswer (Selenium) to give users the permission to use SMTP emailing modules. This rotates through a list of emails that need to be verified and proxies to hide activity.
 
2. Email Content Generation
    - This class will use a series of input statements to gather the data you want to populate your email.
    
3. Sending Email
    - This class uses compiles that outputs from the other classes and sends the email in the format you wish. You can choose to add Attachments and customize its appearance 

# Modules
Selenium 
Pandas
CSV
SMPT
email

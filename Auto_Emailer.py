import smtplib
from time import sleep
from email.message import EmailMessage
from time import sleep
from seleniumwire import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import csv
import pandas as pd
import re

with open('data.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    
    df = pd.DataFrame(data).drop([0])
    df.columns = ['Mail', 'Password', 'Recovery']
    
'''file = open('proxies.txt', 'r')
proxy = file.read()
print(proxy)
'''




PROXY = '209.54.100.48:3111:hunter:pass'
PROXY_HOST = '209.54.100.47'  # rotating proxy or host
PROXY_PORT = '3111' # port
PROXY_USER = 'hunter' # username
PROXY_PASS = 'pass' # password

options = {
        'proxy': {
        'http': 'http://hunter:pass@209.54.100.48:3111',
        'https': 'http://hunter:pass@209.54.100.48:3111',
        'no_proxy': 'localhost,127.0.0.1' # excludes
    }
}


class  Email_validator():
    def __init__(self, url):
        self.url = url
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.drive = webdriver.Chrome(ChromeDriverManager().install(), seleniumwire_options=options)


    def get_chrome(self, user_agent=None):

        if user_agent:
            self.drive.chrome_options.add_argument('--user-agent=%s' % user_agent)
        return self.drive
    
    def request_site(self, Mail, Password, Recovery):
        
        username = Mail
        password = Password

        self.driver = self.get_chrome()

        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_id('identifierId').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        sleep(3)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
        sleep(2)
        self.driver.get('+++')
        switch = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div/div/ul/li/div[1]/div/div[2]/div/div/div[2]/input')
        print(switch.get_attribute("aria-checked"))
        if switch.value == "false":
            switch.click()
        sleep(3)
        self.driver.close()

    def looper(self, data):
        for label, row in data.iterrows():

                Email = label, row["Mail"]
                Email = Email[1]

                Password = label, row["Password"]
                
                Password = Password[1]

                Recovery = label, row["Recovery"]
                
                Recovery = Recovery[1]
                
                self.request_site(Email, Password, Recovery)
                
                
            
        



#This Class will validate each gmail you want to use by changing you account settings
'''class Email_validator():
    
        def __init__(self, url):
            self.url = url
            
        def request_site(self):
            with Session() as s:
                r = s.get(self.url)
                bs_content = bs(r.content, "html.parser")
                token = bs_content.find("input id)
                print(token.content)'''
            
            
        
### This Class will 
class Email_Content():
    def __init__(self):
        pass
     
    def get_inputs():
        print('Enter Receiveing Email Address: ')
        OUTGOING_EMAIL = str(input())

        print('Enter Subject Line: ')
        SUBJECT = str(input())

        print('Enter Body: ')
        BODY = str(input())
        
        print('Are there files to attach?: ')
        Q_ATTACHMENT = str(input())
        
        if Q_ATTACHMENT in ['Yes', 'yes', 'YES']:
            print('What is the file path? : ')
            ATTACHMENT = str(input())

        
        return OUTGOING_EMAIL, SUBJECT, BODY, ATTACHMENT
    
class Email_sender():
    def __init__():
        pass
    
        
        def Email_format(Email, Passwords, OUTGOING_EMAIL, SUBJECT, BODY):
            emails_sent = 0
            HEADER = 'to: ' + str(OUTGOING_EMAIL) + '\n' + 'From: ' + "Joey" + '\n' + 'Subject: ' + str(SUBJECT)
        
        
        
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        
            MSG = EmailMessage()
            MSG['Subject'] = SUBJECT
            MSG['From'] = Email
            MSG['To'] = OUTGOING_EMAIL
            MSG.set_content("Hey This is a test")
        
        
            smtp.login(Email, Passwords)
        
            smtp.send_message(MSG)
        
        
            sleep(10)
            emails_sent += 1
        
            smtp.close()
            print(emails_sent)
        
        
        
            print(f'Sent {emails_sent} entries out')
            
def main():
    url = 'https://accounts.google.com/ServiceLogin/signinchooser?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    a = Email_validator(url)
    a.looper(df)
    
#if __name__ == '__main__':
#    main()

find = r'\d+.\d+.\d+.\d+'
host = re.findall(find, PROXY)
host = str(host[0])
print(host)

find = r':\d+'
port = re.findall(find, PROXY)
port = str(port[0])
port = port[1:]
print(port)

find = r':[a-zA-Z]+'
user = re.findall(find, PROXY)
user = str(user[0])
user = user[1:]
print(user)

find = r':[a-zA-Z0-9]+$'
passw = re.findall(find, PROXY)
passw = str(passw[0])
passw = passw[1:]
print(passw)
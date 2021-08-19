import os
import smtplib
import random
import schedule
import time

GOOD_MORNING_QUOTES = [ ]#Type within the brackets, a sentence in qoutation marks followed by a comma ex. "Good morning", "Rise and Shine"

DAY_QUOTES = [ ]# Type within the brackets, a sentence in quotation marks followed by a comma ex. "You can do it.", "I believe in you."

NIGHT_QUOTES = [ ]# Type within the brackets, a sentence in quotation marks followed by a comma ex. "Goodnight", "You did great today."

LINKS = [ ]# If you'd like to send a link to lets say a website that has random dog pictures or bunnies ex. 'random.dog', 'https://rabbit.org/fun/net-bunnies.html'

EMAIL_ADDRESS = '' #email account works best with gmail. You won't have to change anything.
EMAIL_PASSWORD = '' # email password.

def send_morning(mquotes_list = GOOD_MORNING_QUOTES):
    mquote = mquotes_list[random.randint(0, len(mquotes_list)-1)]
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = '' #this isnt necessary but you can include one if you'd like too. ex. 'I love you!'.
        body = mquote

        msg = f'Subject: {subject}\n\n{body}' 

        smtp.sendmail(EMAIL_ADDRESS, ' ', msg)#within the qoutes add the desired cellular number with the service providers email extention for example.
		#AT&T: phonenumber@mms.att.net
		#T-Mobile: phonenumber@tmomail.net 
		#Sprint: phonenumber@messaging.sprintpcs.com 
		#Verizon: phonenumber@vtext.com or phonenumber@vzwpix.com
		#Virgin Mobile: phonenumber@vmobl.com



def send_daily(dquotes_list = DAY_QUOTES):
    dquotes= dquotes_list[random.randint(0, len(dquotes_list)-1)]
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = '' #this isnt necessary but you can include one if you'd like too. ex. 'I love you!'.
        body = dquotes

        msg = f'Subject: {subject}\n\n{body}' 

        smtp.sendmail(EMAIL_ADDRESS, ' ', msg)#within the qoutes add the desired cellular number with the service providers email extention for example.
		#AT&T: phonenumber@mms.att.net
		#T-Mobile: phonenumber@tmomail.net 
		#Sprint: phonenumber@messaging.sprintpcs.com 
		#Verizon: phonenumber@vtext.com or phonenumber@vzwpix.com
		#Virgin Mobile: phonenumber@vmobl.com



def send_link(alink_list = ANIMAL_LINKS):
    alink= alink_list[random.randint(0, len(alink_list)-1)]
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = '' #this isnt necessary but you can include one if you'd like too. ex. 'I love you!'.
        body = alink

        msg = f'Subject: {subject}\n\n{body}' 

        smtp.sendmail(EMAIL_ADDRESS, ' ', msg)#within the qoutes add the desired cellular number with the service providers email extention for example.
		#AT&T: phonenumber@mms.att.net
		#T-Mobile: phonenumber@tmomail.net 
		#Sprint: phonenumber@messaging.sprintpcs.com 
		#Verizon: phonenumber@vtext.com or phonenumber@vzwpix.com
		#Virgin Mobile: phonenumber@vmobl.com


def send_night(nquotes_list = NIGHT_QUOTES):
    nquotes= nquotes_list[random.randint(0, len(nquotes_list)-1)]
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = '' #this isnt necessary but you can include one if you'd like too. ex. 'I love you!'.
        body = nquotes

        msg = f'Subject: {subject}\n\n{body}' 

        smtp.sendmail(EMAIL_ADDRESS, ' ', msg) #within the qoutes add the desired cellular number with the service providers email extention for example.
		#AT&T: phonenumber@mms.att.net
		#T-Mobile: phonenumber@tmomail.net 
		#Sprint: phonenumber@messaging.sprintpcs.com 
		#Verizon: phonenumber@vtext.com or phonenumber@vzwpix.com
		#Virgin Mobile: phonenumber@vmobl.com

 
#The Schedule library relys on the system clock so if its set to EST or CST or PST that will determine when the messages are sent.
#below is the scheduling for the text messages please enter and change how you see fit Schedule operates on a 24hr time clock so "13:00" is 1pm.
#I made a schedule below that sends one Good Morning text alternates between Daily texts and Links and ends with one Goodnight text.

schedule.every().day.at('07:30').do(send_morning, GOOD_MORNING_QUOTES)

schedule.every().day.at('08:00').do(send_daily, DAY_QUOTES)
schedule.every().day.at('10:00').do(send_daily, DAY_QUOTES)
schedule.every().day.at('12:00').do(send_daily, DAY_QUOTES)
schedule.every().day.at('14:00').do(send_daily, DAY_QUOTES)
schedule.every().day.at('16:00').do(send_daily, DAY_QUOTES)
schedule.every().day.at('18:00').do(send_daily, DAY_QUOTES)
schedule.every().day.at('20:00').do(send_daily, DAY_QUOTES)


schedule.every().day.at('09:00').do(send_link, LINKS)
schedule.every().day.at('11:00').do(send_link, LINKS)
schedule.every().day.at('13:00').do(send_link, LINKS)
schedule.every().day.at('15:00').do(send_link, LINKS)
schedule.every().day.at('17:00').do(send_link, LINKS)
schedule.every().day.at('19:00').do(send_link, LINKS)

schedule.every().day.at('22:00').do(send_night, NIGHT_QUOTES)

while True:
    schedule.run_pending()
    time.sleep(2)
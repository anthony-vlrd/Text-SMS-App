# sms_app.py written by Anthony Velarde, 2024
# import libraries 
import os
import re
import pandas as pd
from twilio.rest import Client

# connect to the Twilio API 
account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

#import the csv file
df = pd.read_csv ('contacts-test.csv')

#pull the phone numbers into a list
phone_numbers = list(df["phone"])
clean_numbers = []

#clean phone numbers data
#strip each number of any non numerical values
for i in range(len(phone_numbers)):    
    x = re.sub('\D', '', phone_numbers[i])
    phone_numbers[i] = x

    #only keep numbers that have 10 digits 
    #(11 if including country code
    if len(phone_numbers[i]) == 10:
        temp = "+1" + phone_numbers[i]
        clean_numbers.append(temp)
        
    elif len(phone_numbers[i]) == 11 and phone_numbers[i][0] == '1':
        temp = "+" + phone_numbers[i]
        clean_numbers.append(temp)

    else:
        continue 
        

#send out message to each phone number 
for number in clean_numbers:
    try:
        message = client.messages \
                        .create(
                             body="Message to send out. :)",
                             from_='+18326696444',
                             to=number
                         )
    except: 
        print("an error occurred")

    print(message.sid)

    
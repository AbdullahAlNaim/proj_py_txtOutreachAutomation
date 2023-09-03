#-*- coding:utf-8 -*-
import os

from twilio.rest import Client


account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)


nums = []


nums_v2 = []


for x in range(len(nums_v2)):
    client.messages.create(
        to=nums_v2[x],
        from_='',
        body=f""
    )
    print(nums_v2[x])


#!/usr/bin/env python
import pika
import sys
import tweepy
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='royalecola', durable=True)

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

tw = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tw.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(tw)


while True:
    

    dms = api.direct_messages()
    print(dms[0].text)
    for message in dms:
        channel.basic_publish(exchange='',
                    routing_key='royalecola',
                    body=message.text,
                    properties=None)
    time.sleep(5)


connection.close()

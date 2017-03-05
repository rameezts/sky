#!/usr/bin/env python
import pika

name = raw_input("What is your name? ")
#print "Hello, %s." % name

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body=name)
print(" [x] Sent 'Hello World!'")
connection.close()

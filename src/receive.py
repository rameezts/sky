#!/usr/bin/env python
import pika
import psycopg2
import sys

con = None
con = psycopg2.connect(database='mydb', user='rameez')
cur = con.cursor()
#cur.execute("INSERT INTO pop (flavor, amount, size) VALUES ('a', 10, 'normal')")
#con.commit()
#con.close()


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    cur.execute("INSERT INTO pop (flavor, amount, size) VALUES (%r, 10, 'normal')" % body)
    con.commit()
    #con.close()

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
con.close()

#!/usr/bin/env python
import pika
from flask import Flask, request

def rabb(val):
#name = raw_input("What is your name? ")
#print "Hello, %s." % name

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='hello')
	channel.basic_publish(exchange='', routing_key='hello', body=val)
	print(" [x] Sent 'Hello World!'")
	connection.close()


app = Flask(__name__)

@app.route('/param')
def param():

	arg1 = request.args['arg1']
        arg2 = request.args['arg2']
	sum = int(arg1) + int(arg2)
	print "Rabbit Strat"
	rabb(str(sum))
	print "Rabbit Exec"
	
	return str(sum)
        #return 'Arg1: ' + arg1 + 'Arg2: ' + arg2


if __name__ == '__main__':
        app.run(debug=True)

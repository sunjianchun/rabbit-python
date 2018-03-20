# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

message = raw_input(">_ ")
while message != "exit":
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print "Product: send {0}".format(message)
	message = raw_input(">_ ")
connection.close()

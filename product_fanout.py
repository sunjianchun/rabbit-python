# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika

exchange = 'logs'
exchange_type = 'fanout'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(
		exchange=exchange,
		exchange_type=exchange_type
	)

message = raw_input(">_ ")
while message != "exit":
	channel.basic_publish(
		exchange=exchange, 
		routing_key='', 
		body=message
	)
	print "Product: send {0}".format(message)
	message = raw_input(">_ ")
connection.close()

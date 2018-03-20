# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika

exchange = 'direct_test'
exchange_type = 'direct'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(
		exchange=exchange,
		exchange_type=exchange_type
	)

message = raw_input(">_ ")
while message != "exit":
	if ":" in message:
		severity = message.split(":")[0]
	else:
		severity = 'info'

	channel.basic_publish(
		exchange=exchange, 
		routing_key=severity, 
		body=message
	)
	print "Product: send {0}".format(message)
	message = raw_input(">_ ")
connection.close()

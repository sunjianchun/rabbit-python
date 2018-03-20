# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika

exchange = 'topic_test'
exchange_type = 'topic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(
		exchange=exchange,
		exchange_type=exchange_type
	)

message = raw_input(">_ ")
while message != "exit":
	if "." in message:
		severity = message.split(" ")[0]
		message = " ".join(message.split(" ")[1:])
	else:
		severity = 'anonymous.info'

	channel.basic_publish(
		exchange=exchange, 
		routing_key=severity, 
		body=message
	)
	print "Product: send {0}".format(message)
	message = raw_input(">_ ")
connection.close()

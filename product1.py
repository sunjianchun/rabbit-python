# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika

queue = 'task_queue'
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True)

message = raw_input(">_: ")
while message != "exit":
	channel.basic_publish(
		exchange='', 
		routing_key=queue, 
		body=message,
		properties=pika.BasicProperties(
			delivery_mode=2,
		)
	)
	print "Product: send {0}".format(message)
	message = raw_input(">_ ")
connection.close()

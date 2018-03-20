# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika
import time



def fib(n):
	if n == 2 or n == 1:
		return n
	else:
		return fib(n-1) + fib(n-2)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')


def callback(ch, method, properties, body):
	print "received %s" % body
	res = fib(int(body))
	print "done"
	channel.basic_publish(
		properties = pika.BasicProperties(
			correlation_id=properties.correlation_id
		),
		routing_key=properties.reply_to,
		exchange='', 
		body=str(res)
	)

	ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
	callback, 
	queue='rpc_queue',
	)
print "[*] Awating Prc requests."
channel.start_consuming()

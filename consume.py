# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika
import time

def callback(ch, method, properties, body):
	time.sleep(10)
	print "received %r" % body
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(callback, queue='hello', no_ack=True)
print " [*] Waiting for messages. To exit press CTRL+C"
channel.start_consuming()

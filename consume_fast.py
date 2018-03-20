# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika
import time

queue='task_queue'
def callback(ch, method, properties, body):
	print "received %s" % body
	time.sleep(2)
	print "done"
	ch.basic_ack(delivery_tag=method.delivery_tag)	

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue)
print "Waiting for messages. To exit press CTRL+C"
channel.start_consuming()

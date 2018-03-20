# encoding:utf-8
#!/opt/environment/python/rabbitmq/bin/python

import pika, uuid

class FibonacciRpcClient(object):
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		self.channel = self.connection.channel()
		self.result = self.channel.queue_declare(exclusive=True)
		self.reply_queue = self.result.method.queue
		self.channel.basic_consume(
			self.on_response, 
			queue=self.reply_queue,
			no_ack=True
		)

	def call1(self, n):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(
			routing_key='rpc_queue', 
			properties=pika.BasicProperties(
				reply_to=self.reply_queue,
				correlation_id=self.corr_id
			),
			body=str(n),
			exchange=''
		)
		while self.response is None:
			self.connection.process_data_events()

		return int(self.response)
			
	def on_response(self, ch, method, props, body):
		if props.correlation_id == self.corr_id:
			self.response = body
			
fib = FibonacciRpcClient()
response = fib.call1(30)
print "[.] Got result %d" % response

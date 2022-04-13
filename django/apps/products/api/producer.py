import pika, json

# amqps://icqbyxli:j2p91iWRBkp6HJ2T1rUwgkXooyKCnFbv@moose.rmq.cloudamqp.com/icqbyxli
params = pika.URLParameters('amqps://icqbyxli:j2p91iWRBkp6HJ2T1rUwgkXooyKCnFbv@moose.rmq.cloudamqp.com/icqbyxli')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print('init publish')
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)





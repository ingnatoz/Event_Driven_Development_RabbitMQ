import pika, json

from models.Product import Product, db

params = pika.URLParameters(
    'amqps://icqbyxli:j2p91iWRBkp6HJ2T1rUwgkXooyKCnFbv@moose.rmq.cloudamqp.com/')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(
            id=data['id'],
            title=data['title'],
            ml_product=data['ml_product']
        )
        product.save()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.get_by_id(data['id'])
        product.title = data['title']
        product.ml_product = data['ml_product']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.get_by_id(data['id'])
        product.delete()
        print('Product Deleted')


channel.basic_consume(
    queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()
channel.close()

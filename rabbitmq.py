# coding: utf8

import pika
import time
import exceptions
from json import dumps, loads
from pika.adapters import blocking_connection


class RabbitMQ(object):

    def connect(self):
        try:
            self.connection = blocking_connection.BlockingConnection()
            self.channel = self.connection.channel()
        except pika.exceptions.AMQPConnectionError:
            raise exceptions.AMQPConnectionError

    def basic_publish_json(self, exchange, routing_key, body, properties=None,
                           mandatory=False, immediate=False):
        self.channel.basic_publish(exchange, routing_key, dump(body), properties,
                                   mandatory, immediate)

    def basic_consume(self):
        pass

    def get_one(self):
        pass

    def get_over_time(self):
        pass

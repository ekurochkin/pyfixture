# coding: utf8
import py.test
from rabbitmq import RabbitMQ
from redis import Redis


__all__ = [
	"rabbbitMQ",
	"redis"
]


@py.test.fixture()
def rabbbitMQ(request):
    rmq = RabbitMQ()

    def fin():
        rmq.close()
    request.addfinalizer(fin)
    return rmq


@py.test.fixture
def redis(request):
    redis = Redis()
    return redis

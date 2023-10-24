#!/usr/bin/env python3

'''
Module that writes to Redis
'''
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps
import sys
import redis


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrap
        :param self:
        :param args:
        :param kwargs:
        :return:
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    Decorator function to record the inputs and outputs
    of methods
    '''
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function"""
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper

class Cache:
    '''
    class defining cache created using redis
    '''
    def __init__(self, ):
        '''
        Initializes the class Cache
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method that takes data as arguments

        Returns a string
        '''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[int, float, bytes, str]:
        '''
        Get method to convert data to desired format
        using the callable function fn
        '''
        if fn:
            return fn(self._redis.get(key))
        return (self._redis.get(key))

    def get_str(self: bytes) -> str:
        '''
        Method to get a string
        '''
        return self.decode('utf-8')

    def get_int(self: bytes) -> int:
        '''
        Method to get a number
        '''
        return int.from_bytes(self, sys.byteorder)


def replay(method: Callable):
    method_name = method.__name__
    key_inputs = f"{method_name}:inputs"
    key_outputs = f"{method_name}:outputs"

    inputs = cache._redis.lrange(key_inputs, 0, -1)
    outputs = cache._redis.lrange(key_outputs, 0, -1)

    if not inputs or not outputs:
        print(f"{method_name} was never called.")
        return

    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_key in zip(inputs, outputs):
        output_key = output_key.decode('utf-8')
        print(f"{method_name}(*{input_data.decode('utf-8')}) -> {output_key}")
        print(f"{method_name}(*{input_data.decode('utf-8')}) -> {output_key}")


# cache = Cache()
# cache.store("foo")
# cache.store("bar")
# cache.store(42)
# replay(cache.store)

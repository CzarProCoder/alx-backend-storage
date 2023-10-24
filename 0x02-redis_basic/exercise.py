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

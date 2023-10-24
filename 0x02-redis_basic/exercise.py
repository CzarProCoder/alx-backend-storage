#!/usr/bin/env python3

'''
Module that writes to Redis
'''
from uuid import uuid4
from typing import Union
import redis


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
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method that takes data as arguments
        
        Returns a string
        '''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

#!/usr/bin/env python3

'''
Module containing functin that returns documents that contains a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Function that returns a list of schools that contains a particular topic
    '''
    return list(mongo_collection.find({"topic": topic}))

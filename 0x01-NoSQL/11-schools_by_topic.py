#!/usr/bin/env python3

'''
Module containing functin that returns documents that contains a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Function that returns a list of schools that contains a particular topic

    Args:
        mongo_collection: Collection containing the documents to check
        topic: Topic to be evaluated
    '''
    return mongo_collection.find({"topics": topic})

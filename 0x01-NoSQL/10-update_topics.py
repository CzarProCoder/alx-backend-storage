#!/usr/bin/env python3

'''
Module containing function that change topics of a school document
'''


def update_topics(mongo_collection, name, topics):
    '''
    Function that updates the name of a document

    Args:
        Mongo_collection: Collection containing the documents
        name: Name to be checked
        topics: Topics to be updated
    '''
    mongo_collection.update_many({"name": name}, { "$set": {"topics": topics}})

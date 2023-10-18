#!/usr/bin/env python3

'''
Module containing a function that inserts a new document
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Function that inserts a new document based on the kwargs

    Args:
        mongo_collection: Collection to be used
        kwargs: Key, values pairs to be added to the document
    '''
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id

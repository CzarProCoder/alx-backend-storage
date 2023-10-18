#!/usr/bin/env python3

'''
Module containing python function to list all documents within a collection
'''


def list_all(mongo_collection):
   '''
   function that returns a list of all documents
   contained in a collection
   '''
   documents = mongo_collection.find()
   return list(documents)

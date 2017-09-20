#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))
        
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''

        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        
    
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)

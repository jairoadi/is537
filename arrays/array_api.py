#!/usr/bin/env python3


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''
    
    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an initial size.'''
        self.data = []
        self.size = 0
        self.increaseNeeded = None
        for i in range(10):
            self.data.append(None)
        
        
    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('DEBUG')
        print(self.size , 'of' , len(self.data) , '>>>' , self.data)
        
        
    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        
        
    def _check_increase(self):
        '''Checks whether the array is full and needs to increase by chunk size in preparation for adding an item to
        the array.'''

        if self.size == len(self.data):
            'increment by 5'
            for i in range(5):
                self.data.append(None)

        
    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''

        self.tempData = []  # creates a tempData arrayObject

        while self.countNone >= 5:

            for i in range(len(self.data)-5):
                self.tempData.append(self.data[i]) #assigning the data values to the tempData array

            self.data = self.tempData #creating a new data array with smaller length
            self.countNone -= 5

        del self.tempData #deleting tempData to not have unnecessary memory allocation being used

        
    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self.increaseNeeded = True
        self.check_size()
        self.data[self.size] = item
        self.size += 1

        print('ADD', item)


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        print('INSERT', index,',',item)
        self.increaseNeeded = True
        self.check_size()

        iCount = 0
        self.tempData = []

        if index > self.size:
            print('Error:', index, 'is not within the bounds of the current array.')
            return

        if self.size < len(self.data):
            while iCount < int(index):
                self.tempData.append(self.data[iCount])
                iCount += 1

            self.tempData.append(item)

            while iCount < len(self.data)- 1:

                self.tempData.append(self.data[iCount])

                iCount += 1

            self.data = self.tempData
            del self.tempData

            self.check_size()

    
    def set(self, index, item):
        '''Sets the given item at the given index. Throws an exception if the index is not within the bounds of the array.'''
        print('SET', index, ',', item)

        inRange = False

        for i in range(self.size):
            if i == index:
                self.data[i] = item
                inRange = True

        if not inRange:
            print('Error:', index, 'is not within the bounds of the current array.')


        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        inRange = False
        getValue = None
        print('GET', index)

        for i in range(self.size):
            if i == index:
                getValue = self.data[i]
                inRange = True
                break

        if not inRange:
            print('Error:', index, 'is not within the bounds of the current array.')
        else:
            print(getValue)

    
    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        print('DELETE',index)
        self.increaseNeeded = False
        for i, value in enumerate(self.data):
            if i == index:
                self.data[i] = None
                self.size = 0

        for i, value in enumerate(self.data):
            if value == None:
                if i+1 < len(self.data) and self.data[i+1] != None : #& self.data[i+1] != None
                    temp = self.data[i+1]
                    self.data[i+1] = value
                    self.data[i] = temp

        self.check_size()
        self._check_decrease()






        # iCount = 0
        # self.tempData = []
        #
        # if index > self.size:
        #     print('Error:', index, 'is not within the bounds of the current array.')
        #     return
        #
        # for i in range(len(self.data)):
        #     if i == index:
        #         self.data[i] = None
        #         break
        #     iCount += 1
        #
        # for i,value in enumerate(self.data):
        #     if value != None:
        #         self.tempData.append(self.data[i])
        #
        # while len(self.tempData) < len(self.data):
        #     self.tempData.append(None)
        #
        #
        # self.data = self.tempData
        # del self.tempData
        # self.countNone = 0
        #
        # for i, value in enumerate(self.data):
        #     if value == None:
        #         self.countNone += 1
        #
        # self._check_decrease()

        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''

    def check_size(self):
        '''checks is there are spaces in the array'''
        # check size
        self.countNone = 0
        self.size = 0
        for i, value in enumerate(self.data):
            if self.data[i] != None:
                self.size += 1
            else:
                self.countNone += 1


        if self.size == len(self.data) and self.increaseNeeded == True:
             self._check_increase()


        
        
###################################################
###   Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''

def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    # self.tempData = []
    # for i in range(len(self.data)):
    #     self.tempData.append(self.data[i])
        

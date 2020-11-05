#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:15:01 2020

@author: zhuyifan
"""


class NHeap:
    def __init__(self, n):
        self.heapList = [0]
        self.currentSize = 0
        self.heapsize = n  # new variable saving the n for how many branch per node

    # swap upwards 
    def percUp(self,i):
        # while the parent node is not zero
        while (i -2)// self.heapsize+1 > 0: 
            # if the parent node is bigger than the child node,swap
            if self.heapList[i] < self.heapList[(i -2)// self.heapsize+1 ]:
               tmp = self.heapList[(i -2)// self.heapsize+1]
               self.heapList[(i -2)// self.heapsize+1] = self.heapList[i]
               self.heapList[i] = tmp
            i = (i -2)// self.heapsize+1

    def insert(self,k):
        # insert an element
        self.heapList.append(k)
        # add one more node 
        self.currentSize = self.currentSize + 1
        # perception up to swap with the parent node
        self.percUp(self.currentSize)
    # swap downwards 
    def percDown(self,i):   #O(k*logk(n))
        # if the children node is smaller than the current size 
        while (self.heapsize * i -2+1) <= self.currentSize:
            # get the mini children of the parent 
            mc = self.minChild(i)
            # exchange the parent node and the children node
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):  #O(k) 
        # get the child node of the specific parent node 
        child= self.heapsize * i -2+1
        # set the current child as the miniml value 
        minchild = child
        # to loop around all the children 
        for j in range(1,self.heapsize):
            # adding more index 
            compare=child+j
            # if the temp is smaller than the min, exchange 
            if compare<=self.currentSize and self.heapList[compare]<self.heapList[minchild]:
                minchild=compare
                
        return minchild

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):  #O(k)
        # node index of the last  parent node with children node
        i = (len(alist) +self.heapsize-2)//self.heapsize
        self.currentSize = len(alist)
        
        self.heapList = [0] + alist[:]
        # while i>0, go down to rebalance 
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def _toString(self, i):
        if i > self.currentSize:
            return '[None]'
        else:
            total = '[' + str(self.heapList[i])
            for j in range(1, self.heapsize+1):
                total += self._toString(self.heapsize*(i-1)+j+1)
            total += ']'
        return total
    
    def __str__(self):
        return self._toString(1)

#Testing 
nh = NHeap(3)
nh.buildHeap([9,5,6,2,3,7,10,23,4,11,8])

print(nh)

print(nh.delMin())
print(nh)
nh.insert(17)
print(nh)
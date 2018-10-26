# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:51:30 2018

@author: Jing
"""

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.Flink = 0
        self.Blink = 0
        
class DoubleLinkedList(object):
    
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 0
        
    def Search(self, key):   # use price as key
        current = self.head
        while current != 0 and current.data.Price != key:
            current = current.Flink
        return current
    
    def Delete(self, key):
        temp = self.Search(key)
        if temp == 0:
            print("No such an item to delete!")
            return 0
        if temp != self.head and temp != self.tail:
            temp.Blink.Flink = temp.Flink
            temp.Flink.Blink = temp.Blink
        elif temp == self.head and temp == self.tail:
            self.head = 0
            self.tail = 0
        elif temp == self.head and temp != self.tail:
            self.head = temp.Flink
            self.head.Blink = 0
        else:
            temp.Blink.Flink = 0
            self.tail = temp.Blink
        self.size = self.size - 1
        return 1
        
    def AppendToHead(self, newCar):
        temp = Node(newCar)
        if self.head == 0:
            self.head = temp
            self.tail = temp
        else:
            self.head.Blink = temp
            temp.Flink = self.head
            self.head = temp
        self.size = self.size + 1
        
    def AppendToTail(self, newCar):
        temp = Node(newCar)
        if self.head == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.Flink = temp
            temp.Blink = self.tail
            self.tail = temp
        self.size = self.size + 1
        
    def RemoveFromHead(self):
        temp = self.head
        if self.head != 0:
            if self.head == self.tail:
                self.head = 0
                self.tail = 0
            else:
                self.head = self.head.Flink
                self.head.Blink = 0
        else:
            print("Empty list!")
        self.size = self.size - 1
        return temp
    
    def RemoveFromTail(self):
        temp = self.tail
        if self.tail != 0:
            if self.head == self.tail:
                self.head = 0
                self.tail = 0
            else:
                self.tail = self.tail.Blink
                self.tail.Flink = 0
        else:
            print("Empty list!")
        self.size = self.size - 1
        return temp
    
    def PrintCars(self):
        temp = self.head
        if temp == 0:
            print("Empty list!")
            return 0
        while temp != 0:
            print("%s %s %d %.0f %.0f" %(temp.data.Make, temp.data.Model, temp.data.Year, temp.data.Mileage, temp.data.Price))
            temp = temp.Flink
        return 1
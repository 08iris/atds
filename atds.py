#!/usr/bin/env python3

"""
atds.py 
A collection of data types for the Advanced Topics class. 
"""


__author__ = "Iris Grether"
__version__ = "2026-02-12"

class Stack(): 
    def __init__(self): 
        """Create an empty stack (as a list)"""
        self.stack = []
    def push(self, item): 
        self.stack.append(item)
    def peek(self): 
        """ Returns the result if one available, otherwise None """ 
        if len(self.stack) > 0: 
            return self.stack[-1]
    def pop(self): 
        if len(self.stack) > 0: 
            return self.stack.pop() 
    def size(self): 
        return len(self.stack) 
    def is_empty(self): 
        return self.size() == 0
    def __repr__(self): 
        return str(self.stack) 
    
class Queue(object): 
    def __init__(self): 
        self.queue = []
    def enqueue(self, item): 
        self.queue.append(item) 
    def dequeue(self): 
        if len(self.queue) > 0: 
            return self.queue.pop(0) 
    def peak(self): 
        if len(self.queue) > 0: 
            return self.queue[0] 
    def is_empty(self):
        return self.size() == 0
    def size(self): 
        return len(self.queue) 
    def __repr__(self):
        return str(self.queue) 

class Deque(object):
    def __init__(self):
        """Creates an empty deque"""
        self.deque = []
    def add_front(self, item):
        self.deque.insert(0, item)
    def add_rear(self, item):
        self.deque.append(item)
    def remove_front(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)
    def remove_rear(self):
        if len(self.deque) > 0:
            return self.deque.pop()
    def peek_front(self):
        if len(self.deque) > 0:
            return self.deque[0]
    def peek_rear(self):
        if len(self.deque) > 0:
            return self.deque[-1]
    def size(self):
        return len(self.deque)
    def is_empty(self):
        return self.size() == 0
    def __str__(self):
        return str(self.deque)

class Node(object): 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
    def get_data(self): 
        return self.data 
    def get_next(self): 
        return self.next 
    def set_data(self, new): 
        self.data = new 
    def set_next(self, new): 
        self.next = new 
    def __repr__(self): 
        return "Node[data = " + str(self.data) + ", next = " + str(self.next) + "]"
    
class UnorderedList(object): 
    def __init__(self): 
        self.head = None 
    def add(self, item): 
        new_node = Node(item) 
        new_node.set_next(self.head) 
        self.head = new_node 
    def length(self):
        node_count = 0
        current = self.head 
        while current != None: 
            node_count += 1 
            current = current.get_next() 
        return node_count
    def is_empty(self): 
        return self.head == None 
    def remove(self, item): 
        prev = None 
        current = self.head 
        while current != None:
            if current.get_data() == item: 
                if prev == None: 
                    self.head = current.get_next()
                else: 
                    prev.set_next(current.get_next()) 
                return 
            else:
                prev = current 
                current = current.get_next() 
        return #default 
    def search(self, item): 
        current = self.head
        while current != None: 
            if current.get_data() == item: 
                return True 
            current = current.get_next()
        return False 
    def append(self, item): 
        new_node = Node(item) 
        if self.head == None: 
            self.head = new_node 
            return 
        current = self.head 
        while current.get_next() != None:
             current = current.get_next() 
        current.set_next(new_node) 
    def index(self, item): 
        current = self.head 
        pos = 0 
        while current != None: 
            if current.get_data() == item: 
                return pos 
            current = current.get_next()
            pos += 1 
    def insert(self, pos, item): 
        new_node = Node(item) 
        if pos == 0: 
            new_node.set_next(self.head)
            self.head = new_node 
            return 
        
        current = self.head
        prev = None 
        index = 0 

        while index < pos: 
            prev = current 
            current = current.get_next() 
            index += 1 
        
        new_node.set_next(current) 
        prev.set_next(new_node) 
    
    def pop(self, pos=None):
        if pos == None:
            current = self.head
            prev = None
            while current.get_next() != None: 
                prev = current
                current = current.get_next() 
            if prev == None: 
                self.head = None 
            else: 
                prev.set_next(None) 
            return current.get_data() 
    
        current = self.head 
        prev = None 
        index = 0 

        while index < pos: 
            prev = current 
            current = current.get_next() 
            index += 1 
        if prev == None: 
            self.head = current.get_next() 
        else: 
            prev.set_next(current.get_next()) 

        return current.get_data() 

    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging. """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        if result[-1] == ",":
            result = result[:-1] # (remove trailing comma)
        result = result + "]"
        return result 

class UnorderedListStack(object): 
    def __init__(self): 
        self.ul = UnorderedList()
    def push(self, item): 
        self.ul.add(item) 
    def pop(self): 
        return self.ul.pop(0) 
    def peek(self): 
        if self.ul.is_empty():
            return None
        return self.ul.head.get_data()
    def is_empty(self): 
        return self.ul.is_empty() 
    def length(self): 
        return self.ul.length() 

class BinarySearcher(object): 
    def search(self, arr: list, value: int): 
        if len(arr) == 0: 
            return None 
        lower = 0
        higher = len(arr) - 1
        while lower <= higher:
            middle = (lower + higher) // 2 
            if arr[middle] == value: 
                return middle 
            elif value < arr[middle]: 
                higher = middle - 1 
            else: 
                lower = middle + 1 
        return None

class BinarySearcherRecursive(object):
    def search(self, arr, value, lower, upper):
        if lower > upper:
            return None
        mid = (lower + upper) // 2
        if arr[mid] == value:
            return mid
        if value < arr[mid]:
            return self.search(arr, value, lower, mid - 1)
        return self.search(arr, value, mid + 1, upper)
    
class LinearSearcher(object):
    def search(self, arr, value):
        i = 0
        while i < len(arr):
            if arr[i] == value:
                return i
            i += 1
        return None

class HashTable(object): 
    def __init__(self, m): 
        self.m = m 
        self.keys = m * [None]
        self.values = m * [None]
    def __repr__(self):
        return "Keys: " + str(self.keys) + " Values: " + str(self.values)
    def hash_function(self, key, m): 
        return key % m 
    def put(self, key, value): 
        hash = self.hash_function(key, self.m) 
        while self.keys[hash] != None and self.keys[hash] != key: 
            hash = (hash + 1) % self.m  
        self.keys[hash] = key 
        self.values[hash] = value
    def get(self, key):
        hash = self.hash_function(key, self.m)
        start = hash 
        while self.keys[hash] != None:
            if self.keys[hash] == key:
                return self.values[hash]
            hash = (hash + 1) % self.m
            if hash == start:
                return None
        return None
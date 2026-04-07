#!/usr/bin/env python3
# pytest -x testing/book_test.py

# or:

# pytest -x testing/book_test.py
class Coffee:
    def __init__(self, size, price):
        # This must match the property name below to trigger the setter
        self.size = size
        self.price = price
    
    def get_size(self):
        return self._size
    
    def set_size(self, value):
        # Wrap the 'or' statements in parentheses or use 'in' for cleaner logic
        if type(value) is str and (value == "Small" or value == "Medium" or value == "Large"):
            self._size = value  
        else: 
            print("size must be Small, Medium, or Large.")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1

    # FIX: This must be named 'size'
    size = property(get_size, set_size)
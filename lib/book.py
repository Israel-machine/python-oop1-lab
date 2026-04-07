#!/usr/bin/env python3
# pytest -x testing/book_test.py

# or:

# pytest -x testing/book_test.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_page_count(self): #getter - view only
        return self._page_count
    
    def set_page_count(self, value):#setter
        if type(value) is int and 0 <= value: #controll valid values
            self._page_count = value  

        else: 
            print("page_count must be an integer.")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)
    
    pass
    
        
# self made iterator

class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.max_num:
            value = self.index
            self.index += 1
            return value
        else:
            self.index = 0
            raise StopIteration
        
my_iterator = MyIterator(5)
for item in my_iterator:
    print(item)
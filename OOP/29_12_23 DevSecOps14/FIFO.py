class FifoList:
    data = []
    
    def __init__(self):
        self.data = []
        
    def __add__(self, item):
        self.data.append(item)
        
    def remove(self):
        return  self.data.pop(0)

    def add(self, param):
        pass


l1 = list()
f1 = FifoList()

f1.add(77)
f1.add(12)
f1.add('johnny')
f1.add('james')

print(f1.remove())
print(f1.remove())
print(f1.remove())
class FifoList:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self):
        if self.data:
            return self.data.pop(0)
        else:
            return None  # or raise an exception if you want to handle an empty list differently


f1 = FifoList()

f1.add(77)
f1.add(12)
f1.add('johnny')
f1.add('james')

print(f1.remove())
print(f1.remove())
print(f1.remove())


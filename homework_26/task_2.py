class Queue():
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        return self.elements.pop(0)
    
q = Queue() 
q.insert(1) 
q.insert(2) 
q.insert(3) 
print(q.pop()) # must return 1
print(q.pop()) # must return 2

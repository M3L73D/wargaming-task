class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    
    def write(self, data):
        if len(self.data) < self.capacity:
            self.data.append(data)
        else:
            raise Exception("Trying to write in full ring buffer")
        
    def read(self):
        try:
            return self.data.pop(0)
        except IndexError:
            raise Exception("Trying to read from empty ring buffer")
    
    
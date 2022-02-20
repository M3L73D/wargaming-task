class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None for i in range(capacity)] # junk values
        self.write_to = 0
        self.read_from = 0
    
    def _inc(self, inx):
        return (inx + 1) % self.capacity
    
    def write(self, data):
        if self.write_to == self.read_from and self.data[self.write_to] is not None: # value is overwritten
            self.read_from = self._inc(self.read_from)
        self.data[self.write_to] = data
        self.write_to = self._inc(self.write_to)
        #print(f"DEBUG: write_to {self.write_to}")
        
    def read(self):
        data = self.data[self.read_from]
        if data is None:
            raise Exception("Trying to read from an empty ring buffer")
        self.data[self.read_from] = None
        self.read_from = self._inc(self.read_from)
        #print(f"DEBUG: read_from {self.read_from}")
        return data
    
    def print(self):
        return print(self.data)

    
if __name__ == "__main__":
    buf = RingBuffer(7)
    for i in range(10):
        buf.write(i)
    print(buf.read())
    print(buf.read())
    print(buf.read())
    print(buf.read())
    print(buf.read())
    buf.write(120)
    print(buf.read())
    buf.write(121)
    print(buf.read())
    print(buf.read())
    print(buf.read())
    buf.write(122)
    print(buf.read())
    buf.print()
    
    
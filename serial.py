"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
        
    def __repr__(self):
        return f'<SerialGenerator start={self.org_start} next={self.start}>'

    def __init__(self, start):
        self.start = start
        self.org_start = start

    def generate(self):
        print(self.start)
        self.start = int(self.start) + 1
    
    def reset(self):
        self.start = self.org_start

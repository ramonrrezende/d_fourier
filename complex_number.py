class complex_number:
    def __init__(self, a, b):
        self.re = a
        self.im = b

    def add(self, c):
        r = self.re + c.re
        i = self.im + c.im
        ret = complex_number(r, i)
        return ret

    def mult(self, c):
        r = self.re * c.re - self.im * c.im
        i = self.re * c.im + self.im * c.re
        ret = complex_number(r, i)
        return ret
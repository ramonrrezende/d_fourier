import math
from complex_number import *

class fourier2d:

    def __init__(self, signal):
        self.signal = signal
    
    def get_transform(self):
        dft = []
        big_n = len(self.signal)
        for k in range(big_n):
            c = complex_number(0, 0)
            for n in range(big_n):
                alpha = (2 * math.pi * k * n) / big_n
                f = complex_number(math.cos(alpha), -math.sin(alpha))
               
                c = c.add(self.signal[n].mult(f))
            
            c.re = c.re / big_n
            c.im = c.im / big_n
            amp = math.sqrt(c.re**2 + c.im**2)
            freq = k
            phase = math.atan2(c.re, c.im)

            term = {'re':c.re, 'im':c.im, 'amp':amp, 'freq':freq, 'phase':phase}
            dft.append(term)
        return dft
import math

class fourier:

    def __init__(self, signal):
        self.signal = signal
    
    def get_transform(self):
        dft = []
        big_n = len(self.signal)
        for k in range(big_n):
            re = 0
            im = 0
            for n in range(big_n):
                alpha = (2 * math.pi * k * n) / big_n
                re += self.signal[n] * math.cos(alpha)
                im -= self.signal[n] * math.sin(alpha)
            re = re / big_n
            im = im / big_n

            amp = math.sqrt(re**2 + im**2)
            freq = k
            phase = math.atan2(re, im)

            term = {'re':re, 'im':im, 'amp':amp, 'freq':freq, 'phase':phase}
            dft.append(term)
        return dft
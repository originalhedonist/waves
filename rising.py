import math
import wavelib


class risinggenerator(wavelib.wavegenerator):
    def __init__(self, length, channels):
        super().__init__(length, channels)
        self.f = 261.6
        self.x = 0.0
        self.dx = 2 * math.pi * self.f / self.N

    def wavefunctionleft(self, n, t):
        y = math.sin(self.x)
        self.x = self.x + self.dx
        self.f = 261.6*(1 + n/self.N)
        self.dx = 2 * math.pi * self.f / self.N
        return y


risinggenerator(2, 2).write('middlecrising.wav')

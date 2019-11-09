import math
import wavelib

f = 261.6


class middlecgenerator(wavelib.wavegenerator):
    def wavefunctionleft(self, n, t):
        return math.sin(2 * math.pi * f * t)


middlecgenerator(2, 2).write('middlec.wav')

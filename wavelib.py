import logging
import struct
import sys
import wave


def setuplogging():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(message)s')


# noinspection PyMethodMayBeStatic
class wavegenerator:
    def __init__(self, length, channels):
        if channels < 1 or channels > 2:
            raise Exception("channels must be either 1 or 2")

        self.length = length
        self.channels = channels
        self.sample = 44100
        self.N = self.sample * self.length

    def write(self, filename):
        setuplogging()

        wf = wave.open(filename, 'wb')
        wf.setsampwidth(2)
        wf.setframerate(self.sample)
        wf.setnframes(self.N)
        logging.info('setting channels to %d', self.channels)
        wf.setnchannels(self.channels)
        try:
            for n in range(0, self.N):
                t = self.length * n / self.N
                self.writefloat(wf, self.wavefunctionleft(n, t), n, t)
                if self.channels == 2:
                    self.writefloat(wf, self.wavefunctionright(n, t), n, t)

            logging.info('Created %s', filename)
        finally:
            wf.close()

    def writefloat(self, wf, a, n, t):
        if a > 1 or a < -1:
            raise Exception('wavefunction returned {} for n = {}, t = {}'.format(a, n, t))

        A = int(((a + 1) * 32767) - 32768)
        thebytes = struct.pack("<h", A)
        wf.writeframes(thebytes)

    def wavefunctionleft(self, n, t):
        return 0

    def wavefunctionright(self, n, t):
        return self.wavefunctionleft(n, t)

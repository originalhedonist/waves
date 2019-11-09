import wave, logging, sys, struct, math

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(message)s')

def createmono(filename, length, wavefunction):
    sample = 44100
    N = sample * length
    wf = wave.open(filename, 'wb')
    wf.setsampwidth(2)
    wf.setframerate(sample)
    wf.setnframes(N)
    wf.setnchannels(1)
    try:    
        for n in range(0,N):
            t = length * n / N
            a = wavefunction(n, t, N)
            if a > 1 or a < -1:
                raise Exception('wavefunction returned {} for n = {}, t = {}'.format(a, n, t))
           
            A = int(((a+1)*32767)-32768)
            thebytes = struct.pack("<h", A)
            wf.writeframes(thebytes)
    finally:
        wf.close()

def createstereo(filename, length, wavefunctionL, wavefunctionR):
    sample = 44100
    N = sample * length
    wf = wave.open(filename, 'wb')
    wf.setsampwidth(2)
    wf.setframerate(sample)
    wf.setnframes(N)
    wf.setnchannels(2)
    try:    
        for n in range(0,N):
            t = length * n / N
            aL = wavefunctionL(n, t, N, 0)
            aR = wavefunctionR(n, t, N, 1)
           
            if aL > 1 or aL < -1:
                raise Exception('wavefunctionL returned {} for n = {}, t = {}'.format(a, n, t))
            if aR > 1 or aR < -1:
                raise Exception('wavefunctionR returned {} for n = {}, t = {}'.format(a, n, t))

            AL = int(((aL+1)*32767)-32768)
            AR = int(((aR+1)*32767)-32768)
            thebytes = bytearray(struct.pack("<h", AL))
            wf.writeframes(thebytes)
            thebytes = bytearray(struct.pack("<h", AR))
            wf.writeframes(thebytes)
    finally:
        wf.close()

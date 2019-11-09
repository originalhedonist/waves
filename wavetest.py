import wave, logging, sys, struct, math

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(message)s')


wf = wave.open('stereo1.wav', 'rb')
logging.info('Channels: %d' , wf.getnchannels())
logging.info('Sample width: %f' , wf.getsampwidth())
logging.info('frame rate: %f', wf.getframerate())
logging.info('n frames: %d', wf.getnframes())
retL = []
retR = []
for n in range(0,5):
    thebytes = wf.readframes(1)
    decodedL = struct.unpack("<h", thebytes[0:2])
    decodedR = struct.unpack("<h", thebytes[2:4])
    #print(decoded)
    retL.append(decodedL)
    retR.append(decodedR)
print(retL)
print(retR)

wf.close()


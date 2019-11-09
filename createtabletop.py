import wavelib, math

f = 261.6
def wavefunctionL(n, t, N, c):
    return math.sin(2*math.pi*f*t)
    
def wavefunctionR(n, t, N, c):
    return math.cos(2*math.pi*f*t)

#wavelib.createmono('monotone_middlec_2s.wav', 2, wavefunction)
wavelib.createstereo('monotone_middlec_2s.wav', 2, wavefunctionL, wavefunctionR)

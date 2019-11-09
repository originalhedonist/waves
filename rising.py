import math
import wavelib

f = 261.6


def wavefunction(n, t, N):
    return math.sin(2 * math.pi * f * t)


def wavefunctionleft(n, t, N, c):
    return math.sin(2 * math.pi * f * t)


def wavefunctionright(n, t, N, c):
    return math.cos(2 * math.pi * f * t)


wavelib.createmono('monotone_middlec_2s.wav', 2, wavefunction)
# wavelib.createstereo('middlec_rising.wav', 1, wavefunctionleft, wavefunctionright)

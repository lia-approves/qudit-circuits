## Implementation of the R = diag(1,1,-1) gate unitarily in qutrit Clifford+T
# accompanying the paper "Qutrit metaplectic gates are a subset of Clifford+T"
# Andrew Glaudell, Neil J. Ross, John van de Wetering, Lia Yeh

# Python code created and maintained by Alex Lim (https://github.com/AlexLim-Pro)

import numpy as np

from src.MiscFunctions import MiscFunctions as MiscFuncs
from src.QuantumCircuitMatrix import QuantumCircuitMatrix as QCM

## identity and zero matrices
I = np.identity(3)       # single-qutrit identity gate, i.e. 3 x 3 identity matrix
II = np.identity(3**2)   # two-qutrit identity gate
zero = np.zeros([3, 3])  # 3 x 3 zero matrix

# Z and X basis states
k0 = QCM.get_ket("0")    # Z-basis states
k1 = QCM.get_ket("1")    # "
k2 = QCM.get_ket("2")    # "
w = np.exp(2 * np.pi * 1j / 3)   # 3rd root of unity
kpl = 1j * (k0 + k1 + k2) / np.sqrt(3)              # X-basis states // Eqs.3-5
kw = 1j * (k0 + w * k1 + w**2 * k2) / np.sqrt(3)    # "
kwsq = 1j * (k0 + w**2 * k1 + w * k2) / np.sqrt(3)  # "

## qutrit generalization of Pauli gates
x = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]])       # X, i.e. tau(0 1 2) // Def.1
z = np.array([[1, 0, 0],
              [0, w, 0],
              [0, 0, w**2]])    # Z = H * X * H' // Def.1

## qutrit S, H, and CX, which generate the Clifford group
s = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, w]])  # S // Def.7
b0 = MiscFuncs.T(k0)
b1 = MiscFuncs.T(k1)
b2 = MiscFuncs.T(k2)
h = (np.kron(kpl, b0) + np.kron(kw, b1) + np.kron(kwsq, b2))  # H // Def.8
cx = np.vstack([np.hstack([I, zero, zero]),
               np.hstack([zero, x, zero]),
               np.hstack([zero, zero, MiscFuncs.T(x)])])  # CX, i.e. tau(10 11 12)(20 22 21) // Def.10

## various other Clifford gates
tau0_1 = np.array([[0, 1, 0],
                   [1, 0, 0],
                   [0, 0, 1]])  # tau(0 1) // Sec.2.1
tau0_2 = np.array([[0, 0, 1],
                   [0, 1, 0],
                   [1, 0, 0]])  # tau(0 2) // Sec.2.1
tau1_2 = np.array([[1, 0, 0],
                   [0, 0, 1],
                   [0, 1, 0]])  # tau(1 2) = H * H up to a global phase of -1 // Sec.2.1; Def.8
zww = np.dot(np.dot(np.dot(tau1_2, s), tau1_2), s)  # = [1 0 0; 0 w 0; 0 0 w] // Def.6
swap = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]])   # two-qutrit SWAP gate

## the T gate
t = np.array([[1, 0, 0],
              [0, w**(1/3), 0],
              [0, 0, w**(-1/3)]])  # T // Def.13

##  Controlled gates from the paper "Factoring with Qutrits: Shor’s
#   Algorithm on Ternary and Metaplectic Quantum Architectures"
p9 = np.dot(np.dot(x, t), MiscFuncs.T(x))  # the P9 gate, which is Clifford equivalent to T
qubitCqutritZe = np.dot(np.dot(np.dot(np.dot(np.dot(cx, np.kron(I, p9)), cx), np.kron(I, p9)), cx), np.kron(I, p9))
tcx = np.dot(np.dot(np.kron(MiscFuncs.T(x), np.dot(MiscFuncs.T(h), MiscFuncs.T(x))), qubitCqutritZe), np.kron(x, np.dot(x, h)))  # tau(20 21 22) // Lem.17
ocx = np.dot(np.dot(np.kron(MiscFuncs.T(x), I), tcx), np.kron(x, I))  # tau(10 11 12)
socxs = np.dot(np.dot(swap, ocx), swap)  # tau(01 11 21)
tau02_20 = np.dot(np.dot(np.dot(np.dot(np.dot(swap, socxs), ocx), socxs), ocx), socxs)  # tau(02 20)
map21_22to02_20 = np.dot(np.dot(np.dot(swap, MiscFuncs.T(cx)), swap), np.kron(I, tau0_1))
tctau1_2 = np.dot(np.dot(MiscFuncs.T(map21_22to02_20), tau02_20), map21_22to02_20)  # |2⟩-controlled tau(1 2), i.e. tau(21 22) // Lem.18

## |2⟩-controlled w^(1/3) * s' gate
tcsdagphase = np.dot(np.dot(np.dot(np.kron(I, np.dot(np.dot(tau0_1, t), tau0_1)), MiscFuncs.T(tcx)), np.kron(I, np.dot(np.dot(tau0_1, MiscFuncs.T(t)), tau0_1))), tcx)  # // Lem.19
## |2⟩-controlled w^(-2/3) * zww gate
tczwwphase = np.dot(np.dot(np.kron(I, tau0_2), tcsdagphase), np.kron(I, tau0_2))  # Cor.20
## |2⟩-controlled -tau(1 2) gate, i.e. tctau1_2 but when the control is |2⟩, the target gains a -1 phase
tcmtau1_2 = np.dot(np.dot(np.kron(MiscFuncs.T(s), np.dot(zww, MiscFuncs.T(h))), np.dot(tczwwphase, np.kron(I, np.dot(h, zww)))), np.dot(np.dot(tczwwphase, np.kron(I, MiscFuncs.T(h))), np.dot(tczwwphase, np.kron(I, np.dot(h, zww)))))  # // Thm.22

## the below two-qutrit Clifford+T unitary is the R gate on one qutrit and the identity gate on the other
rtensorid = np.dot(tcmtau1_2, tctau1_2)
## to verify: subtracting the R gate tensor the single-qutrit identity from it equals zero
r = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, -1]])

assert(np.all(np.all(np.round(rtensorid, 10) - np.kron(r, I) == 0)))  # rounding to the 10^(-10) decimal place due to floating point error

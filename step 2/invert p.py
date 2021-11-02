import numpy
import math
from numpy import matrix
from numpy import linalg

diffusion = [
    0xf26cb481, 0x16a5dc92, 0x3c5ba924, 0x79b65248, 0x2fc64b18, 0x615acd29, 0xc3b59a42, 0x976b2584,
    0x6cf281b4, 0xa51692dc, 0x5b3c24a9, 0xb6794852, 0xc62f184b, 0x5a6129cd, 0xb5c3429a, 0x6b978425,
    0xb481f26c, 0xdc9216a5, 0xa9243c5b, 0x524879b6, 0x4b182fc6, 0xcd29615a, 0x9a42c3b5, 0x2584976b,
    0x81b46cf2, 0x92dca516, 0x24a95b3c, 0x4852b679, 0x184bc62f, 0x29cd5a61, 0x429ab5c3, 0x84256b97]

ip = [
    0x66, 0xd5, 0x4e, 0x28, 0x5f, 0xff, 0x6b, 0x53, 0xac, 0x3b, 0x34, 0x14, 0xb5, 0x3c, 0xb2, 0xc6,
    0xa4, 0x85, 0x1e, 0x0d, 0x86, 0xc7, 0x4f, 0xba, 0x75, 0x5e, 0xcb, 0xc3, 0x6e, 0x48, 0x79, 0x8f]


def bitfield(n):
    ret = [int(digit) for digit in bin(n)[2:]][::-1]
    while(len(ret) != 32):
        ret.append(0)
    return ret


def revBits(arr):
    ret = []
    for i in range(32):
        t = 0
        for j in range(32):
            t += (int(arr[i][j]) * (2**j))
        ret.append(t)
    return ret


def modMatInv(A, p):       # Finds the inverse of matrix A mod p
    n = len(A)
    A = matrix(A)
    adj = numpy.zeros(shape=(n, n))
    for i in range(0, n):
        for j in range(0, n):
            adj[i][j] = (
                (-1)**(i+j)*int(round(linalg.det(minor(A, j, i))))) % p
    return (modInv(int(round(linalg.det(A))), p)*adj) % p


def modInv(a, p):          # Finds the inverse of a mod p, if it exists
    for i in range(1, p):
        if (i*a) % p == 1:
            return i
    raise ValueError(str(a)+" has no inverse mod "+str(p))


def minor(A, i, j):    # Return matrix A with the ith row and jth column deleted
    A = numpy.array(A)
    minor = numpy.zeros(shape=(len(A)-1, len(A)-1))
    p = 0
    for s in range(0, len(minor)):
        if p == i:
            p = p+1
        q = 0
        for t in range(0, len(minor)):
            if q == j:
                q = q+1
            minor[s][t] = A[p][q]
            q = q+1
        p = p+1
    return minor


def test(bits, bitsInv):
    forward = [0]*32
    for i in range(32):
        for j in range(32):
            forward[i] ^= bits[i][j]*ip[j]
    backward = [0]*32
    for i in range(32):
        for j in range(32):
            backward[i] ^= int(bitsInv[i][j])*forward[j]

    print(ip, backward)


bits = []  # bit decompoition
for i in diffusion:
    bits.append(bitfield(i))

bits = numpy.array(bits)
bitsInv = modMatInv(bits, 2)  # inverting array mod 2


"""
BIT DECOMPOSITION OF DIFFUSION ARRAY:
Observe the pattern, bits are repeating x = a | b then x + 16 =  b | a

v-----------------------------v
1 1 1 1 0 0 1 0 0 1 1 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 0 0 0 0 0 1
0 0 0 1 0 1 1 0 1 0 1 0 0 1 0 1 1 1 0 1 1 1 0 0 1 0 0 1 0 0 1 0
0 0 1 1 1 1 0 0 0 1 0 1 1 0 1 1 1 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0
0 1 1 1 1 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0
0 0 1 0 1 1 1 1 1 1 0 0 0 1 1 0 0 1 0 0 1 0 1 1 0 0 0 1 1 0 0 0
0 1 1 0 0 0 0 1 0 1 0 1 1 0 1 0 1 1 0 0 1 1 0 1 0 0 1 0 1 0 0 1
1 1 0 0 0 0 1 1 1 0 1 1 0 1 0 1 1 0 0 1 1 0 1 0 0 1 0 0 0 0 1 0
1 0 0 1 0 1 1 1 0 1 1 0 1 0 1 1 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 0
0 1 1 0 1 1 0 0 1 1 1 1 0 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 0 1 0 0
1 0 1 0 0 1 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0 0 1 0 1 1 0 1 1 1 0 0
0 1 0 1 1 0 1 1 0 0 1 1 1 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 1
1 0 1 1 0 1 1 0 0 1 1 1 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0
1 1 0 0 0 1 1 0 0 0 1 0 1 1 1 1 0 0 0 1 1 0 0 0 0 1 0 0 1 0 1 1
0 1 0 1 1 0 1 0 0 1 1 0 0 0 0 1 0 0 1 0 1 0 0 1 1 1 0 0 1 1 0 1
1 0 1 1 0 1 0 1 1 1 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 0 0 1 1 0 1 0
0 1 1 0 1 0 1 1 1 0 0 1 0 1 1 1 1 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1

                                v-----------------------------v
1 0 1 1 0 1 0 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1 0 1 1 0 0
1 1 0 1 1 1 0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 1 1 0 1 0 1 0 0 1 0 1
1 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 0 1 0 1 1 0 1 1
0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 1 1 0 1 1 0 1 1 0
0 1 0 0 1 0 1 1 0 0 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 1 0 0 0 1 1 0
1 1 0 0 1 1 0 1 0 0 1 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 0 1 1 0 1 0
1 0 0 1 1 0 1 0 0 1 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1 0 1 1 0 1 0 1
0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 0 1 0 0 1 0 1 1 1 0 1 1 0 1 0 1 1
1 0 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 0 1 1 0 0 1 1 1 1 0 0 1 0
1 0 0 1 0 0 1 0 1 1 0 1 1 1 0 0 1 0 1 0 0 1 0 1 0 0 0 1 0 1 1 0
0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 1 0 1 1 0 0 1 1 1 1 0 0
0 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0 1 0 1 1 0 1 1 0 0 1 1 1 1 0 0 1
0 0 0 1 1 0 0 0 0 1 0 0 1 0 1 1 1 1 0 0 0 1 1 0 0 0 1 0 1 1 1 1
0 0 1 0 1 0 0 1 1 1 0 0 1 1 0 1 0 1 0 1 1 0 1 0 0 1 1 0 0 0 0 1
0 1 0 0 0 0 1 0 1 0 0 1 1 0 1 0 1 0 1 1 0 1 0 1 1 1 0 0 0 0 1 1
1 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 1 1 0 1 0 1 1 1 0 0 1 0 1 1 1
"""

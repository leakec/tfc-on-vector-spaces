import numpy as np
import galois

gf = galois.GF(2,2)
elements = gf.Range(0,4)
z = elements[0]
o = elements[1]
A = elements[2]
B = elements[3]

# Addition and multiplication table
dark = np.expand_dims(elements,axis=0)
add_table = dark + dark.T
mult_table = dark * dark.T

# S and alpha
s = [lambda x: o, lambda x: x]
C = [lambda u: u(o), lambda u: u(A) - u(B)]
S = gf([[c(sx) for sx in s] for c in C])

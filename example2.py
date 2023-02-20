import numpy as np
from numpy.typing import NDArray
import sympy as sp
cipher = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

s1 = 4+2j
def s2(x: str) -> complex:
    real = 0
    imag = 0
    for char in x:
        k = cipher[char]
        real += k
        imag += 1j**k
    return real + imag

S = sp.Matrix([[s1, s2("tfc")],[0, s2("dont")-s2("panic")]])
alpha = S.inv()

# Check constrained expression
def g(x: str) -> NDArray:
    g1 = 0.0
    g2 = 1.0
    for char in x:
        k = cipher[char]
        g1 += np.sin(k) - np.cos(k)*1j
        g2 *= k + 3j
    return np.array([[g1],[g2]])

def u(x: str) -> NDArray:
    return g(x) + np.array([[42j],[19+79j]]) - g("tfc") + ( -2.568 - 0.376j + (0.088 + 0.016j) * s2(x)) * (g("panic") - g("dont"))

print("tfc: \n" + str(u("tfc")))
print("\ndont - panic: \n" + str(u("dont") - u("panic")))

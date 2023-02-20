import sympy as sp
from sympy.simplify.simplify import nc_simplify
from tfc.utils import CeSolver

# E1
x = sp.MatrixSymbol("x", 2 ,3)
g = sp.Function("g", commutative=True)
u = sp.Function("u", commutative=True)

A = sp.Matrix([[1, 3, 5],[2, 4, 7]])
B = sp.Matrix([[3],[4]])
C = sp.Matrix([[1, 0, 1],[0, 1, 0]])
D = sp.Matrix([[0, 0, 1],[1, 0, 0]])

Ci = [lambda u: u.subs(x, A), lambda u: u.subs(x,C) - u.subs(x,D)]
K = [B, sp.Matrix([[0],[0]])]
s = [nc_simplify(sp.Matrix([[1, 0]])* x* sp.Matrix([[1],[0],[0]])),nc_simplify(sp.MatMul(sp.Matrix([[1, 0]]), x, sp.Matrix([[0],[1],[0]])))]
cs = CeSolver(Ci, K, s, g(x))


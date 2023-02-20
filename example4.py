import sympy as sp
from tfc.utils import CeSolver

# E3
x = sp.Symbol("x")
y = sp.Symbol("y")
t = sp.Symbol("t")
g = sp.Function("g", commutative=True)
u = sp.Function("u", commutative=True)

Cx = [lambda u: u.subs(x, 0), lambda u: u.subs(x,1) + u.subs(x,2) - u.subs(x,4) - u.subs(x,5)]
Kx = [sp.sin(t), sp.re(0)]
sx = [sp.re(1), x]
csx = CeSolver(Cx, Kx, sx, g(x,y))

Cy = [lambda u: u.subs(y,1)]
Ky = [sp.sin(t)]
sy = [sp.re(1)]
csy = CeSolver(Cy, Ky, sy, g(x,y))

# Print the expression
csx.print_type = "pretty"
csy.print_type = "pretty"
sp.pprint(csx.ce)
sp.pprint(csy.ce)

# Check the constraints are satisfied
assert(csx.checkCe())
assert(csy.checkCe())

csy.g = csx.ce
assert(csy.checkCe())

sp.pprint(csy.ce)

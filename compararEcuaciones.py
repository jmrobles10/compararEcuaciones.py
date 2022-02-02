# Before you run the code, clone the git repository for sympy
# executing this commando line: (git clone https://github.com/sympy/sympy.git)

from sympy import *

theta = symbols("theta", real = True)
theta2 = symbols("theta2", positive = True)
h, R, rho, g, b = symbols("h, R, rho, g, b")
init_printing(use_latex='mathjax')

# Se definen las ecuaciones

d = h - R*(1-cos(theta))
p = d*rho*g

# Se define la primera ecuación
T_2 = p*cos(theta)
dF_2 = T_2*b*R
F_2 = integrate(dF_2, (theta, -theta2, theta2)).simplify()
F_2 = simplify(F_2.subs(theta2, acos((R-h)/R)))

# Se define la segunda ecuación
A1 = pi*(R**2)*((theta2)/(2*pi))
A2 = sqrt((R**2)-(R-h)**2)*(R-h)/2
A_a = A1 - A2
V = 2*A_a*b

V = simplify(V.subs(theta2, acos((R-h)/R)))
F_A = rho*g*V

simplify(F_2/F_A)

# Se comprueba dando valores numéricos
F_A = F_A.subs(R, 4).subs(h, 1.5)
F_2 = F_2.subs(R, 4).subs(h, 1.5)

simplify(F_2/F_A)

msgSuccess = "Las ecuaciones son equivalentes"
msgFailure = "Las ecuaciones no son equivalentes"

def prueba(F_A, F_2):
    if F_A == F_2:
        print(msgSuccess)
    else:
        print(msgFailure)

prueba(F_A, F_2)


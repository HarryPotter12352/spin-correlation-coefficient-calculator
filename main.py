import sympy as sp

# Define the symbols
t, r, theta, phi = sp.symbols('t r theta phi')
a = sp.Function('a')(t)
k = sp.symbols('k')

# Define the tetrad tensor e_a^mu 
e = sp.Matrix([
    [1, 0, 0, 0],
    [0, a * sp.sqrt(1 / (1 - k * r**2)), 0, 0],
    [0, 0, a * r, 0],
    [0, 0, 0, a * r * sp.sin(theta)]
])

# Define the Christoffel symbols of the 2nd kind Gamma_mu_nu^lambda
Gamma = {
    0: sp.zeros(4, 4),
    1: sp.Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, -2 * a**2 * r * (0.5 * (1 - k**2) / a**2), 0],
        [0, 0, 0, -2 * a**2 * r * (0.5 * (1 - k**2) / a**2) * sp.sin(theta)**2]
    ]),
    2: sp.Matrix([
        [0, 0, 0, 0],
        [0, 0, 1 / r, 0],
        [0, 1 / r, 0, 0],
        [0, 0, 0, -sp.sin(theta) * sp.cos(theta)]
    ]),
    3: sp.Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 1 / r],
        [0, 0, 0, sp.cot(theta)],
        [0, 1 / r, sp.cot(theta), 0]
    ])
}

# Initialize the spin correlation coefficient tensor omega
omega = sp.MutableDenseNDimArray.zeros(4, 4, 4)

# Compute 
for mu in range(4):
    for a_idx in range(4):
        for b_idx in range(4):
            term1 = 0
            for alpha in range(4):
                term1 += e[a_idx, alpha] * sp.diff(e[alpha, b_idx], [t, r, theta, phi][mu])
                
            term2 = 0
            for alpha in range(4):
                for nu in range(4):
                    term2 += e[a_idx, alpha] * Gamma[mu][alpha, nu] * e[nu, b_idx]
            
            omega[mu, a_idx, b_idx] = term1 + term2

# Display 
print(omega)

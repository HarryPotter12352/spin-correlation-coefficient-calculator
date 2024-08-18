# spin-correlation-coefficient-calculator
Spin correlation coefficients are parametrized coefficients that act as gauge fields. They ensure that the co-variant derivative accounts for local transformations in the tetrad field correctly. This is because spinors may transform differently than vectors under Lorentz transforms. 
For example, in the context of the Dirac equation, the co-variant derivative of a 4-spinor $\psi$ is given by
$$\Delta_{\mu}\psi = \partial_{\mu} + \frac{1}{4} \omega_{\mu}^{ab}[\gamma_a, \gamma_b]\psi$$
The spin correlation coefficients are given by
$$\omega_{\mu}^{ab} = e^{a\alpha}\left(\partial_
{\mu}e_{\alpha}^b + \Gamma_{\mu\alpha}^{\nu} e_{\nu}^{b}\right)$$
$e$ is the tetrad field given by
$$g_{\mu\nu} = \eta_{ab}e_a^{\mu}e_b^{\nu}$$
and $\Gamma$ are the Christoffel sybmols of the second kind, given by
$$\Gamma_{\mu\nu}^{\lambda} = \frac{1}{2}g^{\lambda\sigma}\left(\partial_{\mu}g_{\nu\sigma} + \partial_{\nu}g_{\mu\sigma} - \partial_{\sigma}g_{\mu\nu}\right)$$
In this example, I have used the FLRW metric, given by
$$ds^2 = -dt^2 + a^2(t)\left[\frac{dr^2}{1-k^2} + r^2 d\Omega^2\right]$$
where $$d\Omega^2 = d\theta^2 + \sin^2 \theta d\phi^2$$
I hope this program can be of assistance.
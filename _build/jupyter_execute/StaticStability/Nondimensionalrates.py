# Non-dimensional rates

In the following, the stability in the other two axes will be described. Note that this is a simplified analysis to facilitate undergraduate understanding at this point in the course. In the full aircraft equations of motion which will be derived in the next module, there are 108 stability derivatives (and we could easily add more). A subset will be spoken about from first principles pertaining to the aircraft static stability.

In the formulations used in this section for the roll, pitch, and yaw stability:

$$
\begin{align}
    C_{\ell} & = C_{\ell_\beta}\cdot\beta + C_{\ell_P}\cdot P + C_{\ell_{\delta_a}}\cdot\delta_a\\
    C_m & = C_{m_\alpha}\cdot\alpha + C_{m_Q}\cdot Q + C_{m_{\delta_e}}\cdot\delta_e\\
    C_n & = C_{n_\beta}\cdot\beta + C_{n_R}\cdot R + C_{n_{\delta_r}}\cdot\delta_r
\end{align}
$$

the product of the right hand terms are unitless, but the derivatives themselves are dimensional. To compare different aircraft, the angular rates are often expressed in non-dimensional forms:

$$
\begin{align}
    \bar{p}&\triangleq\frac{P\, b}{2\,V_\infty}\\
    \bar{q}&\triangleq\frac{Q\, \bar{c}}{2\,V_\infty}\\
    \bar{r}&\triangleq\frac{R\, b}{2\,V_\infty}
\end{align}
$$

this enables simpler expressions to be developed for the corresponding stability derivatives, *e.g.,* $C_{\ell_{\bar{p}}}$ and $C_{\ell_{P}}$ both express *roll damping*, but the dimensional derivative is function of the aircraft geometry and forward speed whereas the nondimensional expression is not.
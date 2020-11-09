# Summary of the equations of motion

With the translational (Eq. {eq}`eq:translationalEoM`) and rotational (Eq. {eq}`eq:rotationalEoM`) defined, and the relationship between the Euler angles and the body rates (Eqs. {eq}`eq:eulerratetoomega` and {eq}`eq:omegatoeulerrate`), fully unconstrained flight in 6DoF can be described.




In total twelve equations have been derived (body/attitude rates are only three but the matrix is tough to invert, so I'll include both versions below) that can describe aircraft position and attitude in a Newtonian framework:

## Translational Motion:

$$m\begin{bmatrix} \dot{U} + Q\,W - R\,V \\ \dot{V} + R\,U-P\,W\\\dot{W}+P\,V-Q\,U\end{bmatrix}=\begin{matrix} -mg\sin\theta - D\cos\alpha + L\sin\alpha + T\cos\theta_T\\mg\sin\phi\cos\theta + F_{A_Y} + F_{T_Y}\\mg\cos\phi\cos\theta - D\sin\alpha - L\cos\alpha - T\sin\theta_T\end{matrix}$$

## Angular Motion:

$$\left[{\begin{matrix} \dot{P}\cdot I_{xx} \\ \dot{Q}\cdot I_{yy} \\\dot{R}\cdot I_{zz}\end{matrix}} \hspace{.5cm} \begin{matrix} + \\+\\+\end{matrix} \hspace{.5cm} {\begin{matrix} Q\cdot R\left(I_{zz} - I_{yy}\right) \\ P\cdot R\left(I_{xx} - I_{zz}\right) \\ P\cdot Q\left(I_{yy} - I_{xx}\right)\end{matrix}} \hspace{.5cm} \begin{matrix} - \\+\\+\end{matrix} \hspace{.5cm} {\begin{matrix}\left(\dot{R} + P\cdot Q\right) I_{xz} \\ \left(P^2 - R^2\right) I_{xz} \\ \left(Q\cdot R - \dot{P}\right) I_{xz}\end{matrix}} \right] = \begin{bmatrix} L \\ M \\ N\end{bmatrix}$$

## Body angular rate due to an attitude rate:

$$\begin{aligned}
    \begin{bmatrix} P\\Q\\R\end{bmatrix} &= \begin{bmatrix}
    1 & 0 & -\sin\theta\\
    0 & \cos\phi & \sin\phi\cos\theta\\
    0 & -\sin\phi & \cos\phi\cos\theta
 \end{bmatrix}\begin{bmatrix} \dot{\phi}\\\dot{\theta}\\\dot{\psi}\end{bmatrix}\end{aligned}$$

## Attitude rate due to a body rate

$$\begin{aligned}
\begin{bmatrix} \dot{\phi}\\\dot{\theta}\\\dot{\psi}\end{bmatrix}&= \begin{bmatrix}
    1 & \sin\phi\tan\theta & \cos\phi\tan\theta\\
    0 & \cos\phi & -\sin\phi    \\
    0 & \frac{\sin\phi}{\cos\theta} & \frac{\cos\phi}{\cos\theta}
 \end{bmatrix}\begin{bmatrix} P\\Q\\R\end{bmatrix}\end{aligned}$$


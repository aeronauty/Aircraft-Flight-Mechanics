# The Road so Far...

In the preceding chapters, nine equations describing unconstrained aircraft flight in six degrees of freedom have been described:

**Translational Motion:**

$$m\begin{bmatrix} \dot{U} + Q\,W - R\,V \\ \dot{V} + R\,U-P\,W\\\dot{W}+P\,V-Q\,U\end{bmatrix}=\begin{matrix} -mg\sin\theta - D\cos\alpha + L\sin\alpha + T\cos\theta_T\\mg\sin\phi\cos\theta + F_{A_Y} + F_{T_Y}\\mg\cos\phi\cos\theta - D\sin\alpha - L\cos\alpha - T\sin\theta_T\end{matrix}$$(eq:tranlationalnonlinear)

**Angular Motion:**

$$\left[{\begin{matrix} \dot{P}\cdot I_{xx} \\ \dot{Q}\cdot I_{yy} \\\dot{R}\cdot I_{zz}\end{matrix}} \hspace{.5cm} \begin{matrix} + \\+\\+\end{matrix} \hspace{.5cm} {\begin{matrix} Q\cdot R\left(I_{zz} - I_{yy}\right) \\ P\cdot R\left(I_{xx} - I_{zz}\right) \\ P\cdot Q\left(I_{yy} - I_{xx}\right)\end{matrix}} \hspace{.5cm} \begin{matrix} - \\+\\+\end{matrix} \hspace{.5cm} {\begin{matrix}\left(\dot{R} + P\cdot Q\right) I_{xz} \\ \left(P^2 - R^2\right) I_{xz} \\ \left(Q\cdot R - \dot{P}\right) I_{xz}\end{matrix}} \right] = \begin{bmatrix} L \\ M \\ N\end{bmatrix}$$(eq:rotationalnonlinear)

**Body angular rate due to an attitude rate:**

$$\begin{aligned}
    \begin{bmatrix} P\\Q\\R\end{bmatrix} &= \begin{bmatrix}
    1 & 0 & -\sin\theta\\
    0 & \cos\phi & \sin\phi\cos\theta\\
    0 & -\sin\phi & \cos\phi\cos\theta
 \end{bmatrix}\begin{bmatrix} \dot{\phi}\\\dot{\theta}\\\dot{\psi}\end{bmatrix}\end{aligned}$$(eq:attitiudetoanglenonlinear)

**Attitude rate due to a body rate**

$$\begin{aligned}
\begin{bmatrix} \dot{\phi}\\\dot{\theta}\\\dot{\psi}\end{bmatrix}&= \begin{bmatrix}
    1 & \sin\phi\tan\theta & \cos\phi\tan\theta\\
    0 & \cos\phi & -\sin\phi    \\
    0 & \frac{\sin\phi}{\cos\theta} & \frac{\cos\phi}{\cos\theta}
 \end{bmatrix}\begin{bmatrix} P\\Q\\R\end{bmatrix}\end{aligned}$$(eq:angletoattitudenonlinear)
 
 and _basic_ static stability characteristics have been explored in the form of derivatives. Whilst further understanding of the static stability derivatives can be performed using the methodologies shown, the full dynamic stability analysis is what is really required for aircraft design.
 
When designing an aircraft for any given use case, the dynamic behaviour must be predicted via modelling of the system[^1]. You may design an aircraft with a drag-saving fuselage, a high-lift supercritical wing section, and a myriad of other 'high-tech' benefits - but if it cannot be flown, then it will be useless (if it is unstable, has poor handling qualities or, in the case of a military aircraft, is *too* stable).

[^1]: note that this is true for any given Engineering task, but particularly for aircraft owing to the complexity

In general, we can define the process for determining an aircraft dynamic properties:

1.  Construct a mathematical model of the system (Module 3)

2.  Determine the open loop stability characteristics (Partially performed in Module 2)

3.  Determine the open loop transient response

4.  Design and model a control system

5.  Determine the closed-loop stability characteristics and transient response

Item 1 was fulfilled in the development of the aircraft equations of motion, which are at the top of this page.

Some of the open loop stability characteristics were explored in [Static Stability](ch:static-stability), but to go into a full analysis and to look at the transient response of the open loop system requires methodologies that will be explored in this and the following chapter.

The control system will not be included in this course just yet, but may be included at a future data if I can offload the performance modules to Freshman/Sophomore classes, as I plan to.

## Nonlinearity

Equations {eq}`eq:tranlationalnonlinear` and {eq}`eq:rotationalnonlinear` comprise the **nonlinear aircraft equations of motion**, since they describe the relationships between forces and moments, and the motion in 6DoF. Equations {eq}`eq:attitiudetoanglenonlinear` and {eq}`eq:angletoattitudenonlinear` are required to related aircraft quantities into the inertial reference frame.

The independent variables are the translational motion, $\vec{V}=\left[U, V, W\right]^T$, and the rotational motion, $\vec{omega}=\left[P, Q, R\right]^T$. These are referred to as **state variables** of the system.

It should be apparent that {eq}`eq:tranlationalnonlinear` and {eq}`eq:rotationalnonlinear` are nonlinear since:
- There are **product terms** in the right hand side _e.g.,_ $P\,V-Q\,U$
- **Trigonometric terms** _e.g.,_ $D\cos\alpha + L\sin\alpha$
- In the above the aerodynamic angle of attack, $\alpha$, is a trigonometric function of two state variables, $U$, and $W$
- We further know that the non-conservative aerodynamic forces, $L$ and $D$ are nonlinear functions of $\alpha$ (and $V_\infty$, $M_\infty$, _etc._)

The full nonlinear equations of motion can only be solved analytically for a small subset of problems, and often they are utilised through numerical solution - which is a _brute force_ means of analysing a system, and cannot easily help us determine stability characteristics. Furthermore, it's an _inelegant_ means to work, and it would be be superb if there were a better means to analyse these equations.

So - the equations of motion shall be linearised to help understand stability.






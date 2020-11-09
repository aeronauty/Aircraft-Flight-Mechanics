# EoMs for Translation

With the expression for the absolute acceleration now obtained, we can apply Newton's second law,

$$\frac{d\left(m\vec{V}\right)}{dt}_{abs}=\sum\vec{F}_{ext}$$ (eq:N2_EOM)

Where the $()_{abs}$ refers to *absolute acceleration*, defined in an inertially-fixed reference frame - which, for our purposes, we may treat Earth axes as being. As we have shown, we have defined forces in *body axes*, which is moving with respect to Earth axes.

When we have accelerations and translations defined in a non-inertial reference frame, we must use Eqn {eq}`eq:coriolis1` to determine *absolute accelerations*.

$$\vec{a}_{b_{abs}} = \left.\frac{\text{d}\vec{V}_b}{\text{d}t}\right|_{Oxyz} + \vec{\omega_b}\times\vec{V}_b$$

where

$$\begin{align}\vec{V}_b&=\begin{bmatrix}U\\V\\W\end{bmatrix}\\
    \vec{\omega}_b&=\begin{bmatrix}P\\Q\\R\end{bmatrix}\end{align}$$
    
so we have

$$\begin{aligned}
        \vec{a}_{b_{abs}} &=\begin{bmatrix}\dot{U}\\\dot{V}\\\dot{W}\end{bmatrix} + \left|\begin{matrix}i & j & k \\ P & Q & R \\U & V & W\end{matrix}\right|\\
        &= \begin{bmatrix} \dot{U} + Q\,W - R\,V \\ \dot{V} + R\,U-P\,W\\\dot{W}+P\,V-Q\,U\end{bmatrix}\end{aligned}$$

Thus we have defined our **absolute acceleration terms in body axes**, which means we can define the LHS of Equation {eq}`eq:N2_EOM`.

$$\frac{d\left(m\vec{V}\right)}{dt}_{abs}=m\begin{bmatrix} \dot{U} + Q\,W - R\,V \\ \dot{V} + R\,U-P\,W\\\dot{W}+P\,V-Q\,U\end{bmatrix}_b$$

The RHS of Equation {eq}`eq:N2_EOM` are the sum of *gravitational/weight*, *aerodynamic*, and *propulsive* forces defined in body axes.

$$\sum{\vec{F}_b} = \vec{F}_{G_b} + \vec{F}_{A_b}  + \vec{F}_{P_b}$$

We have already expressed the aerodynamic and gravitational forces in body axes, Equations {eq}`aero_body` and {eq}`gforce_body`, respectively. We now define the propulsive forces.

We presume the aircraft has one or more propulsors providing thrust, $T$, along a vector defined in the $x/z$ plane, at angle $\theta_T$ to $x$. We include an additional term for sidewash effects due to propulsion, $F_{Ty}$:

$$\vec{F}_{T_b}=\begin{bmatrix} F_{Tx} \\F_{Ty} \\F_{Tz}\end{bmatrix}=\begin{bmatrix} T\cdot\cos\theta_T \\F_{Ty} \\-T\cdot\sin\theta_T\end{bmatrix}$$

Thus we can write out equations of motion for translation:

$$m\begin{bmatrix} \dot{U} + Q\,W - R\,V \\ \dot{V} + R\,U-P\,W\\\dot{W}+P\,V-Q\,U\end{bmatrix}=\begin{matrix} -mg\sin\theta - D\cos\alpha + L\sin\alpha + T\cos\theta_T\\mg\sin\phi\cos\theta + F_{A_Y} + F_{T_Y}\\mg\cos\phi\cos\theta - D\sin\alpha - L\cos\alpha - T\sin\theta_T\end{matrix}$$ (eq:translationalEoM)




Which is a pretty big deal to have derived. Equations {eq}`eq:translationalEoM` describe the response of the aircraft translational acceleration to the aerodynamic forces and vice versa.

This isn't enough to describe flight, though - for that, we require the ability to describe rotation and attitude.




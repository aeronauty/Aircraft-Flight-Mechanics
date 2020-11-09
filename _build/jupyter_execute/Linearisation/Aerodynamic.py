# Linear Aerodynamic Terms

In addition to the terms expressed previously, linear expressions are required for the aerodynamic angles and the total flightspeed.

## Angle of Attack

Angle of attack is defined as

$$\alpha\triangleq\arctan\frac{W}{U}$$

which with the small perturbation theory is

$$\alpha=\arctan\frac{W_0+w}{U_0+u}$$

in stability axes, $W_0=0$

$$\alpha=\arctan\frac{w}{U_0+u}$$

and since $w$ is small

$$\alpha\simeq\frac{w}{U_0+u}$$

the perturbational forward speed is much smaller than the trim forward speed and the **linear angle of attack is**:

$$\alpha=\frac{w}{U_0}$$(eq:linearalpha)

## Sideslip

Sideslip is defined as

$$\beta\triangleq\arcsin\frac{V}{V_f}$$

where $V_f=\sqrt{U^2+V^2+W^2}$. Looking at a linear expression for the total flightspeed:

$$\begin{align}V_f&=\sqrt{\left(U_0+u\right)^2+\left(V_0+v\right)^2+\left(W_0+w\right)^2}\\
&= \sqrt{\left(U_0+u\right)^2+v^2+w^2}\end{align}$$

the trim $U_0$ is $\gg$ all the perturbational terms so

$$V_f\simeq U_0$$

giving the linear sideslip, subject to small $v$ as

$$\beta=\frac{v}{U_0}$$


# Linearisation Theory

Linearisation or *small disturbance* theory is the process via which the equations of motion shall be _simplified_ and how the aircraft dynamic behaviour may be analysed. 

The basic assumptions are that aircraft motion comprises *small disturbances* from a *trim/equilibrium* state. This is a valid assumption for most flight conditions, but care must be taken when exploring high manoeuvre flight as such analyses require solution of the full nonlinear equations of motion (via numerical solution).

It is assumed that at any given time, the instantaneous value of the aircraft state and control variables[^2] may be represented by the trim value (denoted by a subscript $_0$) and this small disturbance (either lowercase, or with $^\prime$ in some cases, or a $\Delta$ in other cases):

[^2]: Control variables $\delta_e,\delta_a, \delta_r$

```{admonition} Nomenclature, again
:class: dropdown
As in Flight Mechanics, Flight Dynamics is a bit of a mish-mash of nomenclature depending whose book you happen to be reading. Some texts use a subscript 'e' for _equilibrium_, but this is ambiguous as it also could be quantities in earth axes. Some texts us a subscript '1', which is a bit strange since it just skips over '0' (_i.e.,_ trim is time zero, surely?).

The lesson here is to be careful and to ensure you understand what you're reading.
```

**Rates:**

$$\begin{aligned}
    U &= U_0 + u\\
    V &= V_0 + v\\
    W &= W_0 + w\\
    P &= P_0 + p\\
    Q &= Q_0 + q\\
    R &= R_0 + r
\end{aligned}$$

**Attitudes**

$$\begin{aligned}
    \phi &= \phi_0 + \phi^\prime\\
    \theta &= \theta_0 + \theta^\prime\\
    \psi &= \psi_0 + \psi^\prime
\end{aligned}$$

**Forces and Moments**

$$\begin{aligned}
    X &= X_0 + \Delta X\\
    Y &= Y_0 + \Delta Y\\
    Z &= Z_0 + \Delta Z\\
    L &= L_0 + \Delta L\\
    M &= M_0 + \Delta M\\
    N &= N_0 + \Delta M
\end{aligned}$$

**Control Settings:**

$$\begin{aligned}
    \delta_a &= \delta_{a_0} + \delta_a^\prime\\
    \delta_e &= \delta_{e_0} + \delta_e^\prime\\
    \delta_r &= \delta_{e_0} + \delta_r^\prime\label{eq:smallP2}    \end{aligned}$$
    
Note that the nomenclature between each is inconsistent, annoyingly. Furthermore, the Roman and Greek letters are difficult to write freehand as uppercase and lowercase letters - hence the subscript $_0$ is integral to distinguishing the trim and perturbation.

We make some inferences and assumptions about our reference trim state

## Trim State Assumptions

-   There are no resultant accelerations on the aircraft (equilibrium state): 

$$\dot{U}_0 = \dot{V}_0 = \dot{W}_0 = \dot{P}_0 = \dot{Q}_0 = \dot{R}_0 = 0$$

-   There is no angular velocity 

$${P}_0 = {Q}_0 = {R}_0 = 0$$

-   Wings level flight 

$$\phi_0=0$$

-   Symmetric/co-ordinated flight, forces represented in *stability axes* 

$$V_0 = W_0 = 0$$

    
## Linearisation Procedure

The following steps will be taken to linearise the equations of motion:

1. Replace each state variable with the sum of the equilibrium and small perturbation term
2. Apply the trim state assumptions from above
3. Assume all perturbations are small and apply small angle assumptions
4. Eliminate all products and powers of perturbations _i.e.,_ if $a,b<1$, then $ab\ll 1\implies ab\simeq0$
5. Evaluate the equation at the trim state, and create an expression to substitute into the linearised expression

This is best highlighted with an example. Taking the first of the translational equations of motion:

$$m\left(\dot{U} + Q\,W - W\,R\right)=-mg\sin\theta - D\cos\alpha + L\sin\alpha + T\cos\theta_T$$

since for stability and control purposes, _stability axes_ are used, the trim angle of attack is zero and the nonservative forces on the RHS can be lumped into a single $X$ (which will later be separated into aero and propulsive terms):

$$m\left(\dot{U} + Q\,W - W\,R\right)=X-mg\sin\theta$$(eq:nonlin1trim)

which immediately makes the equation less brutal looking. 

**Step 1:** Replace each of the state variables with the equilibrium and small perturbation:

$$m\left[\left(\dot{U}_0+\dot{u}\right) +\left(Q_0+q\right)\left(W_0+w\right)-\left(R_0+r\right)\left(V_0+v\right)\right] = \left(X_0+\Delta X\right)   -mg\sin\left(\theta_0+\theta^\prime\right)$$

**Step 2:** Apply the zero trim values from our assumptions above, and expand the trig term:

   $$m\left[\dot{u}+qw-rv\right] =\left(X_0+\Delta X\right) - mg\left(\sin\theta_0\cos\theta^\prime + \cos\theta_0\sin\theta^\prime\right)$$
   
**Step 3:** Assume the perturbations are _small_, which for this equation allows simplification of the terms containing attitude perturbations ($\theta$)

$$m\left[\dot{u}+qw-rv\right]=\left(X_0+\Delta X\right) - mg\left(\sin\theta_0 + \theta^\prime\cos\theta_0\right)$$

**Step 4:** Eliminate products of perturbation - so if $a,b<1$, $ab\ll 1$, and $\dot{u}\gg\left(qw-vr\right)$:

$$m\dot{u} = \left(X_0+\Delta X\right) - mg\left(\sin\theta_0 + \theta^\prime\cos\theta_0\right)$$(eq:step4)

**Step 5:** Evaluate the nonlinear equation of motion (Eq. {eq}`eq:nonlin1trim`) at the trim state, subject to assumptions:

$$0 = X_0 - mg\sin\theta_0$$(eq:trimstate1)

Hence substitution of Eq. {eq}`eq:trimstate1` into Eq. {eq}`eq:step4` yields

$$m\dot{u} = \Delta X - mg\theta^\prime\cos\theta_0$$(eq:lineq1)

Expression {eq}`eq:lineq1` is the nonlinear equation for fore/aft motion. The other expressions may be manipulated similarly to give:

$$m\dot{v} = \Delta Y - mU_0r + mg\phi^\prime\cos\theta_0$$(eq:lineq2)
$$m\dot{w} = \Delta Z + mU_0q - mg\theta^\prime\sin\theta_0$$(eq:lineq3)
$$I_{xx}\dot{p} - I_{xz}\dot{r} = \Delta L$$(eq:lineq4)
$$I_{qq}\dot{q}= \Delta M$$(eq:lineq5)
$$I_{zz}\dot{r} - I_{xz}\dot{p} = \Delta N$$(eq:lineq6)

You should be able to derive expressions {eq}`eq:lineq1` through {eq}`eq:lineq6`, starting from the equations of motion (which, of course, you should also be able to derive).

Recall the relationship between Euler rates and body rates: 

$$\begin{aligned}
    \begin{bmatrix} P\\Q\\R\end{bmatrix} &= \begin{bmatrix}
    1 & 0 & -\sin\theta\\
    0 & \cos\phi & \sin\phi\cos\theta\\
    0 & -\sin\phi & \cos\phi\cos\theta
 \end{bmatrix}\begin{bmatrix} \dot{\phi}\\\dot{\theta}\\\dot{\psi}\end{bmatrix}\end{aligned}$$

Taking the first expression: 

$$\begin{aligned}
    P &= \dot{\phi} - \dot{\Psi}\sin\theta
\end{aligned}$$(eq:nonlinearP)

Replacing all terms with trim + perturbation

$$\begin{aligned}
    \left(P_e + p\right) &= \left(\dot{\phi}_0 + \dot{\phi}^\prime\right) - \left(\dot{\psi}_0 + \dot\psi^\prime\right)\sin\left(\theta_0 + \theta^\prime\right)\end{aligned}$$
    
No angular velocity in trim, and expansion of trig term:

$$\begin{aligned}
    p &= \dot{\phi}^\prime - \dot{\psi}^\prime\left(\sin\theta_0\cos\theta^\prime+\cos\theta_0\sin\theta^\prime\right)
\end{aligned}$$

Apply small angle assumption:

$$\begin{aligned}
    p &= \dot{\phi}^\prime - \dot{\psi}^\prime\left(\sin\theta_0+\theta^\prime\cos\theta_0\right)\end{aligned}$$
    
finally, applying products and power of small terms, the linearised version of equation {eq}`eq:nonlinearP` is produced, and the remaining terms for $q$ and $r$ are also included below (which you should be able to derive):

$$p = \dot{\phi}^\prime-\dot{\psi}^\prime\sin\theta_0$$
$$q = \dot{\theta}^\prime$$(eq:pitchratekinematic)
$$r = \dot{\psi}^\prime\cos\theta_0$$

The remaining task is to obtain linearised expressions for the external forces and moments, $X,Y,Z,L,M,N$, which will be dealt with the following section. 

First we will go over a brief example:


### Linearisation Example

``` {admonition} Linearisation Example:

A fighter aircraft has an ECM pod attached to each wing tip. It is proposed to examine the effect of a rapid yawing motion, due to a sudden rudder input, on a particular sensor in the pod. The pod is located at position $S$, at a distance $l$ behind the centre of gravity, $G$, and a distance $B$ from the aircraft's centreline. Firstly, using the theory from the preceding section, show that the absolute acceleration at the sensor during pure yaw motion is given by:

$$\def\ii{\hat{\imath}}\def\jj{\hat{\jmath}}\def\kk{\hat{k}}$$
$$\begin{align}
		A_S &= A_{S_x}\ii_b + A_{S_y}\jj_b + A_{S_z}\kk_b
\end{align}$$

where

$$\begin{align}
		A_{S_x} &= \dot{U} - VR - b\dot{R} + l R^2\\
		A_{S_y} &= \dot{V} + UR - l\dot{R} - b R^2\\
		A_{S_z} &= \dot{W}
	\end{align}$$
	
**Using the small perturbation theory described in the preceding section, and stating all assumptions made, develop linearised expressions for the three component accelerations.**
```



``` {admonition} Linearisation Solution:
:class: dropdown

Taking the expression for the $X$ component acceleration:

$$
\begin{align}
	A_{S_x} &= \dot{U} - VR - b\dot{R} + l R^2 
\end{align}
$$

we replace each variable with the trim + perturbation value

$$
\begin{align}
	A_{S_{x_e}} &= 	\dot{U}_e + \dot{u} - \left(V_e + v\right)\left(R_e+r\right)-b\left(\dot{R}_e+\dot{r}\right)+l\left(R_e+r\right)^2
    \end{align}
$$

In trim, accelerations, angular velocities, and sideslip is zero:

$$
\begin{align}
	A_{S_{x_e}} + a_{s_x} &= \dot{U}_e = R_e = \dot{R}_e = 0 \\
	\implies a_{s_x} &= \dot{u}-vr-b\dot{r}+lr^2
    \end{align}
$$

we ignore products and power of perturbations

$$
\begin{align}
	a_{s_x} &= \dot{u}-b\dot{r}
        \end{align}
$$

Similarly in the y-direction:

$$
\begin{align}
	A_{s_{y_e}} + a_{s_y} &= \left(\dot{V}_e+\dot{v}\right) + \left(U_e + u\right)\left(R_e+r\right) - l\left(\dot{R}_e+\dot{r}\right) - b\left(R_e + r\right)^2
        \end{align}
$$

again, we may neglect terms that we know are zero

$$
\begin{align}
	a_{s_y} &= \left(\dot{v}\right) + \left(U_e + u\right)\left(+r\right) - l\left(\dot{r}\right) - b\left(r\right)^2\\	
	a_{s_y} &= \dot{v} + r\left(U_e + u\right) - l\dot{r} - br^2
    \end{align}
$$

ignoring products and power of small perturbations

$$
\begin{align}
	a_{s_y} &= \dot{v}+r U_e - l\dot{r}
\end{align}
$$

the z direction is simple

$$
\begin{align}
	A_{s_z} &= \dot{W}\\
	a_{s_z} &= \dot{w}\\
	a_{s_z} &= \dot{w}	
\end{align}
$$
```


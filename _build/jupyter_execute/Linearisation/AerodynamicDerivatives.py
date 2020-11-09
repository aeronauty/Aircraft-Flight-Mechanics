# Stability Derivatives

To complete the linearisation process, linear expressions for the **aerodynamic** and **propulsive** force and moment perturbations are required. The end result of this process will be the **stability derivatives** that we incepted in the static stability module, and we'll find that there are a _lot_ of them. Rather than the approach taken in the previous modules, which constrained motion to single degrees of freedom, an approach is adopted that allows representation of motion in all axes including all cross-couplings.

It is assumed that the external forces ($X,Y,Z$) and moments ($L,M,N$) are functions of the instantaneous values of the disturbance velocities (translational and angular), control angles, and the derivatives of both. That is:

$$\begin{aligned}
    X &= f_1\left(u, \dot{u}, v, \dot{v}, w, \dot{w},   p, \dot{p}, q, \dot{q}, r, \dot{r},\delta_a, \dot{\delta}_a, \delta_e, \dot{\delta}_e,\delta_r, \dot{\delta}_r\right)\\
    Y &= f_2\left(u, \dot{u}, v, \dot{v}, w, \dot{w},   p, \dot{p}, q, \dot{q}, r, \dot{r},\delta_a, \dot{\delta}_a, \delta_e, \dot{\delta}_e,\delta_r, \dot{\delta}_r\right)\\
    Z &= f_3\left(u, \dot{u}, v, \dot{v}, w, \dot{w},   p, \dot{p}, q, \dot{q}, r, \dot{r},\delta_a, \dot{\delta}_a, \delta_e, \dot{\delta}_e,\delta_r, \dot{\delta}_r\right)\\
    L &= f_4\left(u, \dot{u}, v, \dot{v}, w, \dot{w},   p, \dot{p}, q, \dot{q}, r, \dot{r},\delta_a, \dot{\delta}_a, \delta_e, \dot{\delta}_e,\delta_r, \dot{\delta}_r\right)\\
    M &= f_5\left(u, \dot{u}, v, \dot{v}, w, \dot{w},   p, \dot{p}, q, \dot{q}, r, \dot{r},\delta_a, \dot{\delta}_a, \delta_e, \dot{\delta}_e,\delta_r, \dot{\delta}_r\right)\\
    N &= f_6\left(u, \dot{u}, u, \dot{w}, w, \dot{w},   p, \dot{p}, u, \dot{r}, r, \dot{r},\delta_e, \dot{\delta}_e, \delta_r, \dot{\delta}_r,\delta_a, \dot{\delta}_a\right)\end{aligned}$$

Simple expressions for $f_1$ through $f_6$ can be adopted for simple cases (I have an example of this in the previous notes but haven't converted to online yet). There are clearly more complex ways to model aircraft, so the representation above is used as a generality. The method used to linearise the external forces and moments is to represent them by a Taylor series expansion:

```{admonition} *Hopefully* revision - Taylor Series:

Let $f(x)$ be a function having derivatives of all orders in the interval $(a-\delta)<x<(a+\delta)$ surrounding the point $x=a$. If we wish to estimate the value of $f$ at some small perturbation $h$[^3] from $a$ (we require $f(a+h)$), then we use a Taylor series expansion:

$$f(a+h) = f(a) + hf'(a) + \frac{h^2}{2!}f''(a) + \frac{h^3}{3!}f'''(a)+\ldots$$
```
[^3]: $|h|<\delta$

## Linearisation of the Aerodynamic Force and Moment Perturbations

This methodology can be readily extended into a multivariable problem. The perturbations of the external forces and moments, $\Delta X\ldots \Delta N$ are desired, and it is required to know value of these variables at the equilibrium/trim state, $X_0\ldots N_0$. The $\Delta X$ are equivalent to the $f(a)$, and the $X+\Delta X$ are equivalent to $f(a+h)$. The Taylor series expansion for the problem can be written to give, in the $x$-direction:

$$\newcommand{\pd}[2]{\frac{\partial#1}{\partial#2}}$$
$$\newcommand{\ppd}[2]{\frac{\partial^2#1}{\partial#2^2}}$$
$$\newcommand{\pppd}[2]{\frac{\partial^3#1}{\partial#2^3}}$$
$$\begin{split}{X_0} + \Delta X = {X_0} + &\left[\pd{X}{u}{u} + \ppd{X}{u}\frac{u^2}{2!} + \pppd{X}{u}\frac{u^3}{3!} + \ldots\right] +\ldots \\ &\left[\pd{X}{\dot{u}}{\dot{u}} + \ppd{X}{\dot{u}}\frac{\dot{u}^2}{2!} + \pppd{X}{\dot{u}}\frac{\dot{u}^3}{3!} + \ldots\right] +\ldots\\ &\left[\pd{X}{v}{v} + \ppd{X}{v}\frac{v^2}{2!} + \pppd{X}{v}\frac{v^3}{3!} + \ldots\right] + \ldots\\ & \hspace{3cm}\vdots \\ &\left[\pd{X}{\dot{\delta_r}}{\dot{\delta_r}} + \ppd{X}{\dot{\delta_r}}\frac{\dot{\delta_r}^2}{2!} + \pppd{X}{\dot{\delta_r}}\frac{\dot{\delta_r}^3}{3!} + \ldots\right] \end{split}$$(eq:taylorX)

Clearly the the trim term $X_0$ cancels from each side, and it is noted that second and higher order derivatives are, in general, negligible so Eq {eq}`eq:taylorX` may be written as.

$$\Delta X = \pd{X}{u}u + \pd{X}{\dot{u}}\dot{u} + \pd{X}{v} + \ldots + \pd{X}{\dot{\delta_a}}$$

Where the partial derivatives _are_ the **aerodynamic** or **stability derivatives**, and denote the aircraft response to perturbations about a trim state. The derivatives **must be evaluated at the point at which the expansion was defined** which for the general Taylor series was $x=a$, but for the aircraft problem is the equilibrium state. In other words, the terms $\pd{X}{u}$ will be a function of the individual trim state, and hence the expansion is only valid if the derivatives have the correct value for the relevant trim state. This is denoted by writing each with a subscript $_0$ so the full set of force and moment perturbations are:

$$\newcommand{\dd}[2]{\left.\pd{#1}{#2}\right|_0#2~+~\left.\pd{#1}{\dot{#2}}\right|_0\dot{#2}}~$$
$$\newcommand{\allderivs}[1]{\begin{split}& \dd{#1}{u}~+ &&\dd{#1}{v} + &&&\dd{#1}{w}\\& \dd{#1}{p}~+ &&\dd{#1}{q}~+ &&&\dd{#1}{r}\\& \dd{#1}{\delta_a}~+ &&\dd{#1}{\delta_e}~+ &&&\dd{#1}{\delta_r}\end{split}}$$
$$\Delta X = \allderivs{X}$$(eq:deriv1)

$$\Delta Y = \allderivs{Y}$$(eq:deriv2)

$$\Delta Z = \allderivs{Z}$$(eq:deriv3)

$$\Delta L = \allderivs{L}$$(eq:deriv4)

$$\Delta M = \allderivs{M}$$(eq:deriv5)

$$\Delta N = \allderivs{N}$$(eq:deriv6)

The partial derivatives in Equation {eq}`eq:deriv1` through {eq}`eq:deriv6` are known as the **stability derivatives**. The terms that have a control deflection in the denominator may sometimes be referred to as the **control derivatives**.

### Reducing the number of aerodynamic derivatives

Equations {eq}`eq:deriv1` through {eq}`eq:deriv6`, have six states ($u, v, w, p, q, r$) and three control variables ($\delta_e, \delta_a, \delta_r$ - and we could easily add more, consider flaps, thrust, thrust vectoring _etc._). 

In total this gives 18 aerodynamic derivatives for each equation, meaning 108 total aerodynamic derivatives. This would be unwieldy to manipulate. 

Through inspection of the equations, they may be simplified. The $\left.\vphantom{\pd{X}{\dot{u}}}\right|_0$ is dropped for clarity
(assmption:cross-coupling)=
#### Cross-coupling

For any condition of symmetric flight (that constrained to the $x/z$ plane), the asymmetric forces and moments ($Y,L,N$) have to be zero. Hence the derivatives of the asymmetric variables ($Y,L,N$) with respect to the symmetric variables and their derivatives ($u, \dot{u}, w, \dot{w}, q, \dot{q}, \delta_e, \dot{\delta_e}$) are zero:

$$\newcommand{\symmetricderivs}[1]{\pd{#1}{u} = \pd{#1}{\dot{u}} = \pd{#1}{w} = \pd{#1}{\dot{w}} = \pd{#1}{q} = \pd{#1}{\dot{q}} = \pd{#1}{\delta_e} = \pd{#1}{\dot{\delta_e}}}$$
$$\begin{split}\symmetricderivs{Y}\\\symmetricderivs{L}\\\symmetricderivs{N}\end{split} =0$$

It follows that the inverse relationship is also true, also, and the derivatives of the symmetric forces and moments ($X,Z,M$) with respect to the asymmetric variables and their derivatives ($v, \dot{v}, p, \dot{p}, r, \dot{r}, \delta_a, \dot{\delta_a},\delta_r, \dot{\delta_r}$) are also zero:

$$\newcommand{\asymmetricderivs}[1]{\pd{#1}{v} = \pd{#1}{\dot{v}} = \pd{#1}{p} = \pd{#1}{\dot{p}} = \pd{#1}{r} = \pd{#1}{\dot{r}} = \pd{#1}{\delta_a} = \pd{#1}{\dot{\delta_a}} = \pd{#1}{\delta_r} = \pd{#1}{\dot{\delta_r}}}$$

$$\begin{split}\asymmetricderivs{X}\\\asymmetricderivs{Z}\\\asymmetricderivs{M}\end{split} =0$$

#### Accelerations

It has been found through experiment that **all derivatives with respect to an acceleration are negligible *except*** $\pd{M}{\dot{w}}$:

$$\newcommand{\accelerationderivatives}[1]{\pd{#1}{\dot{u}} = \pd{#1}{\dot{v}} = \pd{#1}{\dot{w}} = \pd{#1}{\dot{p}} = \pd{#1}{\dot{q}} = \pd{#1}{\dot{r}}}$$
$$\newcommand{\accelerationderivativesw}[1]{\pd{#1}{\dot{u}} = \pd{#1}{\dot{v}} = \pd{#1}{\dot{p}} = \pd{#1}{\dot{q}} = \pd{#1}{\dot{r}}}$$

$$\begin{split}\accelerationderivatives{X}\\\accelerationderivatives{Y}\\\accelerationderivatives{Z}\\\accelerationderivatives{L}\\\accelerationderivativesw{M}\\\accelerationderivatives{N}\end{split}=0$$

#### The control rate derivatives are all negligible

$$\newcommand{\controlratederivatives}[1]{\pd{#1}{\dot{\delta}_a} + \pd{#1}{\dot{\delta}_e} + \pd{#1}{\dot{\delta}_r}}$$
$$\begin{split}\controlratederivatives{X}\\\controlratederivatives{Y}\\\controlratederivatives{Z}\\\controlratederivatives{L}\\\controlratederivatives{M}\\\controlratederivatives{N}\end{split}=0$$

#### Through experiment, it has been shown that the following derivatives may also be neglected:

$$\pd{X}{q}   = \pd{X}{{\delta_e}} =\pd{Y}{p} = \pd{Y}{r}= \pd{Y}{\delta_a} = 0$$

### Reduced derivative force and moment perturbations:

**So the perturbation forces and moments now become:**

$$\Delta X = \left.\pd{X}{u}\right|_0u + \left.\pd{X}{w}\right|_0w$$(eq:linforce1)
$$\Delta Y = \left.\pd{Y}{v}\right|_0v + \left.\pd{Y}{\delta_r}\right|_0\delta_r$$(eq:linforce2)
$$\Delta Z = \left.\pd{Z}{u}\right|_0u + \left.\pd{Z}{w}\right|_0w + \left.\pd{Z}{\delta_e}\right|_0\delta_e$$(eq:linforce3)
$$\Delta L = \left.\pd{L}{v}\right|_0v + \left.\pd{L}{p}\right|_0p + \left.\pd{L}{r}\right|_0r + \left.\pd{L}{\delta_r}\right|_0\delta_r + \left.\pd{L}{\delta_a}\right|_0\delta_a$$(eq:linforce4)
$$\Delta M = \left.\pd{M}{u}\right|_0u + \left.\pd{M}{w}\right|_0w + \left.\pd{M}{\dot{w}}\right|_0\dot{w} + \left.\pd{M}{q}\right|_0q + \left.\pd{M}{\delta_a}\right|_0\delta_a$$(eq:linforce5)
$$\Delta N = \left.\pd{N}{v}\right|_0v + \left.\pd{N}{p}\right|_0p + \left.\pd{N}{r}\right|_0r + \left.\pd{N}{\delta_r}\right|_0\delta_r + \left.\pd{N}{\delta_a}\right|_0\delta_a$$(eq:linforce6)
    
#### Physical Significance of the Stability Derivatives

The above is, in one sense, a mathematical formulation that has enabled us to write the equations of motion. The derivatives above, though, are significant in that they represent the aircraft response to small perturbations around a trim state.

That is, the derivatives are _just numbers_ for an aircraft, collected either through numerical simulation (which you'll have done some of in XFLR5), or through wind tunnel data whereby the aircraft is moved through a range of angles and rates, and the change to the forces and moments are measured.

As a consequence, it will be restated here that the derivatives are only valid for the point at which they have been evaluated. That is, each derivative will change with the given trim state - and, as such, a function of thins like forward speed, Mach number, angle of attack, aircraft configuration, and many more things.

If, for example, the linearised equations of motion are being used to assess the stability of an aircraft at a flight speed of 200kn, then it is the values of $u,v,w,q,p,r$ at a trimmed speed of 200kn which are used to calculate the derivatives, yielding values of the derivatives in the equation above that are specific to that speed/attitude.


### Linearised Equations of Motion in Dimensional Form

The **linear force and moment perturbations**, Eqs {eq}`eq:linforce1`-{eq}`eq:linforce6`, may be substituted into the **linear equations of motion**, Eqs. {eq}`eq:lineq1` through {eq}`eq:lineq6` to arrive at:

$$\color{red}{m\dot{u}= \left.\pd{X}{u}\right|_0u + \left.\pd{X}{w}\right|_0w - mg\cdot\cos\theta_0\cdot\theta^\prime}$$(eq:dimensional1)

$$\color{darkgreen}{m\dot{v}=\left.\pd{Y}{v}\right|_0v - mU_0r+mg\cdot cos\theta_0\cdot\phi^\prime\left.\pd{Y}{\delta_r}\right|_0\delta_r}$$(eq:dimensional2)

$$\color{red}{m\dot{w}= \left.\pd{Z}{u}\right|_0u + \left.\pd{Z}{w}\right|_0w + mU_0q - mg\cdot\sin\Theta_0\cdot\theta^\prime + \left.\pd{Z}{\delta_e}\right|_0\delta_e}$$(eq:dimensional3)

$$\color{darkgreen}{I_{xx}\dot{p} - I_{xz}\dot{r} = \left.\pd{L}{v}\right|_0v + \left.\pd{L}{p}\right|_0p+\left.\pd{L}{r}\right|_0r+\left.\pd{L}{\delta_r}\right|_0\delta_r+\left.\pd{L}{\delta_a}\right|_0\delta_a}$$(eq:dimensional4)

$$\color{red}{I_{yy}\dot{q} = \left.\pd{M}{u}\right|_0u+\left.\pd{M}{w}\right|_0w+\left.\pd{M}{\dot{w}}\right|_0\dot{w}+\left.\pd{M}{q}\right|_0q+\left.\pd{M}{\delta_e}\right|_0\delta_e}$$(eq:dimensional5)

$$\color{darkgreen}{I_{zz}\dot{r}-I_{xz}\dot{p} = \left.\pd{N}{v}\right|_0v+ \left.\pd{N}{p}\right|_0p + \left.\pd{N}{r}\right|_0r +  \left.\pd{N}{\delta_r}\right|_0\delta_r+ \left.\pd{N}{\delta_a}\right|_0\delta_a}$$(eq:dimensional6)

Equations {eq}`eq:dimensional1` through {eq}`eq:dimensional6` represent the **dimensional linear equations of motion**, with the <span style="color:red">first, third, and fifth</span> equations being <span style="color:red">**symmetric**</span> (flight constrained to X-Z plane) and the <span style="color:green">second, fourth, and sixth</span> equations being <span style="color:green">**asymmetric**</span>.




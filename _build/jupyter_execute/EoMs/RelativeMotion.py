# Absolute Acceleration

In deriving the equations of motion, we use Newton's Second Law as the basis for equating force and the rate of change of both translational and angular momentum:

$$\sum\vec{F}=m\cdot a_{abs}$$

where $a_{abs}$ is the absolute acceleration that defined in an inertial reference frame. Body axes velocities and displacements may be converted to absolute quantities via the Euler angle translation, but accelerations may not be treated as such, owing to the relative motion of the body axes with respect to the earth axes. Stated another way, the body accelerations are not absolute:

$$\begin{aligned}
    \sum F_x\neq m\cdot\dot{U}\\
    \sum F_y\neq m\cdot\dot{V}\\
    \sum F_z\neq m\cdot\dot{W}\end{aligned}$$

This may be demonstrated with a counterexample - an aircraft flying in a loop - see Figure {numref}`SimpleLoop`.

```{figure} ../Images/SimpleLoop.png
---
height: 600px
name: SimpleLoop
---
Aircraft flying in a loop
```


From basic physics, we know that for steady motion in a circle of radius $r$ with angular velocity $\Omega$, the centripetal (centre seeking) acceleration is:

$$a_c = r\cdot\omega^2$$

and that the tangential velocity, which in this case is equal to the aircraft $u$ velocity i

$$\begin{aligned}
    U &= r\cdot\omega\\
    \implies r&=\frac{U}{\omega}\end{aligned}$$
    
which, if we substitute into our expression for centripetal acceleration and recognise that for this example, the angular rate $\omega$ is equal to the body rotation rate around the $y$ axis:

$$a_c = Q\cdot U$$

which gives us an apparent acceleration along the body $z$ axis due to angular rotation, which is to be added to the local acceleration:

$$a_z = \dot{W} - Q\,U = \sum\frac{F_z}{m}$$

If we were to include terms because of all three body rates (you'd have to draw a similar example for a yaw rate - or wait until you've got the Coriolis identity), we would see that:

$$a_z = \dot{W} - Q\,U + R\,V$$

We can see that **absolute acceleration is the sum of translational acceleration AND the vector product of angular and translational rates**. Whenever we have rotation, we cannot simply treat absolute acceleration as the time derivative of velocities. In the following section, we'll develop a methodology to treat this formally.

## Relative Motion: General Form

The extra terms arise because the aircraft axes are moving with respect to earth axes; body axes are a non inertial reference frame and (for our purposes) earth axes *are*. You are probably able to intuit some of these terms - such as the *centrifugal force* that is perceived in a rotating reference frame due to angular translation. We'll develop a mathematical formulation to show the following

$$\begin{aligned}
    \left.\frac{d\ddagger}{dt}  \right|_{abs} &= \left.\frac{d\ddagger}{dt} \right|_{Oxyz} + \vec{\omega}\times\ddagger\end{aligned}$$ (eq:coriolis1)

and

$$\left.\frac{d^2\ddagger}{dt^2}  \right|_{abs} = \left.\frac{d^2\ddagger}{dt^2}\right|_{Oxyz} + \dot{\vec{\omega}} \times\ddagger + 2\cdot\vec{\omega}\times\left.\frac{d\ddagger}{dt}\right|_{Oxyz}+\vec{\omega}\times\left(\vec{\omega}\times\ddagger\right)$$ (eq:coriolis2)

where {eq}`eq:coriolis1` and {eq}`eq:coriolis2` are the first and second order Coriolis identities. $\ddagger$ is a vector quantity relating to translational motion. So, to yield absolute acceleration the *absolute velocity* can be used as $\ddagger$ in {eq}`eq:coriolis1` or the *absolute* position can be used in {eq}`eq:coriolis2`. $()_{abs}$ refers to absolute quantities, which is what we need for Newton's second law, whilst $\left.\frac{\text{d}()}{\text{d}t}\right|_{Oxyz}$ refers to differentiation in a non-inertial reference frame.

Equations {eq}`eq:coriolis1` and {eq}`eq:coriolis2` tend just be given to the engineering student without a derivation, and I *hate* that sort of instruction since it doesn't help learning or understanding, just parroting.

How will {eq}`eq:coriolis1` and {eq}`eq:coriolis2` be determined? Well we know that the effects are related to rotation of a non-inertial reference frame within an inertial one, and some rotation. So that looks like a good place to start.

$$\def\ii{\hat{\boldsymbol{\imath}}}$$
$$\def\jj{\hat{\boldsymbol{\jmath}}}$$
$$\def\kk{\hat{\boldsymbol{k}}}$$

### General position and velocity vectors in unit vector form

The general expressions for position and velocity are, as defined in a non-inertial reference frame (_e.g.,_ aircraft body axes)

$$\vec{r}=\begin{bmatrix}x\\y\\z\end{bmatrix}$$ (eq:genpos)
$$\vec{V}=\begin{bmatrix}U\\V\\W\end{bmatrix}$$ (eq:genvel)

The derivation can be performed using either. Taking Equation {eq}`eq:genpos` and writing in unit vector form:

$$\vec{r}=x\,\ii + y\,\jj + z\,\kk$$

and the first derivative can then be written, using the product rule - noting that $\dot{()}$ denote *absolute derivative*.

$$\dot{\vec{r}}=\begin{split}\dot{x}\,\ii + \dot{y}\,\jj + \dot{z}\,\kk\\x\,\dot{\ii} + y\,\dot{\jj} + z\,\dot{\kk}\end{split}$$ (eq:genfirstderiv)

The terms $\dot{x}, \dot{y}, \dot{z}$ are easy to intuit their meaning - these refer to any change in the vector in the non-inertial reference frame. The second set of terms $\dot{\ii}, \dot{\jj}, \dot{\kk}$ are slightly less instructive. These refer to an _apparent derivative_ that arises due to angular motion; if the original vector is $\vec{r}$, then these are an apparent velocity. If the vector is $\vec{V}$ then these are an apparent acceleration.

Since these are caused by angular rates $\vec{\omega}=[P,Q,R]^T$, the effect of each of these rates can be explored on the unit vectors in time $\Delta t$ - the limit of this change as $\Delta t\rightarrow 0$ will give expressions for $\dot{\ii}, \dot{\jj}, \dot{\kk}$.

Since $P$, $Q$, and $R$ are all defined as rotations about body axes they can be explored independently as three Euler rotations - sequence is irrelevant here.

```{warning} Why does sequence matter for $\psi$, $\theta$, $\psi$, but not for $P$, $Q$, and $R$?
The Euler angles $\psi$, $\theta$, $\psi$ are defined in three different axes sets, earth, intermediate 1, and intermediate 2. None of these angles can be assumed small.

The body rates $P$, $Q$, and $R$ are all defined in body axes and furthermore the angular distance covered in time $\Delta t$ will be small.
```

If the unit vectors can be written as

$$\vec{\boldsymbol{I}}=[\ii, \jj, \kk]^T$$

then 

$$\dot{\vec{\boldsymbol{I}}} = \lim_{\Delta t\rightarrow 0}\frac{\Delta\vec{\boldsymbol{I}}}{\Delta t}$$

and the total change to $\vec{\boldsymbol{I}}$ is the sum of the changes due to the three angular rates

$$\Delta\vec{\boldsymbol{I}}=\Delta\vec{\boldsymbol{I}}_P + \Delta\vec{\boldsymbol{I}}_Q + \Delta\vec{\boldsymbol{I}}_R$$ (eq:dIcomponents)

and all of the RHS components in {eq}`eq:dIcomponents` can be determined from Euler transforms. Consider each rotation as a movement from $\vec{\boldsymbol{I}}$ to $\vec{\boldsymbol{I}}^\prime$. The diagrams three Euler transforms are given below:


#### $\Delta\vec{\boldsymbol{I}}_P$ - change to unit vectors due to body roll, $P$

The angular displacement during time $\Delta t$ due to body roll rate is $P\Delta t$:

```{figure} ../Images/EulerdRoll.png
---
height: 300px
name: EulerdRoll
---
Change to unit vectors due to roll rate $P$
```
where 

$$\begin{alignat}{2}
	\ii^\prime &=&&\ii\\
	\jj^\prime &=&&\jj\cdot\cos(P\Delta t) + \kk\cdot\sin(P\Delta t)\\
	\kk^\prime &=-&&\jj\cdot\sin(P\Delta t) + \kk\cdot\cos(P\Delta t)
\end{alignat}$$

since ultimately the derivative will be given by looking at the limit as $\displaystyle \lim_{\Delta t \to 0}$, the small angle assumption is justified

$$\begin{alignat}{2}
    \ii^\prime &=\ii\\
	\jj^\prime &=\jj + \kk\cdot(P\Delta t)\\
	\kk^\prime &=-\jj\cdot(P\Delta t) + \kk
\end{alignat}$$

and thus we can define the $\Delta\hat{\mathbf{I}}$ due to roll rate:

$$\Delta\vec{\boldsymbol{I}}_P=\begin{bmatrix}\Delta\ii_P\\\Delta\jj_P\\\Delta\kk_P \end{bmatrix} = \begin{bmatrix}\ii^\prime-\ii\\\jj^\prime-\jj\\\kk^\prime-\kk\end{bmatrix} =  \begin{bmatrix}0\\\kk\cdot(P\Delta t)\\-\jj\cdot(P\Delta t)\end{bmatrix}$$

#### $\Delta\vec{\boldsymbol{I}}_P$ - change to unit vectors due to body pitch, $Q$

```{figure} ../Images/EulerdPitch.png
---
height: 400px
name: EulerdPitch
---
Change to unit vectors due to pitch rate $Q$
```

similarly 

$$\begin{alignat}{2}
	\ii^\prime &=\ii\cdot\cos(q\Delta t) - \kk\cdot\sin(Q\Delta t)\\
	\jj^\prime &=\jj\\
	\kk^\prime &=\ii\cdot\sin(q\Delta t) + \kk\cdot\cos(Q\Delta t)
\end{alignat}$$

again, small angle

$$\begin{alignat}{2}
	\ii^\prime &=\ii - \kk\cdot(Q\Delta t)\\
	\jj^\prime &=\jj\\
	\kk^\prime &=\ii\cdot(Q\Delta t) + \kk
\end{alignat}$$

and thus we can define the $\Delta\hat{\mathbf{I}}$ due to pitch rate:

$$\Delta\vec{\boldsymbol{I}}_Q=\begin{bmatrix}\Delta\ii_Q\\\Delta\jj_Q\\\Delta\kk_Q \end{bmatrix} = \begin{bmatrix}\ii^\prime-\ii\\\jj^\prime-\jj\\\kk^\prime-\kk\end{bmatrix} =  \begin{bmatrix}- \ii\cdot(Q\Delta t)\\0\\\kk\cdot(Q\Delta t)\end{bmatrix}$$

#### $\Delta\vec{\boldsymbol{I}}_P$ - change to unit vectors due to body yaw, $R$


```{figure} ../Images/EulerdYaw.png
---
height: 400px
name: EulerdYaw
---
Change to unit vectors due to yaw rate $R$
```

similarly 

$$\begin{alignat}{2}
	\ii^\prime &=\ii\cdot\cos(R\Delta t) + \jj\cdot\sin(R\Delta t)\\
	\jj^\prime &=- \ii\cdot\sin(R\Delta t)+\jj\cdot\cos(R\Delta t) \\
	\kk^\prime &=\kk
\end{alignat}$$

again, small angle

$$\begin{alignat}{2}
	\ii^\prime &=\ii + \jj\cdot(R\Delta t)\\
	\jj^\prime &=\jj - \ii\cdot(R\Delta t)\\
	\kk^\prime &=\kk
\end{alignat}$$

and thus we can define the $\Delta\hat{\mathbf{I}}$ due to yaw rate:

$$\Delta\vec{\boldsymbol{I}}_R=\begin{bmatrix}\Delta\ii_R\\\Delta\jj_R\\\Delta\kk_R \end{bmatrix} = \begin{bmatrix}\ii^\prime-\ii\\\jj^\prime-\jj\\\kk^\prime-\kk\end{bmatrix} =  \begin{bmatrix}\ii\cdot(R\Delta t)\\-\jj\cdot(R\Delta t)\\0\end{bmatrix}$$

#### Total change

The total change is the sum of all three angular components, *i.e.,*

$$\begin{align}
	\Delta\hat{\textbf{I}}&=\Delta\hat{\textbf{I}}_p + \Delta\hat{\textbf{I}}_q + \Delta\hat{\textbf{I}}_r = \begin{matrix} 0-k\cdot (q\Delta t) + \jj\cdot(r\Delta t)\\ k\cdot(p\Delta t) + 0 - \ii\cdot(r\Delta t)\\-\jj\cdot(p\Delta t) + \ii\cdot(q\Delta t) + 0 \end{matrix}\\
	&=  \Delta t\begin{bmatrix} \jj R  - \kk Q\\-\ii R + \kk P \\ \ii Q - \jj P \end{bmatrix}
\end{align}$$

So the apparent motion due to combined angular rates may now be written

$$\begin{equation}
	\dot{\hat{\mathbf{I}}}=\lim_{\Delta t \to 0}	 \frac{\Delta\hat{\textbf{I}}}{\Delta t}=\begin{matrix} \jj R  - \kk Q\\-\ii R + \kk P \\ \ii Q - \jj P \end{matrix}
\end{equation}$$

which, in vector form may be written

$$\begin{equation}
	\begin{bmatrix}\dot{\ii}\\\dot{\jj}\\\dot{\kk}\end{bmatrix}=-\vec{\omega}\times\begin{bmatrix}\ii\\\jj\\\kk\end{bmatrix}\label{eq:Idot}
\end{equation}$$

although the cross product above won't be used right here, it serves to show that the apparent velocity terms comprise cross-couplings.

Now all the terms in Equation {eq}`eq:genfirstderiv` can be expressed in terms of basis vectors and angular rates. So:

$$\begin{align}
	&\begin{split}\dot{\vec{r}}=&\hspace{.5cm}\dot{x}{\ii} + \dot{y}{\jj} + \dot{z}\kk+\ldots\\
		&\hspace{.5cm}{x}\dot{{\ii}} + {y}\dot{{\jj}} + {z}\dot{\kk}\hphantom{+\ldots}	
	\end{split}\end{align}$$
    
may now be populated
    
$$\begin{align}
	&\begin{split}\dot{\vec{r}}=&\hspace{.5cm}\dot{x}\,{\ii} + \dot{y}\,{\jj} + \dot{z}\,{\kk}+\ldots\\
		&\hspace{.5cm}{x}\cdot\left[R\jj - Q\kk\right]+\ldots\\
		&\hspace{.5cm}{y}\cdot\left[P\kk - R\ii\right]+\ldots\\
		&\hspace{.5cm}{z}\cdot\left[Q\ii - P\jj\right]\\	
	\end{split}
\end{align}
$$

and in vector form:

$$\begin{align}
	&\begin{split}
		=&\hspace{.5cm}\begin{matrix} \dot{x} - r\cdot y + q\cdot z \\\dot{y} + r\cdot x - p\cdot z\\\dot{z} - q\cdot x + p\cdot y\end{matrix}
	\end{split}
\end{align}
$$

which may be written as 

$$\left.\dot{r}\right|_{abs}=\hspace{.5cm} \left.\frac{d\vec{r}}{dt}\right|_{Oxyz} + \vec{\omega}\times\vec{r}$$

which in general form is

$$\begin{aligned}
    \left.\frac{d\ddagger}{dt}  \right|_{abs} &= \left.\frac{d\ddagger}{dt} \right|_{Oxyz} + \vec{\omega}\times\ddagger\end{aligned}$$ (eq:coriolis1)
    
the first order Coriolis identity - and can be used to yield absolute acceleration from a velocity vector, or absolute velocities from a position vector.

Sometimes the second order Coriolis identity is required, as we'll see - and there are two ways of yielding it:
1. Differentiate Equation {eq}`eq:genfirstderiv` again and yield the following, Eqn {eq}`eq:gensecondderiv`.Then get the $\ddot{\hat{\textbf{I}}}$ terms by substituting  $\dot{\hat{\textbf{I}}}$ into Eqn {eq}`eq:coriolis1`, then populating Eqn {eq}`eq:gensecondderiv` turning into matrix form
2. The second way is a little easier - you can basically substitute Eqn {eq}`eq:coriolis1` into itself.

$$\begin{align}
	\begin{split}
			\ddot{\vec{r}} =& \ddot{x}\cdot\ii + \ddot{y}\cdot\jj + \ddot{z}\cdot\kk + \ldots\\
			& 2\left(\dot{x}\cdot\dot{\ii} + \dot{y}\cdot\dot{\jj} + \dot{z}_a\cdot\dot{\kk}\right)+\ldots\\
			& x\cdot\ddot{\ii} + y\cdot\ddot{\jj} + z\cdot\ddot{\kk}
	\end{split}
\end{align}$$ (eq:gensecondderiv)

Try either way - both ways you should yield

$$\left.\frac{d^2\ddagger}{dt^2}\right|_{abs}=\left.\frac{d^2\ddagger}{dt^2}\right|_{Oxyz} + \dot{\vec{\omega}} \times\ddagger + 2\cdot\vec{\omega}\times\left.\frac{d\ddagger}{dt}\right|_{Oxyz}+\vec{\omega}\times\left(\vec{\omega}\times\ddagger\right)$$

which is the second order Coriolis identity

## Relative Motion of a point on the aircraft

In the general form of relative motion derived in the preceding section. We can use a relative motion approach to derive expressions for the absolute aircraft velocities based on data measured at a location away from the aircraft centre of gravity.

```{figure} ../Images/AirDataProbe.png
---
height: 600px
name: figADP
---
Air data probe in aircraft axes
```

Consider an aircraft with a co-ordinate system located at its centre of mass, and an air data probe located on a the nose at location $\vec{r}_{p/a}=\left[x_p,y_p,z_p\right]^T_b$, measured in body axes, Figure {ref}`figADP`. Since this the location in body axes, the position vector is the relative position of the probe to aircraft axes.

That is, if the aircraft position is $\vec{r}_a$ in the absolute reference frame, the the absolute position of the probe is

$$\vec{r}_{p} = \vec{r}_a + \vec{r}_{p/a}$$ 

The air data probe measures angle of attack, sideslip, and total velocity - all at the location of the probe. From what we have learned about relative motion, we know that these will not be the same as those for the aircraft centre of mass, so we need a means to convert these measured values back to aircraft absolute velocities - for use in Flight Mechanics. We denote the quantities measured at the probe as $\alpha_p, \beta_p, V_{fp}$, and what we desire is $U,V,W,V_f,\alpha,\beta$.

Expressions are required for the absolute velocity as measured at the probe, so we start with the vector expression for the absolute position of the probe (its position in earth axes).

$$\vec{r}_p = \vec{r}_a + \vec{r}_{p/a}$$

the absolute velocity is the time derivative of this

$$\dot{\vec{r}}_p = \dot{\vec{r}}_a + \dot{\vec{r}}_{p/a}$$


the first term above is simply the aircraft absolute velocity, $\vec{V}_a=\left[u,v,w\right]^T$, and the second term we get from the Coriolis identity

$$\def\dif{\text{d}}$$
$$\dot{\vec{r}}_{p/a} =\frac{\dif{\vec{r}}_{p/a}}{\dif t} + \vec{\omega}\times\dot{\vec{r}}_{p/a} =  \begin{bmatrix}\dot{x}_p\\\dot{y}_p\\\dot{z}_p\end{bmatrix} \vec{\omega}\times\dot{\vec{r}}_{p/a}$$

where the first set of terms represents and change in the probe position in aircraft axes

$$\begin{aligned}\dot{\vec{r}}_p = \begin{bmatrix}U_p\\V_p\\W_p\end{bmatrix} &= \begin{bmatrix}U\\V\\W\end{bmatrix} +  \begin{bmatrix}\dot{x}_p\\\dot{y}_p\\\dot{z}_p\end{bmatrix} +  \vec{\omega}\times\vec{r}_{p/a}\\
    &= \begin{bmatrix}U\\V\\W\end{bmatrix} +  \begin{bmatrix}\dot{x}_p\\\dot{y}_p\\\dot{z}_p\end{bmatrix} +\left|\begin{matrix}i & j & k \\ P & Q & R \\x_p & y_p & z_p\end{matrix}\right|\\
    &= \begin{bmatrix}U + \dot{x}_p + Q\,z_p - R\,y_p\\V + \dot{y}_p + R\,x_p - P\,z_p\\W + \dot{z}_p +P\,y_p - Q\,x_p \end{bmatrix}\end{aligned}$$
    
rearranging for the aircraft absolute velocities gives

$$\begin{bmatrix}U\\V\\W\end{bmatrix} = \begin{bmatrix} R\,y_p - Q\,z_p + U_p - \dot{x}_p\\ P\,z_p - R\,x_p + V_p - \dot{y}_p\\Q\,x_p - P\,y_p + W_p - \dot{z}_p  \end{bmatrix}$$

which gives us the aircraft absolute velocity as a function of those measured at the probe, its position, and the aircraft angular rate (which would be measured at a rate gyroscope in the aircraft). However, we do not have $U_p,V_p,W_p$, we have the local aerodynamic angles and the total velocity, so we need to develop expressions for them using the definition of total velocity and the aerodynamic angles

$$\begin{aligned}
    V_{fp}^2 &=U_p^2 + V_p^2 + W_p^2\\
    \sin\beta_p &= \frac{V_p}{V_{fp}}\\
    \tan\alpha_p &= \frac{W_p}{U_p}\\
    \implies V_p &= V_{fp}\cdot\sin\beta_p\\
    \implies U_p &= V_{fp}\sqrt{\frac{1 - \sin^2\beta_p}{1 + \tan^2\alpha_p}}\\
    \implies W_p &= V_{fp}\tan\alpha_p\sqrt{\frac{1 - \sin^2\beta_p}{1 + \tan^2\alpha_p}}
\end{aligned}$$

hence now we may write expressions for the total aircraft velocity

$$\begin{aligned}
    \begin{bmatrix}U\\V\\W\end{bmatrix} &= \begin{bmatrix} R\,y_p - Q\,z_p + V_{fp}\sqrt{\frac{1 - \sin^2\beta_p}{1 + \tan^2\alpha_p}} - \dot{x}_p\\ P\,z_p - R\,x_p + V_{fp}\cdot\sin\beta_p - \dot{y}_p\\Q\,x_p - P\,y_p + V_{fp}\tan\alpha_p\sqrt{\frac{1 - \sin^2\beta_p}{1 + \tan^2\alpha_p}}-\dot{z}_p  \end{bmatrix}\end{aligned}$$

and the aircraft angle of attack may be developed from the standard aerodynamic angle definitions.

The terms $\dot{\vec{r}}_{p/a}=\left[\dot{x}_p, \dot{y}_p, \dot{z}_p\right]^T$ represent a velocity due to any change in position of the probe in aircraft axes - that is due to _aircraft flexibility_.


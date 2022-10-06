# Dynamic Stability

In this course, the equations of motion have been developed in a Newtonian framework - these, in conjunction with the relationship between body rates and the time rate of change of the Euler angles, allow us to describe full unconstrained flight of a six degree of freedom aircraft.

Regarding static stability, some basic *static stability* properties of fixed-wing aircraft were explored - what the immediate tendency of the aircraft is following a disturbance from trim. In the previous module we developed the equations of motion into two sets of uncoupled linearised equations of motion, representing the longitudinal and lateral/directional motions of fixed wing aircraft.

In this final module, we look at the *dynamic* stability characteristics of an aircraft - how the aircraft actually responds with time, and how the response to basic pilot inputs may be determined. The stability of any dynamic system is governed by consideration of its free (unforced) motion. Its *response* to an input (an aircraft control) is determined by the response of the system to forcing.

A simple example that helps us understand dynamic systems is the mass/spring/damper system as shown:

```{figure} ../Images/MassSpringDamper.png
---
height: 300px
name: fig:massspringdamper
---
Mass Spring Damper System
```

This system is governed by the equation of motion:

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

where $x$ is the displacement, $m$ is the mass, $c$ is the damping, $k$ is the spring stiffness, and $F(t)$ is the input forcing. For free motion, $F(t)=0$:

$$m\ddot{x} + c\dot{x} + kx = 0$$

which we can represent as:

$$\ddot{x} + 2\zeta\omega_n\dot{x} + \omega_n^2 = 0$$(eq:massspringdamper)

where $\omega_n$ is the undamped natural frequency of the system ($=\sqrt{\frac{k}{m}}$ for this case) and $\zeta$ is the damping ratio of the system ($=\frac{c}{2\sqrt{km}}$ for this case).

The stability of this system is given by solution of Eq {eq}`eq:massspringdamper` directly. The general solution  is found by assuming that the solution will have the form $x=Ae^{\lambda_t}$, hence $\dot{x}=A\lambda e^{\lambda t}, \ddot{x} = A\lambda^2 e^{\lambda t}$. Substitution of this into Equation {eq}`eq:massspringdamper` yields the *characteristic equation*:

$$\lambda^2 + 2\zeta\omega_n\lambda + \omega_n^2 = 0$$(eq:msdCE)

the roots of which are

$$\lambda = \omega_n\left(-\zeta \pm \sqrt{-\zeta^2-1}\right)$$(eq:msdEig)

by superposition, the general solution is

$$\begin{aligned}
    x(t) &= A_1\cdot e^{\lambda_1t} + A_2\cdot e^{\lambda_2t}\\
    x(t) &= A_1\cdot e^{\omega_n\left(-\zeta + \sqrt{-\zeta^2-1}\right)\cdot t} + A_2\cdot e^{\omega_n\left(-\zeta - \sqrt{-\zeta^2-1}\right)\cdot t}\end{aligned}$$(eq:dampedgeneral)

where

$$\omega_d = \text{ the damped natural frequency } = \omega_n\sqrt{1-\zeta^2}$$

Because $0\leq\zeta\leq\infty$, the *radicand* may be positive, negative, or zero. These three possibilities give rise to three different types of damped motion, and the difference in behaviour may be classified according to the table below


| $\boldsymbol{\zeta}$ | **Type of Motion**  | $\boldsymbol{\lambda_1,\lambda_2}$ | **Motion Characteristics**                                                                                                                                                    |
|:--------------------:|:-------------------:|:----------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         $>1$         |    'Overdamped'     |      Real, negative, distinct      | Motion decays to zero over a period of time, $t$, with zero oscillation.                                                                                                      |
|         $=1$         | 'Critically Damped' |       Real, negative, equal        | Motion decays to zero over a period of time $t$, where $t$ is the shortest possible time to return to equilibrium for this system.                                            |
|         $<1$         |    'Underdamped'    |              Complex               | Motion returns toward, and beyond zero in time $t$ where $t$ is smaller than the time for the critically damped case. Motion will overshoot and exhibit harmonic oscillation. |

different values of $\zeta$ are demonstrated for free vibration of the mass-spring-damper system, with the maxima/minima of the underdamped cases shown, to show the change in the _damped natural frequencies_ of the system. Furthermore, the period of the oscillatory systems are used to show the damped natural frequency which is then compared with the value from the formula. Hopefully this should elucidate the difference between the two sorts of natural frequencies.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-5107176300009857"
     data-ad-slot="7122611277"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

import numpy as np
import plotly.graph_objects as go
import scipy.signal as sig

# Some constants
m = 1 # mass, kg
k = 25 # spring stiffness, Pa
F0 = 0 # Forcing is zero (free vibration)
x0 = 1 # Initial displacement, m

# time vector
t = np.linspace(0, 2, 10000)

# undamped natural frequency
w_n = np.sqrt(k/m)

# make a figure
fig = go.Figure()

# Iterate over zeta values
for Z in [0.1, .2, 0.3, 0.8, 1, 2.5]:
    lam = np.zeros(2, dtype="complex")
    lam[0] = w_n * (-Z + np.sqrt(Z**2 -1, dtype="complex"))
    lam[1] = w_n * (-Z - np.sqrt(Z**2 -1, dtype="complex"))
    
    x = x0 * (0.5 * np.exp(lam[0] * t) + 0.5 * np.exp(lam[1] * t))
    
    # Plot the solution
    fig.add_trace(go.Scatter(x=t, y=x.real,\
        mode='lines',\
        name=f"$\\zeta={Z}$", showlegend=True))
    
    # put the peaks on
    if (Z > 0) and (Z < 0.8):
        high_peaks = sig.find_peaks(x.real)[0]
        fig.add_trace(go.Scatter(x=t[high_peaks], y=x.real[high_peaks], mode="markers", marker_color="blue", showlegend=False))
        low_peaks = sig.find_peaks(-x.real)[0]
        fig.add_trace(go.Scatter(x=t[low_peaks], y=x.real[low_peaks], mode="markers", marker_color="red", showlegend=False))
        
        # Get the damped natural frequencies from these
        wd_figure = 1/(t[low_peaks[1]] - t[low_peaks[0]])
        wd = w_n * np.sqrt(1 - Z**2)
        def Hertz(rad):
            return rad/np.pi/2
        print(f"From the figure the period gives a frequency of {wd_figure:1.2f}Hz for damping ratio of {Z}. For\
 an undamped natural frequency of {Hertz(w_n):1.2f}Hz, this corresponds to a damped natural frequency of {Hertz(wd):1.2f}Hz.\n")

        
fig.update_layout(
    title="$\\text{Free vibration of an initially displaced mass spring damper system for different }\zeta$",
    title_x=0.5,
    xaxis_title="$t/\\text{s}$",
    yaxis_title="$x/\\text{m}$",
)        
fig.show()

Most aircraft problems that we will look at exhibit underdamped motion $\zeta < 1$ and Eq {eq}`eq:dampedgeneral`[^1] can be re-written as:

[^1]: $\sqrt{\zeta^2-1}=i\sqrt{1-\zeta^2}$ and $e^ae^b=e^{(a+b)}$


$$x(t) = \left(A_1e^{i\sqrt{1-\zeta^2}\omega_n t} + A_2e^{-i\sqrt{1-\zeta^2}\omega_nt}\right)e^{-\zeta\omega_nt}$$

we introduce a parameter $\omega_d=\omega_n\sqrt{1-\zeta^2}$, which represents the \textsl{damped natural frequency}, which allows us to express this as
```{margin}
Hint: $\sqrt{\zeta^2-1}=i\sqrt{1-\zeta^2}$ and $e^ae^b=e^{(a+b)}$
```


$$x(t) = \left(A_3\cos\omega_dt + A_4\sin\omega_dt\right)e^{-\zeta\omega_nt}$$(eq:underdampedsimple)

Where $A_3=A_1+A_2$ and $A_4 = A_1-A_2$. Inspection of {eq}`eq:underdampedsimple` shows an oscillation with angular frequency $\omega_d$, and a decaying amplitude with time. This is demonstrated below:



# Some constants
m = 1 # Mass, kg
k = 36 # Stiffness, Pa
F0 = 0 # Free vibration
x0 = 30e-3 # Initial displacement, 30mm
zeta = 0.083 # Damping

# Time vector
t = np.linspace(0, 4, 1000)

# Natural frequency
w_n = np.sqrt(k/m)

# Eigenvalues
lam = np.zeros(2, dtype="complex")
lam[0] = w_n*(-zeta + np.sqrt(zeta**2 - 1, dtype="complex"))
lam[1] = w_n*(-zeta - np.sqrt(zeta**2 - 1, dtype="complex"))

# Amplitudes
A1 = x0/2
A2 = x0/2

# Solution
x = A1*np.exp(lam[0]*t) + A2*np.exp(lam[1]*t)

# Make a figure
fig = go.Figure()

# Plot the absolute value part or plotly cries
fig.add_trace(go.Scatter(x=t, y=x.real,
    mode='lines',
    line_color='indigo', name="Time response", showlegend=True))

# Put the osillatory and non-oscillatory parts (real and imaginary)
A3 = (A1 + A2)
A4 = 1j*(A1 - A2)

w_d = w_n*np.sqrt(1-zeta**2)

# Alternative form - shows the same
x2 = (A3*np.cos(w_d*t) + A4*(w_d*t))*np.exp(-zeta*w_n*t)

fig.add_trace(go.Scatter(x=t[0::10], y=x2[0::10].real,
    mode='markers',
    line_color='indigo', name="Alternative Form", showlegend=True))

#     h2 = plot(t(1:10:end), x2(1:10:end), 'ok');
    
xd = x0*np.exp(-zeta*w_n*t)

# Put the exponential decay (real part)
fig.add_trace(go.Scatter(x=t, y=xd.real,
    mode='lines', line=dict(
        color="LightSeaGreen",
        width=4,
        dash="dashdot",
    ), name="$\pm x_0e^{-\zeta\,\omega_n\,t}$", showlegend=True))
fig.add_trace(go.Scatter(x=t, y=-xd.real,
    mode='lines', line=dict(
        color="LightSeaGreen",
        width=4,
        dash="dashdot",
    ), name="Time response", showlegend=False))

fig.update_layout(
    title="Free vibration of an initially displaced mass spring damper system", title_x=0.5,
    yaxis_title="$x/\\text{m}$",
    xaxis_title="$t/\\text{s}$",
)

To determine the system's forced response to an input, we set $F(t)$ to a given value, and solve. We will explore this via examples for real aircraft.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-5107176300009857"
     data-ad-slot="7122611277"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Determining Stability - Eigenvalues

We have already shown the characteristic equation of the mass spring damper system to be:

$$\lambda^2 + 2\zeta\omega_n\lambda + \omega_n^2$$

Note that if we had taken the Laplace Transform of the equation of motion with zero initial conditions, we would have arrived at the characteristic equation in terms of the Laplace Operator, $s$

$$s^2 + 2\zeta\omega_n s + \omega_n^2 = 0$$(eq:msdLT)

Clearly equations {eq}`eq:msdCE` and {eq}`eq:msdLT` are equivalent, hence the poles and eigenvalues are equivalent. Since we know that the poles of the system give information on its stability, then we can further surmise that its eigenvalues do the same. Furthermore, we have shown that the eigenvalues are given by the solution of the characteristic equation: 

$$\lambda = \omega_n\left(-\zeta \pm \sqrt{-\zeta^2-1}\right)$$ 

hence we can see that the system's eigenvalues and therefor its stability is a function of both the natural frequency and the damping.

For mechanical systems, damping can only be positive, and hence the term $\zeta\omega_n$ will always be positive. This is a consequence of physical damping being a removal of kinetic energy - hence this *always* causes oscillations to decrease in amplitude. For aircraft, however, the interplay of aerodynamic and propulsive forcing causing a conversion between potential and kinetic energy can give rise to *negative* damping, whereby energy is added to a system. This causes oscillations which increase with time. For solution of the aircraft equations of motion, the eigenvalues may be real or complex, and have a positive or negative real component. This gives rise to four possibilities as shown in the table below:

| $\lambda$                   | Dynamic Response                                                                                                                                                                                          |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Real and Negative           | This denotes an exponential decay or a *convergence*. This is indicative of static stability.                |
| Real and Positive           | This denotes an exponential increase or a *divergence*. This is indicative of static instability.            |
| Complex, $\Re(\lambda) <0$  | This denotes an oscillatory motion with a decreasing amplitude. This is indicative of dynamic stability.     |
| Complex, $\Re({\lambda})>0$ | This denotes an oscillatory motion with an increasing amplitude. This is indicative of dynamic instability. |

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=("$\lambda=1$", "$\lambda=1$", "$\lambda=1\pm 1\imath$", "$\lambda=-1\pm 1\imath$"))

t = np.linspace(0, 5, 1000)
w = 1*2*np.pi

# Make a function that plots a basic system with frequency w over time t
def ft(lam):
    out = np.exp(lam.real * t + 1j * lam.imag * w * t)
    return out.real

# 1 - statically unstable, no dynamic behaviour
lam = 0.1
fig.add_trace(
    go.Scatter(x=t, y=ft(lam), line_color='blue', showlegend=False),
    row=1, col=1
)


# 2 - statically stable, no dynamic behaviour
lam = -1
fig.add_trace(
    go.Scatter(x=t, y=ft(lam), line_color='blue', showlegend=False),
    row=1, col=2
)

# 3 - statically unstable, with dynamic behaviour
lam = 1 + 1j
fig.add_trace(
    go.Scatter(x=t, y=ft(lam), line_color='blue', showlegend=False),
    row=2, col=1
)

# 3 - statically unstable, with dynamic behaviour
lam = -1 + 1j
fig.add_trace(
    go.Scatter(x=t, y=ft(lam), line_color='blue', showlegend=False),
    row=2, col=2
)



fig.update_layout(height=600, width=800, title_text="$\\text{Different Values of }\lambda\\text{ and stability}$", title_x=0.5)
fig.update_xaxes(title_text="t/s")
fig.update_yaxes(title_text="$f(t)$")
fig.show()

you will see from the above that the existence of a complex root gives rise to dynamic behaviour, and its sign does not matter.

### Period and time to half amplitude

If we consider the general eigenvalue and decompose into its imaginary and real parts:

$$\lambda = \Re(\lambda) + i\cdot\Im(\lambda)$$ 

Which gives the response

$$x = x_0e^{\lambda t} = x_ee^{\left(\Re(\lambda) + i\cdot\Im(\lambda)    \right)t}$$

For the oscillatory modes, the angular frequency is given by the imaginary part of the eigenvalue - hence the period of any oscillations, $T$, is given by

$$T = \frac{2\pi}{|\Im(\lambda)|}$$

with a frequency given by

$$f= \frac{|\Im(\lambda)|}{2\pi}    \text{Hz}$$

The decay rate of the oscillatory behaviour is given by the real part of the eigenvalue - hence this determines the damping. When looking at aircraft modes of motion, we tend to talk about the 'time to half amplitude' for convergent modes, or the 'time to double amplitude' for a divergent mode. Since the amplitude of the oscillation is given:

$$|x| = x_0e^{\Re(\lambda)t}$$

hence for a stable system, the time to half amplitude, $t_{.5}$, is given by:

$$\begin{gathered}
    \frac{x_0}{2} = x_0e^{\Re(\lambda)t_{.5}}\\
    \implies \ln|0.5| = \Re\left(\lambda\right)\cdot t_{.5}\\
    \therefore t_{.5} = \frac{-0.69}{\Re({\lambda})}\end{gathered}$$

Note that as the time to half amplitude is only calculated for a stable system where the eigenvalue will be negative, the time will be a positive value. Similarly for an unstable system, the time to double amplitude $t_2$ is found from

$$\begin{gathered}
    2\cdot{x_0} = x_0e^{\Re(\lambda)t_{2}}\\
    \implies \ln|2| = \Re\left(\lambda\right)\cdot t_{2}\\
    \therefore t_{.5} = \frac{\ln(2)}{\Re({\lambda})}\end{gathered}$$

Again, since the time to double amplitude is only calculated for an unstable system where the eigenvalue will be positive, the time will always be a positive value.

**Note that as presented above, we are assuming the dimensional equations of motion. If we are using them in their nondimensional form, then the reduced time is calculated and the answers must be multiplied by $t^*$.**


### Damped and Undamped Natural Frequencies

The *damped natural frequency*, $w_d$, is the frequency at which the actual system will exhibit oscillatory behaviour if measured in the real world, subject to damping. The *natural frequency*, $w_n$, of the system is a frequency that the system would vibrate if the oscillatory behaviour were influenced by the system stiffness alone.

In short, we can get the two from:

$$\omega_d=\Im(\lambda)$$
$$\omega_n=\sqrt{\Re(\lambda)^2+\Im(\lambda)^2}$$

but it's not always apparent why this is the case. We know that a second order system will have the general form of:

$$\ddot{x} + 2\zeta\omega_n\dot{x} + \omega_n^2 = 0$$

and we have further shown that the eigenvalues found determine the modal characteristics of the system. Since these are the roots of the characteristic equation we can write the above as:

$$\ddot{x} + 2\zeta\omega_n\dot{x} + \omega_n^2 = \left(x-\left(Re(\lambda)+i\Im(\lambda)\right)\right)\left(x-\left(Re(\lambda)-i\Im(\lambda)\right)\right)$$

the right hand side can be mutlipled out to give

$$\lambda^2 - 2\cdot\Re(\lambda){\lambda}+\left(\Re^2(\lambda)+\Im^2(\lambda)\right)$$

which, given the relationship between damped and undamped natural frequncies as

$$\omega_d=\omega_n\sqrt{1-\zeta^2}$$

may be readily rearranged to give the two expressions for natural frequency.



### The stability of a multiple degree of freedom system

The theory presented above has been developed in a theory that is easily extensible to multiple degree of freedom systems. The general first order ODE can be represented as 

$$\dot{\vec{x}} = \boldsymbol{A}\vec{x}$$(eq:generalODE2)

This equation represents a system of $n$ equations where $n$ is the number of states and degrees of freedom. Hence for the preceding analysis, $n=1$, whereas it will be $>1$ for our aircraft problem. The general solution will be[^2]:

[^2]: If you've not seen the symbol $\forall$ it means 'for each' or 'for all' dependent upon usage. It's an upside-down 'A'. Not to be confused with what Charles Sanders Peirce denoted it to mean.

$$x_i = x_{0_i}e^{\lambda t}\hspace{1cm}\forall i=1,\ldots,n$$

in vector form

$$\vec{x}=\vec{x}_0e^{\lambda t}$$

similarly, differentiating and substituting into Eq. {eq}`eq:generalODE2`

$$\lambda\vec{x}_0e^{\lambda t} = \boldsymbol{A}\vec{x}_0e^{\lambda t}$$

which is an eigenvalue (matrix/vector) problem and hence we can write

$$\left(\lambda\boldsymbol{I}-\boldsymbol{A}\right)\vec{x}_0=0$$(eq:mdEP)

The trivial solution is zero displacement, $x_0=0$, but more useful solution is given by the determinant 

$$\left|\lambda\boldsymbol{I}-\boldsymbol{A}\right|=0$$(eq:mdCE)

Equation {eq}`eq:mdCE` is the characteristic equation of a multiple degree of freedom system, and will be a polynomial of order $n$, yielding $n$ eigenvalues dictating the system stability. If any single value is unstable, then the aircraft is deemed dynamically unstable. Similarly, if any of the eigenvalues give a complex pair, then the characteristic motion will be oscillatory as the equations are coupled.

Once the eigenvalues have been solved, each of these may be substituted into Eq. {eq}`eq:mdEP` to solve for the vector of amplitudes to give $n$ vectors of $n$ amplitudes. The magnitudes of each respect state motion help us to determine which variables correspond to which eigenvalue (or which eigenvalues correspond to which *mode* of the aircraft).

Before we can utilise the eigenvalues to tell us information about the modes of the aircraft, we will require an understanding of what each of the aircraft modes of motion comprises. The following section will describe what each mode is, in a physical sense before we delve into the governing mathematics.


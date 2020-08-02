# Assumed knowledge

This course assumes a certain level of knowledge on the reader and will not be formally taught in class - you will have been taught this at earlier levels in your undergraduate studies but:
- Students forget things
- Repetition helps to reinforce learning

So a review of what is assumed of your knowledge is suitable at this juncture.

## Aircraft Anatomy

The basic parts of a standard fixed-wing aircraft are labelled in {numref}`AircraftComponents`. Flight is controlled through movable parts of the aircraft, and from adjusting the propulsion.

```{figure} ../Images/AircraftComponents.png
---
height: 300px
name: AircraftComponents
---
Major Aircraft Components
```

Aircraft have control surfaces in red and high-lift devices in blue in {numref}`ControlSurfaces`. Note that some aircraft have additional flow control devices such as *spoilers* but there are not discussed here.

```{figure} ../Images/ControlSurfaces.png
---
height: 300px
name: ControlSurfaces
---
Aircraft Control Surfaces and High Lift Devices
```

The control surfaces are there to alter the aircraft's attitude (its orientation in 3D space). They are:

-   **Ailerons** - these are outboard on each wing, and operate in *differential mode*, meaning if one goes up, the other goes down. These are effected via a sideways stick/yoke movement. This increases lift on one wing, and decreases it on the other, effecting a *roll rate*, $p$, which changes the roll angle, $\phi$.

-   The **elevator** is usually situated on the horizontal stabiliser, and both sides move together. This increases/decreases the tail lift, and changes the aircraft pitch attitude, $\theta$. This is controlled by moving the stick/yoke forward/aft.

-   The **rudder** is on the vertical tail, and is a single control surface. If the rudder moves to the port (left), it creates a sideways aerodynamic force on the tail towards starboard (right), which moves the aircraft nose-port to a *sideslip angle*, $\beta$. This is controlled using pedals in the cockpit.

We will look at *trapezoidal wings* for most of this course - see {numref}`TrapezoidalWing`. In general, we usually define wing parameters in terms of **gross wing** - see {numred}`WingAreas`, $S$. We represent the wing with a simple trapezoid:

```{figure} ../Images/TrapezoidalWing2.png
---
height: 300px
name: TrapezoidalWing
---
Aircraft Trapezoidal Wing
```

```{figure} ../Images/TrapezoidalWing.png
---
height: 300px
name: WingAreas
---
Aircraft Wing Areas
```

you will note that the swing, *sweep*, which is a measure of how far back the tip is compared to the root, is measured by the sweep of the quarter-chord line. The *chord* is the length of the wing in the direction of travel (hence vertical in the image). The so-called **root chord** is usually defined on the aircraft centerline, and not at the actual aircraft root. We can define a few parameters:

$$\begin{aligned}
    \text{Wing taper ratio: } \lambda &= \frac{c_t}{c_0}\\
    \text{Wing area: } S &= \frac{c_t + c_0}{2}\cdot =\bar{c}\cdot b\\
    \text{Standard Mean chord: } \bar{c} &= \frac{c_t + c_0}{2}=\frac{S}{b}\\
    \text{Aspect Ratio: } \bar{AR} &= \frac{b}{\bar{c}}=\frac{b^2}{S}\\
    \text{Mean aerodynamic chord: } \bar{\bar{c}} &= \frac{1}{S}\int^{+s}_{-s}c^2\text{d}y
\end{aligned}$$

## Aerodynamic, Propulsive, and Inertial Forces

As will be covered in the Aircraft Performance module, the simplest regime of flight is that of *steady, level flight*. Steady means not accelerating, and level means that there is no variation in altitude - this *does not* mean that the wings are level, so the aircraft may be turning in a *steady turn*.

Whilst this will be covered in detail later, the basics of this regime *should* be relatable to previous modules.

Since the aircraft is not accelerating, the forces must be in equilibrium. We summarise our forces on the aircraft as two aerodynamic forces, one propulsive, and one inertial:

-   **Lift** - $L$ - the aerodynamic force normal to the incident flow velocity, acting in a 'lifting' sense.

-   **Drag** - $D$ - the aerodynamic force parallel to the incident flow velocity, opposing motion.

-   **Weight** - $W$ - the inertial force acting downward; $W=m\,g$ where $g=9.80665\text{m}\,\text{s}^{-2}$, the acceleration due to gravity.

-   **Thrust** - $T$ - the propulsive force parallel to the aircraft longitudinal axis, providing motion.


```{figure} ../Images/EqForces.png
---
height: 300px
name: EqForces
---
Equilibrium Forces
```


## Aerodynamic Coefficients

In general, it's useful to be able to remove units from expressions in engineering for a number of reasons:

-   It enables us to work between unit systems (i.e., between metric and imperial unit systems) without conversion.

-   It enables us to compare aircraft of differing sizes in terms of performance.

-   It enables us to perform scale model work of aircraft and extend the results to full-size.

Hence, as presented in the preceding section forces $L$ and $D$ represent *dimensional* lift and drag, which we may measure in Newtons, Pounds-Force, Dyne, or Kip. 

```{note}
:class: dropdown
You may not have heard of the last two. Don't worry - we won't be using them.
```

To remove the dimensions from these forces, we divide by something else with the same dimensions. You should be comfortable with the fact that the lift is proportional to the 'dynamic pressure', $q_\infty$ 

$$q_\infty=\frac{1}{2}\,\rho\, V^2$$ 

where $\rho$ is the fluid density, and $V$ is the density of the fluid. Dynamic pressure has dimensions of: 

$$\begin{aligned}
    q_\infty=\frac{1}{2}\,\rho\, V^2     &: \frac{\text{kg}}{{\text{m}^3}}\,\left\{\frac{{\text{m}}}{{{\text{s}}}}\right\}^2\\
    &: \frac{\text{kg}}{{\text{m}\text{s}^2}}\\
    &: \left[\frac{\text{M}}{\text{L}\,\text{T}^2}\right]\end{aligned}$$ 
    
We know that lift and drag may be represented in *Newtons*, which have units of ${\text{N}}={\text{kg}\,\text{m}\,\text{s}^{-2}}$ which has dimensions of

$$\begin{aligned}
    \left[\frac{\text{M}\,\text{L}}{\text{T}^2}\right]  \end{aligned}$$
    
to get something that has the same dimensions as the aerodynamic forces, we need to multiply the dynamic pressure by *some* area. The area that we choose is the *wing area*, $S$, which we'll define in more detail later. But now we've reached the definition of the three-dimensional lift and drag coefficients:

$$\begin{aligned}
    C_L = \frac{L}{\frac{1}{2}\,\rho\,V^2\,S}\\
    C_D = \frac{D}{\frac{1}{2}\,\rho\,V^2\,S}   \end{aligned}$$

The uppercase $L$ and $D$ in the subscript means that we're looking at the three-dimensional lift and drag coefficients. As aeronautical engineers we often like to look at an infinitesimal slice of a wing, which we call an aerofoil/airfoil. 

```{note}
:class: dropdown
Though I live and work in America, I'm a Brit. Hence the 'u's and 's' in place of 'z's. Aerofoil is British English, Airfoil is US English.
```

If we wish to have the lift and drag quantified on 2D aerofoil, then we look at the *lift and drag per unit span*, which we denote with a lowercase $l$ and $d$. The corresponding two-dimensional lift and drag coefficients are:

$$\begin{aligned}
    C_l = \frac{l}{\frac{1}{2}\,\rho\,V^2\,c}\\
    C_d = \frac{d}{\frac{1}{2}\,\rho\,V^2\,c}   \end{aligned}$$

where we've now introduced a new parameter, $c$, in place of the wing area. This $c$ represents the *chord* of the aerofoil, which is simply the length from the very front (the leading edge) to the very aft (the trailing edge).

## Aerofoils and Lift

As discussed above, an aerofoil is an infinitesimal section of a wing, which we can represent in two dimensions (this is helpful, as drawing in 3d is difficult!). The simplest aerofoil is a symmetric one. 

```{note}
:class: dropdown
The simplest aerofoil with thickness - as the simplest 'foil' could be argued to be a flat plate.
```

The nondimensional longitudinal axis is the $x$ direction, and the distance from the front (leading edge) to the tail (trailing edge) of the airfoil is the *chord* line.



import matplotlib.pyplot as plt
import numpy as np
plt.close('all')


def naca4(number='0012', n=1000):
    
    """
    Plots the aerofoill for the given 4 digit NACA number string
    """

    m = float(number[0])/100.0
    p = float(number[1])/10.0
    t = float(number[2:])/100.0

    a0 = +0.2969
    a1 = -0.1260
    a2 = -0.3516
    a3 = +0.2843
    a4 = -0.1015

    # Make a vector of the x spacing
    x =  np.linspace(0, 1, n)

    # Get the thickness distribution
    yt = 5 * t * (a0*x**.5 + a1*x + a2*x**2 + a3*x**3 + a4*x**4)
    
    # Get the camber line
    yc = np.zeros(x.shape)
    if p > 0:
        yc[x <= p] = m / p**2 * (2 * p * x[x <= p] - x[x <= p] **2)
        yc[x > p] = m / (1 - p)**2 * ((1 - 2 * p) + 2 * p * x[x > p] - x[x > p]**2)

    # Get the upper and lower surfaces
    yu = yc + yt
    yl = yc - yt
    
    # Put into Selig format
    Y = np.concatenate((yu[::-1], yl))
    X = np.concatenate((x[::-1], x))
    
    plt.figure()
    plt.plot(x, yu, label="Upper Surface")
    plt.plot(x, yl, label="Lower Surface")
    plt.plot(x, yc, label="Camber Line")
    plt.legend()
    plt.gca().set_aspect('equal')
    plt.gca().axis('off')
    plt.title(f"Normalised aerofoil for NACA {number}")
    plt.gca().legend(bbox_to_anchor=(1.1, 1.05))
    return

naca4('2412')


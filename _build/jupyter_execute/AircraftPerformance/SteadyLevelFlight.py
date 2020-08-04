# Forces in Steady Level Flight

The discipline of Aircraft Flight Mechanics requires the formulation of relationships between aircraft forces, and aircraft motion. In order to define *motion*, it was necessary to define the different airspeeds in the preceding section.

Aircraft have six degrees of freedom - three translational ($x, y, z$), and three rotational ($\phi, \theta, \psi$), and in order to develop the expressions describing aicraft flight, *nine* coupled equations are required. This course will get to that point, and those equations will derived and utilised - but before that, some really handy relationships can be defined for flight constrained to a single direction.

The simplest flight regime is best to start with, which is steady, level (meaning no change in altitude) flight.

```{admonition} A word about SLUF... 
:class: dropdown 

Sometimes you may see this flight regime caled SLUF, standing for **S**teady **L**evel **U**naccellerated **F**light. I don't particularly like this acronym as:
- Steady *means* unaccelerated, so it's tautologous
- There's another, arguably better [definition for SLUF](https://en.wiktionary.org/wiki/SLUF)

```


Let's explore what this regime means, and the assumptions we make

-   We assume that the aircraft is a **point mass**, whereby we assume that the aircraft dimensions are negligible when compared to the dimensions of motion.

-   **Steady** flight means no acceleration, so we can infer from Newton's first law that the sum of forces acting on the aircraft is zero $\sum\vec{F}=0$ . This is the **equilibrium steady flight condition**.

The definition of forces on the aircraft can change depending on the purpose - and it is only be convention that we define lift and drag in the directions we do.

The semantics notwithstanding, it is traditional to define four mutually-orthogonal forces - see {ref}`CruiseForces`. 
- Two aerodynamic; **lift and drag**. 
- One propulsive; **thrust**. 
- One inertial; **weight**.

```{figure} ../Images/CruiseForces.png
---
height: 300px
name: CruiseForces
---
Equilibrium Forces
```

For this regime, it is further assumed that the aerodynamic incidence is small, and that the thrust offset is negligible. Therefore we assume that lift and weight are *perpendicular* to aircraft motion, and that thrust and drag are parallel to aircraft motion.

## Vertical Forces

Looking at the vertical forces, $\sum F_z =0$, therefore $L=W$:

$$C_L = \frac{L}{\tfrac{1}{2}\rho V^2S}$$
    
$$    = \frac{W}{\tfrac{1}{2}\rho V^2S}$$
    
rearranging to find flight speed:

```{math}
:label: ACSpeedEquation
V = \sqrt{\frac{\frac{W}{S}}{\tfrac{1}{2}\rho C_L}}
```
Equation {eq}`ACSpeedEquation` is the **Aircraft Speed Equation** for steady level flight, and some basic aerodynamic behaviour may be inferred from it:

-   Slower flight is possible by reducing wing loading - reducing aircraft mass, or increasing wing area. Or by increasing $C_L$ - increasing $\alpha$

-   The minimum possible flight speed occurs at $C_{L_{max}}$ - just before stall

-   Flight speed may be increased by reducing $\rho$ - by flying at increased altitude

## Longitudinal Forces

Looking at the longitudinal forces, $\sum F_x =0$, therefore $T=D$:

$$\begin{aligned}
    C_D &= \frac{D}{\tfrac{1}{2}\rho V^2S}\nonumber\\
    &= \frac{T}{\tfrac{1}{2}\rho V^2S}\nonumber\end{aligned}$$
    
Drag estimation is complex, and can be performed via a variety of means from datasheets, CFD, wind tunnel testing or - more commonly - a combination of all. A good breakdown of drag sources is given by MacCormick{cite}`MacCormick:1995wq`, and a reproduction of the breakdown given is found in the dropdown below - but this is far beyond the complexity required for Aircraft Performance.

```{admonition} Drag Breakdown (well beyond what we need, but included for reference)
:class: dropdown

The following is an extract from MacCormick{cite}`MacCormick:1995wq` [pp. 162-163]:

**Induced Drag** The drag that results from the generation of a trailing vortex system downstream of a lifting surface of finite aspect ratio.

**Parasite Drag** The total drag of an airplane minus the induced drag. Thus, it is the drag not directly associated with the production of lift. The parasite drag is composed of many drag components, the definitions of which follow.

**Skin Friction Drag** The drag on a body resulting from viscous shearing stresses over its wetted surface.

**Form Drag** (Sometimes Called Pressure Drag) The drag on a body resulting from the integrated effect of the static pressure acting normal to its surface resolved in the drag direction.

**Interference Drag** The increment in drag resulting from bringing two bodies in proximity to each other. For example, the total drag of a wing-fuselage combination will usually be greater than the sum of the wing drag and fuselage drag independent of each other.

**Trim Drag** The increment in drag resulting from the aerodynamic forces required to trim the airplane about its center of gravity. Usually this takes the form of added induced and form drag on the horizontal tail.

**Profile Drag** Usually taken to mean the total of the skin friction drag and form drag for a two-dimensional airfoil section.

**Cooling Drag** The drag resulting from the momentum lost by the air that passes through the power plant installation for purposes of cooling the engine, oil, and accessories.

**Base Drag** The specific contribution to the pressure drag attributed to the blunt after-end of a body.

**Wave Drag** Limited to supersonic flow, this drag is a pressure drag resulting from non-canceling static pressure components to either side of a shock wave acting on the surface of the body from which the wave is emanating.
```


In flight performance, we assume that the aircraft is operating in the region of linear aerodynamics, and utilise a drag model as given by Equation {eq}`DragEquation`:

```{math}
:label: DragEquation
    \underbrace{C_D}_{\text{Total Drag}} = \underbrace{C_{D0}}_{\substack{\text{Zero incidence} \\ \text{drag}}} + \underbrace{K\cdot C_L^2}_{\substack{\text{Induced Drag +} \\ \text{$\alpha$-dependent form drag}}}
```

where

$$    K=\frac{k}{\pi AR}$$

The first term represents the drag that is independent of aerodynamic incidence, whilst the second term is proportional to $C_L^2$, which represents the induced drag and the component of form drag that varies with incidence.

The parameter $k\sim 1.1-1.4$ for most aircraft, and $AR$ is the wing aspect ratio $AR = \frac{b^2}{S}$. $K$, $C_{D0}$ usually assumed constant, but can depend on:

-   configuration changes (flap deployment)

-   Reynolds Number (speed and height)

-   Compressibility (shock waves)

Equation {eq}`DragEquation` assumes that the minimum drag occurs at zero lift. This is the case for a symmetric aerofoil, but not for a cambered one. Since most airfcraft have a cambered wing, Equation {eq}`DragEquation` should be modified to

$$C_D = C_{D, min} + K\left(C_L - C_{L0}\right)^2$$

The second equation is more realistic for real aircraft - but adds complexity to the algebra. For simplicity, Equation {eq}`DragEquation` will be used in development of the Aircraft Performance Equations.

Equation {eq}`ACSpeedEquation` and Equation {eq}`DragEquation` underpin the basics of aircraft performance.

### Drag Polar

The relationship between lift and drag is given through the aircraft drag polar - often plotted as $C_L$ vs $C_D$. Values for $C_L$ and $C_D$ are commonplace in the literature - a quick search yielded data for the Cessna 172S {cite}`Haberkorn:2016bj`.

You will see that the drag model works well for low values of lift - that is, in the linear aerodynamic region. The behaviour at the 'bottom' of the curve is sometimes called the 'drag bucket' - and I spent many years *collecting* these data in a wind tunnel.

The drag polar shows the aerodynamic efficiency of a given aircraft - that is, it represents the lift-to-drag ratio. You can find the best (highest) lift to drag ratio as the tangent of a line drawn from the origin to the curve.

It would be great to be able to find the best lift to drag ratio without having to draw the drag polar. If you looka the source code for the image below, then it's obvious that I haven't drawn the tangent to find the best lift to drag ratio - rather I have drawn the tangent after having found the best lift to drag ratio.

Expand the code to see the source data and coefficients used in the drag model.

# Aircraft Drag polar
import numpy as np
import matplotlib.pyplot as plt

# Data for this graph has been taken from here: 
# https://www.researchgate.net/figure/Figure-A10-Drag-polar-for-the-Cessna-172S-This-plot-is-created-for-NACA-2412-airfoil_fig25_328578766

# Discrete points:
Cd = np.array([0.033099, 0.035185, 0.035214, 0.041961, 0.051143,\
0.064192, 0.080106, 0.096683, 0.104613, 0.11364, 0.121425, 0.130259, 0.138232])
Cl = np.array([0.1454, -0.09219, 0.38303, 0.6238, 0.86305, 1.09772,\
1.31082, 1.45757, 1.51784, 1.55342, 1.58437, 1.60452, 1.58455])

plt.plot(Cd, Cl, 'x', label='Data')

# Put the drag model on top
Clvector = np.linspace(min(Cl) - .2, max(Cl) + .2, int(1e3))
Cd0 = 0.033
Cl0 = 0.14
K = 0.035
Cdvector = Cd0 + K*(Clvector - Cl0)**2
plt.plot(Cdvector, Clvector, '-r', label="Drag Model")
plt.legend
plt.xlabel('$C_D$')
plt.ylabel('$C_L$')

plt.title('Drag Polar: Data vs. Drag Model');

# Determine minimum drag
Clmind = np.sqrt(Cd0/K + Cl0**2)
Cdmind =  Cd0 + K*(Clmind - Cl0)**2

# plot it
plt.plot(Cdmind, Clmind, 'ob', label="$\\frac{L}{D}_{max}$")

# show that this is the tangent
plt.plot([0, Cdmind*2], [0, Clmind*2], '-b', label="Tangent")
plt.gca().set_xlim(0, .14);
plt.gca().set_ylim(-.5, 2);
plt.gca().grid('on')
plt.axhline(0, color='black');

# Legend
plt.legend();




### Best lift to drag ratio

The highest lift to drag ratio gives the position of best aerodynamic efficiency, and sets the best _glide ratio_ for an aircraft.

In the following, the values of $C_L$ and $C_D$ for optimum aerodynamic efficiency - but before diving into the mathematics, some consideration of their significance might be necessary for some readers.

```{admonition} Why do we want to know $C_L$?
:class: dropdown

In the aviation world, pilots tend to be excellent at intuiting flight physics - and being able to relate control movement to aircraft flight, without needed to understand the physics (often in spite of thinking they do). 

By contrast, aerospace engineers tend to be be excellent and understanding the mathematics of flight physics - without any consideration of the physical significance of what they are actually deriving. By way of an example ask yourself - *'what control would you change to effect an altitude change?'*, and if your answer is simply *'pull the stick/yoke back'*, then this highlights a misunderstanding of the aircraft controls and physics. In reality, it would be a combination of throttle and stick, but fundamentally you need to _gain potential energy_ which requires an increase in energy from somewhere, *i.e.,* the engine. 

---------------

Back to the problem at hand:

Consider what *"to fly at a $C_L=X$"* actually means - the pilot controls the *pitch* of the aircraft using fore-aft motion of the stick/yoke. A change in pitch changes the _angle of attack_ of the aircraft, which changes the aircraft lift coefficient.

In reality, a pilot will not tend to consider the numerical value of $\alpha$ they are flying at - and they are even less likely to know the $C_L$ of the aircraft under a given flight regime.

For a given $C_L$, the aircraft speed determines the dimensional value of lift being produced. If $L=W$, this is steady level flight. If $L>W$, the aircraft climbs, if $L<W$, the aircraft descends. 

Through a combination of thottle setting, and elevator deflection (stick fore/aft), steady flight can be achieved. Again - the pilot probably isn't considering the $C_L$ value, and won't know whether they're at the best lift to drag ratio or not.

So - there is a certain speed, in EAS, that will give the best lift to drag ratio. If the pilot is able to maintain this speed with no throttle adjustment, and finds that the aircraft is not climbing nor descending, then they are flying at the best lift to drag ratio - which will give the best **endurance**.

These speeds are usually listed in the aircarft (though in the light aircraft I've been in, they're listed in IAS, and the following questions about EAS fell on deaf ears).

So we, as aerospace engineers, wish to know the lift coefficient for optimum aerodynamic efficiency - but it will be translated into a more pilot-friendly parameter, such as a post-it note on the airspeed indicator.

```

The best lift to drag ratio can be determined from Equation {eq}`DragEquation`. Consider that the lift to drag ratio is equal in dimensional and coefficient form:

$$\frac{L}{D}=\frac{C_L}{C_D}$$

Into which Equation {eq}`DragEquation` may be inserted

$$\frac{L}{D}=\frac{C_L}{C_{D0} + K\cdot C_L^2}$$

The best lift to drag ratio can then be found from minimising $\frac{D}{L}$, so differentiate by $C_L$:

$$\left.\frac{D}{L}\right|_{min}=\left.\frac{C_{D0} + K\cdot C_L^2}{C_L}\right|_{min}$$

A bit of elementary calculus gives the minima of the right hand side as given by

$$C_{L, md}=\sqrt{\frac{C_{D0}}{K}}$$

```{admonition} What about a real aircraft?
:class: dropdown

Remember that Equation {eq}`DragEquation` as used above is only valid for an uncambered wing - the expression for $C_{L, md}$ changes in that case. If you look at the source code for the drag polar, you can see what it changes to. Try to derive this yourself. 

```

### Drag Equation in Dimensional Form

The drag equation can be multiplied by the numerator of the lift and drag coefficients, $\frac{1}{2}\rho\,V^2S$, to yield dimensional drag:

$$ C_D\cdot \frac{1}{2}\rho\,V^2S = C_{D0}\cdot\frac{1}{2}\rho\,V^2S + K\cdot C_L^2\cdot\frac{1}{2}\rho\,V^2S$$

In steady level flight, $L=W$, so the lift coefficient can be expressed as

$$C_L = \frac{W}{\frac{1}{2}\rho\,V^2S}$$

and hence

$$D = C_{D0}\frac{1}{2}\rho\,V^2S + \frac{K\,W^2}{\frac{1}{2}\rho\,V^2S}$$

or

$$D = A\,V^2 + B\,V^{-2}$$

where $A$ and $B$ are functions of density (and therefore functions of altitude).

- $A=C_{D0}\frac{1}{2}\rho S$ represents the **profile drag**, which gets larger with forward speed squared
- $B=\frac{K\,W^2}{\frac{1}{2}\rho S}$ represents the **induced drag**, which gets smaller with forward speed squared

The above should make sense to you *intuitively*. Profile drag is largely viscous drag, which will get larger in proportion to the dynamic pressure. The induced drag is proportional to the bound vortex maintaining lift, which will be proportional to $C_L$ which, for a steady flight, is inversely proportional to the dynamic pressure.

For a set of parameters, the drag equation can be plotted.

import plotly.io as pio
import plotly.express as px
import plotly.offline as py
import plotly.graph_objects as go
from ambiance import Atmosphere

# Define constants
CD0=0.01; K=0.01; alt=0; S=50; W=5000
mosphere = Atmosphere(alt*1000)
rho = mosphere.density

A = CD0 * 0.5 * rho * S
B = K * W **2 / 0.5 / rho / S

# Flight speed
Vs = np.linspace(1, 150, 1000)

# Define drags
Dind = B * Vs**-2
Dprof = A * Vs**2
D = Dind + Dprof

fig = go.Figure()
fig.add_trace(go.Scatter(x=Vs, y=Dind, name="Induced Drag"))
fig.add_trace(go.Scatter(x=Vs, y=Dprof, name="Profile Drag"))
fig.add_trace(go.Scatter(x=Vs, y=D, name="Total Drag"))



fig.update_layout(
    title=f"Variation of Profile, Induced, and Total Drag - CD0 = {CD0}, K={K}, altitude={alt}km, S={S}m^2, W={W/1e3}",
    xaxis_title="TAS / (m/s)",
    yaxis_title="Drag / N",
    legend_title="Drag Breakdown",
)

import ipywidgets as widgets
widgets.IntSlider(
    value=0,
    min=0,
    max=50,
    step=1,
    description='Altitude (km):',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)


# The source for this graph is very poorly written - it's the first graph I've produced with Plotly.
# Things that should be different include, but are not limited to:
# - Hackey way of assigning labels
# - Duplication of A and B definitions

import plotly.graph_objs as go
import numpy as np
from ipywidgets import interact
from ambiance import Atmosphere



# Make a figure
fig = go.FigureWidget()
scatt = fig.add_scatter(name="Total Drag")
scatt = fig.add_scatter(name="Profile Drag")
scatt = fig.add_scatter(name="Induced Drag")

fig.update_layout(
    title="Variation of Profile, Induced, and Total Drag",
    xaxis_title="$\\text{True Airspeed } (ms^{-1})^{-1}$",
    yaxis_title="$\\text{Dimensional Drag } N^{-1}$",
    legend_title="Drag Breakdown",
)

Vs = np.linspace(1, 150, 1000)

@interact(CD0=(0.01, 0.1, 0.01), K=(0.01, 0.2, 0.01), alt = (0, 80, 1), S = (10, 150, 5), W = (1000, 500000, 500), ylim=(10, 50000, 1), xlim=(10, max(Vs), 1))
def update(CD0=0.01, K=0.01, alt=0, S=50, W=5000, ylim=5000, xlim=max(Vs)):
    with fig.batch_update():
        mosphere = Atmosphere(alt*1000)
        rho = mosphere.density
        
        # Define 
        A = CD0 * 0.5 * rho * S
        B = K * W **2 / 0.5 / rho / S
        
        # Total Drag
        fig.data[0].x=Vs
        fig.data[0].y=A * Vs**2 + B * Vs**-2

        
        # Profile Drag
        fig.data[1].x=Vs
        fig.data[1].y=A * Vs**2
        
        # Induced Drag
        fig.data[2].x=Vs
        fig.data[2].y=B * Vs**-2
        
        fig.update_yaxes(range=[0, ylim])
        fig.update_xaxes(range=[0, xlim])
        fig.show()
        


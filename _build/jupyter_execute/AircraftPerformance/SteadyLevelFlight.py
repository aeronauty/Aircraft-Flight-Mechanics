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
    
Drag estimation is complex, and can be performed via a variety of means from datasheets, CFD, wind tunnel testing or - more commonly - a combination of all. A good breakdown of drag sources is given by {cite}`MacCormick:1995wq`, and a reproduction of the breakdown given is found in the dropdown below - but this is far beyond the complexity required for Aircraft Performance.

```{admonition} Drag Breakdown (well beyond what we need, but included for reference)
:class: dropdown

The following is an extract from {cite}`MacCormick:1995wq` [pp. 162-163]:

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


In flight performance, we assume that the aircraft is operating in the region of linear aerodynamics, and utilise a drag model as given by Equation {eqn}`DragEquation`:

```{math}
:label: DragEquation
    \underbrace{C_D}_{\text{Total Drag}} = \underbrace{C_{D0}}_{\substack{\text{Zero incidence} \\ \text{drag}}} + \underbrace{K\cdot C_L^2}_{\substack{\text{Induced Drag +} \\ \text{$\alpha$-dependent form drag}}}
```

where

$$    K=\frac{k}{\pi AR}$$

$k\sim 1.1-1.4$ for most aircraft, and $AR$ is the wing aspect ratio $AR = \frac{b^2}{S}$. $K$, $C_{D0}$ usually assumed constant, but can depend on:

-   configuration changes (flap deployment)

-   Reynolds Number (speed and height)

-   Compressibility (shock waves)



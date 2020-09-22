# Questions and Solutions

The following comprises the theory that I expect you to have absorbed and be fluent in over the preceding module. Some questions have *wordy* answers whilst others have *numerical answers*. The numerical answers are provided, and the method is hidden in dropdowns in some cases, and completely hidden in the source ```ipynb``` notebooks in other cases.

A lot of the theory questions ask you to _derive_ something. I do not include solutions to these questions - they are all 'bookwork' which is included in the notes. If you're not able to answer them, ask on Slack.

Remember that you are expected to be writing your own code snippets rather than simply using this website as a calculator. I might be a real bastard and turn off the _live code_ functionality during certain exams to enforce that.

## Background Questions

These are not directly taught in this course, *per se*, but will prove your abilities to analyse aircraft data in order to even start the problems in Module 1. The following will test your understanding of the drag polar.

### WT Data

A test is carried out on a 1:20 scale model of an aircraft in an atmospheric wind tunnel (ie $\rho = \rho_{SL}$ in the working section) at a speed of 20m/s.  The model has a rectangular wing with a span of 1.70m and a chord of 0.24m. 

| $\alpha/^\circ$      | \-6  | \-3  | 0    | 3    | 6    | 9    | 12   | 15    | 18    |
|----------------------|------|------|------|------|------|------|------|-------|-------|
| $L\,\text{N}^{-1}$  | \-25 | 0    | 25   | 50   | 75   | 100  | 125  | 135   | 115   |
| $D\,\text{N}^{-1}$ | 1\.9 | 1\.6 | 1\.9 | 2\.8 | 4\.3 | 6\.4 | 9\.1 | 13\.8 | 19\.2 |

Perform the following data analysis and presentation:
- Evaluate $C_L$ and $C_D$ for each incidence.  
- Plot $C_D$ against $C_L$.
- Plot lift/drag ratio $C_L$/$C_D$ against $C_L$
- Plot $C_D$ against $C_L^2$.	

and **using these graphs**, estimate:

- The lift curve slope $a$.
- The zero-lift incidence $\alpha_{0L}$.
- The lift coefficient at zero lift, $C_{L0}$
- The induced drag factors $K$ and $k$.
- The zero lift drag $C_{D0}$ (you can assume camber is negligible) 
- The maximum lift/drag ratio.
- The approximate stall angle $\alpha_s$.
- The maximum lift $C_{Lmax}$

```{admonition} Answers
:class: dropdown
$$a= 4.78/rad$$
$$\alpha_{0L}= -3^\circ$$
$$C_{D0} = 0.016, K = 0.048, k=1.07$$
$$L/D_{max}\simeq 18$$
$$\alpha_S\simeq 15^\circ$$
$$C_{Lmax}\simeq 1.35$$
```


import numpy as np
alfas = np.array([-6, -3, 0, 3, 6, 9, 12, 15, 18])
Ls = np.array([-25, 0, 25, 50, 75, 100, 125, 135, 115])
Ds = np.array([1.9, 1.6, 1.9, 2.8, 4.3, 6.4, 9.1, 13.8 ,19.2])

import numpy as np
import plotly.graph_objects as go

# Constants
b = 1.7
S = 1.7 * 0.24
V = 20
rho = 1.225

AR = b**2/S

den = 0.5 * rho * V**2 * S

# Make into coefficients
CL = Ls/den
CD = Ds/den

# Lift and Drag vs. Incidence
fig = go.Figure()

fig.add_trace(go.Scatter(x=alfas, y=CL,
    mode='markers', marker_symbol="circle-open-dot", name="$C_L$",
    showlegend=True))

fig.add_trace(go.Scatter(x=alfas, y=10*CD,
    mode='markers', marker_symbol="circle-open-dot", name="$10\cdot C_D$",
    showlegend=True))

fig.update_layout(
    title="Wind tunnel dimensional lift vs. angle of attack", title_x=0.5,
    xaxis_title="$\\alpha/\circ$",
    yaxis_title="Aerodynamic Coefficients",
)

fig.show()
# Clearly stall occurs at some point beyond 12 degrees so a linear fit of data before 12 degrees will give the lift curve slop
linear_lift = np.polyfit(alfas[alfas < 13], CL[alfas < 13], 1)

print(f"The lift curve slope is a = {linear_lift[0]/np.pi*180:1.2f}/radian")
a = linear_lift[0]/np.pi*180
CL0 = CL[alfas == 0]
alpha0 = alfas[CL == 0]

## Now do the drag polar
fig_dragpolar = go.Figure()

fig_dragpolar.add_trace(go.Scatter(x=CD, y=CL,
    mode='markers', marker_symbol="circle-open-dot", name="WT Data",
    showlegend=True))

fig_dragpolar.update_layout(
    title="Drag Polar", title_x=0.5,
    xaxis_title="$C_D$",
    yaxis_title="$C_L$",
)

fig_dragpolar.show()

## Now do the L/D vs CL
fig_CLCD = go.Figure()

fig_CLCD.add_trace(go.Scatter(x=CL, y=CL/CD,
    mode='markers', marker_symbol="circle-open-dot", name="WT Data",
    showlegend=True))

fig_CLCD.update_layout(
    title="$\\text{Lift to drag ratio vs. }C_L$", title_x=0.5,
    xaxis_title="$C_L$",
    yaxis_title="$\\frac{C_L}{C_D}$",
)

fig_CLCD.show()
# This graph enables us to estimate the minimum drag - since we know that the lift to drag ratio will be maximum at CLmd
CLmd = CL[CL/CD == max(CL/CD)][0]
print(f"Estimated CL for minimum drag {CLmd:1.2f}, corresponding lift to drag ratio is {max(CL/CD):1.1f}")

## Now do the CD vs CL^2
fig = go.Figure()

fig.add_trace(go.Scatter(x=CL**2, y=CD,
    mode='markers', marker_symbol="circle-open-dot",
    showlegend=False))

fig.update_layout(
    title="$\\text{Drag Coefficient vs. }C_L^2$", title_x=0.5,
    xaxis_title="$C_L^2$",
    yaxis_title="${C_D}$",
)

fig.show()


linear_drag_model = np.polyfit(CL[alfas < 15]**2, CD[alfas < 15], 1)
print(f"The linear drag model for this aircraft has CD0 = {linear_drag_model[1]:1.3f}, and K = {linear_drag_model[0]:1.3f}, or k={linear_drag_model[0]*np.pi*AR:1.3f}")
CD0 = linear_drag_model[1]
K = linear_drag_model[0]


# It looks like the points before stall show a learn trend - now this next bit is probably beyond what I'd 
# expect you to be able to do, but we'll go through it anyway.
print("Beyond this point, this is further than what I'd expect but you should be able to understand the following.")

# Add the CLmd onto the data based on these
## Add the full drag polar based on the drag model
CL_vector = np.linspace(CL.min(), CL.max(), int(1e2))
CD_vector = CD0 + K * CL_vector ** 2
CLmd_model = np.sqrt(CD0/K)
CDmd_model = CD0 + K * CLmd_model**2

fig_CLCD.add_trace(go.Scatter(x=[CLmd_model], y=[CLmd_model/CDmd_model],
    mode='markers', marker_symbol="circle-open-dot", name="Drag Model - Minimum Drag",
    showlegend=True))

fig_CLCD.add_trace(go.Scatter(x=CL_vector, y=CL_vector/CD_vector,
    mode='lines', marker_symbol="circle-open-dot", name="Drag Model",
    showlegend=True))

fig_CLCD.show()

fig_dragpolar.add_trace(go.Scatter(x=[CDmd_model], y=[CLmd_model],
    mode='markers', marker_symbol="circle-open-dot", name="Drag Model Minimum Drag",
    showlegend=True))





fig_dragpolar.add_trace(go.Scatter(x=CD_vector, y=CL_vector,
    mode='lines', name="Drag Model",
    showlegend=True))

fig_dragpolar.show()

## Conversion to flight data

The wind tunnel model described above is of an aircraft which weighs 300kN at full scale.  It flies at maximum L/D at a height for which $\sigma$ = 0.25.

Determine the following:
1. The aircraft angle of attack
2. The airspeed, $V$, and the required power at this condition
3. The minimum flight speed at this altitude
4. If the aircraft can produce 100kN thrust at sea level, what is the maximum speed at the altitude in the question
5. Comment on the answer to (4), and whether it is a realistic value.

The solutions are included below - note there is a _choice_ to make in the equations regarding drag polar, which relate to the sparsity of the data. The $C_{L,md}$ can be taken from the raw data or from the drag model. Looking at the drag polar above, and the lift-to-drag ratio, to which both have been added, I think you can reasonably use the drag model but either value is acceptable.

# 1 - Determine the angle of attack
# We know the lift curve slope and zero lift angle from the previous question
# The lift for the aircraft is CL =  a * (alpha - alpha0)
# this can be rearranged to alpha = (CL)/a + alpha0
# Now we just need to know CL - we're told it flies at maximum L/D hence at CLmd

# Get the minikmum 
CLmd_model = np.sqrt(CD0/K)

# First use the data value:
alpha_data = (CLmd)/a + np.radians(alpha0)
# Then the model value:

alpha_model = (CLmd_model)/a+ np.radians(alpha0)

print(f"The aircraft is at an angle of attack of {np.degrees(alpha_data)[0]:1.2f}\
deg from the data or {np.degrees(alpha_model)[0]:1.2f}deg from the model")

# Get the airspeed
W = 300e3
rho_sl = 1.225
sigma=0.25
S_full = S * 20**2 # Don't forget to scale the wing area accordingly 

V_data = np.sqrt(2*W/(rho_sl * sigma * CLmd * S_full))
V_model = np.sqrt(2*W/(rho_sl * sigma * CLmd_model * S_full))
print(f"The corresponding airspeed is {V_data:1.1f}m/s or {V_model:1.1f}m/s ")

# Get the power required
A = 0.5 * CD0 * rho_sl * sigma * S_full
B = K * W**2 / (0.5 * rho_sl * sigma * S_full)

P_data = A * V_data**3 + B * V_data**-1
P_model = A * V_model**3 + B * V_model**-1

print(f"And the power required is {P_data/1e6:1.1f}MW or {P_model/1e6:1.1f}MW")

# Get the thrust available at altitude
T_sl = 100e3
TA = T_sl * sigma
speeds = np.sqrt(np.roots([A, -TA, B]))

# check the stall speed
Vstall = np.sqrt (2 * W /(rho_sl * sigma * S_full * CL.max()))

if Vstall < speeds.min():
    print(f"The minimum airspeed is {max([Vstall, speeds.min()]):1.1f}m/s, which is greater than the stall speed of {Vstall:1.1f}m/s.")
else:
    print(f"The minimum airspeed is {max([Vstall, speeds.min()]):1.1f}m/s, which is the stall speed. V1 is {speeds.min():1.1f}m/s.")
    
# airspeed max
print(f"The maximum airspeed, v2, from the intersection ot TA/TR is {speeds.max():1.1f}m/s.")

# Convert this to speed of sound
from ambiance import Atmosphere

h_vec = np.linspace(0, 80e3, int(100e4))
atmospheres = Atmosphere(h_vec)
sigmas = atmospheres.density/atmospheres.density[0]

# Wont interpolate since the value just needs to be accurate, not precise. Just find the closest 100m value
alt = h_vec[np.argmin(np.abs(sigmas - sigma))]
a_sonic = np.sqrt(1.4 * 287 * atmospheres.temperature[h_vec == alt])
print("")
print(f"The altitude must be {alt/1e3:1.1f}km, at which the speed of sound is {a_sonic[0]:1.1f}m/s, making this \
mach number {speeds.max()/a_sonic[0]:1.2f} M = 0.79 is subsonic, but well into the compressible flow regime \
(M > 0.4), so in practice we would not be justified in extrapolating from the very low speed wind tunnel data of the question \
without making corrections for compressibility effects.  To make matters worse, this Mach Number is well above the \
critical value for a straight wing with a conventional aerofoil section.  We would therefore expect to see regions \
of supersonic flow on the upper and lower surfaces terminated by strong shocks, and hence a (very) large increase \
in form drag (?transonic drag rise?) due to shock-induced flow separation. \
Finally, constant thrust is a poor approximation to modern high-bypass-ratio turbofan engines, which actually \
show a reduction in thrust with forward speed.\
The true maximum speed for this aircraft is therefore likely to be rather lower.")

## Level Flight

### Understanding the drag model

The basic non-dimensional drag equation for an aircraft at low speed is:

$$\begin{align*}
	C_D &= C_{D0} + K\cdot C_L^2\\
		&= C_{D0} + \frac{k}{\pi\cdot AR}C_L^2
\end{align*}$$

**Describe the significant of each term in the equation.**

```{admonition} Answers
:class: dropdown
$C_D$ - Total drag coefficient $C_D\triangleq\frac{D}{\tfrac{1}{2}\cdot\rho\cdot V^2\cdot S}$

$C_L$ - Lift coefficient $C_L\triangleq\frac{D}{\tfrac{1}{2}\cdot\rho\cdot V^2\cdot S}$

$C_{D0}$ - Zero-lift drag - combination of skin friction and the part of form drag that does not vary with incidence.

$K$ - Induced drag effect $K\triangleq\frac{k}{\pi AR}$

$AR$ - Aspect ratio $AR\triangleq\frac{B^2}{S}$

$k$ - Induced drag factor - if wing has a non-elliptical lift distribution ($k>1$)
```
### Understanding EAS

Explain the concept of Equivalent Air Speed (EAS). Writing the drag equation in dimensional form, demonstrate that using EAS enables us to plot a single curve of drag vs. speed for *all* altitudes. Include in your answer a sketch of the variation of drag with speed.

```{admonition} So what is EAS...?
:class: dropdown
Consider an aircraft flying at True Air Speed (TAS or $V$) at some altitude $h$ where the air density is given by $\rho$. The Equivalent Air Speed (EAS or $V_E$) is the speed at which, if flown at ISA sea-level density ($\rho_{SL}=1.225\frac{\text{kg}}{\text{m}^3}$), would give the same dimensional aerodynamic loads for the same aerodynamic configuration \ie *constant $C_L$ etc.*

\begin{equation*}
	V_E\triangleq V\sqrt\frac{\rho}{\rho_{SL}}=V\sqrt{\sigma}
\end{equation*}

Taking the drag equation from question (a), and dimensionalising, we get:

\begin{align*}
	D &= C_{D0}\cdot\frac{1}{2}\cdot\rho\cdot S\cdot V^2 + K\cdot C_L\cdot\frac{1}{2}\cdot\rho\cdot V^2\cdot S
\end{align*}

*i.e.,*

$$\begin{align*}
	D &= f(V,\rho)\\
	&= f(V, h)
\end{align*}$$

So if we plot dimensional drag vs true airspeed, the curves will be different for each altitude. If we take the definition for $V_E$, rearrange for $V$, we may substitute into the dimensional drag equation and get:

\begin{align*}
D &= C_{D0}\cdot\frac{1}{2}\cdot\rho_{SL}\cdot S\cdot V_E^2 + K\cdot C_L\cdot\frac{1}{2}\cdot\rho_{SL}\cdot V_E^2\cdot S
\end{align*}

since $\rho_{SL}$ is constant with altitude,

\begin{align*}
D &= f(V_E)
\end{align*}


Hence drag as a function of EAS is constant with altitude. QED. We can sketch the variation of drag with EAS:

![dragbreakdown](../Images/DragBreakdown.png)

where:


$$\begin{align*}
	A_E &= C_{D0}\cdot\frac{1}{2}\cdot\rho_{SL}\cdot S\\
	B_E &= \frac{K\cdot W^2}{\frac{1}{2}\cdot\rho_E\cdot S}	
\end{align*}$$

```

### Understanding power required

Determine the lift coefficient and drag coefficient when flying at minimum \textsl{power}, and hence show that the corresponding true airspeed is:


\begin{equation*}
	V_{mp} = \left[\frac{2W}{\rho S}\right]^{\tfrac{1}{2}}\left[\frac{K}{3\cdot C_{D0}}\right]^{\tfrac{1}{4}}
\end{equation*}

```{admonition} Bookwork derivation
:class: dropdown

From the question above we have:

\begin{align*}
		D &= A\cdot V^2 + B\cdot V^{-2}
\end{align*}

where

$$\begin{align*}
		A &= C_{D0}\cdot\frac{1}{2}\cdot\rho\cdot S\\
		B &= \frac{K\cdot W^2}{\frac{1}{2}\cdot\rho\cdot S}
\end{align*}$$

power (P) is the rate of work done, or the thrust multiplied by velocity:

\begin{align*}
		P &= T\cdot V\\
\end{align*}

for steady cruise, $T=D$

$$\begin{align*}
		P &= D\cdot V\\
		&= A\cdot V^3 + B\cdot V^{-1}
\end{align*}$$

minimum power at $\frac{\text{d}P}{\text{d}V}=0$

$$\begin{align*}
		\frac{\text{d}P}{\text{d}V} &= 3A\cdot V^{1} - B\cdot V^{-3}=0\\
		\implies 3AV_{mp}^4 &= B\\
		V_{mp}^4 &= \frac{B}{3A}\\
		V_{mp} &= \left[\frac{B}{3A}\right]^{\tfrac{1}{4}}\\
		&= \left[\frac{K\cdot W^2}{\frac{1}{2}\cdot\rho\cdot S}\cdot\frac{2}{3\cdot\rho\cdot C_{D0}\cdot S}\right]^{\tfrac{1}{4}}\\
		&= \left[\left\{\frac{2\cdot W}{\rho\cdot S}\right\}^2\cdot\frac{K}{3\cdot C_{D0}}\right]^{\tfrac{1}{4}}\\
		&= \left[\frac{2W}{\rho S}\right]^{\tfrac{1}{2}}\left[\frac{K}{3\cdot C_{D0}}\right]^{\tfrac{1}{4}}\hspace{1cm}\hfill\text{QED}
\end{align*}$$

```


### Numerical Drag Equation Manipulation

A jet trainer has the drag equation:

\begin{equation*}
	C_D = 0.018 + 0.016\cdot C_L^2
\end{equation*}

and a minimum power speed of 60m/s EAS. What is the thrust to weight ratio required to cruise at 200m/s EAS?

```{admonition} Please attempt the solution yourself first, or you'll learn nothing...
:class: dropdown

**Knowns**:

$$\begin{align*}
	C_{D0} &= 0.018\\
	K &= 0.016\\
	V_{Emp} &= 60\text{m/s}\\
	V_{E} &= 60\text{m/s}
\end{align*}$$

**Required**:

$$\begin{align*}
	\frac{T}{W}_{200EAS} &\therefore \frac{D}{W}_{200EAS}
\end{align*}$$

There are a few ways to go about this equation, you can get $C_{Lmp}$ by differentiating the power equation for $C_L$, and determine $C_D/C_L$ which is the same as $T/W$. Alternatively, you can do the following, which is how I would solve it:

First rearrange the minimum power speed from the previous question for the unknowns ($W$ and $S$):

\begin{equation*}
	\frac{W}{S} = \left(V_{mp}\cdot\left[\frac{K}{3\cdot C_{D0}}\right]^{-\tfrac{1}{4}} \right)^2\cdot\frac{\rho}{2}	
\end{equation*}

we want $\frac{D}{W}$ so:

$$\begin{align*}
	\frac{D}{W} &= \frac{1}{W}\left\{A_E\cdot V^2 + B_E\cdot V^{-2}\right\}\\
	&= C_{D0}\cdot\frac{1}{2}\cdot\rho_{SL}\cdot \left[\frac{W}{S}\right]^{-1}\cdot V_E^2 + \frac{K}{\frac{1}{2}\cdot\rho_{SL}}\cdot\frac{W}{S}\cdot V_E^2\cdot\\
	&= C_{D0}\cdot\left\{V_{mp}\cdot\left[\frac{K}{3\cdot C_{D0}}\right]^{-\tfrac{1}{4}} \right\}^{-2}\cdot V_E^2 + K\cdot\left\{V_{mp}\cdot\left[\frac{K}{3\cdot C_{D0}}\right]^{-\tfrac{1}{4}} \right\}^2 \cdot V_E^{-2}
\end{align*}$$

which, if we insert all the values above, yields $D/W=T/W=0.1115$

```

### Minimum drag speed derivation

Working from first principles show that the the expression for the minimum drag speed of a conventional aircraft is given by:

\begin{equation*}
		V_{MD} = \left[\frac{2W}{\rho S}\right]^{\tfrac{1}{2}}\left[\frac{K}{C_{D0}}\right]^{\tfrac{1}{4}}
\end{equation*}

where all the symbols have their usual meaning. You can assume a knowledge of the lift and drag coefficients' meaning and definitions.

```{admonition} Bookwork derivation
:class: dropdown
We assume that the drag comprises a component that is lift-independent - $C_{D0}$, due to the combination of form drag and skin friction drag, and a second part that rises linearly with the square of the lift due to induced drag, and the $\alpha$-variation of the form drag - $K\cdot C_L^2$. \ie

begin{align*}
	C_D &= C_{D0} + K\cdot C_L^2
\end{align*}

dimensionalising by multiplying by $q_\infty\cdot S$:

$$\begin{align*}
	\implies D &= C_{D0}\cdot\frac{1}{2}\rho\cdot S\cdot V^2 + K\cdot C_L^2\cdot\frac{1}{2}\cdot S\cdot V^{-2}\\
	&= A\cdot V^{2} + B\cdot V^{-2}\\
\end{align*}$$

with $A=C_{D0}\cdot\frac{1}{2}\cdot\rho\cdot S$ and $B=\frac{KW^2}{\frac{1}{2}\cdot\rho\cdot S}$. To find the variation of drag with lift, we can differentiate the above expression wrt V, and find the zero point:

$$\begin{align*}
\frac{\text{d}D}{\text{d}V} &= 2\cdot A\cdot V^{-1} - 2\cdot B\cdot V^{-3}\\
\implies V_{mp} &= \left[\frac{B}{A}\right]^{\tfrac{1}{4}}\\
&= \left[\frac{2W}{\rho S}\right]^{\tfrac{1}{2}}\left[\frac{K}{C_{D0}}\right]^{\tfrac{1}{4}}\text{    QED}
\end{align*}$$
```


### Numerical Minimum Drag Speed

An aircraft with a wing area of 20m$^2$ and drag given by $C_{D0}=0.015$ and $K=0.04$ is flying at an altitude of 6km, at its minimum drag speed.

If the engine thrust is 2500N, what is the speed and weight of the aircraft?


# Inputs\
S = 20
CD0 = 0.015
K = 0.04
alt = 6e3
TA = 2500


# Since flying at Vmd, we know Cl and, hence Cd
CL = np.sqrt(CD0/K)
CD = CD0 + K * CL**2

# The definition of the drag coefficent can be rearranged for V, and using T = D, we *know* the thrust
atm = Atmosphere(alt)
rho = atm.density
V = np.sqrt(TA / (0.5 * rho * S * CD))

# and hence the weight from L = W
W = CL * (0.5 * rho * S * V**2)

print(f"The aircraft is travelling at {V[0]:1.2f}m/s TAS, and has a weight of {W[0]/1e3:1.1f}kN")

The thrust is now increased by 10%, find:

1. The new steady flight speed if the aircraft is held level at the same altitude.

2. If the lift curve slope is 5.7/rad, what change in aerodynamic incidence is required to maintain level flight at these new speed**s**

3. The steady rate of climb, and the climb angle achieved if the aircraft's speed is unchanged.

The hidden sections below correspond to solution, and answer for parts 1 through 3.

## First bit is easy
TA_new = TA * 1.1

lcs = 2*np.pi

# Get the A and B terms for the EAS equation
A = 0.5 * CD0 * rho * S
B = K * W**2 / 0.5 / rho / S

# Get the two possible speeds
Vs = np.sqrt(np.roots([A, -TA_new, B]))

print(f"The two possible steady flight speeds with the thrust increase are {Vs.min():1.1f}m/s and {Vs.max():1.1f}m/s")

# To find the change in incidence, we need to determine the two CLs that correspond to to those two flight speeds
CLs_new = W / (0.5 * rho * S * Vs**2)
print(CL)
print(CLs_new)
dCLs = CLs_new - CL
print(f"Flight at {Vs.min():1.1f}m/s requires a dCL of {dCLs.max():+1.2f} hence a change in incidence of\
 {np.degrees(dCLs.max()/lcs):+1.1f} deg \
and flight at {Vs.max():1.1f}m/s requires a dCL of {dCLs.min():+1.2f} hence a change in incidence of\
 {np.degrees(dCLs.min()/lcs):+1.1f} deg")

# CLimb angle is easy
D = CD * 0.5 * rho * S * V**2
gamma = np.degrees(np.arcsin((TA_new - D) / W))
print(f"The climb angle if the velocity remains constant is gamma = {gamma[0]:1.1f} deg")

Vclimb = V * (TA_new - D) / W

print(f"The associated climb rate is {Vclimb[0]:1.2f}m/s")
*(Note: the US spelling is maneuver, but it took me years of muscle memory training to spell manoeuvre correctly, and I won't be losing it easily.)*

# Acceleration, Manoeuvres, and Aircraft Loading

The preceding analysis has been constrained to *steady* flight - that is, with zero acceleration. For the cases of climb, the climb rate was assumed to be steady.

To understand unconstrained aircraft manoeuvres requires an understanding of accelerated flight.

Manoeuvre will be broken down into horizontal (e.g., flat or banked turns) and vertical manoeuvres (e.g., loops, pull-ups), comprising curvilinear motion. Such manoeuvres are the result of a force *perpendicular* to the flight path, giving a normal acceleration.

All of the manoevures discussed are the result of a **variation in lift**, which can be *large*. Consider that the dynamic pressure rises with the square of the forward speed, so a five-fold speed increase results in twenty-five times the aerodynamic forces.

Before discussing manoeuvres, a means to represent the allowable amount of load on an aircraft will be introduced. 

## Load Factor

The load that can be safely taken through an aircraft dictates the load limits on an aircraft - for this the **load factor** is introduced as a non-dimensional measure of the load variation.

```{math}
:label: LoadFactor
n=\frac{L}{W}
````

```{admonition} So - *what is the load factor for steady level flight?*
:class: dropdown
In steady level flight, the equilibrium steady flight condition is $L=W$ so $n=1$
```

There are two structural limits defined for aircraft:
- **Limit Loads**, $n_{l}$ are the loads at which *plastic deformation* will occur. At flight with $1<n<n_1$, *elastic structural deformation* will occur on parts of the aircraft, and the parts will return to the design or equilibrium position once the loads are removed

   If flight occurs at $n>n_l$, the aircraft will require inspection and likely replacement of parts.
   
   
- **Ultimate Loads**, $n_{u}$ are the loads at which *failure* will occur. At flight with $n>n_u$, *parts of the aircraft will break*

The numerical value of the load factor is an exercise in structural analysis, whereby the loads and their paths are applied to a model of the aircraft, and a determination of $n_l$ and $n_u$ can be made.

In general, $n_l$ and $n_u$ will be defined with a safety factor of 50% - such that plastic structural deformation may not actually occur until $n_l*1.5$. This should not be considered a margin to 'play with', however!

### Values of the load factor

FAR 23 (Federal Aviation Requirement) dictates the *minimum* load factor required for three categories of aircraft:
- Commuter Aircraft
- Utility Aircraft
- Aerobatic Aircraft

The minimum load factors are defined as (since this is from FAR 23, $W$ is defined in $lbf$)


| Aircraft Category | Minimum positive load factor, $n+$    | Minimum negative load factor, $n-$ |
|-------------------|---------------------------------------|------------------------------------|
| Normal/Commuter   | smaller of $2.1+\frac{24000}{W+1000}$ or $3.8$  | $0.4n+$                            |
| Utility           | $4.4$                                 | $0.4n+$                            |
| Aerobatic         | $6.0$                                 | $0.5n+$                            |

Often pilots will talk about *load factor* in terms of "g"s - for straight and level flight, 1$g$ feels like regular earth gravity, whilst an $n=2$ or $2g$ manoeuvre makes the occupants feel *twice as heavy*.

Since the load factor represents the amount of lift being produced, it is an easy and instructive means to define the structural limits of an aircraft - $e.g.,$ the loads for which the wings will break off.

### V-n diagram

```{admonition} Bear in mind...
:class: dropdown

In what's becoming a common phrase in this document - the following is a simplification of the theory, designed to give you a good insight into the physics of the problem. Construction of a full $V-n$ diagram is complicated and more of an exercise in understanding FAA certification than it is the flight physics.

What follows is a suitable explanation for an undergraduate aerospace engineer.

```

The values of the limit loads, and ultimate loads are presented on a graph vs. airspeed. For the following, the loads will be presented against *equivalent airspeed* because that enables a single graph to be plotted, but for real aircraft this is usually presented against *indicated airspeed*, with several lines representing different altitudes.

There are many different means of showing how to construct a $V-n$ diagram in textbook and online, but most seem geared up to helping pilots understand them rather than aerospace engineers. For example - the following show good examples of how to formulate a $V-n$ diagram, [website one](http://www.aviationchief.com/operating-flight-strength-v-g--v-n-diagrams.html), [website two](https://code7700.com/g450_limitations.htm#weight).

For the following example, a representative jet trainer aircraft will be used, with structural limit loads of $-3.0<n_l<7.0$ and ultimate loads of $-5.0<n_u<11.0$.

For a range of flight speeds up to $M=1.0$, the loads above can be plotted against $EAS$ taking into account the $n$ values above only.


import numpy as np
import plotly.graph_objects as go

# Limit loads
n_l = [-3.0, 7.0]

# Ultimate loads
n_u = [-5.0, 11.0]

# Make a figure
fig = go.Figure()

# Make a vector of equivalent airspeed (m/s)
VE = np.linspace(0, 340, 1000)

# Plot the Structural damage area
x_structural_damage = [VE.min(), VE.max()]
y_structural_damage = [n_l[1], n_l[1]]
y_structural_failure = [n_u[1], n_u[1]]

## Positive strucutral damage
# Plot a line of the structural damage
fig.add_trace(go.Scatter(x=VE, y=n_l[1] * np.ones(VE.shape),
    fill=None,
    mode='lines',
    line_color='indigo', name="+nl",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=x_structural_damage,
    y=y_structural_failure,
    fill='tonexty', # fill area between structural failure and structural Damage
    mode='none', fillcolor='rgba(255, 0, 0, 0.25)', name="Structural Damage", showlegend=False))

# Annotate the structural failure area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[0.5 * (n_l[1] + n_u[1])],
    mode='text',
    text="Structural Damage", showlegend=False))

# Add the ultimate load factor
fig.add_trace(go.Scatter(x=VE, y=n_u[1] * np.ones(VE.shape),
    mode='lines',
    line_color='red', name="+nu",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=VE, y=3*n_u[1] * np.ones(VE.shape),
    fill='tonexty', # fill area between structural failure and structural Damage
    mode='none', fillcolor='rgba(255, 0, 0, 0.55)', name="Structural Damage", showlegend=False, hoverinfo="none"))

# Annotate the structural failure area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[n_u[1] + 0.05 * (n_l[1] + n_u[1])],
    mode='text',
    text="Structural Failure", showlegend=False, hoverinfo="none"))




### Negative side



## Negative structural damage
x_structural_damage = [VE.min(), VE.max()]
y_structural_damage = [n_l[0], n_l[0]]
y_structural_failure = [n_u[0], n_u[0]]
# Plot a line of the structural damage
fig.add_trace(go.Scatter(x=VE, y=n_l[0] * np.ones(VE.shape),
    fill=None,
    mode='lines',
    line_color='indigo',
    name="-nl",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=x_structural_damage,
    y=y_structural_failure,
    fill='tonexty', # fill area between trace0 and trace1
    mode='none', fillcolor='rgba(255, 0, 0, 0.25)', name="Structural Damage", showlegend=False))

# Annotate the structural damage area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[0.5 * (n_l[0] + n_u[0])],
    mode='text',
    text="Structural Damage", showlegend=False))

# Add the ultimate load factor
fig.add_trace(go.Scatter(x=VE, y=n_u[0] * np.ones(VE.shape),
    fill=None,
    mode='lines',
    line_color='red', name="-nu",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=VE, y=3*n_u[0] * np.ones(VE.shape),
    fill='tonexty', # fill area between structural failure and structural Damage
    mode='none', fillcolor='rgba(255, 0, 0, 0.55)', name="Structural Damage", showlegend=False, hoverinfo="none"))


# Annotate the structural failure area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[n_u[0] + 0.05 * (n_l[0] + n_u[0])],
    mode='text',
    text="Structural Failure", showlegend=False, hoverinfo="none"))

# Change the limits
fig.update_yaxes(range= [1.2 * n_u[0], 1.2 * n_u[1]])

fig.update_layout(
    title="Representative Structural Damage and Failure Load Factors",
    xaxis_title="$V_E/\\text{m/s}$",
    yaxis_title="$n$",
)

# Dick around with the hover behaviour
fig.update_traces(hovertemplate=None)
fig.update_layout(hovermode="x unified")

fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='black')
fig.show()

At this stage, the $V-n$ diagram isn't particularly useful. You can hover over the graph and see that values of allowable load is constant with airspeed. 

The graph will be adapted by inclusion of other limitations. The first of which is that **at certain airspeeds, the aircraft will stall prior to $n_l$ being reached**, and therefore this influences the speed at which manoeuvres can be attempted safely.

It can be shown from the definition of the load factor, and the definition of the lift coefficient that the load factor associated with *stall* is given by

$$n_{stall}=\frac{C_{L,max}\,\tfrac{1}{2}\rho V^2\,S}{W}$$

If the aircraft is taken to have a wing area of 16m$^2$, and a weight of 53kN, and a $C_{L,max}$ of 1.6 with a $C_{L,min}$ of -1.0, then the variation of $n_{stall}$ can be overlaid on the previous graph

```{margin}
You might not have considered Clmin before - but it's the condition at which the flow around the wing will separate due to *negative* incidence
```


import numpy as np
import plotly.graph_objects as go

# Limit loads
n_l = [-3.0, 7.0]

# Ultimate loads
n_u = [-5.0, 11.0]

# Make a figure
fig = go.Figure()

# Make a vector of equivalent airspeed (m/s)
VE = np.linspace(0, 340, 1000)

# Plot the Structural damage area
x_structural_damage = [VE.min(), VE.max()]
y_structural_damage = [n_l[1], n_l[1]]
y_structural_failure = [n_u[1], n_u[1]]

## Positive strucutral damage
# Plot a line of the structural damage
fig.add_trace(go.Scatter(x=VE, y=n_l[1] * np.ones(VE.shape),
    fill=None,
    mode='lines',
    line_color='indigo', name="+nl",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=x_structural_damage,
    y=y_structural_failure,
    fill='tonexty', # fill area between structural failure and structural Damage
    mode='none', fillcolor='rgba(255, 0, 0, 0.25)', name="Structural Damage", showlegend=False))

# Annotate the structural failure area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[0.5 * (n_l[1] + n_u[1])],
    mode='text',
    text="Structural Damage", showlegend=False))

# Add the ultimate load factor
fig.add_trace(go.Scatter(x=VE, y=n_u[1] * np.ones(VE.shape),
    mode='lines',
    line_color='red', name="+nu",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=VE, y=3*n_u[1] * np.ones(VE.shape),
    fill='tonexty', # fill area between structural failure and structural Damage
    mode='none', fillcolor='rgba(255, 0, 0, 0.55)', name="Structural Damage", showlegend=False, hoverinfo="none"))

# Annotate the structural failure area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[n_u[1] + 0.05 * (n_l[1] + n_u[1])],
    mode='text',
    text="Structural Failure", showlegend=False, hoverinfo="none"))


# Add in stall
S = 16
W = 53e3
Clmax = 1.6
Clmin = -1.0
n_stall = Clmax * 0.5 * 1.225 * VE**2 * S / W
n_stall_negative = Clmin * 0.5 * 1.225 * VE**2 * S / W

## Get the maneovure speeds
Va = np.sqrt(n_l[1] * W / (Clmax * 0.5 * 1.225 * S))
fig.add_trace(go.Scatter(x=[Va], y=[n_l[1]],
    mode='markers+text',
    text="$V_A$",
    textposition="bottom right",
    showlegend=False))

Va2 = np.sqrt(n_l[0] * W / (Clmin * 0.5 * 1.225 * S))
fig.add_trace(go.Scatter(x=[Va2], y=[n_l[0]],
    mode='markers+text',
    text="$V_{A2}$",
    textposition="top right",
    showlegend=False))

# Overlay the stall n diagrams
# Positive
fig.add_trace(go.Scatter(x=VE, y=n_stall,
    mode='lines',
    line_color='red', name="Positive Stall",
    showlegend=True))

# Redo just up to Va to make sure the next fill is correct (else it fills above the limit load)
fig.add_trace(go.Scatter(x=VE[n_stall <= n_l[1]], y=n_stall[n_stall <= n_l[1]],
    mode='lines',
    line_color='red',
    showlegend=False, name="Positive Stall"))

## Put some filled areas in here to show the positive stall limit
V_stall_limited = np.linspace(0.1, Va, 100)
fig.add_trace(go.Scatter(
    x=V_stall_limited, y=n_l[1] * np.ones(V_stall_limited.shape),
    fill='tonexty', fillcolor='rgba(255, 255, 0, 0.55)', 
    name="Stall Limited", showlegend=False, hoverinfo="none"))

# Annotate the postitive stall limit
fig.add_trace(go.Scatter(
    x=[np.mean(V_stall_limited)],
    y=[0.5 * np.array([n_l[1] * np.ones(V_stall_limited.shape)]).mean()],
    mode='text',
    text="Stall Limited", showlegend=False, hoverinfo="none"))

# Negative
fig.add_trace(go.Scatter(x=VE, y=n_stall_negative,
    mode='lines',
    line_color='green', name="Negative Stall",
    showlegend=True))

# Redo just up to Va to make sure the next fill is correct (else it fills above the limit load)
fig.add_trace(go.Scatter(x=VE[n_stall_negative >= n_l[0]], y=n_stall_negative[n_stall_negative >= n_l[0]],
    mode='lines',
    line_color='green',
    showlegend=False, name ="Negative Stall"))

## Put some filled areas in here to show the negative stall limit
V_stall_limited = np.linspace(0.1, Va2, 100)
fig.add_trace(go.Scatter(
    x=V_stall_limited, y=n_l[0] * np.ones(V_stall_limited.shape),
    fill='tonexty', fillcolor='rgba(255, 255, 0, 0.55)', 
    name="Stall Limited", showlegend=False, hoverinfo="none"))

# Annotate the negative stall limit
fig.add_trace(go.Scatter(
    x=[np.mean(V_stall_limited)],
    y=[0.5 * np.array([n_l[0] * np.ones(V_stall_limited.shape)]).mean()],
    mode='text',
    text="Stall Limited", showlegend=False, hoverinfo="none"))




### Negative side
## Negative structural damage
x_structural_damage = [VE.min(), VE.max()]
y_structural_damage = [n_l[0], n_l[0]]
y_structural_failure = [n_u[0], n_u[0]]
# Plot a line of the structural damage
fig.add_trace(go.Scatter(x=VE, y=n_l[0] * np.ones(VE.shape),
    fill=None,
    mode='lines',
    line_color='indigo',
    name="-nl",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=x_structural_damage,
    y=y_structural_failure,
    fill='tonexty', # fill area between trace0 and trace1
    mode='none', fillcolor='rgba(255, 0, 0, 0.25)', name="Structural Damage", showlegend=False))

# Annotate the structural damage area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[0.5 * (n_l[0] + n_u[0])],
    mode='text',
    text="Structural Damage", showlegend=False))

# Add the ultimate load factor
fig.add_trace(go.Scatter(x=VE, y=n_u[0] * np.ones(VE.shape),
    fill=None,
    mode='lines',
    line_color='red', name="-nu",
    showlegend=False))

# Then a line of the structural failure that is filled to the structural damage
fig.add_trace(go.Scatter(
    x=VE, y=3*n_u[0] * np.ones(VE.shape),
    fill='tonexty', # fill area between structural failure and structural Damage
    mode='none', fillcolor='rgba(255, 0, 0, 0.55)', name="Structural Damage", showlegend=False, hoverinfo="none"))


# Annotate the structural failure area
fig.add_trace(go.Scatter(
    x=[np.mean(x_structural_damage)],
    y=[n_u[0] + 0.05 * (n_l[0] + n_u[0])],
    mode='text',
    text="Structural Failure", showlegend=False, hoverinfo="none"))

# Change the limits
fig.update_yaxes(range= [1.2 * n_u[0], 1.2 * n_u[1]])

fig.update_layout(
    title="Representative Structural Damage and Failure Load Factors",
    xaxis_title="$EAS in m/s$",
    yaxis_title="$n$",
)

# Dick around with the hover behaviour
# fig.update_traces(hovertemplate=None)
# fig.update_layout(hovermode="x unified")

fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='black')
fig.show()

#### Manoeuvre Speed

The intersection of the stall boundary and the limit load defines $V_A$, the **Manoeuvre Speed**. 

At speeds below $V_A$, fore/aft motion of the stick cannot produce enough load for structural damage to occur as the flow will separate before reaching an incidence at which $n_l$ would occur. Hence at speeds below $V_A$, the aircraft is *stall limited*.

Hence $V_A$ is the **highest speed for safe application of maximum control deflection**, whereas **at speeds above $V_A$, the controls inputs must be limited to avoid overloading the airframe**.

##### Manoeuvre Speed on a real aircraft

On a real aircraft, $V_A$ may be defined at a *lower* speed allowing for a dynamic overshoot.

Furthermore, $V_A$ is defined **only for pure pitching motion**. Combinations of pitch, roll, and yaw can lead to increased loads, as can *dynamic motion* which allows flow to stay *attached* for higher angles of attack than the steady state condition.

The latter proved fatal in 2001, when American Airlines Flight 587 took off from JFK. The Airbus A300-605R followed Japan Airlines Flight 47, and encountered *wake turbulence*.

The First Officer applied repeated opposite rudder inputs (which, as an aside, is a great way to set up a *Dutch Roll* oscillation), which increased the load on the vertical stabiliser until it ultimately sheared off - which occurred in <7s.

```{epigraph}
*The National Transportation Safety Board determines that the probable cause of this accident was the in-flight separation of the vertical stabilizer as a result of the loads beyond ultimate design that were created by the first officer’s unnecessary and excessive rudder pedal inputs. Contributing to these rudder pedal inputs were characteristics of the Airbus A300-600 rudder system design and elements of the American Airlines Advanced Aircraft Maneuvering Program (AAMP).*

-- [NTSB Accident Report](https://www.ntsb.gov/investigations/AccidentReports/Reports/AAR0404.pdf)
```
There were other contributing factors to the accident, such as the light pedal forces on the aircraft misleading the pilots to the tail aerodynamic forces. But the salient point here is that **the airframe was destroyed due to aerodynamic load at a velocity far lower than the manoeuvring speed**.


## Loops

If the pilot pulls back on the stick, provided there is sufficient thrust, the angle of attack will be increased and the lift will also increase. This increases the load factor.

### Constant Radius Loop

A 'perfect' *constant radius* loop is:
- Constant airspeed
- Constant radius

```{figure} ../Images/Loop.png
---
height: 300px
name: Loop
---
Constant Radius Loop
```
If the angular displacement is denoted by $\gamma$, with $\gamma=0$ being the bottom of the loop, increasing clockwise, then the equations of motion are, in the aircraft longitudinal direction
```{margin}
From motion in a circle, recall that centripetal (centre-seeking) acceleration is:

$a_c = \frac{V^2}{r}$

hence from Newton's second law, the force required to maintain a loop of radius $r$ is:

$F_c=\frac{m\,V^2}{r}$
```
$$T-D-W\sin\gamma=0$$

and

$$L - W\cos\gamma=\frac{W\,V^2}{g\,r}$$

So, at different points in the circle the equations of motion give, with $F_c = \frac{W\,V^2}{g\,r}$:

|         | Horizontal Equilibrium | Vertical Equilibrium |
|---------|------------------------|----------------------|
| Point A | $T-D=0$                | $L-W=F_c$            |
| Point B | $T-D-W=0$              | $L=F_c$              |
| Point C | $T-D=0$                | $L+W=F_c$            |
| Point D | $T-D+W=0$              | $L=F_c$              |

For the perfect loop, the normal acceleration is **constant**, and the load factor varies according to

$$n=\cos\gamma + \frac{V^2}{g\,r}$$

so at the different points of the loop above, the load factor is:

|         | Load Factor          |
|---------|----------------------|
| Point A | $1+\frac{V^2}{g\,r}$ |
| Point B | $\frac{V^2}{g\,r}$   |
| Point C | $\frac{V^2}{g\,r}-1$ |
| Point D | $\frac{V^2}{g\,r}$   |

Hence it is the load factor required to _initiate_ the loop that will set the minimum turn radius.


For reasons that can be readily appreciated, the *lift* and the *thrust* must be continually varied to maintain constant $F_C$ required for a constant radius loop. 

For these reasons, your average loop looks something more like this - consider a loop with **constant load factor**.

### Constant Load Factor Loop

The equation for the load factor in a constant radius loop can be rearranged for the radius

$$r=\frac{V^2}{g\,\left(n+\cos\gamma\right)}$$

*radius*, here might be a little confusing since in the above it refers to the radius of a theoretical circle that would be flown if, at any point in the loop, the *instantaneous* value of the *pitching velocity* were maintained.

Effectively, this means that the distance flow during a given section of the loop is inversely proportional to the load factor - so the aircraft flies *further* during the parts where $\cos\gamma=0$ since $r$ is *larger* there. This means that the shape flow is elongated vertically to give a *tighter* turn at the top and bottom of the loop.



```{figure} ../Images/ConstantLoadFactorLoop.png
---
height: 300px
name: Loop
---
A loop with constant load factor and constant speed (representative, not to scale)
```

```{admonition} Think: why is the constant radius loop shaped like a balloon?
:class: dropdown

From motion in a circle, a tighter radius of turn $r$ can be effected by a greater $F_c$.

Without perfect input by the pilot, the weight vector will *add* to $F_C$ at the top of the loop, *subtract* from it at the bottom, and vary between according the equations of motion already shown.

If the pilot is unable to adjust attitude *perfectly*, it likely that the turn radius will be lowest at the bottom of the loop, and largest at the top - resulting the 'imperfect' shape shown.

```

### Limits on loops
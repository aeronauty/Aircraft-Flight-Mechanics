# Climbing Flight

In climbing flight, $T>D$, so the aircraft cannot maintain equilibrium in straight and level flight.

The aircraft *ascends* with climb angle $\theta$, with the horizontal component of the aircraft weight opposing the thrust.


```{figure} ../Images/ClimbForces.png
---
height: 300px
name: ClimbForces
---
Forces on aircraft in a climb
```

```{admonition} What's actually happening in a climb?
:class: dropdown

Using the same reasoning as before, you can see that the aircraft is converting vertical kinetic energy into gravitational potential energy.

```

## Climb Angle

As for the glide angle, the climb angle can be determined by resolving forces perpendicular to the flight path

$$L=W\cos\theta$$

and parallel to the flight path

$$T-D=W\sin\theta$$

and from trigonometry, the climb angle is simply

$$\sin\theta=\frac{T-D}{W}$$

the rate of climb is $v_{climb}=-w_e$ and is

$$-w_e=V\sin\theta=\frac{V\left(T-D\right)}{W}$$

which gives the rate of increase of GPE

$$\underbrace{W\cdot v_{climb}}_{\substack{\text{Rate of increase}\\\text{of potential energy}}} = \underbrace{T\,V}_{\substack{\text{Thrust}\\\text{Power}}} - \underbrace{D\,V}_{\substack{\text{Drag}\\\text{Power}}}$$

## Climb Performance

The **maximum climb angle** requires the maximum **excess thrust**

The **maximum rate of climb** requires the maximum **excess power** 

This should feel intuitively correct to you, based upon what we know about glide angle/rate and $D_{min}/P_{min}$ and - obviously - these do not occur at the same speed. These depend on the powerplant type, and individual engine characteristics.

Furthermore, the small angle assumption cannot be made, so the climb rate and angles must be determined numerically. The following assumptions are a simplification, but will help to understand the relationships between excess thrust and power, and climbing flight.

### Powerplant assumptions

For **turbojet aircraft** and **low bypass ratio turbofan aircraft** is is assumed that **thrust remains constant with speed**, and accordingly power *increases* with speed.

For **turboprop aircraft** and **high bypass ratio turbofan aircraft** is is assumed that **power remains constant with speed**, and accordingly thrust *falls* with speed.

## Initialise aircraft parameters
from myst_nb import glue
from random import seed
from random import randint
import numpy as np

# Make aircraft parameters
W = np.arange(120e3, 190e3, 10e3)
S = np.arange(45, 85, 5)
CD0 = np.arange(0.008, 0.022, 0.002)
K = np.arange(0.025, 0.065, 0.005)
Clmax = np.arange(1.45, 1.95, 0.05)
TA = np.arange(15e3, 25e3, 2e3)



def getrandomvalue(vectin):
    val_out = vectin[randint(0, len(vectin)-1)]
    return val_out


# Get a random parameter
W = getrandomvalue(W)
S = getrandomvalue(S)
CD0 = getrandomvalue(CD0)
K = getrandomvalue(K)
Clmax = getrandomvalue(Clmax)
TA = getrandomvalue(TA)
PA_constant = TA*100

glue("W", W/1e3, display=False)
glue("S", S, display=False)
glue("CD0", CD0, display=False)
glue("K", K, display=False)
glue("Clmax", Clmax, display=False)
glue("TA", TA/1e3, display=False)
glue("PA_constant", PA_constant/1e6, display=False)


### Climb Curves - Turbojet

For a turbojet aircraft with a drag equation described by:

$$C_D = C_{D0} + K\cdot C_L^2$$

with $C_{D0}$={glue:text}`CD0:1.3f`, and $K$={glue:text}`K:1.3f`, a wing area of {glue:text}`S:1.0f`$\text{m}^2$, a weight of {glue:text}`W:1.3f`kN, and a maximum lift coefficient of {glue:text}`Clmax:1.3f`, capable of producing a thrust of {glue:text}`W:1.3f`kN at a given altitude, the climb rate and angles can be taken from the *difference between* the thrust available/required curves.

These plots are sensible to produce in EAS, for hopefully obvious reasons (if you're unsure why, ask on Slack).

```{admonition} Try and reproduce the plot below (ON YOUR OWN)
:class: dropdown

The source for this plot isn't included on the website (but it is included on GitHub). You should try and reproduce the plot using *some* computational method - Excel, MATLAB, Python using matplotlib, plotly, or whatever.

If you just download the source, you might trick yourself that you know what's going on - but you'll not actually learn anything.

It would be better to do some work to learn some coding and equation manipulation *now*, than lose your first graduate job when they find out that you bluffed your way through your undergraduate degree. That is, I don't care whether you've done your own homework when it comes in - but I promise that cheating on any of my homeworks, graded or not, will not be worth the trade-off you'll make for time now vs. being a shit engineer as a graduate.

Rant aside, I've also chosen not to make the source easily-available for some of these plots because I chose to use *plotly* to enable you guys to pan/zoom/interact with them online. I am far less confident with plotly than I am with matplotlib, so my code probably isn't anything to learn from technique-wise.

```
You can hover over the plots and check the values to see if you get the same answers as the ones I've produced.

Do your best to reproduce these plots as they may help you with a future homework - discuss on Slack and help each other if in doubt how to complete.

import plotly.graph_objects as go


rho_sl = 1.2255

# Get drag curve parameters
A = CD0 * 0.5 * rho_sl * S
B = K * W**2 / 0.5 / rho_sl / S

# Get minimum drag and power speeds
Vmd = (B/A)**.25
Vmp = (B/3/A)**.25

md = A * Vmd**2 + B * Vmd**-2
dmp = A * Vmp**2 + B * Vmp**-2 

# Make a velocity vector
VE = np.linspace(0.1, 300, 1000)

D = A*VE**2 + B*VE**-2
P = A*VE**3 + B*VE**-1

# Power available
PA = TA * VE

# Thrust and power deltas
dT = TA - D
dP = PA - D*VE

# Get the parameters to label - first best angle
v_bestclimb_angle = Vmd
d_bestclimb_angle = md
dd_bestclimb_angle = max(dT)
dp_bestclimb_angle = PA[VE==Vmd] - md*Vmd
p_bestclimb_angle = md*Vmd

# Then best climb rate - this has to be determined from the vectors
v_bestclimb_rate = VE[dP == max(dP)][0]
d_bestclimb_rate = D[dP == max(dP)][0]
p_bestclimb_rate = P[dP == max(dP)][0]
dp_bestclimb_rate = max(dP)
dd_bestclimb_rate = TA - max(dP)/v_bestclimb_rate


########################################################

# Make a plot - first do thrust
fig = go.Figure()
fig.add_trace(go.Scatter(x=VE, y=D, name="$T_R$"))
fig.add_trace(go.Scatter(x=[min(VE), max(VE)], y=[TA, TA], mode='lines', name="$T_A$"))
fig.add_trace(go.Scatter(x=VE, y=dT, name="$T_A - T_R$"))

# Annotations - best angle
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[d_bestclimb_angle],\
                         mode="markers+text", text="$\\theta_{max}$",\
                         textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[dd_bestclimb_angle], mode="markers", text="$\\theta_{max}$", textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))

# Annotations - best rate
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[d_bestclimb_rate],\
                         mode="markers+text", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                         marker=dict(color='DarkBlue')))
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[dd_bestclimb_rate],\
                         mode="markers", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                        marker=dict(color='DarkBlue')))

# Dress the plot
fig.update_layout(
    title="Thrust Available/Required for Turbojet",
    xaxis_title="Airspeed m/s EAS",
    yaxis_title="Thrust Available/Required "
)


fig.update_yaxes(range=[0, 3 * TA])


for trace in fig['data']: 
    if(trace['name'] == "Annotation"): trace['showlegend'] = False

fig.show()

########################################################
# Make a plot - second do power
fig = go.Figure()
fig.add_trace(go.Scatter(x=VE, y=P, name="$P_R$"))
fig.add_trace(go.Scatter(x=VE, y=PA, mode='lines', name="$P_A$"))
fig.add_trace(go.Scatter(x=VE, y=dP, name="$P_A - P_R$"))



# Annotations - best angle
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[p_bestclimb_angle],\
                         mode="markers+text", text="$\\theta_{max}$",\
                         textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[dp_bestclimb_angle], mode="markers", text="$\\theta_{max}$", textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))

# Annotations - best rate
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[p_bestclimb_rate],\
                         mode="markers+text", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                         marker=dict(color='DarkBlue')))
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[dp_bestclimb_rate],\
                         mode="markers", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                        marker=dict(color='DarkBlue')))

fig.update_yaxes(range=[0, 1 * max(PA)])

fig.update_layout(
    title="Power Available/Required for Turbojet",
    xaxis_title="Airspeed m/s EAS",
    yaxis_title="Power Available/Required "
)
for trace in fig['data']: 
    if(trace['name'] == "Annotation"): trace['showlegend'] = False

fig.show()


### Climb Curves - Turboprop

For the same aircraft, with a turboprop capable of producing a constant *power* of {glue:text}`PA_constant`MW, the thrust and power curves can be shown similarly: 


import plotly.graph_objects as go


rho_sl = 1.2255

# Get drag curve parameters
A = CD0 * 0.5 * rho_sl * S
B = K * W**2 / 0.5 / rho_sl / S

# Get minimum drag and power speeds
Vmd = (B/A)**.25
Vmp = (B/3/A)**.25

md = A * Vmd**2 + B * Vmd**-2
dmp = A * Vmp**2 + B * Vmp**-2 

# Make a velocity vector
VE = np.linspace(25, 300, 1000)

D = A*VE**2 + B*VE**-2
P = A*VE**3 + B*VE**-1

# Power available
PA = PA_constant
TA_prop = PA_constant/VE

# Thrust and power deltas
dT = TA_prop - D
dP = PA - D*VE

# Get the parameters to label - first best angle (maximum excess thrust)
index_bestclimb_angle = np.argmax(dT)
v_bestclimb_angle = VE[index_bestclimb_angle]
d_bestclimb_angle = D[index_bestclimb_angle]
dd_bestclimb_angle = dT[index_bestclimb_angle]
dp_bestclimb_angle = dP[index_bestclimb_angle]
p_bestclimb_angle = PA

# Then best climb rate - (maxmimum excess power)
v_bestclimb_rate = Vmp
d_bestclimb_rate = D[dP == max(dP)][0]
p_bestclimb_rate = PA
dp_bestclimb_rate = max(dP)
dd_bestclimb_rate = PA/Vmp - d_bestclimb_rate


########################################################

# Make a plot - first do thrust
fig = go.Figure()
fig.add_trace(go.Scatter(x=VE, y=D, name="$T_R$"))
fig.add_trace(go.Scatter(x=VE, y=TA_prop, mode='lines', name="$T_A$"))
fig.add_trace(go.Scatter(x=VE, y=dT, name="$T_A - T_R$"))

# Annotations - best angle
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[d_bestclimb_angle],\
                         mode="markers+text", text="$\\theta_{max}$",\
                         textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[dd_bestclimb_angle], mode="markers", text="$\\theta_{max}$", textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))

# Annotations - best rate
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[d_bestclimb_rate],\
                         mode="markers+text", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                         marker=dict(color='DarkBlue')))
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[dd_bestclimb_rate],\
                         mode="markers", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                        marker=dict(color='DarkBlue')))

# Dress the plot
fig.update_layout(
    title="Thrust Available/Required for Turboprop",
    xaxis_title="Airspeed m/s EAS",
    yaxis_title="Thrust Available/Required "
)


fig.update_yaxes(range=[0, 3 * TA])


for trace in fig['data']: 
    if(trace['name'] == "Annotation"): trace['showlegend'] = False

fig.update_xaxes(range=[0, 300])

        
fig.show()

########################################################
# Make a plot - second do power
fig = go.Figure()
fig.add_trace(go.Scatter(x=VE, y=P, name="$P_R$"))
fig.add_trace(go.Scatter(x=[min(VE), max(VE)], y=[PA, PA], mode='lines', name="$P_A$"))
fig.add_trace(go.Scatter(x=VE, y=dP, name="$P_A - P_R$"))



# Annotations - best angle
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[p_bestclimb_angle],\
                         mode="markers+text", text="$\\theta_{max}$",\
                         textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))
fig.add_trace(go.Scatter(x=[v_bestclimb_angle], y=[dp_bestclimb_angle], mode="markers", text="$\\theta_{max}$", textposition="top center", name="Annotation", marker=dict(
            color='LightSkyBlue'
            )))

# Annotations - best rate
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[p_bestclimb_rate],\
                         mode="markers+text", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                         marker=dict(color='DarkBlue')))
fig.add_trace(go.Scatter(x=[v_bestclimb_rate], y=[dp_bestclimb_rate],\
                         mode="markers", text="$v_{climb,max}$",\
                         textposition="top center", name="Annotation",\
                        marker=dict(color='DarkBlue')))

fig.update_yaxes(range=[0, 2 * PA])
fig.update_xaxes(range=[0, 300])

fig.update_layout(
    title="Power Available/Required for Turboprop",
    xaxis_title="Airspeed m/s EAS",
    yaxis_title="Power Available/Required "
)
for trace in fig['data']: 
    if(trace['name'] == "Annotation"): trace['showlegend'] = False

fig.show()


## Climb Performance: Summary

The **maximum climb rate** is given by the **maximum excess power**. You can think of this as the exchange of thrust energy to GPE.

The **maximum climb angle** is given by the **maximum excess thrust**. This is where the least horizontal resistance is experienced.

Look at the table below. Confirm using the plots that this is correct.

|                     | Propeller Aircraft | Jet Aircraft |
|---------------------|--------------------|--------------|
| Maximum Climb Rate  | At $V_{mp}$        | $>V_{mp}$    |
| Maximum Climb Angle | $<V_{md}$          | At $V_{md}$  |

Turboprops tend to have superior climb performance - but occurs at a lower speed.


# Range and Endurance

Range and endurance have been mentioned in the preceding sections - and we have introduced that for *maximum range* the pilot should fly at $V_{md}$, whilst to fly for *maximum endurance* the pilot should fly at $V_{mp}$. Range and endurance are intuitive concepts:
- **Range** ($R$): The maximum horizontal distance that an aircraft can cover.
- **Endurance** ($E$): The time an aircraft can remain in flight

In the following analysis, the range and endurance for certain fuel quantities will be determined. For (hopefully) obvious reasons, some further definitions of range will help us here

## Range subdefinitions

1. **Safe Range**: The maximum distance between two airfields, for which an aircraft can fly a safe a reliable mission with a given payload. 
    - This is an involved calculation involving take-off/landing/weather/diversion allowances etc. - there isn't an easy means to do this calculation, so tends to be performed computationally.
    - For aircraft performance there are some more simple definitions of *range*:

2. **Still Air Range (SAR)**: The maximum distance possible if an aircraft takes off, climbs to cruise altitude, and then cruises until all fuel is expended.
    - Obviously not desirable to run out of fuel at altitude, but SAR gives a good indication of the influence of aircraft parameters on range.

3. **Gross Still Air Range (GSAR)**: The maximum distance possible if an aircraft commences cruise at altitude and continues until all fuel is expended.
    - The relationship between SAR and GSAR tends to be easy to define.
    - GSAR much easier to calculate
    - What will be covered here
    
## Defining the problem

To calculate GSAR, you might think that we need to:
- find out the fuel flow rate, $\dot{m}_{fuel}$ for thrust/power associated with $V_{md}$ 
- get the endurance from the fuel mass, $m_{fuel}$ divided by the flow rate $E=\frac{m_{fuel}}{\dot{m}_{fuel}}$
- hence $R=E\cdot V_{md}$

The above reasoning is effectively how range is determined, but there are some complications that you may/may not be considering:
- Aircraft take-off with a *lot* of fuel, so the **aircraft weight changes with time** and accordingly so do almost all the parameters we have considered up to this point
- This means that some trade-offs *have* to be made in efficiency to allow a reasonable cruise - and we will see these

## Breguet Range Equation

The Breguet Range Equation (BRE) is named after a French aircraft designer, but was actually derived in the 1920's by J G Coffin.

```{admonition} History and namesakes...
:class: dropdown
I've loosely read the history of the BRE and it being Coffin who actually came up with it in NACA Report 1969, but I've never actually delved into the legacy of this equation. If you wish to, and suggest a correct here, feel free.
```
The BRE allows a simple means to calculate GSAR, and can be defined in words as:

$$\substack{\text{"The rate of}\\\text{aircraft mass reduction"}}=\substack{\text{"The rate of}\\\text{fuel mass burned"}}$$

A parameter, $f$, is introduced which is:
- Thrust Specific Fuel Consumption (TSFC) for a **turbojet**
    $f$ - **Mass of fuel burned per unit of thrust per second**
    
- Specific Fuel Consumption (SFC) for a **turboprop**
    $f$ - **Mass of fuel burned per unit of power per second**
    
The analysis is slightly different for jet and propeller-driven aircraft, so jet aircraft will be explored first.

## BRE - Jet Aircraft

With $f$ defined as the *mass of fuel burned per unit of thrust per second*, the SI units are $\frac{\text{kg}}{\text{N}\cdot\text{s}}$, and these are what you *must* use in equation form (if you're using SI units), but $f$ can be defined in other units such as $\frac{\text{kg}}{\text{kN}\cdot\text{hr}}$ so you must remember to convert.

The BRE for a jet aircraft is:

$$\frac{\text{d}W}{\text{d}t}=-f\,g\,T$$

which can be rearranged for the time

$$\text{d}t = -\frac{\text{d}W}{f\,g\,T}$$

since the endurance/range is defined by *cruise* conditions, the equilibrium steady flight conditions of $T=D$ and $L=W$ can be utilised such that

$$T=\frac{D}{L}W=\frac{C_D}{C_L}W$$

which can be substituted into the BRE to give

$$\text{d}t = -\frac{1}{f\,g}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

for constant lift-to-drag ratio and TSFC, the equation above can be integrated with the limits $t_{end}$ and $t_{start}$ corresponding to $W_{end}$ and $W_{start}$. This yields the endurance, $E$:

$$E=t_{end}-t_{start}=\frac{1}{f\,g}\frac{C_L}{C_D}\ln\left|\frac{W_{start}}{W_{end}}\right|$$

and hence the range is given if it is assumed TAS remains constant 

```{math}
:label: BRE
R=\frac{V}{f\,g}\frac{C_L}{C_D}\ln\left|\frac{W_{start}}{W_{end}}\right|
```


### What maximises range?

The equation above gives the design/mission choices that help maximise range:

```{figure} ../Images/CruiseClimbBRE.png
---
height: 300px
name: CruiseClimbBRE
---
```

### How is the BRE utilised?

In the Breguet Range Equation, Equation {eq}`BRE`, some parameters are dictated by the problem:
- $W_{start}$ is the weight of the aircraft including fuel
- $W_{end}$ is the weight of the aircraft with no fuel, or with a certain mandated reserve
- $f$ is the TSFC and will generally be given in a problem
- $g$ is accleration due to gravity, and since you're an aerospace engineer you should use $g=9.80665\frac{\text{m}}{\text{s}^{2}}$

```{margin}
*When I was an undergrad...*

...we went through deriving $g$ using Newton's law of gravitation - due to the size of this course, there isn't enough room. [Have a look here instead](https://earth.esa.int/web/guest/-/gravity-in-detail-5728).
```
Other parameters are unknown - so $V$, $C_L$, and $C_D$ need to be *constrained* (defined in terms of other parameters) in order to use Equation {eq}`BRE` to determine the possible range.

In each of these cases, the *range function* is replaced with something else.

```{figure} ../Images/RangeFunction.png
---
height: 300px
name: RangeFunction
---
```
The 'range function' is the expression $V\frac{C_L}{C_D}$ and clearly maximum range is given by the maximum value thereof.

In practice, this means replacing $V\frac{C_L}{C_D}$ with an equivalent expression representing the variation of the parameters therein, by finding another means of representing $V$ as a function of $C_L$ or $C_D$.

Three different means of doing this will be explored - first the theory will be explained, and then numerical examples will follow.

### Most Efficient - Cruise Climb

The most aerodynamically efficient cruise would be with constant best $C_L/C_D$, and constant $f$. These have some implications. Have a look at these in the dropdown below:

```{admonition} Implication of the most efficient cruise
:class: dropdown

Above, it was stipulated that the lift-to-drag ratio ($C_L/C_D$), TSFC $f$, and $V_{T}$ were constant. These assumptions have some implications:
- Fuel burn causes a reduction in aircraft weight - so as $W$ drops, the dimensional value of lift, $L$, must also drop ($L=W$)
- Since TAS is constant, for $L$ to drop, either $C_L$ must drop or $\sigma$ must reduce
    - But it was also assumed that the aircraft flies at the best aerodynamic efficiency, and that $C_L/C_D$ was constant, which implies a constant angle of attack
    - Therefore, $\sigma$ must reduce, and hence **altitude must increase** for an efficient cruise
- As $C_L$ reduces, for constant $C_L/C_D$, $C_D$ must reduce in proportion to $\sigma$ also
    - Since $T=D$, the thrust must reduce with altitude
    - For constant TSFC, $f$, the **throttle setting must be constant**
    - Hence thrust must be modelled from $T=T_{SL}\cdot\sigma^n$ with $n=1$
    - As discussed previously, $n$ is dependent on altitude and engine type - and the thrust model above is a vast simplification *anyway*
    - $n=1$ is more suitable in the *stratosphere* (above 11km-ish), where the temperature falls with altitude (slightly more complicated than this, but it works enough for us).
    - Below 11km, in the *troposphere*, the temperature falls with altitude - and hence $n<1$, so thrust falls less rapidly with altitude. To maintain constant $C_L/C_D$ requires the pilot to reduce the throttle to maintain $V$ or $C_L$, which would change the TSFC

```
The derivation has arrived at the so-called *cruise-climb* case, whereby the aircraft altitude rises along the cruise to maintain peak aerodynamic efficiency. This is infrequently allowed by air traffic control - but aircraft often follow a stepped-climb, which is a planned series of altitude changes to allow some of the benefits.

Further to the above, two cruise-climb cases can be explored:
1. **Throttle Restricted** - The throttle setting is *fixed*, and the aircraft must vary altitude to maintain constant $C_L/C_D$
2. **Throttle Unrestricted** - The throttle can be altered to maintain constant $C_L/C_D$

#### Cruise-Climb 1: Throttle Restricted

'Throttle-restricted' means that the throttle is kept constant, and the maximum range therefore depends on the variation of thrust with altitude, hence:

$T=T_{sl}\cdot\sigma$

Since the variation of altitude is unknown, $T=D$ will be used to develop an expression for $V$ that does not contain $\sigma$:

$$\begin{aligned}T &= T_{sl}\cdot\sigma\\
&= D\end{aligned}$$

from the definition of the drag coefficient

$$\begin{aligned}T_{sl}\,\sigma&= C_D\,\frac{1}{2}\,\rho_{sl}\,\sigma\,V^2\,S\end{aligned}$$

and hence velocity can be represented in terms of constants and the drag coefficient

$$\implies V=\sqrt{\frac{T_{sl}}{\frac{1}{2}\,\rho_{sl}\,S\,C_D}}$$

so the range function becomes

$$V\,\frac{C_L}{C_D}=\sqrt{\frac{T_{sl}}{\frac{1}{2}\,\rho_{sl}\,S\,C_D}}\frac{C_L}{C_D}$$
```{math}
:label: ThrottleRestricted
V\,\frac{C_L}{C_D}=\sqrt{\frac{2\,T_{sl}}{\rho_{sl}\,S}}\frac{C_L}{C_D^{3/2}}
```

So for **maximum range for throttle restricted cruise climb** $\frac{C_L}{C_D^{3/2}}$ must be maximised. In practice it is easier to minimise the reciprocal - inserting the drag equation:

$$\frac{C_D^{3/2}}{C_L} = \frac{\left(C_{D0} + K\cdot C_L^2\right)^{3/2}}{C_L}$$

via the quotient rule
```{margin} 
I'm sure you recall the quotient rule, but here it is anyway: $\text{d}\frac{u}{v}=\frac{v\text{d} u - u\text{d} v}{v^2}$
```

$$\frac{\text{d}\frac{C_D^{3/2}}{C_L}}{\text{d}C_L} = \frac{2\cdot K\cdot C_L^2\tfrac{3}{2}\left(C_{D0}+K\cdot C_L^2\right)^{1/2} - \left(C_{D0} + K\cdot C_L^2\right)^{3/2}}{C_L^2}$$

which has a maximum at 

$$2\cdot C_{D0} = 2\cdot K\cdot C_L^2$$

hence defining the lift and drag coefficients for Throttle-Restricted Cruise-Climb as:

$$\begin{aligned}C_{D_{trcc}} &= \frac{3}{2}\cdot C_{D0}\label{eq:CDmaxRCT}\\
	C_{L_{trcc}} &= \sqrt{\frac{C_{D0}}{2\cdot K}}\end{aligned}$$

you can see that the aerodynamic coefficients above are defined in terms of constants - so these can be determined from design characteristics. Once these are determined, they are substituted into the range function, Equation {eq}`ThrottleRestricted`, which is in turn substituted into the BRE Equation {eq}`BRE` - then this is integrated to yield the range.

#### Cruise-Climb 2: Throttle Unrestricted 

If the throttle can change to maximise aerodynamic efficiency, then the velocity can remain constant. Hence $V$ is defined by the start altitude and weight. In this case, the Aircraft Speed Equation {eq}`ACSpeedEquation` can be used to set $V$:

$$\begin{aligned}
    V &= \sqrt{\frac{W}{\tfrac{1}{2}\cdot\sigma_1\cdot\rho_{SL}\cdot S\cdot C_L}}\\
    \therefore V\cdot\frac{C_L}{C_D} &= \sqrt{\frac{W}{\tfrac{1}{2}\cdot\sigma_1\cdot\rho_{SL}\cdot S}}\cdot\frac{C_L^{1/2}}{C_D}\label{eq:unconstrainedRF}\end{aligned}$$
    
So for **maximum range for throttle unrestricted cruise-climb**, we need to find cruise $C_L$ such that $\frac{C_L^{\tfrac{1}{2}}}{C_D}$ is a maximum:

$$\begin{aligned}\frac{C_D}{C_L^{1/2}} &= \frac{C_{D0}+K\cdot C_L^2}{C_L^{1/2}}\\
 &= \frac{C_{D0}}{C_L^{1/2} + K\cdot C_L^{3/2}}\\
 \frac{\text{d}\frac{C_D}{C_L^{1/2}}}{\text{d}C_L} &= -\frac{1}{2}\frac{C_{D0}}{C_L^{3/2}}+K\cdot\frac{3}{2}\cdot C_L^{1/2}\end{aligned}$$


max range given at the minima of this equation

$$\begin{aligned}C_{D0}&=3\cdot K\cdot C_L^2\\
    \therefore C_{D_{tucc}}&=\frac{4}{3}C_{D0}\label{eq:cdmaxr2}\\
    \therefore C_{L_{tucc}}&=\sqrt{\frac{C_{D0}}{3K}}\label{eq:clmaxr2}\end{aligned}$$
    
the above $C_L$ and $C_D$ are used as before the find the maximum range.

### Constant Altitude Cruise

Instead of cruise-climb, a constant altitude cruise allows the velocity to vary - the range will obviously be different.

Starting again with the the differential range expression where $dS$ is the differential displacement:

$$\text{d}S = -\frac{V}{f\,g}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

Since $\sigma$ is held constant, the aircraft speed equation can be substituted in the above

$$\begin{align}
	dS &= -\frac{1}{fg}\cdot\sqrt{\frac{2}{\rho S}}\frac{C_L^{1/2}}{C_D}\cdot\frac{\text{d} W}{W^{1/2}}\\
	R = S_E - S_S &= \sqrt{\frac{8}{\rho S}}\frac{1}{fg}\frac{C_L^{1/2}}{C_D}\left(W_S^{1/2}-W_E^{1/2}\right)
\end{align}$$

for this case, altitude and $C_L$ are held constant. As $W$ reduces, $L$ reduces, so $V$ must reduce. Hence the range must be less as the aircraft is flying *slower* from $t>0$.

Since $C_D$ is constant, $D$ and hence $T$ must reduce - so throttle must be reduced and a variation in the fuel consumption will occur.

For this case, an average value of $f$ must be used, or treat as a series of shorter steps and integrate numerically.

### Actual Cruise

A third, and much more common cruise profile is to cruise at a constant altitude, at a constant $V$. Hence to reduce $L$ to match the reduction in weight, $\alpha$ must be reduced, changing $C_L/C_D$. This is a more complex analysis and beyond the scope of this course.

## Cruise Comparisons

For an aircraft with the following parameters:

|          |             |
|:--------:|:-----------:|
|  $W_S$   |    100kN    |
|  $W_F$   |    60kN     |
|   $S$    |   50m$^2$   |
| $C_{D0}$ |    0.02     |
|   $K$    |    0.05     |
| $T_{SL}$ |    20kN     |
|   $f$    | 0.0001kg/Ns |

For a cruise starting at 12km altitude, the three different cruise ranges can be calculated

The code below calculates the different cruise-climb cases - note that these calculations could easily be performed by hand.

import numpy as np
from myst_nb import glue
from ambiance import Atmosphere


# Aircraft parameters
Ws = 100*1e3
We = 60*1e3
S = 50
CD0 = 0.02
K = 0.05
T_sl = 20*1e3
f = 0.0001
alt = 12 # altitude in km

g = 9.80665 # Gravitational acceleration
rho_sl = 1.225

############################################
## Thrust restricted cruise-climb parameters
############################################
CL_trcc = np.sqrt(CD0/2/K)
CD_trcc = 3/2 * CD0
range_function_trcc = np.sqrt(2 * T_sl / rho_sl / S) * CL_trcc / CD_trcc ** (3/2)
range_trcc = 1 / f / g * range_function_trcc * np.log(Ws/We)

# Save these values
glue("CD_trcc", CD_trcc, display=False);
glue("CL_trcc", CL_trcc, display=False);
glue("range_function_trcc", range_function_trcc, display=False);
glue("range_trcc", range_trcc/1e3, display=False);

############################################
## Thrust unrestricted cruise-climb parameters
############################################
mosphere = Atmosphere(alt*1000)
rho = mosphere.density[0]
sig_1 = rho/rho_sl

CL_tucc = np.sqrt(CD0/3/K)
CD_tucc = 4/3 * CD0
range_function_tucc = np.sqrt(Ws / (0.5 * sig_1 * rho_sl * S)) * CL_tucc ** .5 / CD_tucc
range_tucc = 1 / f / g * range_function_tucc * np.log(Ws/We)

# Save these values
glue("CD_tucc", CD_tucc, display=False);
glue("CL_tucc", CL_tucc, display=False);
glue("range_function_tucc", range_function_tucc, display=False);
glue("range_tucc", range_tucc/1e3, display=False);


### Thrust Restricted

Using the expressions derived above, the lift coefficient for Thrust restricted cruise climb is {glue:text}`CL_trcc:1.3f`, and the drag coefficient is {glue:text}`CD_trcc:1.3f`. This gives the range function as {glue:text}`range_function_trcc:1.3f` which yields a range of {glue:text}`range_trcc:1.0f`km

### Thrust Unrestricted

Using the expressions derived above, the lift coefficient for Thrust unrestricted cruise climb is {glue:text}`CL_tucc:1.3f`, and the drag coefficient is {glue:text}`CD_tucc:1.3f`. This gives the range function as {glue:text}`range_function_tucc:1.3f` which yields a range of {glue:text}`range_tucc:1.0f`km

## Variation of range with lift coefficient, airspeed

Recall that the lift coefficient is effectively a measure of the aircraft *cruise speed*. The range can be plotted vs. lift coefficient and forward speed for the two different cruise-climb cases over a range of starting altitudes.

```{admonition} Beware of source for the plots below...
:class: dropdown

Producing the plots below is fairly simple - but in order to get the labels and legend to work correctly, there's a bit of obscure logic flow in the way the plot is created.

That is, it makes it look more complicated than it actually is (and it probably could be done better if I knew my way around plotly better).
```

import plotly.graph_objects as go
## Note that there's a lot of slightly peculiar logic in the code below that enables the annotation and the legend
# to to be printed. You don't need to worry about it.

# Define a range of Cls
CLrange = np.linspace(.1, 1.2, 1000)

# Drag is given from the drag model
CDrange = CD0 + K * CLrange**2

# The CL and CD for TRCC and TUCC are defined above, so they can be reused here

# Open three figures
fig = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()


# Make sigma function for convenience
def sigma_function(alt):
    mosphere = Atmosphere(alt)
    rho = mosphere.density[0]
    sig = rho/rho_sl
    return sig

# Iterate over altitudes
for i, h in enumerate(np.arange(4, 14, 2)*1e3):
    # Get the density ratio
    sig = sigma_function(h)
    
    # Determine the cruise speed in TAS at this altitude
    Vtas_knots = np.sqrt(Ws / (.5 * sig * rho_sl * S * CLrange)) /.5144444
    Veas_knots = np.sqrt(Ws / (.5 * rho_sl * S * CLrange)) /.5144444
    
    ######## Thrust Restricted
    # Get the range function (thrust restricted)
    range_funct_trcc = np.sqrt(2 * T_sl / (rho_sl * S)) * CLrange / CDrange ** (3/2)
    
    # Get the range for this altitude
    R_trcc = 1 / f / g * range_funct_trcc * np.log(Ws/We) / 1e3
    
    # Plot it
    if i == 0:
        fig.add_trace(go.Scatter(x=CLrange, y=R_trcc, mode="lines", name=f"Thrust-Restricted",  line=dict(width=4,
                              dash='dash', color='red')))
        fig2.add_trace(go.Scatter(x=Veas_knots, y=R_trcc, mode="lines", name=f"Thrust-Restricted",  line=dict(width=4,
                              dash='dash', color='red')))
        fig3.add_trace(go.Scatter(x=Vtas_knots, y=R_trcc, mode="lines", name=f"Thrust-Restricted",  line=dict(width=4,
                              dash='dash', color='red')))
    else:
        fig.add_trace(go.Scatter(x=CLrange, y=R_trcc, mode="lines", name="DontPrint",  line=dict(width=4,
                              dash='dash', color='red')))
        fig2.add_trace(go.Scatter(x=Veas_knots, y=R_trcc, mode="lines", name="DontPrint",  line=dict(width=4,
                              dash='dash', color='red')))
        fig3.add_trace(go.Scatter(x=Vtas_knots, y=R_trcc, mode="lines", name="DontPrint",  line=dict(width=4,
                              dash='dash', color='red')))
    
   
    ######## Thrust Unrestricted
    # Get the range function (thrust unrestricted)
    range_funct_tucc = np.sqrt(Ws / (0.5 * sig * rho_sl * S)) * CLrange ** .5 / CDrange
    
    # Get the range for this altitude
    R_tucc = 1 / f / g * range_funct_tucc * np.log(Ws/We) / 1e3
    
    # Plot it
    if i == 0:
        fig.add_trace(go.Scatter(x=CLrange, y=R_tucc, mode="lines", name="Thrust-Unrestricted", line=dict(width=4, color='blue')))
        fig2.add_trace(go.Scatter(x=Veas_knots, y=R_tucc, mode="lines", name="Thrust-Unrestricted", line=dict(width=4, color='blue')))
        fig3.add_trace(go.Scatter(x=Vtas_knots, y=R_tucc, mode="lines", name="Thrust-Unrestricted", line=dict(width=4, color='blue')))
    else:
        fig.add_trace(go.Scatter(x=CLrange, y=R_tucc, mode="lines", name="DontPrint", line=dict(width=4, color='blue')))
        fig2.add_trace(go.Scatter(x=Veas_knots, y=R_tucc, mode="lines", name="DontPrint", line=dict(width=4, color='blue')))
        fig3.add_trace(go.Scatter(x=Vtas_knots, y=R_tucc, mode="lines", name="DontPrint", line=dict(width=4, color='blue')))
    
    ######## Label the altitudes: 
    if i == 0: fig.add_trace(go.Scatter(x=[CLrange[0]], y=[R_trcc[0]], mode="text", text="All altitudes", textposition="middle right", name="Annotation"))
    fig.add_trace(go.Scatter(x=[CLrange[0]], y=[R_tucc[0]], mode="text", text=f"{h/1e3:1.0f}km", textposition="middle left", name="DontPrint"))
    
    if i == 0: fig2.add_trace(go.Scatter(x=[Veas_knots[0]+16*i + 2], y=[R_trcc[0]], mode="text", text="All altitudes", textposition="middle right", name="Annotation"))        
    fig2.add_trace(go.Scatter(x=[Veas_knots[0]+2], y=[R_tucc[0]], mode="text", text=f"{h/1e3:1.0f}km", textposition="middle right", name="Annotation"))
    
    fig3.add_trace(go.Scatter(x=[Vtas_knots[0]], y=[R_tucc[0]], mode="text", text=f"{h/1e3:1.0f}km", textposition="bottom center", name="Annotation"))
    fig3.add_trace(go.Scatter(x=[Vtas_knots[0]], y=[R_trcc[0]], mode="text", text=f"{h/1e3:1.0f}km", textposition="bottom center", name="Annotation"))

# Determine the different Cls to plot for comparison    
CL_trcc = np.sqrt(CD0/2/K)
CL_tucc = np.sqrt(CD0/3/K)
CL_md = np.sqrt(CD0/K)
CL_mp = np.sqrt(3*CD0/K)


# Overlay lines for different Cls on the first figure only
fig.add_trace(go.Scatter(x=[CL_trcc, CL_trcc], y=[0, 1500], name="DontPrint", mode="lines"))
fig.add_trace(go.Scatter(x=[CL_tucc, CL_tucc], y=[0, 1500], name="DontPrint", mode="lines"))

fig.add_trace(go.Scatter(x=[CL_trcc], y=[200], mode="text", text="$C_L=\sqrt{\\frac{C_{D0}}{2\,K}}$", textposition="middle right", name="DontPrint"))
fig.add_trace(go.Scatter(x=[CL_tucc], y=[200], mode="text", text="$C_L=\sqrt{\\frac{C_{D0}}{3\,K}}$", textposition="middle left", name="DontPrint"))

    
    
# Remove junk legend entries - this would be more efficient if I weren't lazy
for trace in fig['data']: 
    if (trace['name'] == "DontPrint") or (trace['name'] == "Annotation"): trace['showlegend'] = False

for trace in fig2['data']: 
    if (trace['name'] == "DontPrint") or (trace['name'] == "Annotation"): trace['showlegend'] = False
        
for trace in fig3['data']: 
    if (trace['name'] == "DontPrint") or (trace['name'] == "Annotation"): trace['showlegend'] = False
    

fig.update_layout(
    title="Thrust Restricted and Unrestricted Ranges vs. Lift Coefficient for different starting altitudes",
    xaxis_title="$C_L$",
    yaxis_title="Range/km",
)

fig2.update_layout(
    title="Thrust Restricted and Unrestricted Ranges vs. EAS for different starting altitudes",
    xaxis_title="$V_{E}/\\text{kn}$",
    yaxis_title="Range/km",
)

fig3.update_layout(
    title="Thrust Restricted and Unrestricted Ranges vs. TAS for different starting altitudes",
    xaxis_title="$V/\\text{kn}$",
    yaxis_title="Range/km",
)
    
# Figure 1
fig.update_xaxes(range=[0, 1.5])
fig.update_yaxes(range=[0, 1500])
fig2.update_yaxes(range=[0, 1500])
fig2.update_xaxes(range=[0, 500])
fig3.update_yaxes(range=[0, 1500])
fig.show()

fig2.show()
fig3.show()


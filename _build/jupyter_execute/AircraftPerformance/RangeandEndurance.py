Range and endurance have been mentioned in the preceding sections - and we have introduced that for *maximum range* the pilot should fly at $V_{md}$, whilst to fly for *maximum endurance* the pilot should fly at $V_{mp}$.

However - the above speeds are valid **only for unpowered flight**. So these speeds are suitable for a glider, but once an engine is introduced to an aircraft, these speeds no longer give the maximum range or the maximum endurance.

Furthermore, the propulsor type changes the speeds for both. In the following section, the best range and endurance speeds for jet and propeller-driven aircraft will be explored.

# Range and Endurance

Range and endurance are intuitive concepts:
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

$$\substack{\text{"The rate of}\\\text{aircraft weight reduction"}}=\substack{\text{"The rate of}\\\text{fuel weight burned"}}$$

The BRE was first implemented for propeller aircraft, and is derived differently for thrust and power engines. In the following it will be derived separately for the two engines types.

### Engine fuel burn

To calculate the engine fuel burn of both types of engine, two new parameters are introduced

A parameter, $c_t$, is introduced which is:
- Thrust Specific Fuel Consumption (TSFC) for a **turbojet**
    $c_t$ - **mass of fuel burned per unit of thrust per second**
    
- Specific Fuel Consumption (SFC) for a **turboprop**
    $c$ - **mass of fuel burned per unit of power per second**

#### Thrust specific fuel consumption - units

In the above, the SI units are $\left\{c_t\right\}=\left\{\frac{kg}{N\cdot s}\right\}$ which has dimensions of $\left[\frac{\text{L}}{\text{T}}\right]$. You might see this expressed as $\frac{g}{kN\,s}$, which is actually the same units.

In US customary units, this is  $\left\{c_t\right\}=\left\{\frac{lb}{lbf\cdot s}\right\}$.

You may see some slightly different units such as $\left[\frac{kg}{kN\cdot hr}\right]$ so be sure to convert to SI or US customary base units

#### Specific fuel consumption - units

In the above, the SI units are $\left\{c\right\}=\left\{\frac{kg}{W\cdot s}\right\}$ which has dimensions of $\left[\frac{\text{T}^2}{\text{L}^2}\right]$. You might see this expressed as $\frac{g}{kW\,s}$, which is actually the same units.

In US customary units, this is  $\left\{c_t\right\}=\left\{\frac{lb}{hp\cdot s}\right\}$.

You may see some slightly different units such as $\left[\frac{kg}{kW\cdot hr}\right]$ so be sure to convert to SI or US customary base units
    
The analysis is slightly different for jet and propeller-driven aircraft, so jet aircraft will be explored first.

## BRE - Jet Aircraft

The fundamental concept is, again:

$$\substack{\text{"The rate of}\\\text{aircraft weight reduction"}}=\substack{\text{"The rate of}\\\text{fuel weight burned"}}$$

So for a jet aircraft this is

$$\frac{\text{d}W}{\text{d}t}=-c_t\,T\, g$$

which can be rearranged for the time

$$\text{d}t = -\frac{\text{d}W}{c_t\,T\, g}$$

since the endurance/range is defined by *cruise* conditions, the equilibrium steady flight conditions of $T=D$ and $L=W$ can be utilised such that

```{margin}
*Substitution for thrust*

This always seems like a bit of a *trick* in the derivation - but what's really occurring is that the thrust is defined in terms of aerodynamic variables so the condition for maximum range can be determined.
```

$$T=\frac{D}{L}W=\frac{C_D}{C_L}W$$

which can be substituted into the BRE to give

$$\text{d}t = -\frac{1}{c_t\, g}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

for constant lift-to-drag ratio and TSFC, the equation above can be integrated with the limits $t_{0}$ and $t_{1}$ corresponding to $W_{0}$ and $W_{1}$ where 0 denotes the start of cruise, and 1 denotes the end. 

$$\int^{t_1}_{t_0}\text{d}t = -\frac{1}{c_t\, g}\frac{C_L}{C_D}\int^{W_1}_{W_0}\frac{\text{d}W}{W}$$
$$t_1 - t_0 = -\frac{1}{c_t\, g}\frac{C_L}{C_D}\left[\ln W_1 - \ln W_0\right]$$

This yields the endurance, $E$:

```{math}
:label: EnduranceJet
E=t_{1}-t_{0}=\frac{1}{c_t\, g}\frac{C_L}{C_D}\ln\left|\frac{W_{0}}{W_{1}}\right|
````

### Jet Aircraft: Maximum Endurance

For a given $c_t$, $W_0$, and $W_{1}$, Equation {eq}`EnduranceJet` shows that the **best endurance for a jet aircraft is found at the minimum drag speed**. If you're unsure why it shows this - look at the equation and consider what can be maximised.

To find the range, the equation above needs to be modified - the range is given by the following if it is assumed TAS remains constant.
```{margin}
Is constant airspeed speed a valid assumption? we'll come back at the end consider the effect of our assumptions, don't worry.
```



### Jet Aircraft: Range

If constant true airspeed is assumed, then the range is given by the endurance multiplied by the range

$$R=E\,V$$

or

```{math}
:label: BREjet

R=\frac{V}{c_t\, g}\frac{C_L}{C_D}\ln\left|\frac{W_{0}}{W_{1}}\right|

```

#### The Range Function

The equation above gives the design/mission choices that help maximise range:

```{figure} ../Images/BRE_annotated.png
---
height: 300px
name: CruiseClimbBRE
---
```

In the Breguet Range Equation, Equation {eq}`BRE`, some parameters are dictated by the problem:
- $W_{1}$ is the weight of the aircraft including fuel
- $W_{0}$ is the weight of the aircraft with no fuel, or with a certain mandated reserve
- $c_t$ is the TSFC and will generally be given in a problem

Other parameters are unknown - so the **range function** needs to be constrained (written in terms of other parameters) in order to use Equation {eq}`BRE` to determine the possible range. This will yield the _speed_ for best range, and hence also enable determination of the flight duration.

```{figure} ../Images/RangeFunction.png
---
height: 300px
name: RangeFunction
---
```
The 'range function' is the expression $V\frac{C_L}{C_D}$ and clearly maximum range is given by the maximum value thereof.

In practice, this means replacing $V\frac{C_L}{C_D}$ with an equivalent expression representing the variation of the parameters therein, by finding another means of representing $V$ as a function of $C_L$ or $C_D$.

Different means of doing this will be explored - first the theory will be explained, and then numerical examples will follow.

#### Best Jet Range

To find the best range, the aircraft speed equation, Eq {eq}`ACSpeedEquation` can be used to substitute $V$ for aerodynamic and inertial parameters:

$$V=\sqrt{\frac{2\, W}{\rho\,S\,C_L}}$$

which has $W$ in it, so this needs to be substituted *before* the integration over $W$. Defining the incremental distance covered, $dS$ as $dS=dE\cdot V$:

$$\text{d}S = -\frac{V}{c_t\, g}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

$$\begin{align}
\text{d}S &= -\frac{1}{c_t\, g}\sqrt{\frac{2\, W}{\rho\,S\,C_L}}\frac{C_L}{C_D}\frac{\text{d}W}{W}\\
 &= -\frac{1}{c_t\, g}\sqrt{\frac{2}{\rho\,S}}\frac{C_L^{1/2}}{C_D}\frac{W^{1/2}}{W}\text{d}W\\
  &= -\frac{1}{c_t\, g}\sqrt{\frac{2}{\rho\,S}}\frac{C_L^{1/2}}{C_D}\frac{1}{W^{1/2}}\text{d}W
\end{align}$$

The range, $R$, is the integration of the equation above

$$\begin{align}
R &= -\frac{1}{c_t\, g}\sqrt{\frac{2\, W}{\rho\,S\,C_L}}\frac{C_L}{C_D}\int^{W_1}_{W_0}\frac{\text{d}W}{W}\\
 &= \frac{1}{c_t\, g}\sqrt{\frac{2}{\rho\,S}}\frac{C_L^{1/2}}{C_D}\left[2W_0^{\frac{1}{2}} - 2W_1^{\frac{1}{2}}\right]
\end{align}$$

which yields

```{math}
:label: BREjetmaxrange
R= \frac{1}{c_t\,g}\sqrt{\frac{8}{\rho\,S}}\frac{C_L^{1/2}}{C_D}\left[W_0^{\frac{1}{2}} - W_1^{\frac{1}{2}}\right]
```
Looking at {eq}`BREjetmaxrange`, the choice that can be made to maximise range can be determined:

```{figure} ../Images/BREMaxRangeJet.png
---
height: 300px
name: MaxJetRange
---
```

We can see that for a jet aircraft, the range is a function of the starting altitude. That is, start a cruise _high_ to fly far.

Of the other choices above, the one that is of interest to us is the aerodynamic consideration - maximise $\frac{C_L^{1/2}}{C_D}$. You should be able to easily show that this is achieved by a value of $C_L$

$$C_L=\sqrt{\frac{C_{D0}}{3\,K}}$$

Which is found at the flightspeed

$$V=\sqrt{\frac{2\,W}{\rho\,S\sqrt{\frac{C_{D0}}{3\,K}}}}=\sqrt{\sqrt{3}}\sqrt{\frac{2\,W}{\rho\,S\sqrt{\frac{C_{D0}}{3\,K}}}}$$

So the speed for best range in a jet aicraft is

$$V\simeq1.32\cdot V_{md}$$

Which is an interesting result - since it is the product of $V$ and $\frac{C_L}{C_D}$ that needs to be maximum, this is achieved at a speed *above* $V_{md}$ and hence at a lower value of $\frac{C_L}{C_D}$.

So to go _far_ in a jet aircraft, the speed above gives a lower _endurance_ but but the faster TAS allows more ground to be covered than for the best endurance speed, $V_{md}$. 

## Numerical Example


```{admonition} About units
:class: dropdown

You (that's you, IIT student) should be able to do these calculations *both* in SI units and US customary units. Since I got my degree and PhD outside of America, I have an *appreciation* (to use the term loosely) for US customary units, but my actual application has always been to convert to SI at the start, and then convert the answer *back* to US customary units if I need to provide one.

For this reason, I work in SI in written examples for class but I will provide examples with US customary units used throughout. I simply don't want to make a mistake when going through work in class, and end up a factor of 32 out, or have mixed up lb for lbf or whatever else I could have done.

I managed to find this whilst googling about the US and the metric system, if you want some further reading. https://www.nist.gov/system/files/documents/pml/wmd/metric/1136a.pdf
```
This is an adaptation of Example 5.19 in Anderson{cite}`Anderson:1999AP` - I claim no originality or authorship for the data provided, but I've used it to confirm my US customary calculation is correct before adapting.

```{admonition} Question:

Estimate the maximum range at altitudes of 20,000, 30,000, and 40,000 feet for the Gulfstream IV given the following:

Mass of aircraft without fuel: 43,500lb. Mass of usable fuel: 29,500lb.
Drag model: $C_D=0.015 + 0.08\cdot C_L^2$
Wing area: 950 square feet
TSFC: 0.69 lb of fuel consumed per pound of thrust per hour.

```

import numpy as np
from ambiance import Atmosphere

h1 = 20000
h2 = 30000
h3 = 40000

m_1 = 43500 # mass in lbs of aircraft without fuel
m_fuel = 29500 # mass in lbs of fuel

# # Unit conversions
lb_to_kilo = 0.453592
pound_to_newton = 4.44822
hour_to_second = 3600
ft_to_metre = 0.3048
metre_to_miles = 0.000621371
km_to_miles = 0.621371
g = 9.80665 # Gravitational acceleration
kg_to_slugs = 0.0685218
miles_to_feet = 5280 # Because everyone recalls this number...

# The start weight of the aircraft is equal to the end weight plus the fuel weight
m_0 = m_1 + m_fuel

# Aircraft drag model - from Anderson
CD0 = 0.015
K = 0.08
S = 950 # In square feet

# Thrust specific fuel consumption
c_t = 0.69 # c_t in lb of fuel per pound of thrust per hour

# Convert c_t to consistent units (lb of fuel per pound of thrust per second, not per hour)
c_t = c_t / 3600

# Find the Cl and Cd for max range
Cl = np.sqrt(CD0/3/K)
Cd = CD0 + K * Cl**2

# Iterate over the altitudes
for h_ft in [h1, h2, h3]:
    
    ############################################################################
    ################### First do the calculation in US customary units
    ############################################################################
    # Get density for this altitude - this will be in SI
    h = h_ft * ft_to_metre
    Atmopshere_for_30k = Atmosphere(h)
    rho_SI = Atmopshere_for_30k.density[0]
    
    print(f"For an altitude of {h_ft:1.0f}ft/{h/1e3:1.1f}km")

    # Convert to US customary density units of slugs per cubic feet 
    rho_US = rho_SI * kg_to_slugs * ft_to_metre**3 # i.e., dividing be the reciprocal of ft_to_metre**3

    # Now get range - which will be in feet (US Customary base units), so convert to miles for readability
    ## Note that since c_t has been defined as a mass, and so has the aircraft mass - we can avoid using "g" by
    # keeping the aircraft mass as mass since "g" is in the denominator of the BRE
    # If you don't want to do this you can save g in US customary as 32.17405ft/s^2, but the pounds/pounds/poundal
    # conversion can be a real pain

    R = 2/c_t * np.sqrt(2/rho_US/S) * Cl**.5 / Cd * (m_0**.5 - m_1**.5) / miles_to_feet

    print(f"The range is {R:1.0f} miles")


    ############################################################################
    ################### Now in SI units
    ############################################################################
    # Do the conversion into SI units
    c_t = c_t * lb_to_kilo * g / pound_to_newton

    # Find the Cl and Cd for best range
    Cl = np.sqrt(CD0/3/K)
    Cd = CD0 + K * Cl**2

    # wing area
    S_SI = S * ft_to_metre**2

    # Convert units
    w_0 = m_0 * lb_to_kilo * g
    w_1 = m_1 * lb_to_kilo * g

    # Determine range in km
    R = 2/c_t * np.sqrt(2/rho_SI/S_SI) * Cl**.5 / Cd * (w_0**.5 - w_1**.5) / 1e3

    print(f"The range is {R:1.0f}km which is equal to {R*km_to_miles:1.0f} miles")
    print(" ")

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

<!-- #### Cruise-Climb 1: Throttle Restricted

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
    
the above $C_L$ and $C_D$ are used as before the find the maximum range. -->

### Constant Altitude Cruise

Instead of cruise-climb, a constant altitude cruise allows the velocity to vary - the range will obviously be different.

Starting again with the the differential range expression where $dS$ is the differential displacement:

$$\text{d}S = -\frac{V}{f\,g}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

Since $\sigma$ is held constant, the aircraft speed equation can be substituted in the above

$$\begin{align}
	dS &= -\frac{1}{fg}\cdot\sqrt{\frac{2}{\rho S}}\frac{C_L^{1/2}}{C_D}\cdot\frac{\text{d} W}{W^{1/2}}\\
	R = S_E - S_S &= \sqrt{\frac{8}{\rho S}}\frac{1}{fg}\frac{C_L^{1/2}}{C_D}\left(W_S^{1/2}-W_E^{1/2}\right)
\end{align}$$

Note that for the maximum range, $\frac{C_L^{1/2}}{C_D}$ must be maximised - which is the same as for the thrust unrestricted cruise-climb case.

For this case, altitude and $C_L$ are held constant. As $W$ reduces, $L$ reduces, so $V$ must reduce. Hence the range must be less as the aircraft is flying *slower* from $t>0$.

Since $C_D$ is constant, $D$ and hence $T$ must reduce - so throttle must be reduced and a variation in the fuel consumption will occur.

For this case, an average value of $f$ must be used, or treat as a series of shorter steps and integrate numerically.

### Actual Cruise

A third, and much more common cruise profile is to cruise at a constant altitude, at a constant $V$. Hence to reduce $L$ to match the reduction in weight, $\alpha$ must be reduced, changing $C_L/C_D$. This is a more complex analysis and beyond the scope of this course.

### Cruise Comparisons

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


#### Thrust Restricted

Using the expressions derived above, the lift coefficient for Thrust restricted cruise climb is {glue:text}`CL_trcc:1.3f`, and the drag coefficient is {glue:text}`CD_trcc:1.3f`. This gives the range function as {glue:text}`range_function_trcc:1.3f` which yields a range of {glue:text}`range_trcc:1.0f`km

#### Thrust Unrestricted

Using the expressions derived above, the lift coefficient for Thrust unrestricted cruise climb is {glue:text}`CL_tucc:1.3f`, and the drag coefficient is {glue:text}`CD_tucc:1.3f`. This gives the range function as {glue:text}`range_function_tucc:1.3f` which yields a range of {glue:text}`range_tucc:1.0f`km

### Variation of jet range with lift coefficient, airspeed

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
fig.add_trace(go.Scatter(x=[CL_trcc, CL_trcc], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="crimson")))
fig.add_trace(go.Scatter(x=[CL_tucc, CL_tucc], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="darkgreen")))
fig.add_trace(go.Scatter(x=[CL_md, CL_md], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="mediumpurple")))
fig.add_trace(go.Scatter(x=[CL_mp, CL_mp], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="gold")))

fig.add_trace(go.Scatter(x=[CL_trcc], y=[200], mode="text",\
                         text="$C_{L,trcc}=\sqrt{\\frac{C_{D0}}{2\,K}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="crimson")))
fig.add_trace(go.Scatter(x=[CL_tucc], y=[300], mode="text",\
                         text="$C_{L,tucc}=\sqrt{\\frac{C_{D0}}{3\,K}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="darkgreen")))
fig.add_trace(go.Scatter(x=[CL_md], y=[300], mode="text",\
                         text="$C_{L,md}=\sqrt{\\frac{C_{D0}}{K}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="mediumpurple")))
fig.add_trace(go.Scatter(x=[CL_mp], y=[200], mode="text",\
                         text="$C_{L,mp}=\sqrt{\\frac{3\,C_{D0}}{2\,K}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="gold")))

# Overlay lines for the EAS
def CLtoEAS(CL):
    V = np.sqrt(Ws/(.5 * rho_sl * S * CL)) /.5144444
    return V


fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_trcc), CLtoEAS(CL_trcc)], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="crimson")))
fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_tucc), CLtoEAS(CL_tucc)], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="darkgreen")))
fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_md), CLtoEAS(CL_md)], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="mediumpurple")))
fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_mp), CLtoEAS(CL_mp)], y=[400, 1500], name="DontPrint", mode="lines", line=dict(color="gold")))

fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_trcc)], y=[200], mode="text",\
                         text="$V_{C_{L,trcc}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="crimson")))
fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_tucc)], y=[300], mode="text",\
                         text="$V_{C_{L,tucc}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="darkgreen")))
fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_md)], y=[300], mode="text",\
                         text="$V_{C_{L,md}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="mediumpurple")))
fig2.add_trace(go.Scatter(x=[CLtoEAS(CL_mp)], y=[200], mode="text",\
                         text="$V_{C_{L,mp}}$",\
                         textposition="bottom center", name="DontPrint",\
                         textfont=dict(color="gold")))

    
    
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

Notice that the maximum range is found at a considerably higher speed than both the minimum power and minimum drag speeds, for both types of cruise climb. The ratio between the two speeds and the minimum drag speed may be readily shown.

$$\begin{alignat*}{2}
	\frac{V_{trcc}}{V_{md}}&=\frac{\sqrt{\sqrt{2}}}{1} \hspace{1cm} \frac{V_{tucc}}{V_{md}} &&= \frac{\sqrt{\sqrt{3}}}{1}\\
	&= 1.1892 &&= 1.3161
\end{alignat*}$$

These ratios hold across altitudes, as you should expect.

## BRE - Propeller Aircraft

The BRE for propeller aircraft is similar to that for jet aircraft, but SFC is used in place of TSFC - the SI units are $\text{kg}/{\text W s}$.

The BRE for propeller aircraft is

$$\frac{\text{d}W}{\text{d}t}=-f\,g\,P$$

where $P$ is the power delivered to the aircraft from the propeller. With $\eta$ as the propeller efficiency, the power *delivered* is function of the power *required*

$$\eta P=D\,V$$

so the BRE becomes

$$\frac{\text{d}W}{\text{d}t}=-f\,g\,\frac{D\,V}{\eta}$$

$$\implies \text{d}t=-\frac{\eta}{f\,g\,V}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

Assuming, as for the jet cruise-climb case, that $\tfrac{C_L}{C_D}$, $f$, and $V$ remain constant, the equation above can be integrated from $W_S$ to $W_E$ to yield the endurance, $E$:

```{math}
:label: PropellerEndurance
E_{propeller}=t_e-t_s=\frac{\eta}{f\,g}\frac{1}{V}\frac{C_L}{C_D}\ln\left|\frac{W_S}{W_E}\right|
```

### Propeller Aircraft: Maximum Endurance

Equation {eq}`PropellerEndurance` shows that for the maximum endurance for a propeller-driven aircraft, the quanity $\frac{C_L}{V\,C_D}$ must be maximised, which is different to the jet aircraft case.

$$\frac{C_L}{V\,C_D}=\frac{L}{V\,D}=\frac{W}{V\,D}=\frac{W}{P}$$

Clearly the maximum endurance is found at the **minimum power condition**, thus **for maximum endurance a propeller-driven aircraft should fly at** $V_{mp}$.

### Propeller Aircraft: Maximum Range

The increment in aircraft distance, $\text{d}S$ when flown at velocity $V$ is given by

$$\text{d}S = V\text{d}t=-\frac{\eta}{f\,g}\frac{C_L}{C_D}\frac{\text{d}W}{W}$$

Clearly the maximum endurance is found at the **minimum drag condition**, thus **for maximum endurance a propeller-driven aircraft should fly at** $V_{md}$.

## Range and Endurance Summary

The maximum range for propeller-driven aircraft is the same as for a glider - consider that the maximum range is given by the least resistance encountered in the longitudinal direction, enabling the aircraft to fly *furthest*, so this is the *minimum drag speed*. 

The maximum endurance for propeller-driven aircraft is the same as for a glider - this is determined by the speed at which the most work is done with the least energy (most bang for buck), so this is the *minimum power speed*.

These are relatively easy to intuit because in a glider, there is no input *power* - and for a propeller-driven aircraft, the propulsor is directly providing *power*.

For a jet-driven aircraft, the engine provides *thrust*, and hence the power varies with forward speed. To get maximum range, using a cruise-climb method, the problem must be constrained somehow:
- If the thrust is held constant, and altitude allowed to vary then the best $C_L$ is $\sqrt{\frac{C_{D0}}{2\,K}}$
- If the thrust is allowed to vary to maintain $C_L$, then the best $C_L$ is $\sqrt{\frac{C_{D0}}{3\,K}}$

The best range is found using the second method, starting at a greater altitude.

The starting altitude does not affect the range using the first method.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Glider</th>
    <th class="tg-0pky">Jet Aircraft</th>
    <th class="tg-0lax">Propeller Aircraft</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Maximum Endurance</td>
    <td class="tg-0pky">At $V_{mp}$</td>
    <td class="tg-0pky">At $V_{md}$</td>
    <td class="tg-0lax">At $V_{mp}$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Maximum Range</td>
    <td class="tg-0pky">At $V_{md}$</td>
    <td class="tg-0pky"> $\gt V_{md}$</td>
    <td class="tg-0lax">At $V_{md}$</td>
  </tr>
</tbody>
</table>

All of the cruise-climb scenarios are theoretical behaviour, and are reliant on the assumptions made within these models - furthermore, cruise-climb is typically not allowed by ATC. Rather, a series of stepped-climbs are made.

Nonetheless, the methods shown here allow a good estimate of range to be made - and afford the ability to look at the effect of design parameters on range and endurance.



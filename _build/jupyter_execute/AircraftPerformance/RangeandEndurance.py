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
- hence $R=E\cdot V$

The above reasoning is effectively how range is determined, but there are some complications that you may/may not be considering:
- Aircraft take-off with a *lot* of fuel, so the **aircraft weight changes with time** and accordingly so do almost all the parameters we have considered up to this point, including the aircraft speed whilst the above relationship only holds true for *constant* airspeed
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

```{math}
:label: EnduranceJetDifferential
\int^{t_1}_{t_0}\text{d}t = -\frac{1}{c_t\, g}\frac{C_L}{C_D}\int^{W_1}_{W_0}\frac{\text{d}W}{W}
```

$$t_1 - t_0 = -\frac{1}{c_t\, g}\frac{C_L}{C_D}\left[\ln W_1 - \ln W_0\right]$$

This yields the endurance, $E$:

```{math}
:label: EnduranceJet
E=t_{1}-t_{0}=\frac{1}{c_t\, g}\frac{C_L}{C_D}\ln\left|\frac{W_{0}}{W_{1}}\right|
````

### Jet Aircraft: Maximum Endurance

For a given $c_t$, $W_0$, and $W_{1}$, Equation {eq}`EnduranceJet` shows that the **best endurance for a jet aircraft is found at the minimum drag speed**. If you're unsure why it shows this - look at the equation and consider what can be maximised.

To find the range, we'll take a step back to the Equation {eq}`EnduranceJetDifferential` and substitute the aircraft speed equation.

### Jet Aircraft: Range

Taking Equation{eq} `ACSpeedEquation` and multiplying  Equation {eq}`EnduranceJetDifferential` by it yields the incremental distance, $dS$, covered during cruise

$$\begin{gather}
\text{d}S &= V\,\text{d}t=-\frac{V}{c_t\,g}\frac{C_L}{C_D}\frac{1}{W}\text{d}W\\
&= -\frac{1}{c_t\,g}\sqrt{\frac{2\,W}{\rho S C_L}}\frac{C_L}{C_D}\frac{1}{W}\text{d}W\\
&= -\frac{1}{c_t\,g}\sqrt{\frac{2\,W}{\rho S}}\frac{C_L^{1/2}}{C_D}\frac{1}{W}\text{d}W
\end{gather}$$

Don't be tempted to combine the two $W$ terms at this point - those will be dealt with in a little while, first some observations can be made about the equation above:

```{figure} ../Images/JetRangeAnnotated.png
---
height: 300px
name: JetRangeAnnotated
---
```

As with all things in aeronautics (well, with science and mathematics), if you derive a relationship, you should check that what it says *makes sense*. The equation above says:
- Range is inversely proportional to fuel burn, which makes sense
- Range is inversely proportonal to weight, which makes sense (combine the two into $W^{-1/2}$)
- Range is proportional to altitude (we know aircraft cruise at altitude)

We see that the best range is given at the aerodynamic condition (that is, the velocity) corresponding to the maximum value of $\frac{C_L^{1/2}}{C_D}$ which is given by:

$$C_L=\sqrt{\frac{C_{D0}}{3\,K}}$$

- For equilibrium, lift must equal weight, so for the _best_ $C_L$, this occurs at a single airspeed (Eq. {eq}`ACSpeedEquation`
- Fuel is burned, so the aircraft gets *lighter*, so looking at the definition of the lift coefficient:

$$C_L=\frac{2\,W}{\rho\,S\,V^2}$$

- To maintain the best $C_L$, *either* the velocity has to reduce or the density has to reduce.

This yields two types of cruise:
- Constant Velocity *aka* Cruise-Climb
- Constant Altitude (where the aircraft slows down)

#### Constant Velocity Cruise

Looking at the definition of the lift coefficient, if velocity is constant, then in order to maintain a constant $C_L=\sqrt{\frac{C_{D0}}{3\,K}}$, the ratio $\frac{W}{\rho}$ must be constant. Accordingly, whilst the terms $W$ and $\rho$ both change during the cruise and could be included in the integration, the ratio of them is a **constant**, and can be removed from the integration. If the aircraft starts at an altitude $h_0$ with a corresponding density $\rho_0$, then

$$\frac{W_0}{\rho_0}=\frac{W_1}{\rho_1}=\frac{W_n}{\rho_n}$$

where $n$ is any intermediate value between the start and end of the cruise. Hence $\frac{W}{\rho}$ can be replaced with $\frac{W_0}{\rho_0}$. That is

$$R = \int^{R}_0\text{d}S = -\frac{1}{c_t\,g}\sqrt{\frac{2\,W_0}{\rho_0 S}}\frac{C_L^{1/2}}{C_D}\int_{W0}^{W1}\frac{1}{W}\text{d}W$$

```{math}
:label: BREjetConstantVelocity

R=\frac{1}{c_t\, g}\sqrt{\frac{2\,W_0}{\rho_0 S}}\frac{C_L}{C_D}\ln\left|\frac{W_{0}}{W_{1}}\right|

```

You should be able to see that the range is a function of the starting altitude (to which $\rho_0$ corresponds) - that is, if a cruise is commenced at a higher altitude, the range will be greater.

To determine the end altitude, this can be simply yielded from the relationship between weight and density.

#### Constant Altitude Cruise

Conversely, if the altitude is held constant, then the ratio of

$$\frac{W}{V^2}$$

must be held constant. But since there is no such ratio in the expression for incremental distance, the weight must be moved into the integral:

$$R = \int^{R}_0\text{d}S = -\frac{1}{c_t\,g}\sqrt{\frac{2}{\rho_0 S}}\frac{C_L^{1/2}}{C_D}\int_{W0}^{W1}\frac{W^{1/2}}{W}\text{d}W$$

```{math}
:label: BREjetConstantAltitude

R=\frac{1}{c_t\, g}\sqrt{\frac{8}{\rho_0 S}}\frac{C_L}{C_D}\ln\left[W_0^{1/2} - W_1^{1/2}\right]

```




### Jet BRE: Numerical Example


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

Compare the constant altitude, and the cruise-climb (constant speed ranges).

Show the starting/ending speeds and altitudes for the respective cruise methods.

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
ms_to_knots = 1.94384

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

V = np.zeros(3)

# Make an interpolant for the altitude based on the density:
from scipy.interpolate import interp1d
altitudes = np.linspace(0, 80e3, 10000)
densities = Atmosphere(altitudes).density
altdens = interp1d(densities, altitudes, kind='cubic')


# Iterate over the altitudes
for i, h_ft in enumerate([h1, h2, h3]):
    
    ############################################################################
    ################### First do the calculation in US customary units
    ############################################################################
    # Get density for this altitude - this will be in SI
    h = h_ft * ft_to_metre
    Atmopshere_for_altitude = Atmosphere(h)
    rho_SI = Atmopshere_for_altitude.density[0]
    
    print(f"For an altitude of {h_ft:1.0f}ft/{h/1e3:1.1f}km")

    # Convert to US customary density units of slugs per cubic feet 
    rho_US = rho_SI * kg_to_slugs * ft_to_metre**3 # i.e., dividing be the reciprocal of ft_to_metre**3

    # Now get range - which will be in feet (US Customary base units), so convert to miles for readability
    ## Note that since c_t has been defined as a mass, and so has the aircraft mass - we can avoid using "g" by
    # keeping the aircraft mass as mass since "g" is in the denominator of the BRE
    # If you don't want to do this you can save g in US customary as 32.17405ft/s^2, but the pounds/pounds/poundal
    # conversion can be a real pain

    # Constant altitude range
    Range_constant_altitude = 1/c_t * np.sqrt(8/rho_US/S) * Cl**.5 / Cd * (m_0**.5 - m_1**.5) / miles_to_feet
    
    # Constant speed range
    Range_constant_speed = 1/c_t * np.sqrt(2*m_0/rho_US/S) * Cl**.5 / Cd * (np.log(m_0/m_1)) / miles_to_feet

    print("US Customary Unit Calcs:")
    print(f"The constant altitude range is {Range_constant_altitude:1.0f} miles")
    print(f"The cruise-climb range is {Range_constant_speed:1.0f} miles")


    ############################################################################
    ################### Now in SI units
    ############################################################################
    # Do the conversion into SI units
    c_t_SI = c_t * lb_to_kilo / pound_to_newton

    # Find the Cl and Cd for best range
    Cl = np.sqrt(CD0/3/K)
    Cd = CD0 + K * Cl**2

    # wing area
    S_SI = S * ft_to_metre**2

    # Convert units
    w_0 = m_0 * lb_to_kilo * g
    w_1 = m_1 * lb_to_kilo * g

    # Determine constant altitude range in km
    Range_constant_altitude = 1/c_t_SI / g * np.sqrt(8/rho_SI/S_SI) * Cl**.5 / Cd * (w_0**.5 - w_1**.5) / 1e3
    
    # Determine constant speed range in km
    Range_constant_speed = 1/c_t_SI / g * np.sqrt(2*w_0/rho_SI/S_SI) * Cl**.5 / Cd * (np.log(w_0/w_1)) / 1e3
    

    print(" ")


    print("SI Unit Calcs:")
    print(f"The constant altitude range is {Range_constant_altitude:1.0f}km which is equal to {Range_constant_altitude*km_to_miles:1.0f} miles")
    print(f"The cruise-climb range is {Range_constant_speed:1.0f}km which is equal to {Range_constant_speed*km_to_miles:1.0f} miles")
    
    print(" ")
    
    # Determine the speed difference for the constant altitude cruise
    v0 = np.sqrt(w_0 / (0.5 * rho_SI * S_SI * Cl)) * ms_to_knots
    v1 = np.sqrt(w_1 / (0.5 * rho_SI * S_SI * Cl)) * ms_to_knots
    
    # Determine the altitude difference for cruise climb
    rho_1 = 2*w_1/S_SI/Cl/(v0/ms_to_knots)**2
    h_1 = altdens(rho_1)/ft_to_metre
    
    print(f"For the constant altitude cruise, the starting speed is {v0:1.0f}knTAS and the end speed is {v1:1.0f}knTAS")
    print(f"For the cruise-climb the aircraft gains {(h_1 - h_ft)/1e3:1.1f} thousand feet during the cruise")
    
    print(" ")
    print("-------------------------------------------------------------- ")
    print(" ")













### Variation of jet range with lift coefficient, airspeed

Recall that the lift coefficient is effectively a measure of the aircraft *cruise speed*. The range can be plotted vs. lift coefficient and forward speed for the two different cruise-climb cases over a range of starting altitudes.

```{admonition} Beware of source for the plots below...
:class: dropdown

Producing the plots below is fairly simple - but in order to get the labels and legend to work correctly, there's a bit of obscure logic flow in the way the plot is created.

That is, it makes it look more complicated than it actually is (and it probably could be done better if I knew my way around plotly better).
```



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



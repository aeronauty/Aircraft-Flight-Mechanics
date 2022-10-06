# Worked Example

Data for several aircraft are presented in {cite}`Heffley:1972wb` and, honestly, this is a good exercise in showing you what a tremendous amount of being an engineer is - _extracting data from old reports and doing stuff with it_.

## Data for Boeing 747

Data are given on Page 217 of the aforementioned report for the B-747 in power approach configuration.

### Configuration Information

$$h=SL$$
$$V_\infty=165\text{KTAS}$$
$$S=5500\text{ft}^2$$
$$b=195.68\text{ft}$$
$$\bar{c}=27.31\text{ft}$$
$$\theta_0=0$$

_note that the trim theta is not actually given, but assumed to be zero_

### Nondimensional Stability Derivatives

| Longitudinal                             	| Lateral-Directional                         	|
|------------------------------------------	|---------------------------------------------	|
| $C_L=1.11$                               	| $C_{y_\beta}=-0.96\text{rad}^{-1}$          	|
| $C_D=0.102$                              	| $C_{\ell_\beta}=-0.221\text{rad}^{-1}$      	|
| $C_{L_\alpha}=5.70\text{rad}^{-1}$       	| $C_{n_\beta}=0.150\text{rad}^{-1}$          	|
| $C_{D_\alpha}=0.66\text{rad}^{-1}$       	| $C_{\ell_\hat{p}}=-0.45$                    	|
| $C_{m_\alpha}=-1.26\text{rad}^{-1}$      	| $C_{n_\hat{p}}=-0.121$                      	|
| $C_{L_\dot{\alpha}}=-6.7\text{rad}^{-1}$ 	| $C_{\ell_\hat{r}}=0.101$                    	|
| $C_{m_\dot{\alpha}}=-3.2\text{rad}^{-1}$ 	| $C_{n_\hat{r}}=-0.30$                       	|
| $C_{L_\hat{q}}=5.40$                     	| $C_{\ell_{\delta_a}}=0.0461\text{rad}^{-1}$ 	|
| $C_{m_\hat{q}}=-20.8$                    	| $C_{n_{\delta_a}}=0.0064\text{rad}^{-1}$    	|
| $C_{L_\text{M}}=-0.81$                   	| $C_{y_{\delta_r}}=0.175\text{rad}^{-1}$     	|
| $C_{m_\text{M}}=0.27$                    	| $C_{\ell_{\delta_r}}=0.007\text{rad}^{-1}$  	|
| $C_{L_{\delta_e}}=0.338\text{rad}^{-1}$  	| $C_{n_{\delta_r}}=-0.109\text{rad}^{-1}$    	|
| $C_{m_{\delta_e}}=-1.34\text{rad}^{-1}$  	|                                             	|

Note that in {cite}`Heffley:1972wb`, the derivatives with respect to angular rates are erroneously given units of /rad, when they clearly are non-dimensional rates. The derivatives with respect to aerodynamic angles correctly are given units of /rad.

import numpy as np
from IPython.display import display, Math, Latex, Markdown


# Condition and geometry information
rho = 0.002377 # slugs/cubic feet
# rho = rho * 32.174 # to lb / cubic feet
rho = 0.0765 # lb/ft^3
U0 = 165 # Knots
U0 = U0 * 1.68781 # to feet/second
S = 5500 # square feet
b = 195.68 # feet
c = 27.31 # feet
theta_0 = 0
m = 564000 # lb


Iyy = 32.3e6 # slug-ft^2
Ixx = 14.3e6
Izz = 45.3e6
Ixz = -2.23e6

SIunits = False

if SIunits:
    # Conversion factors
    ft_to_metre = 0.3048
    lb_to_kg = 0.453592
    slug_to_kg = 14.5939
    
    MOIconvert = slug_to_kg*ft_to_metre**2

    
    # Constants
    a = 340 # sonic velocity in m/s
    g = 9.80665 # acceleration due to gravity
    rho = 1.225 # density in kg/m^3
    
    # Convert
    U0 = U0 * ft_to_metre
    S = S * ft_to_metre**2
    b = b * ft_to_metre
    c = c * ft_to_metre
    m = m * lb_to_kg
    Ixx = Ixx * MOIconvert
    Iyy = Iyy * MOIconvert
    Izz = Izz * MOIconvert
    Ixz = Ixz * MOIconvert   
    
else:
    a = 1125.33 # sonic velocity in ft/s
    g = 32.174
    
    # Convert mass moments of inertia to consistent units --> INTO lb-ft^2 FROM slug-ft^2
    Ixx = Ixx * g
    Iyy = Iyy * g
    Izz = Izz * g
    Ixz = Ixz * g

# Store the derivatives in two dictionaries
B747_lon_ders = {'C_L': 1.11, 'C_D': 0.102, 'C_L_a' : 5.7, 'C_D_a' : 0.66, 'C_m_a' : -1.26,
                 'C_L_da' : -6.7, 'C_m_da' : -3.2, 'C_L_hq' : 5.4, 'C_m_hq' : -20.8, 'C_L_M' : -0.81,
                'C_m_M' : 0.27, 'C_L_de' : 0.338, 'C_m_de' : -1.34}

B747_lat_ders = {'C_y_b' : -0.96, 'C_l_b' : -0.221, 'C_n_b' : 0.150, 'C_l_hp' : -0.45, 'C_n_hp' : -0.121,
                'C_l_hr' : 0.101, 'C_n_hr': -0.30, 'C_l_da' : 0.0461, 'C_n_da' : 0.0064, 'C_y_dr' : 0.175,
                'C_l_dr' : 0.007, 'C_n_dr' : -0.109}

# Put the dictionaries into the local namespace
# This might seem a bit convoluted but it enables us to store values of derivatives in the dicionary, above,
# and then put them all into the global namespace.
#
# It's fairly easy to get (key: value) pairs into a dictionary from a text file or xls so this will be handy
# later.
locals().update(B747_lon_ders)

# Note that without doing the dictionary --> local namespace, the we'd have to write:
# Xu = q * S / m / U0 * (2 * B747_lon_ders["C_D"] + M * B747_lon_ders["C_D_M"])

# Convert to dimensional form
q = 0.5 * rho * U0**2
M = U0 / a

Xu = -q * S / m / U0 * (2 * C_D) # No C_D_M term so assumed zero
Xw = q * S / m / U0 * (C_L - C_D_a)
Xq = 0 # No CDq term given in the table so assumed zero
Zu = -q * S / m / U0 * (2 * C_L + M * C_L_M)
Zw = -q * S / m / U0 * (C_D + C_L_a)
Zdw = q * S * c / m / 2 / U0**2 * C_L_da # This is a NEW term for us, but since it was given as C_L_da, must be included
Zq = -q * S * c / 2 / m / U0 * C_L_hq
Mu = q * S * c / Iyy / U0 * M * C_m_M
Mw = q * S * c / Iyy / U0 * C_m_a
Mdw = q * S * c**2 / 2 / Iyy / U0**2 * C_m_da
Mq = q * S * c**2 / 2 / Iyy / U0 * C_m_hq
Mq = q * S * c**2 / 2 / Iyy / U0 * C_m_hq
Zde = -q * S / m * C_L_de
Mde = q * S * c / Iyy * C_m_de

print(f"Xu = {Xu:1.4f}")
print(f"Xw = {Xw:1.4f}")
print(f"Zu = {Zu:1.4f}")
print(f"Zw = {Zw:1.4f}")
print(f"Zdw = {Zdw:1.4f}")
print(f"Zq = {Zq:1.4f}")
print(f"Mu = {Mu:1.4f}")
print(f"Mw = {Mw:1.4f}")
print(f"Mw = {Mw:1.4f}")
print(f"Mdw = {Mdw:1.4f}")
print(f"Mq = {Mq:1.4f}")

print(f"Zde = {Zde:1.4f}")
print(f"Mde = {Mde:1.4f}")



Some units have dimensions of $[\text{T}^{-1}]$ and hence have the same value in either unit system. Expand the below to see this. Other derivatives do not.

# Demonstration of the equality of some derivatives in both unit systems:
SIunits = {"Pressure": "Pa", "Mass": "kg", "Area" : "m^2", "Speed" : "m/s"}
USunits = {"Pressure": "lbs/ft^2", "Mass": "lbs", "Area" : "ft^2", "Speed" : "ft/s"}

# Conversion factors
ft_to_metre = 0.3048
lb_to_kg = 0.453592
slug_to_kg = 14.5939

for SIUNIT in [False, True]:
    if SIUNIT:
        UNITS = SIunits
    else:
        UNITS = USunits
    
    # Convert to some temporary variables to not overwrite the original values
    if SIUNIT:
        u0 = U0 * ft_to_metre
        s = S * ft_to_metre**2
        c2 = c * ft_to_metre
        mass = m * lb_to_kg
        rho = 1.225
        qinf = 0.5 * 1.2255 * u0**2
    else:
        qinf = q
        u0 = U0
        s = S
        c2 = c
        mass = m

    if SIUNIT: print("Using SI Units:") 
    else: print("Using US Customary Units:")
    print(f"Dynamic pressure, q = {qinf:1.4f} {UNITS['Pressure']}")
    print(f"Wing area, S = {s:1.0f}  {UNITS['Area']}")
    print(f"Mass, m = {mass:1.0f}  {UNITS['Mass']}")
    print(f"Trim forward speed, U0 = {u0:1.1f}  {UNITS['Speed']}")
       
    testXu = -qinf * s / mass / u0 * (C_L * 2 + C_L_M * M)    
    testZq = -qinf * s * c2 / 2 / mass / u0 * C_L_hq

    print(f"Gives a value for Xu = {testXu:1.4f}, and a value for Zq of {testZq:1.4f}\n")



Now the system matrix can be constructed:

$$\begin{aligned}
    \begin{bmatrix} \dot{u}\\\dot{w}\\\dot{q}\\\dot{\theta}\end{bmatrix} &= \begin{bmatrix}
        X_u & X_w & 0 & -g\cdot\cos\Theta_e\\
        Z_u & Z_w & U_0 & -g\cdot\sin\Theta_e\\
        M_u^* & M_w^* & M_q^* & M_\theta^*\\
        0 & 0 & 1 & 0   
    \end{bmatrix}\begin{bmatrix}
        {u}\\{w}\\{q}\\{\theta}         
    \end{bmatrix} + \begin{bmatrix}
        0\\Z_{\delta_e}\\M_{\delta_e}^*\\0          
    \end{bmatrix}\left[\delta_e\right]\end{aligned}$$
    
well...almost - you'll see two things that need to be performed:
1. The starred terms need to be made from the products of the stability derivatives.
2. We have a $Z_q$ term from conversion of the stability derivatives, but no corresponding place to put it.

The first problem is easy. From Equations {eq}`eq:conciseqterms`

Mustar = Mu + Mdw * Zu
Mwstar = Mw + Mdw * Zw
Mqstar = Mq + Mdw * Zq
Mthetastar = -Mdw * g * np.sin(theta_0)
Mdestar = Mde + Mdw * Zde

Now we've got all the terms, we don't know where to put $Z_q$. The answer should be obvious - it goes where the $U_0$ term is - it doesn't _replace_ it, but is _added to it_. So:

import sympy as sp

Alon = np.matrix([[Xu, Xw, 0, -g*np.cos(theta_0)],
               [Zu, Zw, U0 + Zq, -g*np.sin(theta_0)],
               [Mustar, Mwstar, Mqstar, Mthetastar],
               [0, 0, 1, 0]])

print("The system matrix for longitudinal motion is ")
display(Math('[A_{lon}] = ' + sp.latex(sp.Matrix(Alon).evalf(5))))

# Get the eigenvalues - this is my own checking I got the matrix correct. It'll make sense later.
eigs, _ = np.linalg.eig(Alon)

print("The eigenvalues are:", eigs)

print("The coefficients of the CE are:", np.poly(Alon))


The same can be performed for the lateral-directional matrix:

# Put the non-dimensional derivatives into the local namespace
locals().update(B747_lat_ders)

Yv = q * S / m / U0 * C_y_b
Yp = 0
Yr = 0
Lv = q * S * b / Ixx / U0 * C_l_b
Lp = q * S * b**2 / 2/ Ixx / U0 * C_l_hp
Lr = q * S * b**2 / 2/ Ixx / U0 * C_l_hr
Nv = q * S * b / Izz / U0 * C_n_b
Np = q * S * b**2 / 2 / Izz / U0 * C_n_hp
Nr = q * S * b**2 / 2 / Izz / U0 * C_n_hr


print(f"Yv = {Yv:1.4f}")
print(f"Yp = {Yp:1.4f}")
print(f"Yr = {Yr:1.4f}")
print(f"Lv = {Lv:1.4f}")
print(f"Lp = {Lp:1.4f}")
print(f"Lr = {Lr:1.4f}")
print(f"Nv = {Nv:1.4f}")
print(f"Np = {Np:1.4f}")
print(f"Nr = {Nr:1.4f}")

# Do the sadme with the control terms 
# 'C_l_da' : 0.0461, 'C_n_da' : 0.0064, 'C_y_dr' : 0.175,
#                 'C_l_dr' : 0.007, 'C_n_dr' : -0.109}
Yda = 0
Ydr = q * S / m * C_y_dr
Lda = q * S * b / Ixx * C_l_da
Ldr = q * S * b / Ixx * C_l_dr
Nda = q * S * b / Izz * C_n_da
Ndr = q * S * b / Izz * C_n_dr


# 


And put into the system matrix for lateral-directional motion

$$\boldsymbol{A}=\begin{bmatrix}Y_v & 0 & -U_0 & g\cdot\cos\theta_0 & 0\\L_v^* & L_p^* & L_r^* & 0 & 0\\N_v^* & N_p^* & N_r^* & 0 & 0\\0 & 1 & \tan\theta_0 & 0 & 0 \\ 0 & 0 & \sec\theta_0 & 0 & 0\end{bmatrix}$$

# Making the starred terms
Imess = Ixx * Izz / (Ixx * Izz - Ixz**2)
I2 = Ixz / Ixx

# Lstarred terms
Lvstar = Imess * (Lv + I2 * Nv)
Lpstar = Imess * (Lp + I2 * Np)
Lrstar = Imess * (Lr + I2 * Nr)
Ldrstar = Imess * (Ldr + I2 * Ndr)
Ldastar = Imess * (Lda + I2 * Nda)

# Nstarred terms
I2 = Ixz / Izz
Nvstar = Imess * (Nv + I2 * Lv)
Npstar = Imess * (Np + I2 * Lp)
Nrstar = Imess * (Nr + I2 * Lr)
Ndrstar = Imess * (Ndr + I2 * Ldr)
Ndastar = Imess * (Nda + I2 * Lda)

Alat = np.matrix([[Yv, 0, -U0, g*np.cos(theta_0), 0],
               [Lvstar, Lpstar, Lrstar, 0, 0],
               [Nvstar, Npstar, Nrstar, 0, 0],
               [0, 1, np.tan(theta_0), 0, 0],
               [0, 0, 1/np.cos(theta_0), 0, 0]])

print("The system matrix for lateral-directional motion is ")
display(Math('[A_{lat}] = ' + sp.latex(sp.Matrix(Alat).evalf(5))))

print("The eigenvalues are:", np.linalg.eig(Alat)[0])

print("The coefficients of the CE are:", np.poly(Alat))

np.pi*2/.7420

### Transient Longitudinal Response

Note that we've not made either of the control matrices yet - and there's a good reason for that. If we consider 
the linearised model of the aircraft created, the _stability_ of the aircraft (_i.e.,_ its response to a perturbation) will be governed by the system matrix.

In the first instance, it is desired to understand the _stick fixed stability_ and understand what will happen to the aircraft if no inputs are made.

Consider what the two matrices developed actually show us; if the aircraft is disturbed from a given condition, then if the disturbance is a _symmetric_ state variable ($u, w, q, \theta$), then the output is a time rate of change of _all_ other symmetric variables. 

The control matrices tell us how the aircraft responds due to control input. Therefore, if we're interested in aircraft response in the absense of pilot or control-system input, then we're only interested in the A matrices themselves. The A matrices give the _open loop response_ of the aircraft.

Since these are ODEs, we could write a means to time-march through the solution - but there are some handy inbuilt tools in Python to look at the responses of state-space systems to different inputs.

You will probably need to install these to work on your system - [look here](https://python-control.readthedocs.io/en/0.8.3/intro.html#overview-of-the-toolbox).

But if we create the $B$ matrix, it can be used to excite the aircraft with unity impulse input. For this reason, it makes sense to make the two control matrices with derivatives that have been scaled by a factor of $\frac{\pi}{180}$ to allow a unity _degree_ control input.

import control
import control.matlab

# We will make a B matrix to enable us to use the control system toolbox by _exciting the aircraft_ through
# Elevator input. Turn from Zde in 1/radians to 1/degree to put a useful input in.
Blon = np.matrix([[0], [np.radians(Zde)], [np.radians(Mdestar)], [0]])

# Turn the matrices into a state space object
LonSS = control.StateSpace(Alon, Blon, np.eye(Alon.shape[0]), np.zeros(Blon.shape))

# Look at the first 100 seconds response to a unit impulse in the only
Time, [u, w, q, theta] = control.impulse_response(LonSS, T=np.linspace(0, 200, 10000))

u, w, q, theta = u[0], w[0], q[0], theta[0]

# Convert q and theta
q = np.degrees(q)
theta = np.degrees(theta)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=("Forward Speed", "Heave Velocity", "Pitch Rate", "Pitch Attitude"))

fig.add_trace(
    go.Scatter(x = Time, y = u, showlegend=False), row=1, col=1)

fig.add_trace(
    go.Scatter(x = Time, y = w, showlegend=False), row=1, col=2)

fig.add_trace(
    go.Scatter(x = Time, y = q, showlegend=False), row=2, col=1)

fig.add_trace(
    go.Scatter(x = Time, y = theta, showlegend=False), row=2, col=2)

# Make a label based upon the units
if SIunits:
    speedlabel = "m/s"
else:
    speedlabel = "ft/s"

fig.update_xaxes(title_text="Time", row=1, col=1)
fig.update_yaxes(title_text=f"u / ({speedlabel})", row=1, col=1)
fig.update_xaxes(title_text="Time", row=1, col=2)
fig.update_yaxes(title_text=f"w / ({speedlabel})", row=1, col=2)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_yaxes(title_text="q / (deg/s)", row=2, col=1)
fig.update_xaxes(title_text="Time", row=2, col=2)
fig.update_yaxes(title_text="θ / deg", row=2, col=2)



As much as a pain as the non-dimensional to dimensional procedure is, it is useful in that you can take fully non-dimensional data and then use whatever unit system you prefer, and you'll get results in those units.

Note that there is a flag to convert between US Customary (ugh) and SI units in the code above. You can see that there's some very annoying fiddly bits that have to be performed with the US Customary units to ensure consistency - that is, the mass moments of inertia are given in slugs-ft^2, but the masses etc. are presented in lbs. This can cause some dimensional moments of inertia to be about thirty-two times too large, which has a large effect on the end result.

My strong advice is if you're required to do anything in US Customary units, to convert to SI at the start, and then convert to US Customary at the end. There's just too many pitfalls in the US Customary system.

```{admonition} Other inputs?
If you wanted to look at the transient response of the aircraft to control inputs other than one degree, what could we do with the _output_ to explore this?

Discuss this on the slack space.
```
#### Response characteristics

We'll spend the next module understanding the actual characteristics of the aircraft in terms of dynamic response, but we can start to intuit some of this now:
- There are two phases to the aircraft response - a short-term response that is heavily damped, affecting mainly heave (_i.e._, angle of attack) and pitch rate, and a long-term response that is lightly-damped, affecting mainly speed and pitch attitude, but also showing in the other state variables.

Non-state variables can be explored - we *could* go back and change the state variable $w$ for $\alpha$, for example, and then explore the change in AoA. This would require calculating a new set of stability derivatives (many sources use $\alpha$ in place of $u$). Instead, perturbational angle of attack can be determined from the linear relationship

alpha = np.degrees(w/(U0+u))

fig = go.Figure()
fig.add_trace(
    go.Scatter(x = Time, y = alpha, showlegend=False))

fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="$\\alpha/\\text{deg}$")

You will see that the angle of attack is affected much more by the short-term response than the long-term response.

### Transient Lateral Response

A similar exercise can be performed for the lateral response


# We will make a B matrix to enable us to use the control system toolbox by _exciting the aircraft_ through
# Elevator input. Turn from Zde in 1/radians to 1/degree to put a useful input in.
Blat = np.matrix([[Ydr, Yda], [Ldrstar, Ldastar], [Ndrstar, Ndastar], [0, 0], [0, 0]])
Blat = np.radians(Blat)

# Turn the matrices into a state space object
LatSS = control.StateSpace(Alat, Blat, np.eye(Alat.shape[0]), np.zeros(Blat.shape))

# do this twice, for rudder and then aileron
Time, [v, p, r, phi, psi] = control.impulse_response(LatSS, T=np.linspace(0, 200, 10000), input=0)

v, p, r, phi, psi = v[0], p[0], r[0], phi[0], psi[0]

# Convert p, r, and phi
p = np.degrees(p)
r = np.degrees(r)
phi = np.degrees(phi)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=("Sideslip Velocity", "Roll Rate", "Yaw Rate", "Roll Attitude"))

fig.update_layout(title=f"Unit Rudder Input", title_x=0.5)

fig.add_trace(
    go.Scatter(x = Time, y = v, showlegend=False), row=1, col=1)

fig.add_trace(
    go.Scatter(x = Time, y = p, showlegend=False), row=1, col=2)

fig.add_trace(
    go.Scatter(x = Time, y = r, showlegend=False), row=2, col=1)

fig.add_trace(
    go.Scatter(x = Time, y = phi, showlegend=False), row=2, col=2)

# Make a label based upon the units
if SIunits:
    speedlabel = "m/s"
else:
    speedlabel = "ft/s"

fig.update_xaxes(title_text="Time", row=1, col=1)
fig.update_yaxes(title_text=f"v / ({speedlabel})", row=1, col=1)
fig.update_xaxes(title_text="Time", row=1, col=2)
fig.update_yaxes(title_text=f"p / (deg/s)", row=1, col=2)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_yaxes(title_text="r / (deg/s)", row=2, col=1)
fig.update_xaxes(title_text="Time", row=2, col=2)
fig.update_yaxes(title_text="φ  / deg", row=2, col=2)
fig.show()



# Second time - aileron
Time, [v, p, r, phi, psi] = control.impulse_response(LatSS, T=np.linspace(0, 200, 10000), input=1)
v, p, r, phi, psi = v[0], p[0], r[0], phi[0], psi[0]


# Convert p, r, and phi
p = np.degrees(p)
r = np.degrees(r)
phi = np.degrees(phi)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=("Sideslip Velocity", "Roll Rate", "Yaw Rate", "Roll Attitude"))
fig.update_layout(title="Unit Aileron Input", title_x=0.5)

fig.add_trace(
    go.Scatter(x = Time, y = v, showlegend=False), row=1, col=1)

fig.add_trace(
    go.Scatter(x = Time, y = p, showlegend=False), row=1, col=2)

fig.add_trace(
    go.Scatter(x = Time, y = r, showlegend=False), row=2, col=1)

fig.add_trace(
    go.Scatter(x = Time, y = phi, showlegend=False), row=2, col=2)

# Make a label based upon the units
if SIunits:
    speedlabel = "m/s"
else:
    speedlabel = "ft/s"


fig.update_xaxes(title_text="Time", row=1, col=1)
fig.update_yaxes(title_text=f"v / ({speedlabel})", row=1, col=1)
fig.update_xaxes(title_text="Time", row=1, col=2)
fig.update_yaxes(title_text=f"p / (deg/s)", row=1, col=2)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_yaxes(title_text="r / (deg/s)", row=2, col=1)
fig.update_xaxes(title_text="Time", row=2, col=2)
fig.update_yaxes(title_text="φ  / deg", row=2, col=2)
fig.show()


### Getting eigenvalues from the graph data

This bit wont make much sense until you watch the corresponding lecture...

# Just plot the roll attitude
fig = go.Figure()
fig.update_layout(title="Roll Attitude", title_x=0.5)

fig.add_trace(
    go.Scatter(x = Time, y = phi, showlegend=False))

# Estimate the spiral mode
lam_sp_est = 1/50 * np.log(0.02/0.19)
print(f"Estimated spiral eigenvalue = {lam_sp_est:1.4}")

dphi_est = 0.19
sp_est = dphi_est * np.exp(lam_sp_est*Time)

fig.add_trace(
    go.Scatter(x = Time, y = sp_est, name="Estimated Spiral Mode", showlegend=True))

# Now estimate the dutch roll
import scipy.signal as sig
peaks_all = sig.find_peaks(phi)[0]

phi_dr = np.zeros(peaks_all.shape)

for i, p in enumerate(peaks_all[:4]):
    fig.add_trace(go.Scatter(x = [Time[p]], y = [phi[p]], mode='markers+text', text=f"{Time[p]:1.3f},{phi[p]:1.3f}", showlegend=False))

    # Get the value without the spiral mode
    phi_dr[i] = phi[p] - dphi_est * np.exp(lam_sp_est * Time[p])
    
fig.show()
fig.update_traces(textposition='top right')

# Estimate the damping in the Dutch Roll
lam_real_DR = 1/(Time[peaks_all[2]] - Time[peaks_all[1]]) * np.log(phi_dr[2]/phi_dr[1])


# remove the spiral completely from the data
just_dr = phi - sp_est
fig.add_trace(
    go.Scatter(x = Time, y = just_dr, name="Estimated Dutch Mode", showlegend=True))

# And the imaginary part is simply the damped natural frequency
lam_imag_DR = 2 * np.pi / ((Time[peaks_all[2]] - Time[peaks_all[1]]))
print(f"Estimated spiral eigenvalue = {lam_sp_est:1.4}")
print(f"Estimated DR eigenvalue {lam_real_DR:1.4}±{lam_imag_DR:1.4}j\n")

# Compare to those from the data - first get the spiral
lat_eigs = np.linalg.eig(Alat)[0]
real_eigs = lat_eigs[lat_eigs.imag == 0] # Gets just the real eigenvalues but they're still returned as complex numbers
real_eigs = real_eigs[real_eigs != 0] 
the_spiral_index = np.argmin(np.abs(real_eigs)) # Finds which has the least damping - this must be the spiral
spiral_eigenvalue = real_eigs[the_spiral_index].real # Returns it without the zero imaginary part
print(f"Compared with those from the A matix - spiral = {spiral_eigenvalue:1.4f}")

# Now get the DR
DR_eigs = lat_eigs[lat_eigs.imag != 0]
print(f"Compared with those from the A matrix - Dutch Roll = {DR_eigs[0]:1.4f}")



phi_dr1 = 0.164 - 0.19 * np.exp(lam_sp_est * 9.881)
phi_dr2 = 0.104 - 0.19 * np.exp(lam_sp_est * 18.242)

print(phi_dr1)
print(phi_dr2)

sp_dr = 1/(18.242 - 9.881)*np.log(phi_dr2/phi_dr1)
print(sp_dr)

np.sqrt(0.025**2 + 0.025**2)

help(np.random.randint(10, size=(10, 10)))

## Other Condition Data

The data as presented in the original report are only tabulated for a couple of aircraft conditions for the Boeing 747, with the remainder of the data presented in graphical form. Thankfully, someone has already done the hard work of extracting those data from the graph and presenting in tabular form (it wasn't me, the following is taken from [Caughey's online course notes](https://courses.cit.cornell.edu/mae5070/Caughey_2011_04.pdf), borrowed with thanks).

The condition number confers to the Mach/SL diagram on Page 212 of the original report.

| Derivative                  | Condition 2        | Condition 5        | Condition 7       | Condition 9        | Condition 10       |
|-----------------------------|--------------------|--------------------|-------------------|--------------------|--------------------|
| $h$/ft                      | 0                  | 20,000             | 20,000            | 40,000             | 40,000             |
| $M$                         | 0.25               | 0.50               | 0.80              | 0.80               | 0.90               |
| $\alpha$/$^\circ$           | 5.70               | 6.80               | 0.0               | 4.60               | 2.40               |
| $W$/lb                      | 564,032            | 636,636            | 636,636           | 636,636            | 636,636            |
| $I_{xx}$ /(slug-ft$^2$) | 14.3 x $10^6$  | 18.4 x $10^6$  | 18.2 x $10^6$ | 18.2 x $10^6$  | 18.2 x $10^6$  |
| $I_{yy}$ /(slug-ft$^2$) | 32.3 x $10^6$  | 33.1 x $10^6$  | 33.1 x $10^6$ | 33.1 x $10^6$  | 33.1 x $10^6$  |
| $I_{zz}$ /(slug-ft$^2$) | 45.3 x $10^6$  | 49.5 x $10^6$  | 49.7 x $10^6$ | 49.7 x $10^6$  | 49.7 x $10^6$  |
| $I_{xz}$ /(slug-ft$^2$) | -2.23 x $10^6$ | -2.76 x $10^6$ | 0.97 x $10^6$ | -1.56 x $10^6$ | -0.35 x $10^6$ |
| $C_L$                       | 1.11               | 0.68               | 0.266             | 0.66               | 0.521              |
| $C_D$                       | 0.102              | 0.0393             | 0.0174            | 0.0415             | 0.0415             |
| $C_{L_\alpha}$              | 5.7                | 4.67               | 4.24              | 4.92               | 5.57               |
| $C_{D_\alpha}$              | 0.66               | 0.366              | 0.084             | 0.425              | 0.527              |
| $C_{m_\alpha}$              | -1.26              | -1.146             | -629              | -1.033             | -1.613             |
| $C_{L_\dot{\alpha}}$        | 6.7                | 6.53               | 5.99              | 5.91               | 5.53               |
| $C_{m_\dot{\alpha}}$        | -3.2               | -3.35              | -5.4              | -6.41              | -8.82              |
| $C_{L_q}$                   | 5.4                | 5.13               | 5.01              | 6                  | 6.94               |
| $C_{m_q}$                   | -20.8              | -20.7              | -20.5             | -24                | -25.1              |
| $C_{L_M}$                   | 0                  | -0.0875            | 0.105             | 0.205              | -0.278             |
| $C_{D_M}$                   | 0                  | 0                  | 0.008             | 0.0275             | 0.242              |
| $C_{m_M}$                   | 0                  | 0.121              | -0.116            | 0.166              | -0.114             |
| $C_{L_{\delta_e}}$          | 0.338              | 0.356              | 0.27              | 0.367              | 0.3                |
| $C_{m_{\delta_e}}$          | -1.34              | -1.43              | -1.06             | -1.45              | -1.2               |
| $C_{y_\beta}$               | -0.96              | -0.9               | -0.81             | -0.88              | -0.92              |
| $C_{l_\beta}$               | -0.221             | -193               | -0.164            | -0.277             | -0.095             |
| $C_{n_\beta}$               | 0.15               | 0.147              | 0.179             | 0.195              | 0.207              |
| $C_{l_p}$                   | -0.45              | -0.323             | -0.315            | -0.334             | -0.296             |
| $C_{n_p}$                   | -0.121             | -0.069             | 0.0028            | -0.042             | 0.023              |
| $C_{l_r}$                   | 0.101              | 0.212              | 0.0979            | 0.3                | 0.193              |
| $C_{n_r}$                   | -0.3               | -0.278             | -0.265            | -0.327             | -333               |
| $C_{l_{\delta_a}}$          | 0.0461             | 0.0129             | 0.012             | 0.0137             | 0.0139             |
| $C_{n_{\delta_a}}$          | 0.0064             | 0.0015             | 0.0008            | 0.0002             | -0.003             |
| $C_{y_{\delta_r}}$          | 0.175              | 0.1448             | 0.0841            | 0.1157             | 0.062              |
| $C_{l_{\delta_r}}$          | 0.007              | 0.0039             | 0.009             | 0.007              | 0.0052             |
| $C_{n_{\delta_r}}$          | -0.109             | -0.1081            | -0.099            | -0.1256            | -0.091             |


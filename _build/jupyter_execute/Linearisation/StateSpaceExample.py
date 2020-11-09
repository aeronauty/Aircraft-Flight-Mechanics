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
U0 = 165 # Knots
U0 = U0 * 1.68781 # to feet/second
S = 5500 # square feet
b = 195.68 # feet
c = 27.31 # feet
theta_0 = 0
W = 564032 # lbf
m = W/32.174 # mass
Iyy = 32.3e6 # slug-ft^2
Ixx = 14.3e6
Izz = 45.3e6
Ixz = -2.23e6

a = 1125.33 # sonic velocity in ft/s
g = 32.174

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

# Nstarred terms
I2 = Ixz / Izz
Nvstar = Imess * (Nv + I2 * Lv)
Npstar = Imess * (Np + I2 * Lp)
Nrstar = Imess * (Nr + I2 * Lr)

Alat = np.matrix([[Yv, 0, -U0, g*np.cos(theta_0), 0],
               [Lvstar, Lpstar, Lrstar, 0, 0],
               [Nvstar, Npstar, Nrstar, 0, 0],
               [0, 1, np.tan(theta_0), 0, 0],
               [0, 0, 1/np.cos(theta_0), 0, 0]])

print("The system matrix for lateral-directional motion is ")
display(Math('[A_{lat}] = ' + sp.latex(sp.Matrix(Alat).evalf(5))))

Note that we've not made either of the control matrices yet - and there's a good reason for that. If we consider the linearised model of the aircraft created, the _stability_ of the aircraft (_i.e.,_ its response to a perturbation) will be governed by the system matrix.

In the first instance, it is desired to understand the _stick fixed stability_ and understand what will happen to the aircraft if no inputs are made.

Consider what the two matrices developed actually show us; if the aircraft is disturbed from a given condition, then if the disturbance is a _symmetric_ state variable ($u, w, q, \theta$), then the output is a time rate of change of _all_ other symmetric variables. 

The control matrices tell us how the aircraft responds due to control input. Therefore, if we're interested in aircraft response in the absense of pilot or control-system input, then we're only interested in the A matrices themselves. The A matrices give the _open loop response_ of the aircraft.

Since these are ODEs, we could write a means to time-march through the solution - but there are some handy inbuilt tools in Python to look at the responses of state-space systems to different inputs.

You will probably need to install these to work on your system - [look here](https://python-control.readthedocs.io/en/0.8.3/intro.html#overview-of-the-toolbox): 

import control
import control.matlab

# We will make a unity B matrix to enable us to use the control system toolbox by _exciting the aircraft_ through
# Elevator input. Turn from Zde in 1/radians to 1/degree to put a useful input ino
Blon = np.matrix([[0], [np.radians(Zde)], [np.radians(Mdestar)], [0]])

# Turn the matrices into a state space object
LonSS = control.StateSpace(Alon, Blon, np.eye(Alon.shape[0]), np.zeros(Blon.shape))

# Look at the first 100 seconds response to a unit impulse in the only
Time, [u, w, q, theta] = control.impulse_response(LonSS, T=np.linspace(0, 500, 10000))


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

fig.update_xaxes(title_text="Time", row=1, col=1)
fig.update_yaxes(title_text="$u$", row=1, col=1)
fig.update_xaxes(title_text="Time", row=1, col=2)
fig.update_yaxes(title_text="$w$", row=1, col=2)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_yaxes(title_text="$q$", row=2, col=1)
fig.update_xaxes(title_text="Time", row=2, col=2)
fig.update_yaxes(title_text="$\\theta$", row=2, col=2)



Note that units have deliberately not been included in the above - we we started with the non-dimensional stability derivatives and then _dimensionalised_ them via US customary units for the aircraft geometry and conditions. So the units for the velocities are in feet/s, and the units for the angular quantities are in radians/s and radians.

If we'd used SI units at the outset to perform create the derivatives, we'd have ended up with different numbers in the matrix but very similar-looking graphs - simply with SI units on the y axis of each.

**Zoom into the graphs and see if you can see any difference between the short and long term response for this aircraft**


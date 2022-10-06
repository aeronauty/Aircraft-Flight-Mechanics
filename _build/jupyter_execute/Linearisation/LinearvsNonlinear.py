The following is a direct adaptation of an example given in my own undergraduate notes - reproduced with permission. Thanks, Dougie.

# Comparison of the Linear and Nonlinear Equations of Motion: Aircraft Simulation

The nonlinear equations of motion have been derived and will be repeated here:

$$m\begin{bmatrix} \dot{U} + QW - UR \\ \dot{V} + RU-PW\\\dot{W}+PV-QU\end{bmatrix}=\begin{matrix} -mg\sin\Theta - D\cos\alpha + L\sin\alpha + T\cos\Theta_T\\mg\sin\Phi\cos\Theta + F_{A_Y} + F_{T_Y}\\mg\cos\Phi\cos\Theta - D\sin\alpha - L\cos\alpha - T\sin\Theta_T\end{matrix}$$ 

$$\left[{\begin{matrix} \dot{P}\cdot I_{xx} \\ \dot{Q}\cdot I_{yy} \\\dot{R}\cdot I_{zz}\end{matrix}} \hspace{.5cm} \begin{matrix} + \\+\\+\end{matrix} \hspace{.5cm} {\begin{matrix} Q\cdot r\left(I_{zz} - I_{yy}\right) \\ P\cdot R\left(I_{xx} - I_{yy}\right) \\ P\cdot Q\left(I_{yy} - I_{xx}\right)\end{matrix}} \hspace{.5cm} \begin{matrix} - \\+\\+\end{matrix} \hspace{.5cm} {\begin{matrix}\left(\dot{R} + P\cdot Q\right) I_{xz} \\ \left(P^2 - R^2\right) I_{xz} \\ \left(Q\cdot R - \dot{P}\right) I_{xz}\end{matrix}} \right] = \begin{bmatrix} L \\ M \\ N\end{bmatrix}$$ 

$$\begin{aligned}
    \begin{bmatrix} P\\Q\\R\end{bmatrix} &= \begin{bmatrix}
    1 & 0 & -\sin\Theta\\
    0 & \cos\Phi & \sin\Phi\cos\Theta\\
    0 & -\sin\Phi & \cos\Phi\cos\Theta
 \end{bmatrix}\begin{bmatrix} \dot{\Phi}\\\dot{\Theta}\\\dot{\Psi}\end{bmatrix}\end{aligned}$$ 
 
 $$\begin{aligned}
\begin{bmatrix} \dot{\Phi}\\\dot{\Theta}\\\dot{\Psi}\end{bmatrix}&= \begin{bmatrix}
    1 & \sin\Phi\tan\Theta & \cos\Phi\tan\Theta\\
    0 & \cos\Phi & -\sin\Phi    \\
    0 & \frac{\sin\Phi}{\cos\Theta} & \frac{\cos\Phi}{\cos\Theta}
 \end{bmatrix}\begin{bmatrix} P\\Q\\R\end{bmatrix}\end{aligned}$$

a simulation of this aircraft in the longitudinal plane will be presented in this section. By constraining to longitudinal motion only, the solution of the nonlinear equations is heavily simplified, but the analysis can be expanded for the unconstrained case and if we assume the thrust inclination is zero. The simplifying assumption is: 

$$V=P=R=\Phi=\Psi=\Theta_0 = 0$$ 

and the equations describing longitudinal flight may now be we written: 

$$\begin{aligned}
    m\left(\dot{U} + Q\,W\right)     &= T - D\cos\alpha + L\cos\alpha - mg\,\sin\Theta\\
    m\left(\dot{W} - Q\,U\right)     &= -L\cos\alpha - D\sin\alpha+ mg\,\cos\Theta\\
    I_{yy}\,\dot{Q} &= M_A - T\,\Delta_{zT}\\
    \dot{\Theta}&=Q\end{aligned}$$
    
## HS125 (Hawker 800) Business Jet)

```{image} /Images/Hawker800.jpg
:alt: Hawker800
:class: bg-primary
:width: 300px
:align: center
```

The data for the HS125 Business jet are given in the table below. The aerodynamic model gives the lift, drag, and pitching moment coefficients as:

$$\begin{aligned}
    C_L &= C_{L_0} + C_{L_\alpha}\,\alpha + C_{L_{\delta_e}}\,\delta_e\\
    C_D &= C_{D_0} + C_{D_\alpha}\,\alpha + C_{D_{\alpha^2}}\,\alpha^2\\
    C_M &= C_{M_0} + C_{M_\alpha}\,\alpha + C_{M_{\delta_e}}\,\delta_e + C_{M_q}\,\hat{q}\\
    \hat{q}&\triangleq \frac{Q\,\bar{c}}{V_f}\end{aligned}$$




|          **Parameter**           |                        **Symbol**                     |           **Value**           |
|:--------------------------------:|:-----------------------------------------------------:|:-----------------------------:|
|               Mass               |                           $m$                         |             7500kg              |
|            Wing Area             |                           $S$                         |             32.8$\text{m}^2$              |
|    Pitching Moment of Inertia    |                         $I_{yy}$                      |            84,309$\text{kg m}^2$             |
|               MAC                |                        $\bar{c}$                      |             2.29m              |
| Thrustline vertical displacement |                      $\Delta_{zT}$                    |            -0.378m             |
|        Lift Coefficients         |      $C_{L_0},\, C_{L_\alpha},\, C_{L_{\delta_e}}$    |      0.895, 5.01, 0.722       |
|        Drag Coefficients         |      $C_{D_0},\, C_{D_\alpha},\, C_{D_{\alpha^2}}$    |      0.177, 0.232, 1.393      |
|         PM Coefficients          | $C_{M_0},\, C_{M_\alpha},\, C_{M_{\alpha^2},\, C_{M_q}}$| -0.046, -1.087, -1.88, -7.055 |

The reduced nonlinear equations of motion can be constructed into a function `eqnofmotion800`:

def eqnofmotion800(y, t=[], Thrust=13878):
    # The reduced state vector is a 7 x 1 vector
    # y = [U, W, Q, Theta, X_E, Z_E, dE]

    
    # Aircraft Parameters (all in SI)
    m=7484.4 # mass  = 7484.4kg  etc.
    s=32.8 #
    Iyy=84309
    cbar=2.29 
    dZt=-0.378
    rho=1.225 
    CD0=0.177 
    CDa=0.232 
    CDa2= 1.393
    CL0=0.895
    CLa=5.01 
    CLde=0.722
    CM0=-0.046 
    CMa=-1.087 
    CMde=-1.88 
    CMq=-7.055 

    
    # Get the current values of aircraft states
    dE = y[6] # Elevator input

    U=y[0] # Forward speed
    W=y[1] # Heave velocity
    Q=y[2] # Pitch rate
    Theta=y[3] # Pitch attitude
    
    # Determine some aerodynamic terms
    Vf=np.sqrt(U**2 + W**2) # Flight speed
    alpha = np.arctan(W/U) # Angle of attack
    qh = Q*cbar/Vf # Nondimensional pitch rate
    
    # Aerodynamic coefficients from Hawker model:
    CL = CL0 + CLa*alpha + CLde*dE
    CD = CD0 + CDa*alpha + CDa2*alpha*alpha
    CM = CM0 + CMa*alpha + CMde * dE + CMq*qh

    q_inf = .5*rho*Vf**2*s
    
    # Dimensional aero terms
    lift = q_inf*CL
    drag = q_inf*CD
    pm = q_inf*cbar*CM

    # Simplified nonlinear equations of motion
    ydot = np.zeros(7, dtype='float64')
    ydot[0] = -Q*W + (lift*np.sin(alpha) - drag*np.cos(alpha) + Thrust)/m - 9.80665*np.sin(Theta) # Udot
    ydot[1] = Q*U + (-lift*np.cos(alpha) - drag*np.sin(alpha))/m + 9.80665*np.cos(Theta) # Wdot
    ydot[2] = (pm - Thrust*dZt)/Iyy # M
    ydot[3] = Q # ThetaDot
    ydot[4] = U*np.cos(Theta) - W*np.sin(Theta) # X_Edot (earth axes)
    ydot[5] = U*np.sin(Theta) + W*np.cos(Theta) # Z_Edot (earth axes)
    ydot[6] = 0 # No change to elevator

    return ydot


To determine the transient aircraft response, first the trim state must be determined.

## Trim State Determination

By definition, the trim case is found by setting the accelerations and angular velocities to zero. Hence the equations of motion become:

$$\begin{aligned}
    0    &= T - D\cos\alpha + L\cos\alpha - mg\,\sin\Theta\\
    0    &= -L\cos\alpha - D\sin\alpha+ mg\,\cos\Theta\\
    0 &= M_A - T\Delta_{zT}\end{aligned}$$
    
The knowns in the above are flightspeed, $V_f$, density (from altitude), $\rho$, and climb angle/flight path angle $\gamma$ (setting $U_E$ and $W_E$). These may be solved via any means you like to get the reference trim state. An example of a Newton-Raphson solver[^4] is included below as `TrimState` which finds trim using `TotalForces`:

[^4]: You will not be tested on things like this in an examination in this course, but it's really in your interest to ensure that you can a) understand how this solver works and b) be confident you could write something that does the same job yourself.

from ambiance import Atmosphere
import numpy as np

def TotalForces(T, de, Theta, Vf, h, gamma):
    '''This gives the total forces for the HS 125 simplified longitudinal
    aircraft
    Inputs: Thrust/N, elevator deflection/deg, theta/rad, flightspeed/m/s,
    flightpath/rad
    altitude/m
    '''


    # Aircraft Parameters (all in SI)
    m=7484.4 # mass  = 7484.4kg  etc.
    s=32.8 #
    Iyy=84309
    cbar=2.29 
    dZt=-0.378
    rho=1.225 
    CD0=0.177 
    CDa=0.232 
    CDa2= 1.393
    CL0=0.895
    CLa=5.01 
    CLde=0.722
    CM0=-0.046 
    CMa=-1.087 
    CMde=-1.88 
    CMq=-7.055 
    Thrust=13878
    g = 9.80665

    qh = 0  # Trim definition
    
    rho = Atmosphere(h).density

    # Get the Ue and Ve
    alpha = Theta - gamma
    CL = CL0 + CLa*alpha + CLde*de
    CD = CD0 + CDa*alpha + CDa2*alpha*alpha
    CM = CM0 + CMa*alpha + CMde * de + CMq*qh

    q_infs = .5*rho*Vf**2*s

    # Dimensional lift
    lift = q_infs*CL
    drag = q_infs*CD
    pm = q_infs*cbar*CM


    # Determine lift and drag
    F = np.zeros((3, 1))

    F[0] = T - drag*np.cos(alpha) + lift*np.sin(alpha) - m*g*np.sin(Theta)
    F[1] = -lift*np.cos(alpha) -drag*np.sin(alpha) + m*g*np.cos(Theta)
    F[2] = pm - T*dZt
    return F

def TrimState(Vf = 120 * 0.5144444, h = 0, gamma = 0):
    '''This function solves for the longitudinal trim of the HS125 using a Newton-Raphson method'''



    # First guess and increments for the jacobian <---- may need to adjust these
    T = 15000
    dT = 1
    de = 0*np.pi/180
    dde = .01*np.pi/180
    Theta = 2*np.pi/180
    dTheta = dde;

    # Gets the value of the functions at the initial guess
    trim = TotalForces(T, de, Theta, Vf, h, gamma);

    Trimstate = np.array([[T], [de], [Theta]])

    itercount = 0
    while max(abs(trim)) > 1e-5:  
        itercount = itercount + 1
        # Get value of the function
        trim = TotalForces(T, de, Theta, Vf, h, gamma);


        # Get the Jacobian approximation (3 x 3)
        JT = np.squeeze(TotalForces(T + dT, de, Theta, Vf, h, gamma)/dT)
        Jde = np.squeeze(TotalForces(T, de + dde, Theta, Vf, h, gamma)/dde)
        JTheta = np.squeeze(TotalForces(T, de, Theta + dTheta, Vf, h, gamma)/dTheta)
        Jac = np.transpose(np.array([JT, Jde, JTheta]))

        # Get the next iteration
        Trimstate = Trimstate - np.dot(np.linalg.inv(Jac), trim)


        T = Trimstate[0]
        de = Trimstate[1]
        Theta = Trimstate[2]
    
    print(f"Converged after {itercount} iterations")
    print(f'For inputs of Vf = {Vf:1.2f}m/s, h = {h/1e3:1.2f}km, gamma = {gamma:1.2f}deg\n')
    print(f'Thrust = {T[0]/1e3:1.2f}kN, de = {np.degrees(de[0]):1.2f}deg, Theta = {np.degrees(Theta[0]):1.2f}deg\n')

    return Trimstate

TrimState();


For a trim input of sea-level and 120kn, the trim is found to be - $T = 13.84$kN, $\delta_e = -0.98^\circ$, $\Theta = 0.84^\circ$. A quick sense check shows that the aircraft is slightly nose up (less than a degree) so the aerodynamic pitching moment from the wing/fuselage will be nose-up, and the elevator is deflected trailing edge *up* to balance the pitching moment.

## Transient Simulation

For level flight (trim), the initial conditions are given from from the previous step - if the aircraft remains undisturbed, then there will be no variation in any of the parameters. The nonlinear equations cannot be solved analytically, so if the aircraft response to control inputs is desired, then a numerical scheme must be used.

The case of a positive elevator deflection corresponding to a stick-forward displacement will be explored. First, the response to a $\delta_e^\prime=1^\circ$ will be explored - this is equivalent to the pilot pushing the stick forward and holding it, keeping other controls constant. 

The equations are solved numerically using `scipy`'s `odeint` (which is very similar to ODE45 in MATLAB)

# Set the inputs
de = -1
de = np.radians(de)
h = 0
Vf = 120*.51444
gamma = 0

# Determine the trim state   
trimstate = TrimState(Vf, h, gamma)
alpha = trimstate[2] - gamma
Ue = Vf*np.cos(alpha)
We = Vf*np.sin(alpha)
Qe = 0
ThetaE = trimstate[2]
Xe = 0
Ze = h; 
    
# Initial conditions
from scipy.integrate import odeint
y0 = np.array([Ue[0], We[0], Qe, ThetaE[0], Xe, Ze, (de + trimstate[1])[0]])

t = np.linspace(0, 100, 1000)
output = odeint(eqnofmotion800, y0, t, args=(trimstate[0],))

U = output[:, 0]
W = output[:, 1]
Q = output[:, 2]
Theta = output[:, 3]
Alt = output[:, 5]
alpha = np.arctan2(W, U)
FS = np.sqrt(U**2 + W**2)

# Plot 'em
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=2, subplot_titles=("Forward Speed", "Heave Velocity", "Pitch Rate", "Pitch Attitude", "Altitude", "AoA"))

fig.add_trace(
    go.Scatter(x = t, y = U, showlegend=False), row=1, col=1)

fig.add_trace(
    go.Scatter(x = t, y = W, showlegend=False), row=1, col=2)

fig.add_trace(
    go.Scatter(x = t, y = Q, showlegend=False), row=2, col=1)

fig.add_trace(
    go.Scatter(x = t, y = Theta, showlegend=False), row=2, col=2)

fig.add_trace(
    go.Scatter(x = output[:, 4], y = Alt, showlegend=False), row=3, col=1)

fig.add_trace(
    go.Scatter(x = t, y = alpha, showlegend=False), row=3, col=2)



fig.update_xaxes(title_text="Time", row=1, col=1)
fig.update_yaxes(title_text=f"U / (m/s)", row=1, col=1)
fig.update_xaxes(title_text="Time", row=1, col=2)
fig.update_yaxes(title_text=f"W / (m/s)", row=1, col=2)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_yaxes(title_text="Q / (deg/s)", row=2, col=1)
fig.update_xaxes(title_text="Time", row=2, col=2)
fig.update_yaxes(title_text="θ / deg", row=2, col=2)
fig.update_xaxes(title_text="Horizontal Distance", row=3, col=1)
fig.update_yaxes(title_text="Alt / m", row=3, col=1)
fig.update_xaxes(title_text="Time", row=3, col=2)
fig.update_yaxes(title_text="AoA / deg", row=3, col=2)



It should be noted that the values above are *total* values and NOT perturbational values. We can compare a linear model of the HS125 with the reduced nonlinear model, above - but rather than sourcing HS 125 data of unknown legacy, it makes _more_ sense (but more work) to use the HS125 model to produce numerical derivatives based upon small perturbation theory using the model itself.

$$\newcommand{\pd}[2]{\frac{\partial#1}{\partial#2}}$$
$$\newcommand{\ppd}[2]{\frac{\partial^2#1}{\partial#2^2}}$$
$$\newcommand{\pppd}[2]{\frac{\partial^3#1}{\partial#2^3}}$$

# Numerical Linearisation of the Equations of Motion

This section shall stick with the HS 125 business jet. For the longitudinal equations of motion:

$$\begin{aligned}
    \begin{bmatrix} \dot{u}\\\dot{w}\\\dot{q}\\\dot{\theta}\end{bmatrix} &= \begin{bmatrix}
        X_u & X_w & 0 & -g\cdot\cos\theta_0\\
        Z_u & Z_w & U_0 & -g\cdot\sin\theta_0\\
        M_u^* & M_w^* & M_q^* & M_\theta^*\\
        0 & 0 & 1 & 0   
    \end{bmatrix}\begin{bmatrix}
        {u}\\{w}\\{q}\\{\theta^\prime}         
    \end{bmatrix} + \begin{bmatrix}
        0\\Z_{\delta_0}\\M_{\delta_0}^*\\0          
    \end{bmatrix}\left[\delta_0\right]\\
    \dot{\vec{x}} &= \hspace{2cm} A\vec{x} + B\vec{u}
\end{aligned}$$

$$\begin{aligned}
        M_u^*&\triangleq M_u + M_{\dot{w}}Z_u\,\,\,\,\,\,\,\,M_w^*\triangleq M_w+M_{\dot{w}}Z_w\,\,\,\,\,\,\,\,M_q^*\triangleq M_q+M_{\dot{w}}U_0\nonumber\\
        M_{\delta_0}^*&\triangleq M_{\delta_0}+M_{\dot{w}}Z_{\delta_0}\,\,\,\,\,\,\,\,M_{\theta}^*\triangleq-M_{\dot{w}}g\sin\theta_0 \nonumber  \end{aligned}$$

For each of the derivatives contained above, a central-difference approach may be utilised. That is, if the longitudinal force is a function of the aircraft states:

$$X = f\left(U, W, Q,\Theta_0,\delta_{e_0}\right)$$

then each of the stability derivatives may be expressed as a numerical partial derivative. For example

$$X_u = \frac{1}{m}\left.\pd{X}{u}\right|_0=\frac{1}{m}\left[\frac{f\left(U_0+\delta U,W_0,Q_0,\theta_0,\delta_{e_0}\right)-f\left(U_0- \delta U,W_0,Q_0,\theta_0,\delta_{e_0}\right)}{2\delta U}\right]$$

Note that the variable that the derivative is with respect to is altered, and the others are held constant - this is a partial derivative. This can be repeated for the remaining derivatives. This procedure has been used below to create stability derivatives.

`ForcesandMoments` gives values of the $X$, $Z$, and $M$ force and moments, and then `NumerialDerivatives` uses a central difference approach _with_ `ForcesandMoments` to create the s 




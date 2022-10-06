You guys have the supplementary notes in PDF form for the aircraft modes of motion, and the last bit is best taught by way of an example.

# Final Examples

## Aircraft Modes from Stability Derivatives

Consider the following aircraft data for the Pipe Cherokee PA-28-180 flying at 50m/s.

|                         |                         |                         |
|:------------------------|:------------------------|:------------------------|
| $m$ = 1090kg            | $S$ = 15                | $I_{yy}$ = 1700         |
| $I_{xx}$ = 3100         | $I_{zz}$ = 1400         | $I_{xz}$ = 0            |
| $U_e$ = 50              | $\rho$=1.06             | $\bar{c}$ = 1.6         |
| $C_{L_0}$ = 0.543       | $C_{D_0}$ = 0.0615      | $b$ = 9.11              |
|                         |                         |                         |
| $X_u$ = -0.06728        | $Z_u$ = -0.396          | $M_u$ = 0.0             |
| $X_w$ = 0.02323         | $Z_w$ = -1.729          | $M_w$ = -0.2772         |
| $X_q$ = 0.0             | $Z_q$ = -1.6804         | $M_q$ = -2.207          |
| $M_{\dot{w}}$ = -0.0197 | $Z_{\delta_e}$ = -17.01 | $M_{\delta_e}$ = -44.71 |
|                         |                         |                         |
| $Y_v$ = -0.1444         | $L_v$ = -0.1166         | $N_v$ = 0.174           |
|                         | $L_p$ = -2.283          | $N_p$ = -1.732          |
|                         | $L_r$ = 1.053           | $N_r$ = -1.029          |
| $Y_{\delta_r}$ = 2.113  | $L_{\delta_r}$ = 0.6133 | $N_{\delta_r}$ = -6.583 |
|                         | $L_{\delta_a}$ = 3.101  | $N_{\delta_a}$ = 0.0    |

The following example has been completed using Python, and I'm a better coder than when I first wrote the examples [in MATLAB nearly three years ago](https://aircraftflightmechanics.com/otherfiles/PiperCherokee.m), so my codes look more like programs than a list of calculator instructions.

I know that this can make things seem _less_ accessible to some, but it's smarter to keep data in a class like below.

# The means that I'm using the compute this is to store the Cherokee stability derivatives in a class,
# and then make a function to produce the stability deritatives. This is the easiest way to make readable code
# that's easily extensible to other aircraft without copying and pasting, or having all the derivatives live
# in the general namespace

import numpy as np
import sympy as sp
from IPython.display import display, Math, Latex, Markdown
import plotly.graph_objects as go


# All data for Piper Cherokee PA-28-180
class Cherokee():
    h = 1200
    V = 50
    S = 15
    m = 1090
    Ixx = 1300 
    Izz = 1400
    Ixz = 0
    Iyy = 1700 
    CL0 = 0.543
    CD0 = 0.0615
    b = 9.11
    cbar = 1.3
    U0 = 50
    theta_0=0

    Ue = V

    g = 9.80665

    Xu = -0.06728
    Zu = -0.396
    Mu = 0.0
    Xw = 0.02323
    Zw = -1.729
    Mw = -0.2772
    Xq = 0.0
    Zq = -1.6804
    Mq = -2.207
    Mdw = -0.0197
    Zde = -17.01
    Mde = -44.71

    Yv = -0.1444
    Lv = -0.1166
    Nv = 0.174
    Lp = -2.283
    Np = -1.732
    Lr = 1.053
    Nr = -1.029
    Ydr = 2.113
    Ldr = 0.6133
    Ndr = -6.583
    Lda = 3.101
    Nda = 0.0
    
# Make A and B matrices for longitudinal motion
def MakeLongitudinal(ac):    
    # Determine the M* derivatives (assuming Theta_e = 0)
    Mu_star = ac.Mu + ac.Mdw*ac.Zu;
    Mw_star = ac.Mw + ac.Mdw*ac.Zw;
    Mq_star = ac.Mq + ac.Mdw*ac.Ue;
    Mth_star = 0;
    Mde_star = ac.Mde + ac.Mdw*ac.Zde;
    
    if not hasattr(ac, 'theta0'):
        ac.theta0 = 0
    
    A = np.array([[ac.Xu, ac.Xw, 0, -ac.g*np.cos(ac.theta0)],
                [ac.Zu, ac.Zw, ac.U0, -ac.g*np.sin(ac.theta0)],
                [Mu_star, Mw_star, Mq_star, Mth_star],
                [0, 0, 1, 0]])
    
    # Make the control/input matrix, for good measure
    B = np.array([[0], [ac.Zde], [Mde_star], [0]])
    return A, B

def MakeLateral(ac):
    # Making the starred terms
    Imess = ac.Ixx * ac.Izz / (ac.Ixx * ac.Izz - ac.Ixz**2)
    I2 = ac.Ixz / ac.Ixx

    # Lstarred terms
    Lvstar = Imess * (ac.Lv + I2 * ac.Nv)
    Lpstar = Imess * (ac.Lp + I2 * ac.Np)
    Lrstar = Imess * (ac.Lr + I2 * ac.Nr)
    Ldrstar = Imess * (ac.Ldr + I2 * ac.Ndr)
    Ldastar = Imess * (ac.Lda + I2 * ac.Nda)

    # Nstarred terms
    I2 = ac.Ixz / ac.Izz
    Nvstar = Imess * (ac.Nv + I2 * ac.Lv)
    Npstar = Imess * (ac.Np + I2 * ac.Lp)
    Nrstar = Imess * (ac.Nr + I2 * ac.Lr)
    Ndrstar = Imess * (ac.Ndr + I2 * ac.Ldr)
    Ndastar = Imess * (ac.Nda + I2 * ac.Lda)
    
    # Make the lateral matrix
    A = np.matrix([[ac.Yv, 0, -ac.U0, ac.g*np.cos(ac.theta_0), 0],
                   [Lvstar, Lpstar, Lrstar, 0, 0],
                   [Nvstar, Npstar, Nrstar, 0, 0],
                   [0, 1, np.tan(ac.theta_0), 0, 0],
                   [0, 0, 1/np.cos(ac.theta_0), 0, 0]])

    # And the control matrix
    if not hasattr(ac, 'Yda'):
        ac.Yda = 0
        
    B = np.matrix([[ac.Ydr, ac.Yda], [Ldrstar, Ldastar], [Ndrstar, Ndastar], [0, 0], [0, 0]])
    
    return A, B

# Make the two sets of matrices
Alon, Blon = MakeLongitudinal(Cherokee)
Alat, Blat = MakeLateral(Cherokee)

print("The longitudinal A and B matrices for this aircraft are")
display(Math('[A_{lon}] = ' + sp.latex(sp.Matrix(Alon).evalf(5))))
display(Math('[B_{lon}] = ' + sp.latex(sp.Matrix(Blon).evalf(5))))

print("The lateral/directional A and B matrices for this aircraft are")
display(Math('[A_{lat}] = ' + sp.latex(sp.Matrix(Alat).evalf(5))))
display(Math('[B_{lat}] = ' + sp.latex(sp.Matrix(Blat).evalf(5))))

# Get the eigenvalues
eigs_lon, eigv_lon = np.linalg.eig(Alon)

# We know these will always be a complex pair, so can separate. You could get the second one
# by fixing the index, but I like to do boolean indexing
eig1 = eigs_lon[0]
eig2 = eigs_lon[eigs_lon.real != eig1.real][0]

# A quick function to print the single eigenvalue as a complex pair
def makecomplexpair(eigin, roundto=4):
    return str(eigin.round(roundto)).replace('+', '±').strip('(').strip(')')

print(f"The eigenvalues associated with longtudinal motion are the complex pair {makecomplexpair(eig1)}, and {makecomplexpair(eig2)}")

from myst_nb import glue
glue("eig1", f"{makecomplexpair(eig1)}", display=False)
glue("eig2", f"{makecomplexpair(eig2)}", display=False)
   


# do the same for the lateral-directional modes
# Get the eigenvalues
eigs_lat, eigv_lat = np.linalg.eig(Alat)


# Find the dutch roll - the only part with a non-zero imaginary component
eig_DR = eigs_lat[eigs_lat.imag > 0][0]
other_lat_eigs = eigs_lat[eigs_lat.imag == 0]

print(f"The eigenvalues associated with lateral-direction motion are:\nThe complex pair {makecomplexpair(eig_DR)}")
# This next line is complicated but elegant because I like to enjoy how wonderfully easy it is to manipulate strings in Python by contrast to MATLAB
print(f"and {len(other_lat_eigs)} other real eigenvalues:  {' '.join(str(other_lat_eigs.real.round(4)).split())[2:].replace(' ', ' and ').strip('[').strip(']')}")


from myst_nb import glue
glue("eig3", f"{makecomplexpair(eig_DR)}", display=False)
glue("eig4", f"{str(other_lat_eigs[0].real.round(4))}", display=False)
glue("eig5", f"{str(other_lat_eigs[1].real.round(4))}", display=False)
glue("eig6", f"{str(other_lat_eigs[2].real.round(4))}", display=False)
   


<!-- <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-5107176300009857"
     data-ad-slot="7122611277"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script> -->

### Longitudinal Modes

The two eigenvalues are {glue:text}`eig1` and  {glue:text}`eig2`, and we can easily discriminate between the two modes because of the respective size. Recall that the _damped natural frequency_ is given by the imaginary part of the eigenvalue, so we can see:

# A bit of logic to determine which mode is which
if eig1.imag > eig2.imag:
    SP = eig1
    PH = eig2
else:
    SP = eig2
    PH = eig1


    
print(f"From inspection of the imaginary part of the eigenvalues, {makecomplexpair(SP)} is clearly the short period mode, with a period of {2*np.pi/SP.imag:1.4}s\n")
print(f"From inspection of the imaginary part of the eigenvalues, {makecomplexpair(PH)} is clearly the Phugoid mode, with a period of {2*np.pi/PH.imag:1.4}s\n")


Since both modes are stable, the time to _half_ amplitude can be found from the real part of the eigenvalue

def timetohalf(eig):
    return -0.69/eig.real

for e, n in zip([SP, PH], ['Short Period', "Phugoid"]):
    print(f"The time to half amplitude of the {n} mode is {timetohalf(e):1.2f}s")

The undamped natural frequency, $\omega_n$, is given by the absolute value of the eigenvalue,

$$\omega_n=\sqrt{\Re\left({\lambda}\right)^2 + \Im\left({\lambda}\right)^2}$$

and hence the damping ratio, $\zeta$ can be determine either from comparison with the standard form characteristic equation and

$\zeta = -\frac{\Re(\lambda)}{\omega_n}$

or from the definition of the damped natural frequency

$\zeta = \sqrt{1-\frac{\omega_d^2}{\omega_n^2}}$

for e, n in zip([SP, PH], ['Short Period', "Phugoid"]):
    print(f"The undamped natural frequency of the {n} mode is {np.abs(e):1.4f}rad/s")
    
    zeta = -e.real/np.abs(e)
    print(f"which gives a damping ratio, from method 1 of {zeta:1.4f}")
    
    zeta = np.sqrt(1-e.imag**2/np.abs(e)**2)
    print(f"and a damping ratio, from method 2 of {zeta:1.4f}\n")

the two methodologies obviously are, and were always going to be equivalent, but it's nice to show redundancy in methods.

<!-- <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-5107176300009857"
     data-ad-slot="7122611277"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script> -->

### Lateral Directional Modes

From the A matrix for lateral directional motion the eigenvalues 

{glue:text}`eig3`, 
{glue:text}`eig4`,  
{glue:text}`eig5`, 
{glue:text}`eig6` 

are found. The first value is the only complex pair, and therefore _has_ to be the Dutch Roll mode (the only oscillatory lateral/directional mode). We can see that is **stable** (negative real part) and the following can be yielded using the same as before:

print(f"From inspection of the imaginary part of the eigenvalue, {makecomplexpair(eig_DR)}, the Dutch Roll mode, has a period of {2*np.pi/eig_DR.imag:1.4}s\n\
and a time to half amplitude of {-0.69/eig_DR.real:1.4}s.")


For the remaining eigenvalues, one simply denotes the aircraft's ability to yaw - the zero value shows that the aircraft has directional freedom and no real concept of heading stability (you _could_ at most say the aircraft possesses _neutral_ heading stability). The other two eigenvalues are real-only; {glue:text}`eig5` and {glue:text}`eig6`. 

We know that one denotes the **spiral** mode and one denotes the **roll mode**. The absolute magnitude of the damping indicates that {glue:text}`eig5` is the **roll mode**, whilst it can also be seen that {glue:text}`eig6` is _unstable_ so _cannot be the roll mode_.

In summary:


print(f"For this aircraft the spiral mode is unstable with a time to double amplitude of {0.69/other_lat_eigs[2].real:1.2f}s")

print(f"For this aircraft the roll mode is stable (which is *has* to be) with a time to half amplitude of {0-0.69/other_lat_eigs[1].real:1.2f}s")

## Extracting Aircraft Modes from Data

Say you've been given some data for an aircraft subjected to a roll disturbance in a datafile - the information you have is [roll attitude vs time in a text file](https://www.aircraftflightmechanics.com/Data/RollDisturbance.csv).

The data is the free-response of the aircraft, just as seen in the examples following the _impulsive_ forcing of the aircraft.


# Make up some data - first, spiral mode
Phi_dist = 1.23
Phi_final = 10
t_final = 80

# get the eigenvalue
lam_spiral_input = np.log(Phi_final/Phi_dist)/t_final


# Simulate the data
t = np.linspace(0, t_final, 1000)
Phi_spiral = Phi_dist * np.exp(lam_spiral_input * t)

# # Just plot the roll attitude
# fig = go.Figure()
# fig.update_layout(title="Roll Attitude", title_x=0.5)
# fig.add_trace(go.Scatter(x=t, y=Phi_spiral.real))

# Add in a Dutch Roll Mode
a = -0.15 # Real part
w = 1.24 # Frequency
Phi_dist_dr = 2.57

Phi_dr = Phi_dist_dr*np.exp(a*t + w*1j*(t+np.random.random(1)[0]*0))

Phi_total = Phi_spiral + Phi_dr



# # Make a data file of these 
data = np.array([t.transpose(), Phi_total.real.transpose()]).transpose()

np.savetxt('RollDisturbance.csv', data, delimiter=',', header="Time, Phi");


Plotting these data vs time is the first step, and we can see:

fig = go.Figure()
fig.update_layout(title="Roll Attitude", title_x=0.5)
fig.add_trace(go.Scatter(x=t, y=Phi_total.real))
fig.update_xaxes(title_text="Time/s")
fig.update_yaxes(title_text="Roll Attitude/deg")
fig.show()

Note that the file itself doesn't actually tell you the units of the roll attitude, but for determination of the modal qualities, it doesn't acutally matter. The y axis values are only used to get the damping _ratios_.

You can determine that this file contains information about the lateral-directional modes since we're looking at _roll attitude_. Furthermore, you can see:
- Spiral mode and Dutch roll mode are superposed on the data.
- The Dutch roll mode is *stable* (decreasing amplitude).
- The Spiral mode is *unstable* (increasing amplitude).
- The Roll mode is not visible.

This is the same as the example went over in class _except_ the spiral mode is unstable. The theory is the same, though. We need to remove the effect of the spiral mode on the roll mode. You can do this by hand, or using computational methods.

The first step is to graphically separate the two modes. We will look at what the starting value of the spiral mode is. Visually, this is the intercept if we were to imagine the curve _without_ the Dutch roll mode.

from scipy.interpolate import interp1d
r60 = interp1d(t, Phi_total.real)(60)
r80 = interp1d(t, Phi_total.real)(80)

fig = go.Figure()
fig.update_layout(title="Roll Attitude", title_x=0.5)
fig.add_trace(go.Scatter(x=t, y=Phi_total.real, showlegend=False))
fig.update_xaxes(title_text="Time/s")
fig.update_yaxes(title_text="Roll Attitude/deg")

fig.add_trace(go.Scatter(x=[60], y=[r60], mode="markers+text", text=f"   60s, {r60:1.3}deg", showlegend=False, textposition='middle right'))
fig.add_trace(go.Scatter(x=[80], y=[r80], mode="markers+text", text=f"80s, {r80:1.3}deg     ", showlegend=False, textposition='middle left'))

The spiral roll attitude is of the form

$$\phi_{sp}=\phi_0 e^{\lambda_{sp}t}$$

where $\phi_{0}$ is intercept on the y-axis if the Dutch roll were not present.

We can see that if we extend the curve to the y-axis, it looks like it would intercept _around_ 1.2 degrees, and has the two values given above. We can try this number and see if it works well by looking at the final value on the curve. That is, if we hvae $\phi_0=1.2$, then use the fact that we know $\phi(80s)=10$ and solve for $\lambda_{sp}$

Below shows two methods - one is guessing, which you can perform by trial and error and _see_ which is a good fit through different data points, and the other is a means to fit the curve. That's just there for advanced folks.

import warnings
warnings.filterwarnings('ignore')

## Method 1 = just make a guess
phi_0_guess = 1.2

lam_sp_guess = np.log(10/phi_0_guess)/80
print(f"With a guess of {phi_0_guess} as the intercept, the eigenvalue for the spiral mode is {lam_sp_guess:1.4}")



fig = go.Figure()
fig.update_layout(title="Roll Attitude", title_x=0.5)
fig.add_trace(go.Scatter(x=t, y=Phi_total.real, showlegend=False))
fig.update_xaxes(title_text="Time/s")
fig.update_yaxes(title_text="Roll Attitude/deg")

fig.add_trace(go.Scatter(x=[60], y=[r60], mode="markers+text", text=f"   60s, {r60:1.3}deg", showlegend=False, textposition='middle right'))
fig.add_trace(go.Scatter(x=[80], y=[r80], mode="markers+text", text=f"80s, {r80:1.3}deg     ", showlegend=False, textposition='middle left'))

# Add the guess
spiral_guess = phi_0_guess * np.exp(lam_sp_guess * t)
fig.add_trace(go.Scatter(x=t, y=spiral_guess, showlegend=True, name=f"Guessed Intercept = {phi_0_guess}"))

## Method two - do a fit
# Make a function to minimise
def just_the_spiral(t, phi_0sp, lam_sp):
    return phi_0sp * np.exp(lam_sp * t)

from scipy.optimize import curve_fit

# Need to supply an intial guess or it'll have trouble
params, _ = curve_fit(just_the_spiral, t[t > 30], Phi_total[t > 30], p0=[phi_0_guess, lam_sp_guess])


fig.add_trace(go.Scatter(x=t, y=just_the_spiral(t, params[0], params[1]), name="Least-squares fit"))
fig.show()

print(f"Using the intial guess as the starting point for a least-squares fit gives {params[0]:1.3}\
as the intercept,\n the eigenvalue for the spiral mode is {params[1]:1.4}")



With the eigenvalue for the spiral mode now known, it can be _removed_ from the data to look at the Dutch Roll on its own.

If you were doing this by hand, you could look at the peaks of the DR on its own, but it's relatively easy to do this on the whole array. This will be completed with the least-squares fit _and_ the guessed values from above.

# Using guessed values for the spiral mode intial value and eigenvalue, it can be subtracted from the Dutch Roll
just_dutch_roll = Phi_total - phi_0_guess * np.exp(t * lam_sp_guess)

# Repeats the original figure
fig.show()

# Adds on the bit we've just calculated
fig.add_trace(go.Scatter(x=t, y=just_dutch_roll.real, name="Spiral Removed"))

# Find some peak values using Scipy
from scipy.signal import find_peaks

# Get the indices of the peaks for the total signal and the bit we've just removed
ipeaks_total = find_peaks(Phi_total)[0]
ipeaks_dr = find_peaks(just_dutch_roll)[0]
# Add on the first couple of peaks to both
for i in range(2):
    fig.add_trace(go.Scatter(x=[t[ipeaks_total[i]]], y = [Phi_total[ipeaks_total[i]].real], mode="markers+text", text=f"{t[ipeaks_total[i]]:1.2f}, {Phi_total.real[ipeaks_total[i]]:1.2f}", textposition='top center', showlegend=False))
    fig.add_trace(go.Scatter(x=[t[ipeaks_dr[i]]], y = [just_dutch_roll[ipeaks_dr[i]].real], mode="markers+text", text=f"{t[ipeaks_dr[i]]:1.2f}, {just_dutch_roll.real[ipeaks_dr[i]]:1.2f}", textposition='bottom center', showlegend=False))

fig.show()

The damped natural frequency is available from the _red_ plot. The logic used to display them on the graph isn't necessary for you guys to do. You can do this by inspection of the graph - but it's easier to do it as an example this way.

The damped natural frequency is:

# Get the damped natural frequency from the curve containing *just* the spiral mode
wd_dr = 2*np.pi / (t[ipeaks_dr[1] - ipeaks_dr[0]])

# If you didn't remove the spiral_mode
wd_dr_wrong = 2*np.pi / (t[ipeaks_total[1] - ipeaks_total[0]])

print(f"The damped natural frequency of the Dutch Roll mode is {wd_dr:1.4}rad/s, but you would have got {wd_dr_wrong:1.4f}rad/s if you didn't remove the spiral mode" )

The damping ratio is given by the exponential decay:

# Remake the figure, again. Tis time we'll just include the DR
fig = go.Figure()
fig.update_xaxes(title_text="Time/s")
fig.update_yaxes(title_text="Roll Attitude/deg")
fig.add_trace(go.Scatter(x=t, y=just_dutch_roll.real, name="Spiral Removed"))


# Get the exponential decay thus giving the eigenvalue
lam_dr_real = np.log(just_dutch_roll.real[ipeaks_dr[1]]/just_dutch_roll.real[ipeaks_dr[0]])/t[ipeaks_dr[1] - ipeaks_dr[0]]
lam_dr_real_wrong = np.log(Phi_total.real[ipeaks_total[1]]/Phi_total.real[ipeaks_total[0]])/t[ipeaks_total[1] - ipeaks_total[0]]

print(f"The real part of the eigenvalue of the Dutch Roll mode is {lam_dr_real:1.3f}")

# Make the eigenvalue
eig_dr = lam_dr_real + wd_dr * 1j
eig_dr_wrong = lam_dr_real_wrong + wd_dr_wrong * 1j

print(f"This makes the total eigenvalue of the Dutch Roll mode is {makecomplexpair(eig_dr)}\n\n")

print(f"If you didn't get rid of the spiral mode, you would have got {makecomplexpair(eig_dr_wrong)}")

# Put on the graph to check
exp_bracket_upper = just_dutch_roll.real[0] * np.exp(eig_dr.real * t)
fig.add_trace(go.Scatter(x=t, y=exp_bracket_upper.real, name="Exponential Decay"))
fig.show()


The exponential decay 'envelope' is pretty good, but it neither tends to actual zero, which it should, not does it really go through the actual peaks. This is because the spiral mode hasn't been fully removed from the data above due to the guess not being quite correct.

Now this will be repeated with the _fitted_ values in place of the guessed ones for the Spiral mode:

# Using fitted values
just_dutch_roll = Phi_total - params[0] * np.exp(t * params[1])

# Remake the figure, again
fig = go.Figure()
fig.update_layout(title="Roll Attitude", title_x=0.5)
fig.add_trace(go.Scatter(x=t, y=Phi_total.real, showlegend=True, name="Total Roll"))
fig.update_xaxes(title_text="Time/s")
fig.update_yaxes(title_text="Roll Attitude/deg")
fig.add_trace(go.Scatter(x=t, y=just_dutch_roll.real, name="Spiral Removed"))

# Put first two peaks to get the info for the Dutch Roll
from scipy.signal import find_peaks

ipeaks_total = find_peaks(Phi_total)[0]
ipeaks_dr = find_peaks(just_dutch_roll)[0]

for i in range(2):
    fig.add_trace(go.Scatter(x=[t[ipeaks_total[i]]], y = [Phi_total[ipeaks_total[i]].real], mode="markers+text", text=f"{t[ipeaks_total[i]]:1.2f}, {Phi_total.real[ipeaks_total[i]]:1.2f}", textposition='top center', showlegend=False))
    fig.add_trace(go.Scatter(x=[t[ipeaks_dr[i]]], y = [just_dutch_roll[ipeaks_dr[i]].real], mode="markers+text", text=f"{t[ipeaks_dr[i]]:1.2f}, {just_dutch_roll.real[ipeaks_dr[i]]:1.2f}", textposition='bottom center', showlegend=False))

fig.show()

# Get the damped natural frequency
wd_dr = 2*np.pi / (t[ipeaks_dr[1] - ipeaks_dr[0]])

# If you didn't remove the spiral_mode
wd_dr_wrong = 2*np.pi / (t[ipeaks_total[1] - ipeaks_total[0]])

print(f"The damped natural frequency of the Dutch Roll mode is {wd_dr:1.4}rad/s, but you would have got {wd_dr_wrong:1.4f}rad/s if you didn't remove the spiral mode" )

and, again, the damping ratio:

# Remake the figure
fig = go.Figure()
fig.update_xaxes(title_text="Time/s")
fig.update_yaxes(title_text="Roll Attitude/deg")
fig.add_trace(go.Scatter(x=t, y=just_dutch_roll.real, name="Spiral Removed"))
fig.show()

# Get the exponential decay thus giving the eigenvalue
lam_dr_real = np.log(just_dutch_roll.real[ipeaks_dr[1]]/just_dutch_roll.real[ipeaks_dr[0]])/t[ipeaks_dr[1] - ipeaks_dr[0]]
lam_dr_real_wrong = np.log(Phi_total.real[ipeaks_total[1]]/Phi_total.real[ipeaks_total[0]])/t[ipeaks_total[1] - ipeaks_total[0]]

print(f"The real part of the eigenvalue of the Dutch Roll mode is {lam_dr_real:1.3f}")

# Make the eigenvalue
eig_dr = lam_dr_real + wd_dr * 1j
eig_dr_wrong = lam_dr_real_wrong + wd_dr_wrong * 1j

print(f"This makes the total eigenvalue of the Dutch Roll mode is {makecomplexpair(eig_dr)}\n\n")

print(f"If you didn't get rid of the spiral mode, you would have got {makecomplexpair(eig_dr_wrong)}")

# Put on the graph to check
exp_bracket_upper = just_dutch_roll.real[0] * np.exp(eig_dr.real * t)
fig.add_trace(go.Scatter(x=t, y=exp_bracket_upper.real, name="Exponential Decay"))
fig.show()



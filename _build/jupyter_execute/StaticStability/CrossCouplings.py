# Cross-couplings 
(cross-couplings)=

The stability derivatives discussed so far have been *direct* terms - that is, the moment produced in a given axis due to motion/displacement in that axis.

Any moment (or force) caused due to motion/displacement about another axis is proportional to a cross-coupling derivative. A couple (no pun intended) of these derivatives will be explored

## Aerodynamics Yaw/Roll Coupling

There is a strong coupling between yaw and roll in fixed-wing aircraft due to aerodynamic effects. First, the effect of **yaw motion** on **roll moment** will be explored

```{admonition} Which derivative does this affect?
:class: dropdown
Yaw motion is $R$ or $\bar{r}$, and roll moment is $L$, so the derivative of interest is $C_{\ell_R}$ or $C_{\ell_\bar{r}}$
```

The coupling arises due to the combined aircraft, but the main effects are from the wing and the vertical stabiliser

### Wing effect

A positive yaw rate is nose towards starboard. This causes an increase in dynamic pressure on the port wing, and a decrease on the starboard wing. The resulting lift difference gives a roll starboard wing down.

```{figure} ../Images/YawRollWing.png
---
height: 600px
name: WingCLR
---
How a yaw rate causes a roll rate
```
Hence $\left.C_{\ell_R}\right|_{wings}>0$. This does not yield stability in an of itself, but can contribute to an unstable *spiral mode* which will be discussed in Module 5.

You can similarly intuit that the resulting drag increase/decrease due to the yaw rate gives $\left.C_{n_R}\right|_{wings}<0$, and hence assists in yaw damping.

### VT effect

You will be able to appreciate that a yaw rate also causes a sidewash on the vertical stabiliser, approaching the VT from the port side. This causes an effective negative sideslip on the stabiliser, giving a sideforce from the VT towards starboard.

For any VT located above the aircraft centerline (and hence the CG), the resulting rolling moment will be positive. Hence $\left.C_{\ell_R}\right|_{VT}>0$.

## Aerodynamic Roll/Yaw Coupling

The effect on $dC_L^\prime$ due to a positive roll rate has been described previously. There is a proportional increase in $dC_D^\prime$, also, which gives rise to a positive yaw rate. Hence $\left.C_{n_P}\right|_{wings}>0$.

Similarly, a positive roll rate causes a sideforce on the VT that is positive towards port. This causes an aircraft moment nose starbard. Hence $\left.C_{\ell_R}\right|_{VT}>0$

## Gyroscopic Pitch/Yaw Coupling

The inclusion of *anything* rotating on an aircraft causes a coupling in pitch/roll due to the conservation of angular momentum and **gyroscopic precession**.

The sense of the coupling depends on the rotation sense of the propeller.

We describe the *angular momentum* in the rotating system as a vector, $\vec{H}$, which is defined in accordance with the right-hand rule. So, for a propeller that is rotating clockwise when viewed from the pilot's seat, this is a **positive rotation**.


```{figure} ../Images/PositiveProp.png
---
height: 600px
name: PositiveProp
---
A 'positive' propeller subject to pitch
```

If the aircraft is subject to a nose-up (positive) pitch rate, the angular momentum vector is similarly tilted upwards. For conservation of angular momentum, the total system must lose nor gain no angular momentum. 

So, the propeller actually loses some, and the propeller angular momentum along its axis is changed to $\vec{H}^\prime$, and it converts the change in momentum into the direction normal to the axis that completes the vector triangle - so the total vector amount is the same. This results in the vector pointed downwards, $\delta\vec{H}$, which amounts to angular momentum along positive $Z$, and hence causing the aircraft to tilt nose starboard.

So, for a propeller that rotates clockwise when viewed from the pilot's seat, any nose-up pitch is accompanied by a nose-starboard moment.

For a propeller rotating in the other sense (counterclockwise when viewed from the cockpit), the reverse is true - a nose-up motion results in a nose-port moment. It is left as an exercise to the reader to draw the diagram from this angular momentum situation (hint, the $\vec{H}$ arrow points out the aircraft tail).



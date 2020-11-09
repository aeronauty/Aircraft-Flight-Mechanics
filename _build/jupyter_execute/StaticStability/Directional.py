# Directional Stability

Directional stability refers to the aircraft's ability to maintain a stable attitude in yaw or heading. 

The aerodynamic angle relating to yaw movement is $\beta$.

A quick consideration of the signs convention will yield the stability criterion for $C_{n_\beta}$ - which is the **yaw stiffness** - sometimes called the **weathercock derivative**:
- A positive sideslip means the velocity approaches the aircraft from the stbd side, meaning that a positive sideslip is achieved by an aircraft motion *nose port*.
- Hence this is achieved from a *negative* perturbation in $\psi$.
- To return the aircraft back to equilubrium would require a postive moment to cause the aircraft to move nose starboard.
- Hence for stability, if $\beta$ increases, $N$ also needs to increase. Hence $C_{m_\beta}>0$ for stability.

This can be confusing when compared with $C_{m_\alpha}<0$ for stability, but a quick consideration of the aircraft axes and the direction of positive aerodynamic angles shows that this makes sense. It's actually the definition of alpha and beta that are opposite to one another - positive angle of attack is caused by a positive aircraft pitch, whereas positive sideslip is caused by negative aircraft yaw.

For all the same reasoning as was shown for $C_{m_\alpha}$, positive yaw stability is achieved if the lateral aerodynamic centre is situated aft of the centre of gravity. The lateral aerodynamic centre is the point at which the yawing moment does not vary with sideslip, and it can be readily intuited that this *must* be somewhere aft of the CG for any aircraft with a vertical stabiliser at the aft of the aircraft (that is, all of them).

Yaw damping, $C_{n_R}$, the *rate of change of yawing moment with yaw rate* will always be restorative for the same reasoning as $C_{m_Q}$.

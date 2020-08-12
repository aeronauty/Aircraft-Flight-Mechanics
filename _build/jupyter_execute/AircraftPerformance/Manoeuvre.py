*(Note: the US spelling is maneuver, but it took me years of muscle memory training to spell manoeuvre correctly, and I won't be losing it easily.)*

# Manoeuvres and Aircraft Loading

Manoeuvre will be broken down into horizontal (e.g., flat or banked turns) and vertical manoeuvres (e.g., loops, pull-ups), comprising curvilinear motion. Such manoeuvres are the result of a force *perpendicular* to the flight path, giving a normal acceleration.

All of the manoevures discussed are the result of a **variation in lift**, which can be *large*. Consider that the dynamic pressure rises with the square of the forward speed, so a five-fold speed increase results in twenty-five times the aerodynamic forces.

## Load Factor

The load that can be safely taken through an aircraft dictates the load limits on an aircraft - for this the **load factor** is introduced as a non-dimensional measure of the load variation.

```{math}
:label: LoadFactor
n=\frac{L}{W}
````

```{admonition} So - *what is the load factor for steady level flight?*
:class: dropdown
In steady level flight, the equilibrium steady flight condition is $L=W$ so $n=1$
```

## Loops

If the pilot pulls back on the stick, provided there is sufficient thrust, the angle of attack will be increased and the lift will also increase. This increases the load factor.

A 'perfect' loop is:
- Constant airspeed
- Constant radius

```{figure} ../Images/Loop.png
---
height: 300px
name: Loop
---
Constant Radius Loop
```
If the angular displacement is denoted by $\gamma$, with $\gamma=0$ being the bottom of the loop, increasing clockwise, then the equations of motion are, in the aircraft longitudinal direction
```{margin}
From motion in a circle, recall that centripetal (centre-seeking) acceleration is:

$a_c = \frac{V^2}{r}$

hence from Newton's second law, the force required to maintain a loop of radius $r$ is:

$F_c=\frac{m\,V^2}{r}$
```
$$T-D-W\sin\gamma=0$$

and

$$L + W\cos\gamma=\frac{W\,V^2}{g\,r}$$

So, at different points in the circle the equations of motion give, with $F_c = \frac{W\,V^2}{g\,r}$:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:9px 20px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:9px 20px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-zd5i{border-color:inherit;font-size:14px;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-zd5i">Horizontal Equilibrium</th>
    <th class="tg-zd5i">Vertical Equilibrium</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Point A</td>
    <td class="tg-0pky">$T-D=0$</td>
    <td class="tg-0pky">$L-W=F_c$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Point B</td>
    <td class="tg-0pky">$T-D-W=0$</td>
    <td class="tg-0pky">$L=F_c$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Point C</td>
    <td class="tg-0pky">$T-D=0$</td>
    <td class="tg-0pky">$L+W=F_c$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Point D</td>
    <td class="tg-0pky">$T-D+W=0$</td>
    <td class="tg-0pky">$L=F_c$</td>
  </tr>
</tbody>
</table>

For the perfect loop, the normal acceleration is **constant**, and the load factor varies, so at the different points of the loop above, the load factor is:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:9px 20px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:9px 20px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-zd5i{border-color:inherit;font-size:14px;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-zd5i">Load Factor</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Point A</td>
    <td class="tg-0pky">$1+\frac{V^2}{g\,r}$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Point B</td>
    <td class="tg-0pky">$\frac{V^2}{g\,r}$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Point C</td>
    <td class="tg-0pky">$\frac{V^2}{g\,r}-1$</td>
  </tr>
  <tr>
    <td class="tg-0pky">Point D</td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal">$\frac{V^2}{g\,r}$</span></td>
  </tr>
</tbody>
</table>

For reasons that can be readily appreciated, the *lift* and the *thrust* must be continually varied to maintain constant $F_C$ required for a constant radius loop. For these reasons, your average loop looks something more like this:


```{figure} ../Images/CrapLoop.png
---
height: 300px
name: Loop
---
A more realistic loop
```

```{admonition} Think: why is the average loop shaped like a balloon?
:class: dropdown

From motion in a circle, a tighter radius of turn $r$ can be effected by a greater $F_c$.

Without perfect input by the pilot, the weight vector will *add* to $F_C$ at the top of the loop, *subtract* from it at the bottom, and vary between according the equations of motion already shown.

If the pilot is unable to adjust attitude *perfectly*, it likely that the turn radius will be lowest at the bottom of the loop, and largest at the top - resulting the 'imperfect' shape shown.

```
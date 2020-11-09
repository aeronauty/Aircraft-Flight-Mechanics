# Introduction

The following definitions will be revision, but a thorough understanding of them is imperative for the remainder of this course.

## Newton's laws of motion

In this course we utilise Newtonian Mechanics - Newton's laws should be familiar, and you should be able to recite them:

1. An object remains at rest or in a state of uniform motion unless acted on by an external, unbalanced force.
2. Net force acting on rigid body is equal to its absolute momentum flux, or $\sum\vec{F}=m\cdot a_{abs}$.	
3. Every action force has a reaction force that is equal in magnitude, and opposite in direction.

Newton's second law will be used in this section to derive the full six degree of freedom (6DoF) equations of motion for unconstrained aircraft flight. Before diving into the derivation, further definitions are required:
- Most of the quantities used are easiest to define in different axes systems
- A thorough understanding of relative motion will need to be employed

### Reference Frames and Aircraft Axis Systems

All motion is relative - there is no *luminiferous aether*[^1], and there is no universal 'grid system' in which we can define position or motion. In the absence of this, we define different axes systems depending on what helps to simplify the mathematics that we need to use - it is easier to define forces in an axis system where those forces are aligned with the reference system.

Newton's laws are only valid in an *inertial reference frame* - one that is not moving. We use the *Earth* as our inertial reference frame - this is not actually the case as it is obviously moving, but for flight mechanics purposes, we rely on the fact that the rotation of the Earth is slow compared to aircraft motions.

#### A note on vector notation

To differentiate vector quantities from scalar quantities, several conventions are commonplace. If $U, V, W$ are vector components, the vector may be defined using

-   **Boldface** $\displaystyle\mathbf{U}=[U,V,W]^T$

-   **Arrow** $\vec{U}=[U,V,W]^T$

-   **Underline** $\underline{U}=[U,V,W]^T$

I tend to use $\vec{U}$ in typeset documents as it causes the least conflicts when using LaTeX. When writing on the board, I tend to use $\underline{U}$ notation as it is easier - but sometimes I'll draw an arrow if I'm feeling adventurous[^mynote]. I don't mind which you use, as long as you are consistent within a single derivation. Just be aware that things change between sources.

[^1]: Read [the 'Michelson-Morley experiment'](https://en.wikipedia.org/wiki/Michelson–Morley_experiment) if that means nothing to you

[^mynote]: I know, way to live dangerously.

#### Earth Axes

We utilise the Earth axis system, see Figure {red}`EarthAxes`, because, for our purposes, it is an inertial reference frame - so we require this in order to utilise Newton's second law. We make some simplifications, and impose the following:

-   Assume the Earth is a flat plane  [^flatearth]

-   NED (North, East Down) = $x_E, x_E, x_E$

[^flatearth]: This doesn't make you a flat earther, don't worry.


```{figure} ../Images/EarthAxes.png
---
height: 300px
name: EarthAxes
---
Earth Axes
```

#### Aircraft Body Axes

We also require a frame of reference that is fixed to the aircraft because:

1.  That is the frame of reference in which the pilot sits, so we require one to determine forces on them

2.  Moments/products inertia, and centre of gravity position are easily defined in an axis system fixed to the aircraft

This axis system is usually defined with its origin at the aircraft centre of gravity.\\

$x$ is defined positive forward, and may be defined along the propeller rotation axis for a single-engine propeller-driven aircraft, along the floor for a large transport aircraft, or along the wing root chord line.

$y$ is defined along the starboard axis along a plane equidistant vertically from both wings at each spanwise location ($Y_B$ does not not travel along a wing dihedral angle).

$z$ is defined down, normal to the plane defined by the $x$, $y$ intersection.

These have [already been introduced in the previous module](Aircraft-Body-Axes).

We can normally define thrust in aircraft body axes, and we may also define aerodynamic forces in body axes (as *normal* and *axial* force), but it is more convenient to define aerodynamic in *stability axes* as *lift* and *drag*.

#### Stability Axes

```{warning}
Note that the nomenclature of wind/stability systems is inconsistent depending on which textbook you look at. The version presented herein is the most common, and the most sensible
```
Aircraft, in general, are usually flown at some angle of attack, $\alpha$ - which means that the incident freestream velocity is not aligned with the aircraft body axes. Lift and drag are defined parallel to, and normal to the incident flow vector, so we require an axes set called **stability axes** - $[x_s, y_s, z_s]$.

We rotate the aircraft body axes through $\alpha$, around $y$ - thus $y=y_s$.

The $x/y$ planes of body and stability axes intersect along the shared $y, y_s$ axis - [\[fig:stabilityplanes\]](#fig:stabilityplanes){reference-type="ref" reference="fig:stabilityplanes"}.

The $x/z$ planes of body are co-planar, but rotated about $\alpha$ - [\[fig:stabilityplanesXZ\]](#fig:stabilityplanesXZ){reference-type="ref" reference="fig:stabilityplanesXZ"}.

It is important to note that this treatment neglects sideslip $\beta$ - so we are treating $V_\infty$ as the projection of the relative wind into the aircraft body $x_b/z_b$ plane.

Aircraft data is usually defined in the stability axes system - it is important, however, to have an appreciation of **wind axes**.

import numpy as np
import meshio
import plotly.graph_objects as go
from myst_nb import glue
with open("AircraftModels/Spitfire.obj", "rb") as file:
    obj_data = file.read().decode('utf-8')

def obj_data_to_mesh3d(odata):
    # odata is the string read from an obj file
    vertices = []
    faces = []
    lines = odata.splitlines()   
   
    for line in lines:
        slist = line.split()
        if slist:
            if slist[0] == 'v':
                vertex = np.array(slist[1:], dtype=float)
                vertices.append(vertex)
            elif slist[0] == 'f':
                face = []
                for k in range(1, len(slist)):
                    face.append([int(s) for s in slist[k].replace('//','/').split('/')])
                if len(face) > 3: # triangulate the n-polyonal face, n>3
                    faces.extend([[face[0][0]-1, face[k][0]-1, face[k+1][0]-1] for k in range(1, len(face)-1)])
                else:    
                    faces.append([face[j][0]-1 for j in range(len(face))])
            else: pass
    
    
    return np.array(vertices), np.array(faces)  

vertices, faces = obj_data_to_mesh3d(obj_data)

x, y, z = vertices[:,:3].T
I, J, K = faces.T

degangle = 11
rot = np.radians(degangle)
cos = np.cos(rot)
sin = np.sin(rot)

X = z + 40
Y = x
Z = -y + 50

for i in range(len(X)):
    X[i] = cos * X[i] - sin * Z[i]
    Z[i] = sin * X[i] + cos * Z[i]

mesh = go.Mesh3d(
            x=X,
            y=Y,
            z=Z,
            i=I,
            j=J,
            k=K,
            name='',
            showscale=False)

mesh.update(lighting=dict(ambient= 0.6,
                          diffuse= 1,
                          fresnel=  5,
                          specular= 1,
                          roughness= 1),
                         
            lightposition=dict(x=-1000,
                               y=1000,
                               z=1000));
tiprange = 200

layout = go.Layout(title='Aircraft Body Axes and Stability Axes', title_x=0.5,
                   font=dict(size=14, color='black'),
                   width=900,
                   height=900,
                   scene=dict(xaxis=dict(visible=False, title='X', range=[-tiprange*1.5, tiprange*1.5]),
                              yaxis=dict(visible=False, title='Y', range=[tiprange*1.5, -tiprange*1.5]),  
                              zaxis=dict(visible=False, title='Z', range=[tiprange*1.5, -tiprange*1.5]), 
                              aspectratio=dict(x=1,
                                               y=1,
                                               z=1
                                         ),
                              camera=dict(eye=dict(x=1., y=1., z=0.5)),
                        ), 
                  margin=dict(t=175),
                  paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)') 




fig = go.Figure(data=[mesh], layout=layout)


########################################################################################
## Add some axes - first body axes
fig.add_trace(go.Scatter3d(x=[0, tiprange], y=[0, 0], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4), legendgroup="Body Axes"))

fig.add_trace(go.Cone(x=[tiprange], y=[0], z=[0], u=[100], v=[0], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False, legendgroup="Body Axes"))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, tiprange], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4), legendgroup="Body Axes"))

fig.add_trace(go.Cone(x=[0], y=[tiprange], z=[0], u=[0], v=[100], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False, legendgroup="Body Axes"))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, tiprange],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4), legendgroup="Body Axes"))

fig.add_trace(go.Cone(x=[0], y=[0], z=[tiprange], u=[0], v=[0], w=[100], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False, legendgroup="Body Axes"))

fig.add_trace(go.Scatter3d(x=[tiprange, 0, 0], y=[0, tiprange, .2], z=[0, 0, tiprange], mode='text', text=['x', 'y', 'z'], name='Body Axes', showlegend=True, legendgroup="Body Axes"))

########################################################################################
## Add some axes - then stability axes
AoA = np.radians(15)
cos = np.cos(AoA)
sin = np.sin(AoA)
fig.add_trace(go.Scatter3d(x=[0, tiprange * cos], y=[0, 0], z=[0, tiprange * sin],
    mode='lines',
    showlegend=False, line=dict(color='darkgreen', width=4), legendgroup="Stability Axes"))

fig.add_trace(go.Cone(x=[tiprange * cos], y=[0], z=[tiprange * sin], u=[100 * cos], v=[0], w=[100 * sin], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(0,100,0)'], [1, 'rgb(0,100,0)']],\
                      showscale=False, legendgroup="Stability Axes"))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, tiprange], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='darkgreen', width=4), legendgroup="Stability Axes"))

fig.add_trace(go.Cone(x=[0], y=[tiprange], z=[0], u=[0], v=[100], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(0,100,0)'], [1, 'rgb(0,100,0)']],\
                      showscale=False, legendgroup="Stability Axes"))

fig.add_trace(go.Scatter3d(x=[0, -tiprange * sin], y=[0, 0], z=[0, tiprange*cos],
    mode='lines',
    showlegend=False, line=dict(color='darkgreen', width=4), legendgroup="Stability Axes"))

fig.add_trace(go.Cone(x=[-tiprange * sin], y=[0], z=[tiprange * cos], u=[-100*sin], v=[0], w=[100*cos], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(0,100,0)'], [1, 'rgb(0,100,0)']],\
                      showscale=False, legendgroup="Stability Axes"))

fig.add_trace(go.Scatter3d(x=[tiprange*cos, 0, -tiprange*sin], y=[0, tiprange, .3], z=[tiprange*sin, 0, tiprange*cos], mode='text', text=['x_s', 'y_s', 'z_s'], name='Stability Axes', showlegend=True, legendgroup="Stability Axes"))

########################################################################################
## Add some axes - then put the flight speed vector on
SS = np.radians(15)
cosS = np.cos(SS)
sinS = np.sin(SS)

Vf = 300

U = Vf * cos * cosS
V = Vf * sinS
W = Vf * cosS * sin

## Add on the flightspeed vector
fig.add_trace(go.Scatter3d(x=[0, U], y=[0, V], z=[0, W],
    mode='lines', name='$V_f\\text{ - Flightspeed}$',
    showlegend=True, line=dict(color='red', width=4)))

fig.add_trace(go.Cone(x=[U], y=[V], z=[W], u=[U/Vf], v=[V/Vf], w=[W/Vf], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(255,0,0)'], [1, 'rgb(255,0,0)']],\
                      showscale=False))

# Add in cosine beta
## Add on the flightspeed vector
fig.add_trace(go.Scatter3d(x=[0, U], y=[0, 0], z=[0, W],
    mode='lines', name='$V_f\cos\\beta$',
    showlegend=True, line=dict(color='red', width=4, dash='dash')))

fig.add_trace(go.Cone(x=[U], y=[0], z=[W], u=[U/Vf], v=[0/Vf], w=[W/Vf], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(255,0,0)'], [1, 'rgb(255,0,0)']],\
                      showscale=False))


## Add on sideslip angle
Ub = np.zeros(100)
Vb = np.zeros(100)
Wb = np.zeros(100)

for i, b in enumerate(np.linspace(0, SS, 100)):
    Ub[i] = .8*Vf * cos * cosS
    Vb[i] = .8*Vf * sinS
    Wb[i] = .8*Vf * cos * sinS
    
# Put SS plot in
fig.add_trace(go.Scatter3d(x=Ub, y=Vb, z=Wb,
    mode='lines', name='$\\beta$', legendgroup="Sideslip",
    showlegend=True, line=dict(color='blue', width=10, dash='solid')))    

# And label it
fig.add_trace(go.Scatter3d(x=[Ub[50]], y=[Vb[50]], z=[Wb[50]], mode='text', text=['β'],\
                           textposition='bottom center', name='<span style="color:blue">β - Sideslip</span>', showlegend=False, textfont=dict(
                color="blue",
                size=12), legendgroup="Sideslip"))


# # Draw coloured arrows to show rotation - first around X
# dist = 7
# rad = 1
# dTH = np.radians(np.linspace(45, 325, 100))
# xX = np.ones(dTH.shape) * dist
# yX = rad * np.sin(dTH)
# zX = -rad * np.cos(dTH)

# fig.add_trace(go.Scatter3d(x=xX, y=yX, z=zX,
#     mode='lines',
#     showlegend=False, line=dict(color='royalblue', width=4)))

# fig.add_trace(go.Cone(x=[xX[-1]], y=[yX[-1]], z=[zX[-1]], u=[0], v=[1], w=[-1], cmin=1, cmax=1,\
#                       colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
#                       showscale=False))

# # Then around y
# yY = np.ones(dTH.shape) * dist
# xY = -rad * np.sin(dTH)
# zY = -rad * np.cos(dTH)

# fig.add_trace(go.Scatter3d(x=xY, y=yY, z=zY,
#     mode='lines',
#     showlegend=False, line=dict(color='royalblue', width=4)))

# fig.add_trace(go.Cone(x=[xY[-1]], y=[yY[-1]], z=[zY[-1]], u=[-1], v=[0], w=[-1], cmin=1, cmax=1,\
#                       colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
#                       showscale=False))

# # Then around z
# zZ = np.ones(dTH.shape) * dist
# xZ = -rad * np.sin(dTH)
# yZ = rad * np.cos(dTH)

# fig.add_trace(go.Scatter3d(x=xZ, y=yZ, z=zZ,
#     mode='lines',
#     showlegend=False, line=dict(color='royalblue', width=4)))

# fig.add_trace(go.Cone(x=[xZ[-1]], y=[yZ[-1]], z=[zZ[-1]], u=[-1], v=[1], w=[0], cmin=1, cmax=1,\
#                       colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
#                       showscale=False))

# fig.add_trace(go.Scatter3d(x=[tiprange+1, 0, 0], y=[0, tiprange+1, 0], z=[0, 0, tiprange+1], mode='text', text=['X', 'Y', 'Z'],\
#                            textposition='middle center', name='<span style="color:red">Forces</span>', showlegend=True, textfont=dict(
#                 color="red",
#                 size=12)))

# fig.add_trace(go.Scatter3d(x=[11.5, 0, 0], y=[0, 11.5, 0], z=[0, 0, 11.5], mode='text', text=['U', 'V', 'W'],\
#                            textposition='middle center', name='<span style="color:darkviolet">Translational Velocity</span>', showlegend=True, textfont=dict(
#                 color="darkviolet",
#                 size=12)))

# fig.add_trace(go.Scatter3d(x=[dist, xY[50], xZ[50]], y=[yX[50], dist, yZ[50]], z=[zX[50], zY[50], dist*.95], mode='text', text=['L', 'M', 'N'],\
#                            textposition='bottom center', name='<span style="color:green">Moments</span>', showlegend=True, textfont=dict(
#                 color="green",
#                 size=12)))

# fig.add_trace(go.Scatter3d(x=[dist, xY[75], xZ[75]], y=[yX[75], dist, yZ[75]], z=[zX[75], zY[75], dist*.95], mode='text', text=['P', 'Q', 'R'],\
#                            textposition='bottom center', name='<span style="color:blue">Angular Velocity</span>', showlegend=True, textfont=dict(
#                 color="blue",
#                 size=12)))


# fig.add_trace(go.Scatter3d(x=[dist, xY[25], xZ[25]], y=[yX[25], dist, yZ[25]], z=[zX[25], zY[25], dist*.95], mode='text', text=['ϕ', 'θ', 'Ψ'],\
#                            textposition='bottom center', name='<span style="color:darkslategray">Angular Displacement</span>', showlegend=True, textfont=dict(
#                 color="darkslategray",
#                 size=12)))

# fig.add_trace(go.Scatter3d(x=[dist, xY[0], xZ[0]], y=[yX[0], dist, yZ[0]], z=[zX[0], zY[0], dist*.95], mode='text', text=['Roll', 'Pitch', 'Yaw'],\
#                            textposition='bottom left', name='<span style="color:maroon">Angular Motions</span>', showlegend=True, textfont=dict(
#                 color="maroon",
#                 size=12)))

fig.layout.scene.camera.projection.type = "orthographic"


fig.show()

# glue("AircraftBodyAxes3d", fig, display=False)



#### Wind Axes

Stability axes are defined from the *projection of freestream into the $X_b/Z_b$ plane*. That is, disregarding sideslip.

*Wind axes* take account of this, and are aligned with $x_w$ defined along the actual freestream.

In general, however, aircraft coefficients will be defined in stability axes - but you should have an appreciation of this axis set.

## Defining quantities in different axes sets

The axes systems that used in this course have been described - as mentioned earlier, it is easier to define certain quantities in one axis system over another:

### Gravitational Force - Weight

The aircraft weight vector is, by definition, aligned with the Earth Z ($z_e$) axis as it is oriented towards the centre of the Earth. That is:

$$\vec{F}_G = \begin{bmatrix}0\\0\\W\end{bmatrix}_{e}    =\begin{bmatrix}0\\0\\ mg\end{bmatrix}_{e}\label{eq:FW}$$(gforce_earth)

### Displacements

For positioning purposes, the aircraft location must be defined in earth axes.

$$\vec{R}_{ac} = \begin{bmatrix}x_{ac}\\y_{ac}\\z_{ac}\end{bmatrix}_{e}$$

### Propulsive Forces

Aircraft thrust is generally aligned along the aircraft $x$-axis $x$, and is thus best defined in body axes:

$$\begin{aligned}
    \vec{F}_P&=\begin{bmatrix} T_x \\ T_y \\ T_z \end{bmatrix}_b = \begin{bmatrix} T\cdot\sin\theta_T \\ F_{P_y} \\ T\cdot\cos\theta_T \end{bmatrix}_b 
   \end{aligned}$$
   
For this course we will disregard effects such as thrust axis misalignment or thrust vectoring, so this simplifies to

$$\vec{F}_P=\begin{bmatrix} T \\ 0 \\ 0 \end{bmatrix}_b$$

### Aerodynamic Force

The aerodynamic forces of lift, $L$, and drag, $D$, are, by definition, defined normal to and parallel to the incident flow vector, $V_\infty^\prime=V_\infty\cos\beta$. It is most useful to use these force in stability axes:

$$\vec{F}_A=\begin{bmatrix} -D \\ F_{A_y} \\ -L \end{bmatrix}_s\label{eq:FA}$$

Where the term $F_{A_y}$ is the side component of aerodynamic force due to sideslip.

### Translations and Rotations

Aircraft velocity and accelerations are defined in body axes:

$$\begin{aligned}
    \vec{V} &= \begin{bmatrix}U\\V\\W\end{bmatrix}_b   \\
    \vec{a} = \dot{\vec{V}} &= \begin{bmatrix}\dot{U}\\\dot{V}\\\dot{W}\end{bmatrix}_b    \neq \vec{a}_{abs}\label{eq:linearacc}\end{aligned}$$

One must be careful with the equation above; in the case of zero angular motion, you may differentiate the *absolute* velocities $[U,V,W]$ to obtain the *absolute* acceleration $[a_x,a_y,a_z]_{abs}$, **but for the case of non-zero angular velocity, these are not equivalent**, $a_x\neq\dot{U}$. This will all make a lot more sense (hopefully) when you're introduced to Coriolis theorem later, but the fact that we cannot get absolute accelerations so simply deserves a mention at this juncture.

Angular velocities of the aircraft, with respect to the inertial reference frame, are defined in body axes as roll, pitch, and yaw rates:

$$\vec{\omega} = \begin{bmatrix}P\\Q\\R\end{bmatrix}_b$$

Note that if you see $P$, $Q$, or $R$ in practice, they are defined as *body angular rates*, and are as measured in body axes.

### Aircraft total forces and moments

We define the total external forces and moments on the aircraft in body axes

$$\begin{aligned}
    \vec{F}_b&=\begin{bmatrix}X\\Y\\Z\end{bmatrix}\\
    \vec{M}_b&=\begin{bmatrix}L\\M\\N\end{bmatrix}\end{aligned}$$


## The requirement for axis conversion

Since it is desired to utilise Newtonian mechanics to define the motion of the aircraft, it is hence needed to be able to equate forces to the product of mass and accelerations (Newton's second law). 

So far, forces, displacements, and velocities are defined in all three axis systems - earth, body, and stability.

Relating stability and body axes is relatively simple since they are only rotated through a single angle, $\alpha$. Body and earth, by contrast, are oriented at an arbitrary angular displacement to each other. 

The **aircraft attitude** defines the relationship between earth and body axes, and this hence allows conversion of quantities between the two different axes systems.

To define the aircraft attitude, there are different ways that can be chosen from mathematics:

-   Sequence of Rotations

-   Quaternion methods

-   Direction cosine matrix

In this course, we will use the sequence of rotations - **yaw, pitch, roll**. **These need to be defined in that order**.[^2]

[^2]: Well, you can define them in whatever order you want, but the resulting transformation matrix will be different, and hence incorrect - and the standard for aerospace is 1. yaw, 2. pitch, 3. roll.


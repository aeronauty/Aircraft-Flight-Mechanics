#  Defining Static Stability

import numpy as np
import meshio
import plotly.graph_objects as go
from myst_nb import glue

In the preceding module, the equilibrium steady flight condition was utilised

$$\Sigma\vec{F}=0$$

inherent in the analysis but not explicitly stated is the further consideration that in order to stay at a constant *attitude* (angular) orientation, the sum of the moments must also be zero

$$\Sigma\vec{M}=0$$

the equilibrium state is known as a *trim* condition. In the preceding chapter a short little about *speed* stability due to $\frac{\text{d}D}{\text{d}V}$ was explored, but stability itself has not been defined not explored.

```{admonition} Nomenclature
:class: dropdown
Be careful - **trim** is sort-of loosely defined in aeronautics. For our purposes, 'trim condition' will mean one where the moments are zero. For a pilot, it *is* that but they actually mean where the *stick force* is zero due to careful adjustment of the trim tabs of the aircraft.
```

## What is stability?

For an aircraft, stability denotes the response of the aircraft if disturbed from an equilibrium or trim state.

### Static Stability 

Primarily in this chapter, we will be concerned with the *static stability* of the aircraft which is defined as *the tendency of an aircraft, following an external disturbance (e.g., a gust) to return to the undisturbed condition*. There are three categories of static stability that we can describe qualitatively; *statically stable*, *statically neutral*, and *statically unstable*.

This is best described with a graphic:

```{figure} ../Images/StaticStability.png
---
height: 200px
name: StaticStability
---
Stable, Neutral, and Unstable
```

In Figure {numref}`StaticStability` a ball is placed on three surfaces in an equilibrium state. On the leftmost case, if disturbed (pushed left or right), the ball would return to its initial equilibrium condition. This is *statically stable*. In the centre case, after a disturbance the ball would find a new equilibrium condition - this is *statically neutral*. On the rightmost case, the ball would accelerate away from the initial condition - this is *statically unstable*.

For the simple ball case, with no forcing or excitation, it can be appreciated that the actual end position of the ball is dictated by its static stability. That is, there are no dynamic phenomena that cause the behaviour to change with time. By contrast, this is not the same for an aircraft - that is, an aircraft may have static stability, but have longer-term trend to move away from equilibrium. This is *dynamic stability*.


### Dynamic stability

*Dynamic Stability* describes whether or not the aircraft will *actually* return to its trim state following a disturbance. An aircraft may be statically stable, but dynamically unstable. Static instability, however, is always accompanied by dynamic instability. See Figure {numref}`DifferentStabilities` for examples of the combinations of static/dynamic stability as a response to a disturbance at $t=0$. In Figure {numref}`DifferentStabilities`, $f(t)$ is any function describing an aircraft *state*; these are the aircraft velocities and angular orientations.

```{figure} ../Images/DifferentStabilities.png
---
height: 400px
name: DifferentStabilities
---
Different Stabilities
```

## Stability Requirements

It can be appreciated that in certain situations, good stability is highly desirable - it will be shown that for *any* aircraft certified under FAR 23, pitch stability is a necessary requirement to be able to produce an aircraft.

However, *too much* stability can make an aircraft *sluggish*. Stability is a measure not simply of how well an aircraft responds to disturbances - it also denotes how difficult the aircraft will be to manoeuvre. For this reason, the same stability characteristics are not found in airliners and fighter aircraft.

To explore the dynamic stability of an aircraft requires the full equation of motion, which are nine coupled nonlinear equations. Modules 3, 4, and 5 of this course will be spend deriving, linearising, and then utilising these equations.

Before them, however, we can gain a good intuitive sense of static stability by using some reduced models. With these reduced models, some great predictions can be made about the following:
- What size does my tail need to be?
- What tail incidence gives zero elevator deflection at cruise $C_L$ (and thus the lowest drag in cruise)?
- How far forward can I place cargo in an aircraft?

# Aircraft Body Axes

In module 3, four distinct axes sets will be utilised; body, wind, stability, and earth axes. For this module, aircraft body axes is the only one required. Hopefully aircraft body axes have been covered in previous courses but a bit of revision never hurts.

Aircraft body axes is a right-handed Cartesian axis set, centred at the aircraft centre of gravity. $x$ is defined positive along the aircraft longitudinal axis, positive forward. $y$ is positive over the starboard wing. $z$ is positive down, in accordance with the right hand rule.

Along each of the $x, y, z$ axes the forces, moments, and velocities can be summarised:

| Direction | Force | Linear Velocity | Description | Moment | Angular Displacement | Angular Velocity | Description |
|:---------:|:-----:|:---------------:|:-----------:|:------:|:--------------------:|:----------------:|:-----------:|
|    $x$    |  $X$  |       $U$       |   Fore/aft  |   $L$  |        $\phi$        |        $P$       |     Roll    |
|    $y$    |  $Y$  |       $V$       |   Sideward  |   $M$  |       $\theta$       |        $Q$       |    Pitch    |
|    $z$    |  $Z$  |       $W$       |    Heave    |   $N$  |        $\psi$        |        $R$       |     Yaw     |

The direction of positive rotations is defined in accordance with the right-hand screw rule - see the interactive figure below, which enables you to rotate an aircraft model, and click on the legend to show/hide different components.



with open("AircraftModels/hawk_t1.obj", "rb") as file:
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

mesh = go.Mesh3d(
            x=z+1.5,
            y=x,
            z=-y+1.64,
            i=I,
            j=J,
            k=K,
            name='',
            showscale=False)

mesh.update(lighting=dict(ambient= 0.5,
                          diffuse= 1,
                          fresnel=  5,
                          specular= 1,
                          roughness= 1),
                         
            lightposition=dict(x=-1000,
                               y=1000,
                               z=1000));
tiprange = 8

layout = go.Layout(title='Aircraft Body Axes', title_x=0.5,
                   font=dict(size=14, color='black'),
                   width=900,
                   height=900,
                   scene=dict(xaxis=dict(visible=False, title='X', range=[-tiprange*1.2, tiprange*1.2]),
                              yaxis=dict(visible=False, title='Y', range=[tiprange*1.2, -tiprange*1.2]),  
                              zaxis=dict(visible=False, title='Z', range=[tiprange*1.2, -tiprange*1.2]), 
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



## Add some axes
fig.add_trace(go.Scatter3d(x=[0, tiprange], y=[0, 0], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[tiprange], y=[0], z=[0], u=[1], v=[0], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, tiprange], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[0], y=[tiprange], z=[0], u=[0], v=[1], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, tiprange],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[0], y=[0], z=[tiprange], u=[0], v=[0], w=[1], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[tiprange, 0, 0], y=[0, tiprange, .2], z=[0, 0, tiprange], mode='text', text=['x', 'y', 'z'], name='Directions', showlegend=True))

# Draw coloured arrows to show rotation - first around X
dist = 7
rad = 1
dTH = np.radians(np.linspace(45, 325, 100))
xX = np.ones(dTH.shape) * dist
yX = rad * np.sin(dTH)
zX = -rad * np.cos(dTH)

fig.add_trace(go.Scatter3d(x=xX, y=yX, z=zX,
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[xX[-1]], y=[yX[-1]], z=[zX[-1]], u=[0], v=[1], w=[-1], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

# Then around y
yY = np.ones(dTH.shape) * dist
xY = -rad * np.sin(dTH)
zY = -rad * np.cos(dTH)

fig.add_trace(go.Scatter3d(x=xY, y=yY, z=zY,
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[xY[-1]], y=[yY[-1]], z=[zY[-1]], u=[-1], v=[0], w=[-1], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

# Then around z
zZ = np.ones(dTH.shape) * dist
xZ = -rad * np.sin(dTH)
yZ = rad * np.cos(dTH)

fig.add_trace(go.Scatter3d(x=xZ, y=yZ, z=zZ,
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[xZ[-1]], y=[yZ[-1]], z=[zZ[-1]], u=[-1], v=[1], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[tiprange+1, 0, 0], y=[0, tiprange+1, 0], z=[0, 0, tiprange+1], mode='text', text=['X', 'Y', 'Z'],\
                           textposition='middle center', name='<span style="color:red">Forces</span>', showlegend=True, textfont=dict(
                color="red",
                size=12)))

fig.add_trace(go.Scatter3d(x=[11.5, 0, 0], y=[0, 11.5, 0], z=[0, 0, 11.5], mode='text', text=['U', 'V', 'W'],\
                           textposition='middle center', name='<span style="color:darkviolet">Translational Velocity</span>', showlegend=True, textfont=dict(
                color="darkviolet",
                size=12)))

fig.add_trace(go.Scatter3d(x=[dist, xY[50], xZ[50]], y=[yX[50], dist, yZ[50]], z=[zX[50], zY[50], dist*.95], mode='text', text=['L', 'M', 'N'],\
                           textposition='bottom center', name='<span style="color:green">Moments</span>', showlegend=True, textfont=dict(
                color="green",
                size=12)))

fig.add_trace(go.Scatter3d(x=[dist, xY[75], xZ[75]], y=[yX[75], dist, yZ[75]], z=[zX[75], zY[75], dist*.95], mode='text', text=['P', 'Q', 'R'],\
                           textposition='bottom center', name='<span style="color:blue">Angular Velocity</span>', showlegend=True, textfont=dict(
                color="blue",
                size=12)))


fig.add_trace(go.Scatter3d(x=[dist, xY[25], xZ[25]], y=[yX[25], dist, yZ[25]], z=[zX[25], zY[25], dist*.95], mode='text', text=['ϕ', 'θ', 'Ψ'],\
                           textposition='bottom center', name='<span style="color:darkslategray">Angular Displacement</span>', showlegend=True, textfont=dict(
                color="darkslategray",
                size=12)))

fig.add_trace(go.Scatter3d(x=[dist, xY[0], xZ[0]], y=[yX[0], dist, yZ[0]], z=[zX[0], zY[0], dist*.95], mode='text', text=['Roll', 'Pitch', 'Yaw'],\
                           textposition='bottom left', name='<span style="color:maroon">Angular Motions</span>', showlegend=True, textfont=dict(
                color="maroon",
                size=12)))

fig.layout.scene.camera.projection.type = "orthographic"


# fig.show()

glue("AircraftBodyAxes3d", fig, display=False)



# Aerodynamic Angles


The aerodynamic angles, angle of attack - $\alpha$, and sideslip - $\beta$, will be familiar to you. You might not be so comfortable however, with their actual definitions.

with open("AircraftModels/harrier.obj", "rb") as file:
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

# Normalise the aircraft
# x = z, y = x, z = -y
degangle = 5
rot = np.radians(degangle)
cos = np.cos(rot)
sin = np.sin(rot)
Tmatrix = np.array([[cos, 0, -sin],[0, 1, 0],[sin, 0, cos]])

X = z + 1.5
Y = x
Z= -y + 1.5

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

mesh.update(lighting=dict(ambient= 0.5,
                          diffuse= 1,
                          fresnel=  5,
                          specular= 1,
                          roughness= 1),
                         
            lightposition=dict(x=-1000,
                               y=1000,
                               z=1000));
tiprange = 12

layout = go.Layout(title='Aerodynamic Angles', title_x=0.5,
                   font=dict(size=14, color='black'),
                   width=900,
                   height=900,
                   scene=dict(xaxis=dict(visible=False, title='X', range=[-tiprange*1.2, tiprange*1.2]),
                              yaxis=dict(visible=False, title='Y', range=[tiprange*1.2, -tiprange*1.2]),  
                              zaxis=dict(visible=False, title='Z', range=[tiprange*1.2, -tiprange*1.2]), 
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



## Add some axes
fig.add_trace(go.Scatter3d(x=[0, tiprange], y=[0, 0], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[tiprange], y=[0], z=[0], u=[1], v=[0], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, tiprange], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[0], y=[tiprange], z=[0], u=[0], v=[1], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, tiprange],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[0], y=[0], z=[tiprange], u=[0], v=[0], w=[1], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[tiprange, 0, 0], y=[0, tiprange, .2], z=[0, 0, tiprange], mode='text', text=['x', 'y', 'z'], name='Directions', showlegend=False))


## Add in teh flightspeed
Vf = tiprange*.8
alfa = np.radians(20)
beta = np.radians(30)
U = Vf * np.cos(alfa) * np.cos(beta)
V = Vf * np.sin(beta)
W = Vf * np.cos(beta) * np.sin(alfa)

## Add on the flightspeed vector
fig.add_trace(go.Scatter3d(x=[0, U], y=[0, V], z=[0, W],
    mode='lines', name='$V_f\\text{ - Flightspeed}$',
    showlegend=True, line=dict(color='red', width=4)))

fig.add_trace(go.Cone(x=[U], y=[V], z=[W], u=[U/Vf], v=[V/Vf], w=[W/Vf], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(255,0,0)'], [1, 'rgb(255,0,0)']],\
                      showscale=False))

# Now do the same for the velocity components - first U
fig.add_trace(go.Scatter3d(x=[0, U], y=[0, 0], z=[0, 0],
    mode='lines', name='$U$', legendgroup="Velocity Components",
    showlegend=True, line=dict(color='red', width=10, dash='solid')))

fig.add_trace(go.Cone(x=[U], y=[0], z=[0], u=[U/Vf], v=[0/Vf], w=[0/Vf], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(255,0,0)'], [1, 'rgb(255,0,0)']],\
                      showscale=False, legendgroup="Velocity Components"))

# Now do the same for the velocity components - aecond V
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, V], z=[0, 0],
    mode='lines', name='$V$', legendgroup="Velocity Components",
    showlegend=True, line=dict(color='rgb(0,255,0)', width=10, dash='solid')))

fig.add_trace(go.Cone(x=[0], y=[V], z=[0], u=[0/Vf], v=[V/Vf], w=[0/Vf], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(0,255,0)'], [1, 'rgb(0,255,0)']],\
                      showscale=False, legendgroup="Velocity Components"))

# Now do the same for the velocity components - last W
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, W],
    mode='lines', name='$W$', legendgroup="Velocity Components",
    showlegend=True, line=dict(color='rgb(0,0,255)', width=10, dash='solid')))

fig.add_trace(go.Cone(x=[0], y=[0], z=[W], u=[0/Vf], v=[0/Vf], w=[W/Vf], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(0,0,255)'], [1, 'rgb(0,0,255)']],\
                      showscale=False, legendgroup="Velocity Components"))

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
for i, b in enumerate(np.linspace(0, beta, 100)):
    Ub[i] = .8*Vf * np.cos(alfa) * np.cos(b)
    Vb[i] = .8*Vf * np.sin(b)
    Wb[i] = .8*Vf * np.cos(b) * np.sin(alfa)
    
# Put SS plot in
fig.add_trace(go.Scatter3d(x=Ub, y=Vb, z=Wb,
    mode='lines', name='$\\beta$', legendgroup="Sideslip",
    showlegend=True, line=dict(color='blue', width=10, dash='solid')))    

# And label it
fig.add_trace(go.Scatter3d(x=[Ub[50]], y=[Vb[50]], z=[Wb[50]], mode='text', text=['β'],\
                           textposition='bottom center', name='<span style="color:blue">β - Sideslip</span>', showlegend=False, textfont=dict(
                color="blue",
                size=12), legendgroup="Sideslip"))

## Add on AoA
Ua = np.zeros(100)
Va = np.zeros(100)
Wa = np.zeros(100)
for i, a in enumerate(np.linspace(0, alfa, 100)):
    Ua[i] = .9*Vf * np.cos(a) * np.cos(beta)
    Va[i] = 0
    Wa[i] = .9*Vf * np.cos(beta) * np.sin(a)
    
# Put AoA plot in
fig.add_trace(go.Scatter3d(x=Ua, y=Va, z=Wa,
    mode='lines', name='$\\alpha$', legendgroup="AoA",
    showlegend=True, line=dict(color='rgb(0,0,0)', width=10, dash='solid')))   

fig.add_trace(go.Scatter3d(x=[Ua[50]], y=[Va[50]], z=[Wa[50]], mode='text', text=['α'],\
                           textposition='middle right', name='<span style="color:blue">AoA</span>', showlegend=False, textfont=dict(
                color="blue",
                size=12), legendgroup="AoA"))


fig.layout.scene.camera.projection.type = "orthographic"

fig.show()


The aircraft flightspeed is a vector, $\vec{V}_f$, when defined in body axes is:

$$\vec{V}_f=\begin{bmatrix}U\\V\\W\end{bmatrix}=\begin{bmatrix}\left|V_f\right|\cdot\cos\alpha\cos\beta\\\left|V_f\right|\cdot\sin\beta\\\left|V_f\right|\cdot\sin\alpha\cos\beta\end{bmatrix}$$

From the diagram above, you can see the sign convention can be remembered by $V_f$ being drawn between the $x-y$ axes, and the projection onto the aircraft $x-z$ plane, $V_f\cos\beta$, as drawn between the $x-z$ axes.

This can be recalled as **positive angle of attack is nose up** and **positive sideslip is nose port**, as in the aircraft movement with respect to the flightspeed vector.

```{warning} Be careful with the definition of $V_f$ - 
$V_f$ is the aircraft velocity vector, and hence defined as moving *away* from the aircraft. It is not the vector defining the inclement wind - which is actually colinear to $V_f$ but opposite in sign.
```

```{admonition} Why I don't use 'plane' for 'aircraft'
:class: dropdown
'plane' is acceptable parlance for aircraft in North America, but it really should not be part of a good aeronautical engineer's speech. It can be confusing because *plane* has a strict definition in geometry, and we use that meaning **all the time**.

Furthermore, and this might just be my British sensibilities - it's informal and lazy to use in speech when talking in aeronautical engineer terms, but much worse to use in technical written English. Would you trust a cardiac surgeon who referred to your heart as your ticker? Or an automotive engineer referring to a car, in professional speed, as 'wheels'? Try and use aeroplane/airplane/aircraft.
```


Through the remainder of the course, means will be developed to analyse the full stability characteristics of aircraft, including the dynamic behaviour. For this, we will separate the aircraft into *longitudinal* motion (pitching), and combined *lateral/directional* (rolling/yawing).

For the purposes of static stability, aircraft motion can be isolated to looking at moments about each of the three axes independently.

# Longitudinal Stability

Longitudinal stability is *more interesting* and *more complicated* than than both lateral and directional stability, so it will be analysed first and the same techniques used to explore the other two axes.

For longitudinal stability, the static response is concerned with the aircraft pitching motion - so the parameter of interest is the pitching moment. A model needs to be formulated than can account for the combined effect of the wing, horizontal stabiliser, the elevator, and the aircraft weight therereupon. The pitching moment coefficient is defined

$$C_M\triangleq\frac{M}{\tfrac{1}{2}\rho V^2 S\bar{c}}$$

Before building a model, consider what stability would look like for aircraft pitching motion. The desired behaviour for stability would be that if the aircraft were perturbed in pitch, it would return to the equilibrium position. That is, pitch stability means that a nose-up perturbation is accompanied by a nose-down pitching moment.

## Stability Derivatives

The assumption is made that the aircraft pitching moment can be represented as the product of terms comprising the product of **stability derivatives** and variables, and constants.

The **stability derivatives** are written in non-dimensional form as:

$$C_{A_B}=\frac{\partial C_A}{B}$$

The pitching moment coefficient is assumed to be of the form:

$$C_M = C_{M_0} + C_{M_\alpha}\cdot\alpha + C_{M_Q}\cdot{Q}$$

where $C_{M_0}$ is a *constant* term and hence does not affect stability in any way.

### Condition for $C_{M_\alpha}$

Since $\alpha$ is defined as a nose-up motion, and $M$ is defined positive nose-up, it follows that **for stability, $C_{M_\alpha}$ must be negative**

$$\begin{align}
    C_{M_\alpha} &< 0 \rightarrow\text{stable}\\
    C_{M_\alpha} &>0 \rightarrow\text{unstable}\\
\end{align}$$

What aircraft design parameters lead to $C_{M_\alpha}$ being negative? A full model will be formulated that will lead to design parameters, but some simple observations can be made from first principles. Consider the respective longitudinal locations of the aircraft centre of gravity (CG), and the aircaft centre of pressure (CP).

```{margin} Aircraft Centre of Pressure
You will be familiar with centre of pressure from 2D aerofoil theory - the point at which the lift can be assumed to act as a resultant force. (Though a lot of undergrads confuse centre of pressure and aerodynamic centre).

The whole aircraft has two main lifting surfaces - the wing and the horizontal stabiliser. In this model, the CP is taken to be the position at which the resultant force of the two lifting surfaces acts. In a more complicated model, the lifting effect of the fuselage and other surfaces could also be considered.
```

There are two possibilties; the CP can be ahead of the CG, or the CP can be behind the CG.

#### CP Ahead of CG

```{figure} ../Images/CPCG1.png
---
height: 300px
name: CPCG1
---
CP ahead of CG
```

Consider the case with the CP ahead of the CG. The lift is directly proportional to the angle of attack, and the nose-up moment is directly proportional to the lift. In the following, $M_0$ represents the lift independent pitching moment *and* the pitching moment at $\alpha=0$ for the sake of mathematical simplicity.

$$M(\alpha) = M_0 + a\cdot\alpha\cdot l$$
$$\frac{\text{d}M}{\text{d}\alpha}= a\cdot l > 0$$

So with the CP ahead of the CG, the aircraft is statically unstable in pitch.

#### CP Aft of CG

```{figure} ../Images/CPCG2.png
---
height: 300px
name: CPCG2
---
CP aft of CG
```

Consider the case with the CP aft of the CG. 

$$M(\alpha) = M_0 - a\cdot\alpha\cdot l$$
$$\frac{\text{d}M}{\text{d}\alpha}= -a\cdot l < 0$$

So with the CP aft of the CG, the aircraft is statically stable in pitch.

This shows why most aircraft *except* fighter aircraft have aft horizontal tails - the horizontal tail *pulls* the centre of pressure aft, and allows the CG to be moved further aft.

A model will be formulated to show the numerical relationship between the tail and the centre of pressure, but the result above has been shown from first principles, and is instructive and intuitive. If you're still not wholly satisfied in this result - try throwing a dart/nerf vortex/arrow "tail first". It will immediately flip over. 

So the stability condition for $C_{M_\alpha}$ has been established, and a model will be developed to relate design parameters to the numerical value thereof. Before this, though, the stability of $C_{M_Q}$ will be explored.

### Condition for $C_{M_Q}$

Using similar reasoning, both conditions for CP/CG location can be overlaid in a single diagram:

```{figure} ../Images/CMQ.png
---
height: 500px
name: CMQ
---
CP and CG with a pitch rate
```


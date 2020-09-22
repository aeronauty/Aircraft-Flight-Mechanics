#  Defining Static Stability

import numpy as np
import meshio
import plotly.graph_objects as go

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
layout = go.Layout(title='$\\text{Aircraft Body Axes}$', title_x=0.5,
                   font=dict(size=14, color='black'),
                   width=900,
                   height=900,
                   scene=dict(xaxis=dict(visible=False, title='X', range=[-12, 12]),
                              yaxis=dict(visible=False, title='Y', range=[12, -12]),  
                              zaxis=dict(visible=False, title='Z', range=[12, -12]), 
                              aspectratio=dict(x=1,
                                               y=1,
                                               z=1
                                         ),
                              camera=dict(eye=dict(x=1., y=1., z=0.5)),
                        ), 
                  paper_bgcolor='rgb(235,235,235)',
                  margin=dict(t=175)) 




fig = go.Figure(data=[mesh], layout=layout)



## Add some axes
fig.add_trace(go.Scatter3d(x=[0, 10], y=[0, 0], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[10], y=[0], z=[0], u=[1], v=[0], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 10], z=[0, 0],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[0], y=[10], z=[0], u=[0], v=[1], w=[0], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, 10],
    mode='lines',
    showlegend=False, line=dict(color='royalblue', width=4)))

fig.add_trace(go.Cone(x=[0], y=[0], z=[10], u=[0], v=[0], w=[1], cmin=1, cmax=1,\
                      colorscale=[[0, 'rgb(65,105,225)'], [1, 'rgb(65,105,225)']],\
                      showscale=False))

fig.add_trace(go.Scatter3d(x=[10, 0, 0], y=[0, 10, .2], z=[0, 0, 10], mode='text', text=['x', 'y', 'z'], name='Directions', showlegend=True))

# Draw coloured arrows to show rotation - first around X
dist = 9
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

fig.add_trace(go.Scatter3d(x=[11, 0, 0], y=[0, 11, 0], z=[0, 0, 11], mode='text', text=['X', 'Y', 'Z'],\
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



fig.show()

# from plotly.offline import iplot
# from IPython.core.display import display, HTML


# iplot(fig, filename = 'figure_1.html')
# display(HTML('figure_1.html'))
# # plot_url = py.plot(fig, filename='latex', include_mathjax='cdn')

A cell below


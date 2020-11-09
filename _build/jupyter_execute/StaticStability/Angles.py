# Co-ordinate system and Angles

In module 3, four distinct axes sets will be utilised; body, wind, stability, and earth axes. For this module, aircraft body axes is the only one required. Hopefully aircraft body axes have been covered in previous courses but a bit of revision never hurts.
(Aircraft-Body-Axes)=
## Aircraft Body Axes

Aircraft body axes is a right-handed Cartesian axis set, centred at the aircraft centre of gravity. $x$ is defined positive along the aircraft longitudinal axis, positive forward. $y$ is positive over the starboard wing. $z$ is positive down, in accordance with the right hand rule.

Along each of the $x, y, z$ axes the forces, moments, and velocities can be summarised:

| Direction | Force | Linear Velocity | Description | Moment | Moment Coefficient | Angular Displacement | Angular Velocity | Nondimensional angular rate | Description |
|-----------|-------|-----------------|-------------|--------|--------------------|----------------------|------------------|-----------------------------|-------------|
| $x$       | $X$   | $U$             | Fore/aft    | $L$    | $C_\ell$           | $\phi$               | $P$              | $\bar{p}$                   | Roll        |
| $y$       | $Y$   | $V$             | Sideward    | $M$    | $C_m$              | $\theta$             | $Q$              | $\bar{q}$                   | Pitch       |
| $z$       | $Z$   | $W$             | Heave       | $N$    | $C_n$              | $\psi$               | $R$              | $\bar{r}$                   | Yaw         |

The direction of positive rotations is defined in accordance with the right-hand screw rule - see the interactive figure below, which enables you to rotate an aircraft model, and click on the legend to show/hide different components.

```{admonition} A note on lift vs rolling moment
:class: dropdown
You'll hear me lament about this occasionally, but it was a *terrible* choice to decide to start the moments alphabetically at "L", because $L$ is ambiguous - it's sometimes dimensional lift, and it's sometimes the rolling moment.

It's almost always clear from context which is required, but I know this is often confusing to students who can just think "I see an L, it must be lift". The lesson is to *think* about the terms in front of you and what they're being used for.

The nomenclature for the coefficients is inconsistent from text to text, also. Most texts use a lowercase $l$ in the rolling moment coefficient, but not all. Some texts use an 'extra curly' l, which is what I've used in this section. This is achieved in LaTeX via \ell.

So: $C_\ell$ - RM coefficient, $C_L$ - Lift coefficient, $C_l$ - 2D lift coefficient

But just be careful when comparing texts. I've seen $C_{LM}$ for 'rolling moment', and a fair few texts keep the pitching and yawing moment coefficients as uppercase subscripts (though many use the nomenclature I've gone with). For consistency, I've made all the moment coefficients lowercase, and the rolling moment is the 'extra curly L'.

Just be careful, and make sure you're certain about which part you need.
```



import numpy as np
import meshio
import plotly.graph_objects as go
from myst_nb import glue
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



(aerodynamic-angles)=
## Aerodynamic Angles


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



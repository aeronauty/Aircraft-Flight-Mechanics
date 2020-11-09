## Concise Form of Dimensional EoMs

$$\newcommand{\pd}[2]{\frac{\partial#1}{\partial#2}}$$
$$\newcommand{\ppd}[2]{\frac{\partial^2#1}{\partial#2^2}}$$
$$\newcommand{\pppd}[2]{\frac{\partial^3#1}{\partial#2^3}}$$

As demonstrated above, the dimensional EoMs are either symmetric (a.k.a. longitudinal), where $u,w,q$ are controlled by $\theta$ and $\delta_e$, or asymmetric (a.k.a. lateral/directional) where $v,p,r$ are controlled by $\delta_a$ and $\delta_r$. This is a consequence of our assumptions made to remove stability derivatives.

That is, this was _enforced_ by the [assumption of zero cross-coupling](assmption:cross-coupling) rather than being a natural consequence of the physics.

Since these assumptions have been made, the two sets of equations may be treated in isolation from each other and presented in a matrix form. First, look at the symmetric equations:

$$\color{red}{m\dot{u}= \left.\pd{X}{u}\right|_0u + \left.\pd{X}{w}\right|_0w - mg\cdot\cos\theta_0\cdot\theta^\prime}$$(eq:fwdspeedeqn)


$$\color{red}{m\dot{w}= \left.\pd{Z}{u}\right|_0u + \left.\pd{Z}{w}\right|_0w + mU_0q - mg\cdot\sin\Theta_0\cdot\theta^\prime + \left.\pd{Z}{\delta_e}\right|_0\delta_e}$$(eq:heaveequation)



$$\color{red}{I_{yy}\dot{q} = \left.\pd{M}{u}\right|_0u+\left.\pd{M}{w}\right|_0w+\left.\pd{M}{\dot{w}}\right|_0\dot{w}+\left.\pd{M}{q}\right|_0q+\left.\pd{M}{\delta_e}\right|_0\delta_e}$$(eq:pitchmomentequation)




### Longitudinal EoMs

1.  The X-Force equation (*forward speed equation*):

    Taking Equation {eq}`eq:fwdspeedeqn` and dividing by $m$:

    $$\dot{u} = X_uu + X_ww - g\cdot\cos\theta_0\theta^\prime$$(eq:concisex)
    
    where
    
    $$X_u\triangleq \frac{1}{m}\left.\pd{X}{u}\right|_0, X_w\triangleq \frac{1}{m}\left.\pd{X}{w}\right|_0$$
    
2.  The Z-Force equation (*heave equation*):

    Taking Equation {eq}`eq:heaveequation` and dividing by $m$:

    $$\dot{w} = Z_uu + Z_ww + U_eq - g\cdot\sin\theta_0\cdot\theta^\prime + Z_{\delta_e}\delta_e$$(eq:concisew)
    
    where
    
    $$Z_u\triangleq \frac{1}{m}\left.\pd{Z}{u}\right|_0, Z_w\triangleq \frac{1}{m}\left.\pd{Z}{w}\right|_0,  Z_{\delta_e}\triangleq \frac{1}{m}\left.\pd{Z}{\delta_e}\right|_0$$

3.  The M-Moment equation (*pitching moment equation*):

    If we take Equation {eq}`eq:pitchmomentequation` and divide by $I_{yy}$:

    $$\dot{q} = M_uu + M_ww + M_{\dot{w}}\dot{w} + M_qq + M_{\delta_e}\delta_e$$
    
    where
    
    $$M_u\triangleq \frac{1}{I_{yy}}\left.\pd{M}{u}\right|_0, \text{and the rest of the pattern should be clear}$$
            
    There is already an expression for $\dot{w}$, Equation {eq}`eq:concisew`, which may be substituted in:
    
    $$\dot{q} = M_uu + M_ww + M_{\dot{w}}\left(Z_uu + Z_ww + U_eq - g\cdot\sin\theta_0\cdot\theta^\prime + Z_{\delta_e}\delta_e \right) + M_qq + M_{\delta_e}\delta_e$$
    
    and can be simplified[^4] to:
    
    $$\dot{q} = M_u^*u + M_w^*w +M_\omega^*\omega + M_q^*q + M_{\delta_e}^*\delta_e$$(eq:conciseq)
    
    where
    
    $$\begin{split}&M_u^*\triangleq M_u + M_{\dot{w}}Z_u\hphantom{======} M_w^*\triangleq M_w+M_{\dot{w}}Z_w\hphantom{======}M_q^*\triangleq M_q+M_{\dot{w}}U_0\\
&M_{\delta_e}^*\triangleq M_{\delta_e}+M_{\dot{w}}Z_{\delta_e}\hphantom{======}M_{\theta}^*\triangleq-M_{\dot{w}}g\sin\theta_0
        \end{split}$$(eq:conciseqterms)

4.  The linearised Euler pitch equation (*pitch rate kinematic equation*):

    $q$ is pitch rate, from Eq {eq}`eq:pitchratekinematic`: 
    
    $$\dot{\theta}^\prime = q$$

Now Equations {eq}`eq:concisex`, {eq}`eq:concisew`, {eq}`eq:conciseq`, and {eq}`eq:pitchratekinematic` can be written in matrix form to give the **linearised equation of longitudinal motion in concise form**:

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
    \end{bmatrix}\left[\delta_e\right]\end{aligned}$$(eq:conciselon)
$$\dot{\vec{x}} =  A\vec{x} + B\vec{u}$$

Which is in state space form. Equation {eq}`eq:conciselon` is a series of simultaneous 1st order ODEs with constant coefficients which may solved to find the longitudinal response ($u,v,q,\theta$) of an aircraft due to elevator deflection ($\delta_e$).

[^4]: recalling that _simplify_ often means _make look nicer, but complicate the matter by introducing new terminology_

### Lateral/Directional EoMs

The asymmetric or lateral/directional EoMs may be similarly manipulated.

$$\color{darkgreen}{m\dot{v}=\left.\pd{Y}{v}\right|_0v - mU_0r+mg\cdot cos\theta_0\cdot\phi^\prime\left.\pd{Y}{\delta_r}\right|_0\delta_r}$$(eq:sideslipequation)
    
$$\color{darkgreen}{I_{xx}\dot{p} - I_{xz}\dot{r} = \left.\pd{L}{v}\right|_0v + \left.\pd{L}{p}\right|_0p+\left.\pd{L}{r}\right|_0r+\left.\pd{L}{\delta_r}\right|_0\delta_r+\left.\pd{L}{\delta_a}\right|_0\delta_a}$$(eq:rollmomentequation)

$$\color{darkgreen}{I_{zz}\dot{r}-I_{xz}\dot{p} = \left.\pd{N}{v}\right|_0v+ \left.\pd{N}{p}\right|_0p + \left.\pd{N}{r}\right|_0r +  \left.\pd{N}{\delta_r}\right|_0\delta_r+ \left.\pd{N}{\delta_a}\right|_0\delta_a}$$(eq:yawmomentequation)

1.  The Y-Force equation (*sideslip equation*): Taking Equation {eq}`eq:sideslipequation` and dividing by $m$:

    $$\dot{v} = Y_vv-U_er + g\cdot\cos\theta_0\phi + Y_{\delta_r}{\delta_r}$$

    where
    
    $$Y_v\triangleq\frac{1}{m}\pd{Y}{v},\,Y_{\delta_r}\triangleq\frac{1}{m}\pd{Y}{\delta_r}$$

2.  The two moment equations are coupled, so need to be decoupled. Dividing Equation {eq}`eq:rollmomentequation` by the rolling moment of inertia, $I_xx$:

    $$\dot{p} = \frac{I_{xz}}{I_{xx}}\dot{r} + L_vv + L_pp + L_rr + L_{\delta_r}{\delta_r} + L_{\delta_a}\delta_a$$(eq:rollingint)
    
    where
    
    $$L_v\triangleq\frac{1}{I_{xx}}\pd{L}{v},\,L_{p}\triangleq\frac{1}{I_{xx}}\pd{L}{p},\,\text{etc.}$$

    the same can be performed for {eq}`eq:yawmomentequation`, dividing by the yawing moment of inertia $I_{zz}$:

    $$\dot{r} = \frac{I_{xz}}{I_{zz}}\dot{p} + N_vv+N_pp + N_rr + N_{\delta_r}\delta_r+N_{\delta_a}\delta_a$$(eq:yawingint)

    Clearly Equations {eq}`eq:rollingint` and {eq}`eq:yawingint` are coupled, and must be decoupled if we want to use them in standard form. Substituting equation {eq}`eq:yawingint` into {eq}`eq:rollingint`, after a little manipulation (if you do this yourself, I promise you'll understand this subject better), the following is achieved:    

    $$\begin{split}\dot{p}\left(1-\frac{I_{xz}^2}{I_{xx}I_{zz}}\right) &= \left(L_v + \frac{I_{xz}}{I_{xx}}N_v\right)v + \left(L_p + \frac{I_{xz}}{I_{xx}}N_p\right)p+\left(L_r+\frac{I_{xz}}{I_{xx}}N_r\right)r +\ldots\\ &\left(L_{\delta_r} + \frac{I_{xz}}{I_{xx}N_{\delta_r}}\right)\delta_r + \left(L_{\delta_a}+\frac{I_{xz}}{I_{xx}}N_{\delta_a}\right)\delta_a\end{split}$$

    Noting that:

    $$1-\frac{I_{xz}^2}{I_{xx}I_{zz}} = \frac{I_{xx}I_{zz}-I_{zz}^2}{I_{xx}I_{zz}}$$

    hence, the **rolling moment equation** may be weitten as:

    $$\dot{p} = L_v^*v + L_p^*p + L_r^*r+L_{\delta_r}^*\delta_r+L_{\delta_a}^*\delta_a$$

    where:

    $$\begin{gathered}
            L_v^* = \frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(L_v+\frac{I_{xz}}{I_{xx}}N_v\right) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\, L_p^*=\frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(L_p+\frac{I_{xz}}{I_{xx}}N_p\right)\\
            L_r^* = \frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(L_r+\frac{I_{xz}}{I_{xx}}N_r\right) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\, L_{\delta_r}^*=\frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(L_{\delta_r}+\frac{I_{xz}}{I_{xx}}N_{\delta_r}\right)\\
            L_{\delta_a}^*=\frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(L_{\delta_a}+\frac{I_{xz}}{I_{xx}}N_{\delta_a}\right)
        \end{gathered}$$

    Similarly, by substituting {eq}`eq:rollingint` into {eq}`eq:yawingint`, the **yawing moment equation** is yielded:

    $$\dot{r} = N_v^*v + N_p^*p + N_r^*r + N_{\delta_r}^*\delta_r + N_{\delta_a}^*\delta_a$$

    where:

    $$\begin{gathered}
            N_v^* = \frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(N_v+\frac{I_{xz}}{I_{zz}}L_v\right) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\, N_p^*=\frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(N_p+\frac{I_{xz}}{I_{zz}}L_p\right)\\
            N_r^* = \frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(N_r+\frac{I_{xz}}{I_{zz}}L_r\right) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\, N_{\delta_r}^*=\frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(N_{\delta_r}+\frac{I_{xz}}{I_{zz}}L_{\delta_r}\right)\\
            N_{\delta_a}^*=\frac{I_{xx}I_{zz}}{I_{xx}I_{zz}-I_{xz}^2}\left(N_{\delta_a}+\frac{I_{xz}}{I_{zz}}L_{\delta_a}\right)        
        \end{gathered}$$

    often $I_{xz}$ is small compared to $I_{xx}$ and $I_{zz}$, so for these circumstances $N_v^*\simeq N_v$, $L_v^*\simeq L_v$


3.  Lastly, the yaw rate and body rate kinematic equations give:

    $$\begin{aligned}
            r &= \dot{\psi}\cos\theta_0\\
            \implies \dot{\psi} &= r\cdot\sec\theta_0\\
            p &= \dot{\phi}-\dot{\psi}\sin\theta_0\\
            \implies\dot{\phi} &= p + r\cdot\tan\theta_0
        \end{aligned}$$

So finally, the *linearised lateral/directional equations of motion* may be expressed in *state-space form:*

$$\begin{bmatrix}\dot{v}\\\dot{p}\\\dot{r}\\\dot{\phi}\\\dot{\psi}\end{bmatrix}=\begin{bmatrix}Y_v & 0 & -U_0 & g\cdot\cos\theta_0 & 0\\L_v^* & L_p^* & L_r^* & 0 & 0\\N_v^* & N_p^* & N_r^* & 0 & 0\\0 & 1 & \tan\theta_0 & 0 & 0 \\ 0 & 0 & \sec\theta_0 & 0 & 0\end{bmatrix}\begin{bmatrix}v\\p\\r\\\phi\\\psi\end{bmatrix}+\begin{bmatrix}Y_{\delta_r} & 0\\L_{\delta_r}^* & L_{\delta_a}^*\\N_{\delta_r}^* & N_{\delta_a}^*\\0 & 0\\0 & 0\end{bmatrix}\begin{bmatrix}\delta_r\\\delta_a\end{bmatrix}$$(eq:conciselat)

These are a series of linear differential equations which may be solved to give the aircraft lateral/directional response to inputs of rudder and aileron. You can observe that only the final equation has terms that involve $\psi$, and it may solved in isolation.

The two sets of matrix equations, {eq}`eq:conciselon` and {eq}`eq:conciselat`, are known as *the equations of motion in concise form*.

As will prove to be integral to Module 5, these are in **state space form**

$$\dot{\vec{x}} = \boldsymbol{A}\vec{x} + \boldsymbol{B}\vec{u}$$

where 

$$\vec{x} = \text{the state vector (n)}$$
$$\vec{u} = \text{the control matrix (m)}$$
$$\boldsymbol{A} = \text{the system matrix (n by n)}$$
$$\boldsymbol{B} = \text{the control matrix (n by m)}$$

for a system with $n$ states and $m$ controls. There are three reasons why we write the equations of motion in state space form:

-   The aircraft stability characteristics are obtained directly from the system matrix, $\boldsymbol{A}$ - this will be explored in the final module.

-   In studies of aircraft control systems, the state space form is easiest to analyse.

-   Since $\boldsymbol{A}$ and $\boldsymbol{B}$ are constant matrices, we can numerically integrate the equations of motion (using a Runge-Kutta method) to obtain the **time response** of the aircraft to a given control displacement - we may wish to calculate the longitudinal response (time histories of $u,w,q,\theta$) to a step change in elevator, $\delta_e$.

For the longitudinal equations in state space form, we have:

$$\boldsymbol{A}=\begin{bmatrix}
        X_u & X_w & 0 & -g\cdot\cos\theta_0\\
        Z_u & Z_w & U_0 & -g\cdot\sin\theta_0\\
        M_u^* & M_w^* & M_q^* & M_\theta^*\\
        0 & 0 & 1 & 0   
    \end{bmatrix}, \vec{x}=\begin{bmatrix}
        {u}\\{w}\\{q}\\{\theta}         
    \end{bmatrix}, \boldsymbol{B}= \begin{bmatrix}
        0\\Z_{\delta_e}\\M_{\delta_e}^*\\0          
    \end{bmatrix}, \vec{u}=\left[\delta_e\right]$$

For the lateral/directional equations in state space form:

$$\boldsymbol{A}=\begin{bmatrix}Y_v & 0 & -U_0 & g\cdot\cos\theta_0 & 0\\L_v^* & L_p^* & L_r^* & 0 & 0\\N_v^* & N_p^* & N_r^* & 0 & 0\\0 & 1 & \tan\theta_0 & 0 & 0 \\ 0 & 0 & \sec\theta_0 & 0 & 0\end{bmatrix}, \vec{x} = \begin{bmatrix}v\\p\\r\\\phi\\\psi\end{bmatrix}, \boldsymbol{B}=\begin{bmatrix}Y_{\delta_r} & Y_{\delta_a}\\L_{\delta_r}^* & L_{\delta_a}^*\\N_{\delta_r}^* & N_{\delta_a}^*\\0 & 0\\0 & 0\end{bmatrix}, \vec{u}=\begin{bmatrix}\delta_r\\\delta_a\end{bmatrix}$$


Some aircraft may have derivatives listed that have been neglected in the preceding - for example, you may find an aircraft with a nonzero $C_{D_q}$, which is the nondimensional form of $X_q$. You can hopefully appreciate that it can be readily re-inserted into the longitudinal equations of motion by choosing the logical place to insert into the system matrix:

$$\boldsymbol{A}=\begin{bmatrix}
        X_u & X_w & \color{red}{X_q} & -g\cdot\cos\theta_0\\
        Z_u & Z_w & U_0 & -g\cdot\sin\theta_0\\
        M_u^* & M_w^* & M_q^* & M_\theta^*\\
        0 & 0 & 1 & 0   
    \end{bmatrix}$$
    
Similarly, if you have an aircraft with a $C_{X_{\delta_e}}$ and hence $\cdot X_{\delta_e}$ term, then this would be inserted into the control matrix

$$\boldsymbol{B}= \begin{bmatrix}
        \color{red}{X_{\delta_e}}\\Z_{\delta_e}\\M_{\delta_e}^*\\0          
    \end{bmatrix}$$




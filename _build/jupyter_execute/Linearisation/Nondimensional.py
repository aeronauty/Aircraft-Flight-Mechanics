# Nondimensional Equations of Motion

$$\newcommand{\od}[2]{\frac{\text{d}#1}{\text{d}#2}}$$
$$\newcommand{\pd}[2]{\frac{\partial#1}{\partial#2}}$$
$$\newcommand{\ppd}[2]{\frac{\partial^2#1}{\partial#2^2}}$$
$$\newcommand{\pppd}[2]{\frac{\partial^3#1}{\partial#2^3}}$$

The equations of motion are sometimes used in non-dimensional form, where all the states and derivatives are non-dimensionalised. Different nondimensionalision schemes can be found, but they are of the form:

```{table} Nondimensionalisation Scheme for Equations of Motion
:name: nondimensionalisationscheme
|          Quantity          |        Divisor         |    Non-dimensional Form    |
|:--------------------------:|:----------------------:|:--------------------------:|
|          $X,Y,Z$           | $\frac{1}{2}\rho V^2S$ |       $C_X,C_Y,C_Z$        |
|          $L,M,N$           |      $\rho V^2Sl$      |      $C_l, C_m, C_n$       |
|          $u,v,w$           |         $U_0$          |   $\hat{u},\beta,\alpha$   |
|          $p,q,r$           |    $\frac{1}{t^*}$     | $\hat{p},\hat{q}, \hat{r}$ |
| $\dot{\alpha},\dot{\beta}$ |    $\frac{1}{t^*}$     |      $D\alpha,D\beta$      |
|            $m$             |       $\rho Sl$        |           $\mu$            |
|         $I_{xx},$          |      $\rho S l^3$      |         $i_{xx},$          |
|            $t$             |         $t^*$          |         $\hat{t}$          |
```

Note that $D=\od{}{\hat{t}}$ and $t^*=\frac{l}{U_e}$.\
The representative distance $l$ is $\frac{\bar{c}}{2}$ when dealing with the longitudinal equations, and $\frac{b}{2}$ for the lateral/directional equations.

We will not use the equations of motion in non-dimensional form, but they are presented below for completeness and for your future reference. There are advantages to the nondimensional form:
- The stability derivatives become _coefficients_ which enables comparison between aircraft

But the drawbacks are:
- A whole new set of nomenclature
- The output from solution of the equations are _also_ **nondimensional states** so need to be converted for interpretation


## The Longitudinal Equations in Non-Dimensional Form:

$$\begin{bmatrix} 
            2\mu & 0 & 0 & 0\\
            0 & 2\mu & 0 & 0\\
            0 & -C_{m_\alpha} & i_{yy} & 0 \\
            0 & 0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
        D\hat{u}\\D\alpha\\D\hat{q}\\D\theta
    \end{bmatrix}=
    \begin{bmatrix}
        \left(C_{x_u} + 2C_{L_0}\tan\Theta_e\right) & C_{x_\alpha} & 0 & -C_{L_0}\\
        \left(C_{z_u} - 2C_{L_0}\right) & C_{z_u} & 2\mu & -C_{L_0}\tan\Theta_e\\
        C_{m_u} & C_{m_\alpha} & C_{m_q} & 0\\
        0 & 0 & 1 & 0
    \end{bmatrix}
    \begin{bmatrix}
        \hat{u} \\ \alpha \\ \hat{q} \\ \theta
    \end{bmatrix} + 
    \begin{bmatrix}
        0 \\ C_{z_{\delta_e}} \\ C_{m_{\delta_e}} \\ 0
    \end{bmatrix}
    \begin{bmatrix}
        \delta_e
    \end{bmatrix}
$$(eq:lonnondimensional)

## The Lateral/Directional Equations in Non-Dimensional Form:

$$
    \begin{bmatrix} 
        2\mu & 0 & 0 & 0 & 0\\
        0 & i_{xx} & -i_{xz} & 0 & 0\\
        0 & -i_{xz} & i_{zz} & 0 & 0\\
        0 & 0 & 0 & 1 & 0\\
        0 & 0 & 0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
        D\beta\\D\hat{p}\\D\hat{r}\\D\phi\\D\psi
    \end{bmatrix}=
    \begin{bmatrix}
        C_{y_\beta} & 0 & -2\mu & C_{L_0} & 0\\
        C_{l_\beta} & C_{l_p} & C_{l_r} & 0 & 0\\
        C_{n_\beta} & C_{n_p} & C_{n_r} & 0 & 0\\
        0 & 1 & \tan\Theta_e & 0 & 0\\
        0 & 0 & \sec\Theta_e & 0 & 0
    \end{bmatrix}
    \begin{bmatrix}
        \beta \\ \hat{p} \\ \hat{r} \\\phi \\ \psi
    \end{bmatrix} + 
    \begin{bmatrix}
        0 & C_{y_{\delta_r}} \\ C_{l_{\delta_a}} & C_{l_{\delta_r}} \\ C_{n_{\delta_a}} & C_{n_{\delta_r}} \\ 0& 0\\0 & 0
    \end{bmatrix}
    \begin{bmatrix}
        \delta_a\\\delta_r
    \end{bmatrix}
$$(eq:latnondimensional)

$$\boldsymbol{A_1}D\vec{x} = \boldsymbol{A_2}\vec{x} + \boldsymbol{B_1}\vec{u}$$

where the matrices $\boldsymbol{A_1}$ are taken directly from {eq}`(eq:latnondimensional)` and {eq}`eq:lonnondimensional`, and $\vec{x}=[\hat{u},\alpha,\hat{q},\theta]^T$. To express this in state space form, one must determine:

$$\boldsymbol{A} = \boldsymbol{A_1}^{-1}\boldsymbol{A_2}\text{, and } \boldsymbol{B} = \boldsymbol{A_1}^{-1}\boldsymbol{B_1}$$

## Nondimensional stability derivatives

The procedure via which the stability derivatives are nondimensionalised is involved and you will not be expected to repeat the following, but the process will be demonstrated before a summary of the conversions is included.

Taking the speed damping derivative, $X_u$,

$$X_u=\frac{1}{m}\pd{X}{u}$$

the $X$ force can be written as

$$X=q\,S\,C_X$$

where, $q$ is dynamic pressure and not perturbational pitch rate. Hence

$$X_u=\frac{1}{m}\pd{}{u}\left[q\,S\,C_X\right]$$

the next step is convoluted by the fact that the dynamic pressure is a function of the perturbation forward speed, so the product rule must be used

$$X_u=\frac{1}{m}S\left[q_0\pd{C_X}{u} + \pd{q}{u}\cdot C_{X_0}\right]$$

the partial derivative $\pd{C_X}{u}$ is NOT equal to the non-dimensional derivative $C_{X_u}$ because the non-dimensional derivatives are, well, non-dimensional so

$$C_{X_u}\triangleq\pd{C_X}{\hat{u}}=\pd{C_X}{\frac{u}{U_0}}$$

so

$$\pd{C_X}{u} = \pd{C_X}{\frac{u}{U_0}}\pd{\frac{u}{U_0}}{u}=\frac{1}{U_0}C_{X_u}$$

$$X_u=\frac{1}{m}S\left[q C_{X_u}\frac{1}{U_0} + \pd{q}{u}\cdot C_{X_0}\right]$$(eq:Xu1)


where the term $C_{X_u}$ is the rate of change of $X$ force coefficient with non-dimensional forward speed, and $C_{X_0}$ is the trim value of $X$ force coefficient. The partial derivative $\pd{q}{u}$ will need a little evaluation

$$\begin{align}\pd{q}{u} &= \pd{}{u}\frac{1}{2}\rho\left[U_0+u\right]^2\\
&= \frac{1}{2}\rho\pd{}{u}\left[U_0^2 + 2U_0\,u+u^2\right]\\
&= \frac{1}{2}\rho\left[2U_0 +2u\right]\end{align}$$

$U_0\gg u$

$$\begin{align}\pd{q}{u} &= \frac{1}{2}\rho\left[U_0\right]\cdot2\\
&=\frac{2\cdot q}{U_0}\end{align}$$

so this can be substituted into {eq}`eq:Xu1`

$$X_u=\frac{q\,S}{m\,U_0}\left[C_{X_u}+2C_{X_0}\right]$$

various expressions are presented in the literature for $C_{X_u}$ incorporating lift terms, but in stability axes these are very small, and the only term of significance in $C_{X_u}$ is the compressibility effect due to drag, $-M\,C_{D_M}$ where $M$ is Mach number. The trim $C_{X_0}$ term is, by definition in stability axes, $-C_{D_0}$. 
Hence

$$X_u=-\frac{q\,S}{m\,U_0}\left[2\,C_{D_0}+M\,C_{D_M}\right]$$

You will appreciate that the process to go from each dimensional derivative to the non-dimensional derivative is involved, hence I will not expect you to go over the whole process, rather that you should have an appreciation of the entire process and be able to relate to the quantities below.

In practice, you will often start with the non-dimensional derivatives and convert to the dimensional form. For this, the table below will be useful

### Converting from nondimensional to dimensional stability derivatives

Conversion between the nondimensional and dimensional longitudinal stability derivatives is as follows.

In the tables below, the rates are given as nondimensional rates e.g., $C_{m_{\hat{q}}}$ to _remind_ you that they're nondimensional. You'll often just seem them listed as $C_{m_q}$ in the literature

|           	| X                                                                 	| Z                                                                 	| M                                                                   	|
|-----------	|-------------------------------------------------------------------	|-------------------------------------------------------------------	|---------------------------------------------------------------------	|
| $u$       	| $X_u = \frac{q_\infty\,S}{m\,U_0}\left[2C_{X_0} + C_{X_u}\right]$ 	| $Z_u = \frac{q_\infty\,S}{m\,U_0}\left[2C_{Z_0} + C_{Z_u}\right]$ 	| $M_u = \frac{q_\infty\,S\,\bar{c}}{I_{yy}\,U_0}C_{m_u}$             	|
| $w$       	| $X_w= \frac{q_\infty\,S}{m\,U_0}C_{X_\alpha}$                     	| $Z_w= \frac{q_\infty\,S}{m\,U_0}C_{Z_\alpha}$                     	| $M_w= \frac{q_\infty\,S\,\bar{c}}{I_{yy}\,U_0}C_{m_\alpha}$         	|
| $\dot{w}$ 	| $X_{\dot{w}}=\frac{q\,S\,\bar{c}}{2\,m\,U_0^2}C_{X_\dot{\alpha}}$ 	| $Z_{\dot{w}}=\frac{q\,S\,\bar{c}}{2\,m\,U_0^2}C_{Z_\dot{\alpha}}$ 	| $M_{\dot{w}}=\frac{q\,S\,\bar{c}^2}{2\,m\,U_0^2}C_{m_\dot{\alpha}}$ 	|
| $q$       	| $X_q=\frac{q\,S\,\bar{c}}{2\,m\,U_0}C_{X_\hat{q}}$                	| $Z_q=\frac{q\,S\,\bar{c}}{2\,m\,U_0}C_{Z_\hat{q}}$                	| $M_q=\frac{q\,S\,\bar{c}^2}{2\,I_{yy}\,U_0}C_{m_\hat{q}}$           	|
| $\delta$  	| $X_{\delta}=\frac{q\,S}{m}C_{\delta}$                              	| $Z_{\delta}=\frac{q\,S}{m}C_{\delta}$                              	| $M_{\delta}=\frac{q\,S\,\bar{c}}{I_{yy}}C_{\delta}$                       	|
The same can be performed for the lateral-directional stability derivatives

|          	| Y                                                      	| L                                                               	| N                                                            	|
|----------	|--------------------------------------------------------	|-----------------------------------------------------------------	|--------------------------------------------------------------	|
| $v$      	| $Y_v = \frac{q_\infty\,S}{m\,U_0}C_{y_\beta}$          	| $L_v=\frac{q_\infty\,S\,b}{I_{xx}\,U_0}C_{\ell_\beta}$          	| $N_v=\frac{q_\infty\,S\,b}{I_{zz}\,U_0}C_{n_\beta}$          	|
| $p$      	| $Y_p= \frac{q_\infty\,S\,b}{2\,m\,U_0}C_{y_{\hat{p}}}$ 	| $L_p=\frac{q_\infty\,S\,b^2}{2\,I_{xx}\,U_0}C_{\ell_{\hat{p}}}$ 	| $N_p=\frac{q_\infty\,S\,b^2}{2\,I_{zz}\,U_0}C_{n_{\hat{p}}}$ 	|
| $r$      	| $Y_r=\frac{q\,S\,b}{2\,m\,U_0}C_{y_{\hat{r}}}$         	| $L_r=\frac{q_\infty\,S\,b^2}{2\,I_{xx}\,U_0}C_{\ell_{\hat{r}}}$ 	| $N_r=\frac{q_\infty\,S\,b^2}{2\,I_{zz}\,U_0}C_{n_{\hat{r}}}$ 	|
| $\delta$ 	| $Y_{\delta}=\frac{q\,S}{m}C_{\delta}$                   	| $L_{\delta}=\frac{q\,S\,b}{I_{xx}}C_{\delta}$                       	| $N_{\delta}=\frac{q\,S\,b}{I_{zz}}C_{\delta}$                    	|

We must be careful as data are often not presented in the form of $C_{Z_\alpha}$, for example, rather as $C_{L_\alpha}$. In such case, we simply note that in stability axes 

$$C_{Z_\alpha}= -C_{L_\alpha}$$

Furthermore, you often wont see data presented for terms like $C_{X_u}$:

$$C_{X_u}\triangleq\pd{C_X}{\frac{u}{U_0}}$$

or the rate of change of $X$ force with non-dimensional forward speed. But you _will_ often see this presented as a compressibility effect, $C_{D_M}$. Noting that in stability axes, $C_X=-C_D$, then we can see

$$C_{X_u}=-M\,C_{D_M}$$



Hopefully it'll all become clear after an example

### 
# State Space Model Example

The preceding theory can be tested using data taken from the Appendix of 'Introduction to Aircraft Flight Dynamics' {cite}`Schmidt:1998fd` which, helpfully, provides the stability derivatives both in reduced dimensional form, and in non-dimensional form. This will allow verification of the conversion between the two forms.

## MD DC-8 Jet Transport Aircraft Data

The following data are reproduced from Appendix B.4{cite}`Schmidt:1998fd`.

Four conditions are given:
1. Power Approach
2. Holding
3. Cruise
4. $V_{NE}$

### Constants

$$\begin{align}
S &=2600\text{ft}^2\\
b &= 142.3\text{ft}\\
\bar{c} &= 23\text{ft}
\end{align}$$

### Condition and Geometric Data

| Condition                   	| 1        	| 2        	| 3        	| 4        	|
|-----------------------------	|----------	|----------	|----------	|----------	|
| $h$, ft                     	| 0        	| 15,000   	| 33,000   	| 33,000   	|
| $M$                         	| 0.218    	| 0.443    	| 0.84     	| 0.88     	|
| $V_\infty$\text{ft s}^{-1}$ 	| 243      	| 468      	| 825      	| 868      	|
| $q_\infty$ \text{lb ft}^2$  	| 70.4     	| 164      	| 271      	| 300      	|
| $W$ lb                      	| 190,000  	| 190,000  	| 230,000  	| 230,000  	|
| $I_{xx}$ slug-ft$^2$        	| 3.09E+06 	| 3.11E+06 	| 3.77E+06 	| 3.77E+06 	|
| $I_{yy}$ slug-ft$^2$        	| 2.94E+06 	| 2.94E+06 	| 3.56E+06 	| 3.56E+06 	|
| $I_{zz}$ slug-ft$^2$        	| 5.58E+06 	| 5.88E+06 	| 7.13E+06 	| 7.13E+06 	|
| $I_{xz}$ slug-ft$^2$        	| 28,000   	| -64500   	| 45,000   	| 53,700   	|
| $\delta_{flap}$ deg         	| 35       	| 0        	| 0        	| 0        	|

### Longitudinal Nomalised Derivatives

| Condition        	| 1       	| 2       	| 3       	| 4       	|
|------------------	|---------	|---------	|---------	|---------	|
| $h$, ft          	| 0       	| 15,000  	| 33,000  	| 33,000  	|
| $M$              	| 0.218   	| 0.443   	| 0.84    	| 0.88    	|
| $X_u$            	| -0.0291 	| -0.0071 	| -0.014  	| -0.0463 	|
| $X_\alpha$       	| 15.32   	| 15.03   	| 3.544   	| -22.36  	|
| $Z_u$            	| -0.251  	| -0.133  	| -0.074  	| 0.062   	|
| $Z_\alpha$       	| -152.8  	| -354    	| -664.3  	| -746.9  	|
| $M_u$            	| 0       	| 0       	| -0.0008 	| -0.0025 	|
| $M_\alpha$       	| -2.118  	| -5.01   	| -9      	| -12.003 	|
| $M_\dot{\alpha}$ 	| -0.26   	| -0.337  	| -0.42   	| -0.449  	|
| $M_q$            	| -0.792  	| -0.991  	| -0.924  	| -1.008  	|
| $X_{\delta_e}$   	| 0       	| 0       	| 0       	| 0       	|
| $Z_{\delta_e}$   	| -10.17  	| -23.7   	| -34.69  	| -39.06  	|
| $M_{\delta_e}$   	| -1.351  	| -3.241  	| -4.589  	| -5.12   	|

### Lateral-Directional Normalised Derivatives

| Condition          	| 1      	| 2      	| 3      	| 4      	|
|--------------------	|--------	|--------	|--------	|--------	|
| $h$, ft            	| 0      	| 15,000 	| 33,000 	| 33,000 	|
| $M$                	| 0.218  	| 0.443  	| 0.84   	| 0.88   	|
| $Y_\beta$          	| -27.05 	| -47.19 	| -71.73 	| -81.28 	|
| $L_\beta$          	| -1.334 	| -2.684 	| -4.449 	| -5.111 	|
| $L_p$              	| -0.949 	| -1.234 	| -1.184 	| -1.299 	|
| $L_r$              	| 0.611  	| 0.391  	| 0.337  	| 0.352  	|
| $N_\beta$          	| 0.762  	| 1.272  	| 2.175  	| 2.497  	|
| $N_p$              	| -0.119 	| -0.048 	| -0.013 	| -0.008 	|
| $N_r$              	| -0.268 	| -0.253 	| -0.231 	| -0.254 	|
| $Y_{\delta_r}$     	| 5.782  	| 13.47  	| 18.38  	| 20.35  	|
| $L_{\delta_r}$     	| 0.185  	| 0.375  	| 0.561  	| 0.639  	|
| $N_{\delta_r}$     	| -0.389 	| -0.861 	| -1.173 	| -1.298 	|
| $Y_{\delta_a}$     	| 0      	| 0      	| 0      	| 0      	|
| $L_{\delta_a}$     	| 0.725  	| 1.622  	| 2.12   	| 2.329  	|
| $N_{\delta_a}$     	| 0.05   	| 0.036  	| 0.052  	| 0.062  	|
| $L_\beta^*$        	| -1.327 	| -2.711 	| -4.424 	| -5.076 	|
| $L_p^*$            	| -0.95  	| -1.233 	| -1.184 	| -1.299 	|
| $L_r^*$            	| 0.609  	| 0.397  	| 0.335  	| 0.349  	|
| $N_\beta^*$        	| 0.756  	| 1.302  	| 2.148  	| 2.459  	|
| $N_p^*$            	| -0.124 	| -0.035 	| -0.021 	| -0.017 	|
| $N_r^*$            	| -0.264 	| -0.257 	| -0.228 	| -0.251 	|
| $L_{\delta_{r}}^*$ 	| 0.181  	| 0.393  	| 0.547  	| 0.621  	|
| $N_{\delta_{r}}^*$ 	| -0.388 	| -0.866 	| -1.169 	| -1.294 	|
| $L_{\delta_{a}}^*$ 	| 0.726  	| 1.622  	| 2.12   	| 2.33   	|
| $N_{\delta_{a}}^*$ 	| 0.053  	| 0.018  	| 0.065  	| 0.08   	|

### Lateral-Directional Dimensionless Derivatives

| Condition             	| 1       	| 2       	| 3       	| 4       	|
|-----------------------	|---------	|---------	|---------	|---------	|
| $h$, ft                	| 0       	| 15000   	| 33000   	| 33000   	|
| $M$                   	| 0.218   	| 0.443   	| 0.84    	| 0.88    	|
| $C_{y_\beta}$         	| -0.8727 	| -0.6532 	| -0.7277 	| -0.7449 	|
| $C_{\ell_\beta}$      	| -0.1582 	| -0.1375 	| -0.1673 	| -0.1736 	|
| $C_{\ell_\hat{p}}$          	| -0.385  	| -0.416  	| -0.516  	| -0.538  	|
| $C_{\ell_\hat{r}}$          	| 0.248   	| 0.132   	| 0.147   	| 0.146   	|
| $C_{n_\beta}$         	| 0.1633  	| 0.1232  	| 0.1547  	| 0.1604  	|
| $C_{n_\hat{p}}$             	| -0.087  	| -0.0331 	| -0.011  	| -0.006  	|
| $C_{n_\hat{r}}$             	| -0.196  	| -0.161  	| -0.019  	| -0.199  	|
| $C_{y_{\delta_r}}$    	| 0.1865  	| 0.1865  	| 0.1865  	| 0.1865  	|
| $C_{\ell_{\delta_r}}$ 	| 0.0219  	| 0.0192  	| 0.0211  	| 0.0217  	|
| $C_{n_{\delta_r}}$    	| -0.0834 	| -0.0834 	| -0.0834 	| -0.0834 	|
| $C_{y_{\delta_a}}$    	| 0       	| 0       	| 0       	| 0       	|
| $C_{\ell_{\delta_a}}$ 	| 0.086   	| 0.0831  	| 0.0797  	| 0.0791  	|
| $C_{n_{\delta_a}}$    	| 0.0106  	| 0.035   	| 0.0037  	| 0.004   	|

### Longitudinal Dimensionless Derivatives

| Condition            	| 1      	| 2      	| 3      	| 4      	|
|----------------------	|--------	|--------	|--------	|--------	|
| $h$, ft              	| 0      	| 15000  	| 33000  	| 33000  	|
| $M$                  	| 0.218  	| 0.443  	| 0.84   	| 0.88   	|
| $C_D$                	| 0.1095 	| 0.0224 	| 0.0188 	| 0.0276 	|
| $C_{D_\alpha}$       	| 0.487  	| 0.212  	| 0.272  	| 0.486  	|
| $C_{D_M}$            	| 0.0202 	| 0.0021 	| 0.1005 	| 0.365  	|
| $C_{L}$              	| 1.038  	| 0.445  	| 0.326  	| 0.295  	|
| $C_{L_\alpha}$       	| 4.81   	| 4.876  	| 6.744  	| 6.899  	|
| $C_{L_M}$            	| 0.02   	| 0.048  	| 0      	| -1.2   	|
| $C_{m_\alpha}$       	| -1.478 	| -1.501 	| -2.017 	| -2.413 	|
| $C_{m_M}$            	| -0.006 	| -0.02  	| -0.17  	| -0.5   	|
| $C_{m_\dot{\alpha}}$ 	| -3.84  	| -4.1   	| -6.62  	| -6.83  	|
| $C_{m_\hat{q}}$      	| -11.7  	| -12.05 	| -14.6  	| -15.2  	|
| $C_{D_{\delta_e}}$   	| 0      	| 0      	| 0      	| 0      	|
| $C_{L_{\delta_e}}$   	| 0.328  	| 0.328  	| 0.352  	| 0.358  	|
| $C_{m_{\delta_e}}$   	| -0.943 	| -0.971 	| -1.008 	| -1.016 	|

These data are all saved in an excel file, which is available for download. They can be pulled out of the excel file using the following scripts:

## Import Pandas
import pandas as pd

## Import the Nomdimensional Longitudinal
DC8Data = 'Data/DC8Data.xlsx'
Nondim_lon_data = pd.read_excel(DC8Data, sheet_name="Longitudinal Dimensionless")
other_data = pd.read_excel(DC8Data, sheet_name="Geometric")

# These are now imported as a pandas dataframe - which measn they're in slightly an awkward format to work with
# But you *could* just hard code them all manually. This is just how I'd like to import them.

# This extracts the names of all the longitudinal nondimensional derivatives
lon_derivs_names = Nondim_lon_data["Condition"].tolist()[2:]

# Which condition? Let's look at the first condition
cond = 3

# Make an empty dictionary
DC8_lon_nondim = {}

# Now we can iterate through the list of deriatives and store each value in the dictionary
for deriv in lon_derivs_names:
    # Get the row corresponding to this derivative
    this_row = Nondim_lon_data[Nondim_lon_data["Condition"] == deriv]
    
    # Get the derivative corresponding to the condition
    this_derivative = this_row[cond]
    
    # Add it to the dictionary
    DC8_lon_nondim[deriv] = this_derivative.item()
    
# Print the dictionary to show what cool work we've done
print("The longitudinal non-dimenional deriviatives, taken from the Appendix are:", DC8_lon_nondim)

# Do the same with the dimensional deribatives
## Import the Nomdimensional Longitudinal
DC8Data = 'Data/DC8Data.xlsx'
dim_lon_data = pd.read_excel(DC8Data, sheet_name="Longitudinal")


# This extracts the names of all the longitudinal nondimensional derivatives
lon_derivs_names = dim_lon_data["Condition"].tolist()[2:]



# Make an empty dictionary
DC8_lon_dim_data = {}

# Now we can iterate through the list of deriatives and store each value in the dictionary
for deriv in lon_derivs_names:
    # Get the row corresponding to this derivative
    this_row = dim_lon_data[dim_lon_data["Condition"] == deriv]
    
    # Get the derivative corresponding to the condition
    this_derivative = this_row[cond]
    
    # Add it to the dictionary
    DC8_lon_dim_data[deriv] = this_derivative.item()
    
print("From the table, the data are:", DC8_lon_dim_data)

# Now we can convert them to the dimensional form by going through the equations in the table we produced
# We need to get out some of the constants from the table, which have some awkward names
DC8_lon_dim = {}
q = other_data[other_data["Condition"] == "Q lb/ft^2"][cond].item()
m = other_data[other_data["Condition"] == "W lb"][cond].item()/32.17 # Data is as W to need to divide by slugs
U0 = other_data[other_data["Condition"] == "V f/s"][cond].item()
M = other_data[other_data["Condition"] == "M"][cond].item()
S = 2600 # Wing area in ft^2
b = 142.3 # span in ft
c = 23 # MAC in ft

# We'll work in US customary units to confirm that the conversion between nondimensional and dimensional works
# as expected - if it *does*, then we can convert to good-old SI units

# Xu
DC8_lon_dim['Xu'] = -q * S / m / U0 * (2 * DC8_lon_nondim['Cd'] + M * DC8_lon_nondim['Cdm'])
print(f"From our conversion, Xu is {DC8_lon_dim['Xu']:1.4f}, from the table it is {DC8_lon_dim_data['Xu']:1.4f}")

# Xw
DC8_lon_dim['Xw'] = q * S / m / U0 * (DC8_lon_nondim['Cl'] - DC8_lon_nondim['Cda'])

print(DC8_lon_dim['Xw']*U0)

$$\newcommand{\od}[2]{\frac{\text{d}#1}{\text{d}#2}}$$
$$\newcommand{\pd}[2]{\frac{\partial#1}{\partial#2}}$$
$$\newcommand{\ppd}[2]{\frac{\partial^2#1}{\partial#2^2}}$$
$$\newcommand{\pppd}[2]{\frac{\partial^3#1}{\partial#2^3}}$$

Here we reach an issue - we have calculate $X_u$, but the table has presented $X_\alpha$. We can use the relationship

$$X_w\triangleq\frac{1}{m}\pd{X}{\alpha}\pd{\alpha}{w}=X_\alpha\pd{\alpha}{w}=X_\alpha\frac{1}{U_0}$$

print(f"From our conversion, Xw is {DC8_lon_dim['Xw']:1.4f}, from the table it is {DC8_lon_dim_data['Xalpha']/U0:1.4f}")

# Xq = 0 as it doesn't exist in the table
DC8_lon_dim['Xq'] = 0

# Xde
DC8_lon_dim['Xde'] = -q * S / m * DC8_lon_nondim['Cde']
print(f"From our conversion, Xde is {DC8_lon_dim['Xde']:1.4f}, from the table it is {DC8_lon_dim_data['Xde']:1.4f}")

# Zu
DC8_lon_dim['Zu'] = -q * S / m / U0 * (2*DC8_lon_nondim['Cl'] + M * DC8_lon_nondim['Clm'])
print(f"From our conversion, Zu is {DC8_lon_dim['Zu']:1.4f}, from the table it is {DC8_lon_dim_data['Zu']:1.4f}")


# Try the corvair
S = 2000
b = 120
c = 18.94
W = 126000
q = 61
m = W / 32.17
# W = 155000
V = 227
M = 0.203

Cd = 0.154
Cdm = 0
Xu = -q*S/m/V * (2 * Cd + M * Cdm)
print(Xu)

Cl = 1.029
Cda = 0.43
Xa = q * S / m * (Cl - Cda)
print(Xa)

Clm = 0
Zu = -q * S / m / V * (2*Cl + M * Clm)
print(Zu)

Clda = 4.66
Zda = -q*S/m * (c/2/V) * Clda





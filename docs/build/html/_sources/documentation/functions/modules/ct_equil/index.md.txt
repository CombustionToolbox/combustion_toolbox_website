# Thermochemical equilibrium module

In this section, you will find the documentation of the kernel of the code, which is used to obtain the chemical equilibrium composition for a desired thermochemical transformation, e.g., constant enthalpy and pressure. It also includes routines to compute chemical equilibrium assuming a complete combustion and the calculation of the thermodynamic derivates. The code stems from the minimization of the free energy of the system by using Lagrange multipliers combined with a Newton-Raphson method, upon condition that initial gas properties are defined by two functions of states, e.g., temperature and pressure.


```{note}
The kernel of the code is based on Gordon, S., & McBride, B. J. (1994). NASA reference publication, 1311.
```

## Thermodynamic derivatives

All thermodynamic first derivatives can be obtained with any set of three independent first derivatives [1]. Combustion Toolbox computes all thermodynamic first derivatives from $(\partial \text{ln } V/\partial \text{ln } T)_p$, $(\partial \text{ln } V/\partial \text{ln } p)_T$, and $(\partial h/\partial T)_p = c_p$. Considering the ideal equation of state

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      pV = nRT
    \end{equation}
```
and applying logarithms to both sides

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      \text{ln } V = \text{ln } n + \text{ln } R + \text{ln } T - \text{ln } p
    \end{equation}
```

is readily seen that

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      \left(\dfrac{\partial \text{ln } V }{\partial \text{ln } T}\right)_p = 1 + \left(\dfrac{\partial \text{ln } n }{\partial \text{ln } T}\right)_p,
    \end{equation}
```
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      \left(\dfrac{\partial \text{ln } V }{\partial \text{ln } p}\right)_T = -1 + \left(\dfrac{\partial \text{ln } n }{\partial \text{ln } p}\right)_T.
    \end{equation}
```

To compute $c_p$ we have to distinguish between the frozen contribution and the reaction contribution

```{eval-rst}
.. math::
    :nowrap:
    
    \begin{equation}
      c_p = c_{p,f} + c_{p,r}
    \end{equation}
```

given by the following relations

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      c_{p,f} = \sum\limits_{j=1}^{\text{NS}} n_j c_{p,f}^\circ,
    \end{equation}
    \begin{equation}
      c_{p,r} = \dfrac{1}{T}\left[\sum\limits_{j=1}^{\text{NS}} [1 + \delta_j(n_j - 1)] h_j^\circ\left(\dfrac{\partial \eta_j}{\partial \text{ln } T} \right)\right],
    \end{equation}
```

with $\eta_j = \text{ln } n_j$ and $\delta_j = 1 $ for $j=1,\dots,NG$ (non-condensed species), and $\eta_j = n_j$ and $\delta_j = 0$ for $j = NG + 1, \dots, NS$ (condensed species).

### Derivatives with respect to temperature

```{eval-rst}
.. math::
    :nowrap:

    \begin{aligned}
      \delta_j\left(\dfrac{\partial \eta_j }{\partial \text{ln } T}\right)_p - \sum\limits_{i = 1}^{\text{NE}} a_{ij} \left(\dfrac{\partial \pi_i }{\partial \text{ln } T}\right)_p - \delta_j\left(\dfrac{\partial \text{ln } n}{\partial \text{ln } T}\right)_p &= \dfrac{h_j^\circ}{RT}, \quad &\text{for } j=1, \dots, \text{NS}\\

       \sum\limits_{j = 1}^{\text{NS}} a_{ij} [1 + \delta_j(n_j - 1)] \left(\dfrac{\partial \eta_j }{\partial \text{ln } T}\right)_p &= 0, \quad &\text{for } i=1, \dots, \text{NE}\\

       \sum\limits_{j = 1}^{\text{NG}} n_j \left(\dfrac{\partial \eta_j }{\partial \text{ln } T}\right)_p - n \left(\dfrac{\partial \text{ln } n}{\partial \text{ln } T}\right)_p&= 0,
    \end{aligned}
```

<!-- To solve the stem is more practical to change it into matricial form, namely -->

### Derivatives with respect to pressure

```{eval-rst}
.. math::
    :nowrap:

    \begin{aligned}
      \delta_j\left(\dfrac{\partial \eta_j }{\partial \text{ln } p}\right)_T - \sum\limits_{i = 1}^{\text{NE}} a_{ij} \left(\dfrac{\partial \pi_i }{\partial \text{ln } p}\right)_T - \delta_j\left(\dfrac{\partial \text{ln } n}{\partial \text{ln } p}\right)_T &= -\delta, \quad &\text{for } j=1, \dots, \text{NS}\\

       \sum\limits_{j = 1}^{\text{NS}} a_{ij} [1 + \delta_j(n_j - 1)] \left(\dfrac{\partial \eta_j }{\partial \text{ln } p}\right)_T &= 0, \quad &\text{for } i=1, \dots, \text{NE}\\

       \sum\limits_{j = 1}^{\text{NG}} n_j \left(\dfrac{\partial \eta_j }{\partial \text{ln } p}\right)_T - n \left(\dfrac{\partial \text{ln } n}{\partial \text{ln } p}\right)_T&= 0.
    \end{aligned}
```

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.modules.ct_equil
   :members:
```
:::

1. McBride, Bonnie J. Computer program for calculation of complex chemical equilibrium compositions and applications. Vol. 2. NASA Lewis Research Center, 1996.
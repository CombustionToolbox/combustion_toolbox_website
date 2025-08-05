# Complete combustion

For instance, let's complicate the previous example by considering different fuel-oxidizer ratios, given the equivalence ratio $\phi$. For a stoichiometric mixture, we have $\phi = 1$, and the chemical system of its complete combustion is the same as above. For a fuel-lean mixture, we have $\phi < 1$, we do not have enough fuel to react with all the oxidizer, thus we have unreacted oxidizer in the final state. For a fuel-rich mixture, we have $\phi > 1$, we have excess fuel that does not react with all the oxidizer. In this case, the excess of fuel react with CO$_2$ and H$_2$O, producing CO and H$_2$. Finally, for a sufficiently rich mixture, we have $\phi > \phi_c$, all CO$_2$ and H$_2$O is depleted, producing CO, H$_2$, and C<sub>gr</sub> (soot). Here, $\phi_c$ represents the theoretical value at which soot is produced.

`````{tab-set}

````{tab-item} Lean

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \underbrace{\text{CH}_4 + 2 (\text{O}_2 + 3.76 \text{N}_2)}_{\rm{reactants\ (initial\ state)}} \rightleftharpoons \underbrace{\text{CO}_2 + 2 \text{H}_2\text{O} + 7.52 \text{N}_2}_{\rm{products\ (final\ state)}}.
    \end{equation}

```

````

````{tab-item} Stoichiometric

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \underbrace{\text{CH}_4 + 2 (\text{O}_2 + 3.76 \text{N}_2)}_{\rm{reactants\ (initial\ state)}} \rightleftharpoons \underbrace{\text{CO}_2 + 2 \text{H}_2\text{O} + 7.52 \text{N}_2}_{\rm{products\ (final\ state)}}.
    \end{equation}

```

````

````{tab-item} Rich

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \underbrace{\text{CH}_4 + 2 (\text{O}_2 + 3.76 \text{N}_2)}_{\rm{reactants\ (initial\ state)}} \rightleftharpoons \underbrace{\text{CO}_2 + 2 \text{H}_2\text{O} + 7.52 \text{N}_2}_{\rm{products\ (final\ state)}}.
    \end{equation}

```

````

````{tab-item} Sufficiently rich (soot)

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \underbrace{\text{CH}_4 + 2 (\text{O}_2 + 3.76 \text{N}_2)}_{\rm{reactants\ (initial\ state)}} \rightleftharpoons \underbrace{\text{CO}_2 + 2 \text{H}_2\text{O} + 7.52 \text{N}_2}_{\rm{products\ (final\ state)}}.
    \end{equation}

```

````

`````
#!/usr/bin/env python
# coding: utf-8

# # Reaction Mechanisms

# ## Motivation
# 
# Many reactions proceed through interemdiates before achieving their products.  The step-by-step process of going from reactants to products is called a reaction mechanism.  The mechanism that a reaction follows affects its kinetics.  In these notes, we will ee how proposed mechanisms can be shown to be consistent or incosistent with experimental data. 

# ## Learning Goals
# 
# After working through these notes, you should be able to:
# 
# 1. Determine a net reaction from a proposed mechanism
# 2. Determine the rate law from some proposed mechanism
# 3. Invalidate mechanisms based on their rate law and the experimentally determined rate law
# 4. Identify unimolecular, bimolecular, and termolecular elementary steps
# 5. Right the rate laws for unimolecular, bimolecular, and termolecular elementary steps

# ## Coding Concepts
# 
# The following coding concepts are used in this notebook:
# 
# 1. None, yet.

# ## Most Reactions Proceed through at least one Intermediate

# Most reaction do not proceed in a straightforward manner from reactants to products.  Typically, an intermediate, or multiple intermediates, are formed before the products form.  The presence of these intermediates complicates the molecularity of the rate law making it such that the overall rate law need not match the stoichiometry of the overall balanced chemical reaction. 
# 
# The goal here is to describe the steps that makeup a mechanism.  Each proposed step, a so called "elementary step", must obey the molecularity of the balanced chemical reaction for that step.  For example, if you propose an elementary step that is, e.g.,
# \begin{equation}
# NO_3(g) + CO(g) \overset{k_1}{\Longrightarrow} NO_2(g) + CO_2(g)
# \end{equation}
# you are actually saying that one molecule of $NO_3(g)$ and one molecule of $CO(g)$ collide to form a transition state that then dissociates into one molecule of $NO_2(g)$ and another molecule of $CO_2(g)$.  No intermediates are formed in between the reactants and products.  Thus, the rate law for this step will be
# \begin{equation}
# v(t) = \frac{d[NO_2]}{dt} = \frac{d[CO_2]}{dt} = k_1[NO_3][CO]
# \end{equation}

# ## Rules for a Valid Mechanism
# 
# An almost infinite number of mechanisms can be proposed for a given reaction.  In order for a mechanism to be ***valid***, it must abide by the following criteria:
# 
# 1. The sum of all elementary steps must net the overall balanced chemical reaction.
# 2. The rate law coming from the mechanism must agree with (in terms of order of rxn with respect to reactants) the experimentally determined rate law.
# 3. All species must make some semblence of chemical sense.
# 
# This last criteria can sometimes be difficult to determine as it can be challenging to determine the rate law from a given mechanism.

# ## Example Mechanisms

# Consider the reaction
# 
# \begin{equation}
# 2NO(g) + O_2(g) \overset{k_{obs}}{\longrightarrow} 2NO_2(g)
# \end{equation}
# The rate law has been experimentally determined to be
# \begin{equation}
# \frac{1}{2} \frac{d[NO_2]}{dt} = k_{obs}[NO]^2[O_2]
# \end{equation}
# 
# Consider four propsed mechanisms.  Determine if each is valid.
# 
# *Mechanism 1:*
# \begin{eqnarray}
# NO(g) + O_2(g) &\overset{k_1}{\overset{\Longrightarrow}{\underset{k_{-1}}{\Longleftarrow}}}& NO_3(g) \quad \text{(rapid equilibrium)} \\
# NO_3(g) + NO(g) &\overset{k_2}{\Longrightarrow}& 2NO_2(g) \quad \text{(slow)}
# \end{eqnarray}
# 
# *Mechanism 2:*
# \begin{eqnarray}
# NO(g) + NO(g) &\overset{k_1}{\overset{\Longrightarrow}{\underset{k_{-1}}{\Longleftarrow}}}& N_2O_2(g) \quad \text{(steady-state)} \\
# N_2O_2(g) + O_2(g) &\overset{k_2}{\Longrightarrow}& 2NO_2(g) 
# \end{eqnarray}
# 
# *Mechanism 3:*
# \begin{eqnarray}
# 2O_2(g) + 2O_2(g) &\overset{k_1}{\Longrightarrow}& 2O_3(g) + 2O(g)  \\
# 2NO(g) + 2O(g) &\overset{k_2}{\Longrightarrow}& 2NO_2(g) 
# \end{eqnarray}
# 
# *Mechanism 4:*
# \begin{eqnarray}
# O_2(g) + O_2(g) &\overset{k_1}{\overset{\Longrightarrow}{\underset{k_{-1}}{\Longleftarrow}}}& O_4(g) \quad \text{(rapid equilibrium)} \\
# NO(g) + NO(g) &\overset{k_2}{\overset{\Longrightarrow}{\underset{k_{-2}}{\Longleftarrow}}}& N_2O_2(g) \quad \text{(rapid equilibrium)} \\
# N_2O_2(g) + O_4(g) &\overset{k_3}{\Longrightarrow}& 2NO_2(g) + O_2(g) 
# \end{eqnarray}

# ### Mechanism 1:
# 
# \begin{eqnarray}
# NO(g) + O_2(g) &\overset{k_1}{\overset{\Longrightarrow}{\underset{k_{-1}}{\Longleftarrow}}}& NO_3(g) \quad \text{(rapid equilibrium)} \\
# NO_3(g) + NO(g) &\overset{k_2}{\Longrightarrow}& 2NO_2(g) \quad \text{(slow)}
# \end{eqnarray}
# 
# We start by checking that the two reactions sum to the net reaction.  The summed reaction from mechanism 1 is:
# \begin{eqnarray}
# NO(g) + O_2(g) + NO_3(g) + NO(g) &\longrightarrow& NO_3(g) + 2NO_2(g) \\
# 2NO(g) + O_2(g) &\longrightarrow& 2NO_2(g)
# \end{eqnarray}
# The last being the same as the net reaction (after cancelling intermediate $NO_3(g)$ from both sides) and thus this mechanism satistifies our first criteria for a valid mechanism.
# 
# Now to determine the rate law from this mechanism. We start by writing out the differential equation for the rate of appearance of the product in step 2:
# \begin{eqnarray}
# \frac{1}{2}\frac{d[NO_2]}{dt} = k_2[NO_3][NO]
# \end{eqnarray}
# we note that the left-hand side is equivalent to the rate law expression of the overall net reaction (experimentally determined rate law) thus we are off to a good start.  We also note that the rate depends on the concentration of $NO_3$, an intermediate in our reaction.  We need to get rid of that.  We will use the rapid equilibrium in the first step.
# 
# A rapid equilibrium in step 1 means that we can assume that the concentrations of the species in step 1 are always their equilibrium concentrations.  Namely
# \begin{eqnarray}
# K_{C,1} &=& \frac{[NO_3]}{[NO][O_2]} \\
# \Rightarrow [NO_3] &=& K_{C,1}[NO][O_2]
# \end{eqnarray}
# 
# Plugging this into the equation above yields
# \begin{eqnarray}
# \frac{1}{2}\frac{d[NO_2]}{dt} = k_2K_{C,1}[NO]^2[O_2]
# \end{eqnarray}
# 
# Thus, we see that this mechanism is consistent with the experimentally determined rate law with $k_{obs} = k_2K_{C,1}$.
# 
# None of the species proposed in this mechanism are out of the realm of chemical possibility and thus we conclude that the proposed mechanism is valid and consistent with all of the relevant experimental data.

# ### Mechanism 2: 
# \begin{eqnarray}
# NO(g) + NO(g) &\overset{k_1}{\overset{\Longrightarrow}{\underset{k_{-1}}{\Longleftarrow}}}& N_2O_2(g) \quad \text{(steady-state)} \\
# N_2O_2(g) + O_2(g) &\overset{k_2}{\Longrightarrow}& 2NO_2(g) 
# \end{eqnarray}
# 
# We start by checking that the two reactions sum to the net reaction.  The summed reaction from mechanism 2 is:
# \begin{eqnarray}
# NO(g) + NO(g) + O_2(g) + N_2O_2(g) &\longrightarrow& N_2O_2(g) + 2NO_2(g) \\
# 2NO(g) + O_2(g) &\longrightarrow& 2NO_2(g)
# \end{eqnarray}
# The last being the same as the net reaction (after cancelling intermediate $NO_3(g)$ from both sides) and thus this mechanism satistifies our first criteria for a valid mechanism.
# 
# Now to determine the rate law from this mechanism. We start by writing out the differential equation for the rate of appearance of the product in step 2:
# \begin{eqnarray}
# \frac{1}{2}\frac{d[NO_2]}{dt} = k_2[N_2O_2][O_2]
# \end{eqnarray}
# we note, again, that the left-hand side is equivalent to the rate law expression of the overall net reaction (experimentally determined rate law) thus we are off to a good start.  We also note that the rate depends on the concentration of $N_2O_2$, an intermediate in our reaction.  We need to get rid of that.  We will use the steady-state approximation for the intermediate.
# 
# The steady-state approximation implies that the concentration of the intermediate species, $N_2O_2$ in this case, is constant with respect to time ($\frac{d[N_2O_2]}{dt} = 0$).  To see how we can use this we write out the diffential expression for $[N_2O_2]$ with respect to time for this mechanism:
# \begin{eqnarray}
# \frac{d[N_2O_2]}{dt} = k_1[NO][NO] - k_{-1}[N_2O_2] - k_2[N_2O_2][O_2]
# \end{eqnarray}
# where the first two terms on the r.h.s. come from step 1 of the mechanism and the last term comes from step 2 of the mechanism.  We now apply the steady-state approximation and solve the resulting equation for $[N_2O_2]$
# \begin{eqnarray}
# \frac{d[N_2O_2]}{dt} \overset{s.s.}{=} 0 &=& k_1[NO][NO] - k_{-1}[N_2O_2] - k_2[N_2O_2][O_2] \\
# \Rightarrow [N_2O_2](k_{-1} + k_2[O_2]) &=& k_1[NO]^2 \\
# \Rightarrow [N_2O_2] &=& \frac{k_1[NO]^2}{(k_{-1} + k_2[O_2])}
# \end{eqnarray}
# The steady-state approximation is only valid in this case when the rate of the reverse reaction in step 1 is much larger than the rate of the forward reactions in steps 1 and 2.  Or, $k_{-1} >> k_2[O_2]$.  Thus, we get that
# \begin{equation}
# [N_2O_2] = \frac{k_1}{k_{-1}}[NO]^2 = K_{C,1}[NO]^2
# \end{equation}
# 
# Plugging this into the equation above yields
# \begin{eqnarray}
# \frac{1}{2}\frac{d[NO_2]}{dt} = k_2K_{C,1}[NO]^2[O_2]
# \end{eqnarray}
# 
# Thus, we see that this mechanism is consistent with the experimentally determined rate law with $k_{obs} = k_2K_{C,1}$.
# 
# None of the species proposed in this mechanism are out of the realm of chemical possibility and thus we conclude that the proposed mechanism is valid and consistent with all of the relevant experimental data.

# ### Mechanism 3:
# \begin{eqnarray}
# 2O_2(g) + 2O_2(g) &\overset{k_1}{\Longrightarrow}& 2O_3(g) + 2O(g)  \\
# 2NO(g) + 2O(g) &\overset{k_2}{\Longrightarrow}& 2NO_2(g) 
# \end{eqnarray}
# 
# We start by checking that the two reactions sum to the net reaction.  The summed reaction from mechanism 3 is:
# \begin{eqnarray}
# 2NO(g) + 2O(g) + 4O_2(g) &\longrightarrow& 2O_3(g) + 2O(g) + 2NO_2(g)  \\
# 2NO(g) + 4O_2(g) &\longrightarrow& 2NO_2(g) + 2O_3(g)
# \end{eqnarray}
# Clearly this reaction does not match the net balanced reaction thus this mechanism is invalid.

# ### Mechanism 4:
# 
# \begin{eqnarray}
# O_2(g) + O_2(g) &\overset{k_1}{\overset{\Longrightarrow}{\underset{k_{-1}}{\Longleftarrow}}}& O_4(g) \quad \text{(rapid equilibrium)} \\
# NO(g) + NO(g) &\overset{k_2}{\overset{\Longrightarrow}{\underset{k_{-2}}{\Longleftarrow}}}& N_2O_2(g) \quad \text{(rapid equilibrium)} \\
# N_2O_2(g) + O_4(g) &\overset{k_3}{\Longrightarrow}& 2NO_2(g) + O_2(g) 
# \end{eqnarray}
# 
# We start by checking that the two reactions sum to the net reaction.  The summed reaction from mechanism 2 is:
# \begin{eqnarray}
# NO(g) + NO(g) + O_2(g) + O_2(g) N_2O_2(g) + O_4(g) &\longrightarrow& O_4(g) + O_2(g) + N_2O_2(g) + 2NO_2(g) \\
# 2NO(g) + O_2(g) &\longrightarrow& 2NO_2(g)
# \end{eqnarray}
# The last being the same as the net reaction (after cancelling intermediates $N_2O_2(g)$ and $O_4(g)$ as well as one mole of $O_2$ that appears as both reactant and product) and thus this mechanism satistifies our first criteria for a valid mechanism.
# 
# Now to determine the rate law. We start by writing out the differential equation for the rate of appearance of the product in step 3:
# \begin{eqnarray}
# \frac{1}{2}\frac{d[NO_2]}{dt} = k_3[N_2O_2][O_4]
# \end{eqnarray}
# we note that the left-hand side is equivalent to the rate law expression of the overall net reaction (experimentally determined rate law) thus we are off to a good start.  We also note that the rate depends on the concentration of intermediates $N_2O_2$ and $O_4$.  
# 
# We will use the rapid equilibria from steps 1 and 2 to substitute the concentrations of intermediates with concentrations of reactants.
# \begin{eqnarray}
# K_{C,1} &=& \frac{[O_4]}{[O_2][O_2]} \\
# \Rightarrow [O_4] &=& K_{C,1}[O_2]^2
# \end{eqnarray}
# \begin{eqnarray}
# K_{C,2} &=& \frac{[N_2O_2]}{[NO][NO]} \\
# \Rightarrow [N_2O_2] &=& K_{C,2}[NO]^2
# \end{eqnarray}
# 
# Substituting these two relationships into the rate law yields
# \begin{eqnarray}
# \frac{1}{2}\frac{d[NO_2]}{dt} = k_3 K_{C,1}K_{C,2}[NO]^2[O_2]^2
# \end{eqnarray}
# 
# We see that this rate law is second order in $O_2$ which is inconsistent with the experimentally determined rate law.  Thus, this mechanism is invalid.

# ## Types of Elementary Steps
# 
# The above example has a number of different types of elementary steps.  Here we describe them in terms of how many reactants must collide to produce products.  Elementary steps that involve one, two, and three reactant molecules are termed *unimolecular, bimolecular, and termolecular* respectively.  
# 
# The probability of having simultaneous collision between all reactants decreases with increasing molecularity.  No elementary step with a molecularity greater than three is known.  

# ### Unimolecular
# 
# Unimolecular elementary steps involve only one reactant.  In general these are written as 
# \begin{equation}
# A \Longrightarrow P
# \end{equation}
# 
# These types of reactions could be isomerizations (molecular reorganizations) or dissoications.  Since these types of reactions don't require collisions with other molecules they can happen rapidly.  The rate law for such elementary steps are first order and are written as
# \begin{equation}
# v = k[A]
# \end{equation}

# ### Bimolecular
# 
# Bimolecular elementary steps involve the collision of two reactantd.  In general these are written as 
# \begin{equation}
# A + B \Longrightarrow P
# \end{equation}
# 
# These types of reactions could be addition or replacement reactions. The rate law for such elementary steps are second order overall and are written as
# \begin{equation}
# v = k[A][B]
# \end{equation}

# ### Termolecular
# 
# Termolecular elementary steps involve the simultaneous collision of three reactants.  In general these are written as 
# \begin{equation}
# A + B + C \Longrightarrow P
# \end{equation}
# 
# These types of reactions could be addition or replacement reactions. The rate law for such elementary steps are third order overall and are written as
# \begin{equation}
# v = k[A][B][C]
# \end{equation}

#!/usr/bin/env python3
"""
Assignment 1 Problem 2

Drew Smith
PHZ 4151C
1/30/23
"""

# Constants
ENERGY = 10 # eV
POTENTIAL = 9 # eV
M = 9.11e-31 # kg
HBAR = 1.0546e-34 # J*s


def convert_to_joules(ev):
    """
    Converts energies in eV to Joules

    Parameters
    ---------
    eV : int
        The energy given in eV.
    
    Returns
    -------
    joules : float
        The energy converted to Joules.
    """
    joules = ev*1.6022e-19
    return joules

def compute_k(E, V):
    """
    Computes the k values from energies.

    Parameters
    ---------
    E : float
        Particle energy in Joules.
    
    V : float
        Potential energy in Joules.
    
    Returns
    -------
    (k_1, k_2) : tuple
        Tuple containing the calculated k values.
    """
    k_1 = ((2*M*E)**(1/2))/HBAR
    k_2 = ((2*M*(E-V))**(1/2))/HBAR
    return (k_1, k_2)

def compute_probabilities():
    """
    Computes the transmission and reflection probabilities.

    Parameters
    ---------
    None
    
    Returns
    -------
    None
    """
    k = compute_k(convert_to_joules(ENERGY), convert_to_joules(POTENTIAL))
    k_1 = k[0]
    k_2 = k[1]
    transmit_prob = (4*k_1*k_2)/((k_1 + k_2)**2)
    reflect_prob = ((k_1 - k_2)/(k_1 + k_2))**2
    print(f"Probability of transmission: {round(transmit_prob, 4)}\n" \
          f"Probability of reflection: {round(reflect_prob, 4)}")

compute_probabilities()

#!/usr/bin/env python3
"""
Assignment 1 Problem 3

Drew Smith
PHZ 4151C
1/30/23
"""

# Constants
A1 = 15.67 # MeV
A2 = 17.23 # MeV
A3 = 0.75 # MeV
A4 = 93.2 # MeV

def calculate_binding_energy():
    """
    Calculates the binding energy in meV of an atom.

    Parameters
    ---------
    None
    
    Returns
    -------
    None
    """
    while True:
        try:
            a = int(input("Enter the mass number A of the atom: "))
            z = int(input("Enter the atomic number Z of the atom: "))
        except:
            print('Invalid input given, please enter a number')
        else:
            break
    if z%2 == 0 and (a-z)%2 == 0:
        A5 = 12
    elif z%2 != 0 and (a-z)%2 != 0:
        A5 = -12
    else:
        A5 = 0
    energy = (A1*a - A2*(a)**(2/3)
              - A3*(z**2/a**(1/3)) 
              - A4*(a - 2*z)**2/a 
              + A5/(a**(1/2)))
    print(f"The binding energy of this atom is {round(energy, 2)} MeV")

calculate_binding_energy()

#!/usr/bin/env python3
"""
Assignment 1 Problem 1

Drew Smith
PHZ 4151C
1/30/23
"""

from math import pi

# Constants
G = 6.67e-11 # m^3/kg*s^2
M = 5.97e24 # kg
R = 6371e3 # m

# Take user input of period
while True:
    try:
        period = float(input("Enter the period T of the satellite: "))
    except:
        print('Invalid input given, please enter a number')
    else:
        break

def calculate_altitude(T):
    """
    Calculates the height of a satellite with a given orbital period.

    Parameters
    ---------
    T : float
        The period of orbit in seconds.
    
    Returns
    -------
    None
    """
    h = (G*M*(T**2)/4*(pi**2))**(1/3) - R
    if h > 0:
        print(f"The satellite has an altitude of {round(h)} meters.")
    elif h <= 0:
        print("Oops, a satellite cannot orbit with this period!")

calculate_altitude(period)

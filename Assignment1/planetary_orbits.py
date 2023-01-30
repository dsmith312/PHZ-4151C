#!/usr/bin/env python3
"""
Assignment 1 Problem 4

Drew Smith
PHZ 4151C
1/30/23
"""

from math import pi

# Constants
M_SUN = float(1.9891e30) # kg
G = float(6.6738e-11) # m^3*/kg*s^2

def calculate_v2(v1, l1):
    """
    Calculates velocity of the object at it's aphelion

    Parameters
    ---------
    v1 : float
        Velocity of object at it's perihelion.
    
    l1 : float
        Distance from object to the Sun at it's perihelion.
    
    Returns
    -------
    v2_plus : float
        One of the roots of the quadratic formula for v2.

        Returns this if it is the smaller value.
    
    v2_minus : float
        One of the roots of the quadratic formula for v2.

        Returns this if it is the smaller value.
    """
    a = 1
    b = -(2*G*M_SUN/(v1*l1))
    c = -(v1**2 - 2*G*M_SUN/l1)
    v2_plus = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    v2_minus = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
    if v2_plus < v2_minus:
        return v2_plus
    elif v2_minus < v2_plus:
        return v2_minus
    else:
        print("Equal roots")
        return v2_minus

def calculate_l2(v1, l1, v2):
    """
    Calculates the distance of the object to the Sun at it's aphelion.

    Parameters
    ---------
    v1: float
        Velocity of object at it's perihelion.

    l1 : float
        Distance from object to the Sun at it's perihelion.

    v2 : float
        Velocity of object at it's aphelion.
    
    Returns
    -------
    l1*v1/v2 : float
        Distance from object to the Sun at it's aphelion.
    """
    return l1*v1/v2

def calculate_period(v1, l1, l2):
    """
    Calculates the orbital period of the object in seconds.

    Parameters
    ---------
    v1: float
        Velocity of object at it's perihelion.

    l1 : float
        Distance from object to the Sun at it's perihelion.
    
    l2 : float
        Distance from object to the Sun at it's aphelion.
    
    Returns
    -------
    2*pi*major*minor/(l1*v1) : float
        Orbital period in seconds.
    """
    major = (l1 + l2)/2
    minor = (l1*l2)**(1/2)
    return 2*pi*major*minor/(l1*v1)

def calculate_eccentricity(l1, l2):
    """
    Calculates the orbital eccentricity of the object.

    Parameters
    ---------
    l1 : float
        Distance from object to the Sun at it's perihelion.
    
    l2 : float
        Distance from object to the Sun at it's aphelion.
    
    Returns
    -------
    (l2-l1)/(l2+l1) : float
        Object's orbital eccentricity.
    """
    return (l2-l1)/(l2+l1)

def planetary_properties():
    """
    Main function

    Prints the object's data calculated in other functions.

    Parameters
    ---------
    None
    
    Returns
    -------
    None
    """
    while True:
        try:
            l1 = float(input("Enter the object's distance from the Sun at it's perihelion: "))
            v1 = float(input("Enter the object's velocity at it's perihelion: "))
        except:
            print('Invalid input given, please enter a number')
        else:
            break
    print("Calculating planetary data...\n")
    v2 = calculate_v2(v1, l1)
    l2 = calculate_l2(v1, l1, v2)
    period = (calculate_period(v1, l1, l2))/(60*60*24*365)
    eccentricity = calculate_eccentricity(l1, l2)
    print(f"Object's distance at it's aphelion (m): {round(l2, 2)}\n" \
          f"Object's velocity at it's aphelion (m/s): {round(v2, 2)}\n" \
          f"Orbital period (yrs): {round(period)}\n" \
          f"Orbital eccentricity: {round(eccentricity, 4)}")

planetary_properties()

"""This class wil contain utilities for manipulating matrices"""

import numpy as np
import scipy as sc
from numpy import linalg as lanp
from scipy import linalg as lasc
from sympy import *

def hilbertIT(n):
    """ Iterative method of populating an nxn hilbert matrix
    Param:
        n : int
            square size of matrix

    Returns:
        H : matrix
            The hilbert matrix
    """

    H = np.asmatrix(np.identity(n),Rational)    #doesn't need to be an identity matrix

    for row in range(0,n):
        for col in range(0,n):
            H[row,col] = Rational(1,((row+1) + (col+1)-1))

    return H

def hilbertLA(n):
    """ Utilisise scipy.linalg for populating an nxn hilbert matrix
    Param:
        n : int
            square size of matrix

    Returns:
        H : matrix
            The hilbert matrix
    """
    return lasc.hilbert(n)

def condInf(m):
    """ Utilises numpy.linalg for calculating the cond of a matrix (using inf order norms)
    Param:
        m : matrix

    Returns:
        c : float
            The conditional number
    """
    return lanp.cond(m,np.inf)

def condInfIT(m):
    """ Iterative method for calculating the cond of a matrix (using inf order norms)
    Param:
        m : matrix

    Returns:
        c : float
            The conditional number
    """
    return normInfIT(m) * normInfIT(inverse(m))

def condEst(A,x,B):
    """ """
    return (normInf(A) * normInfIT(x))/normInf(B)

def condEstIT(A,x,B):
    """ """
    return ((normInfIT(A) * normInfIT(x))/normInfIT(B))

def normInf(m):
    """ Utilises numpy.linalg for calculating the norm of a matrix (inf order)
    Param:
        m : matrix

    Returns:
        c : float
            The norm
    """
    return lanp.norm(m, np.inf)

#could probably be optimised significantly
def normInfIT(m):
    """Iterative method for calculating the cond of a matrix (using inf order norms)
    Param:
        m : matrix

    Returns:
        c : float
            The conditional number
    """
    m = abs(m[:,:])
    res = np.ones(len(m))
    for i in range(0,len(m)):
        res[i] = np.sum(m[i,:])
    return max(res)

def normEuclid(v):
    """used for vectors(nx1)"""
    return lanp.norm(v)

def inverse(m):
    """ Utilises numpy.linalg for calculating the inverse of a matrix
        m : matrix
            Square Matrix

    Returns:
        mInv : matrix
            The inverse matrix
    """
    return lanp.inv(m)

def detLA(m):
    """ Utilises numpy.linalg for calculating the determinant of a matrix
    Param:
        m : matrix

    Returns:
        c : float
            The conditional number
    """
    return lanp.det(m)



def exportM(m):
    s = ""
    n = len(m)
    for row in range(0,n):
        for col in range(0,n):
           s += str(m[row,col])
           s += ";"

        s += ";"
    return s

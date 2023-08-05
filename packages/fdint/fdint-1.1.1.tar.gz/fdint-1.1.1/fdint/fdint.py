#
#   Copyright (c) 2015, Scott J. Maddox
#
#   This file is part of Fermi-Dirac Integrals (FDINT).
#
#   FDINT is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   FDINT is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with FDINT.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
'''
Precise and fast Fermi-Dirac integrals of integer and half integer order.
    
[1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral
    of integer and half integer order by piecewise minimax rational
    approximation," Applied Mathematics and Computation, vol. 259,
    pp. 708-729, May 2015.
'''
import fd
import numpy

__all__ = ['fd', 'fdk', 'dfdk']

def fdk(k, phi):
    '''
    Double precision Fermi-Dirac integral of order k.
    
    Parameters
    ----------
    k : float
        Order of the Fermi-Dirac integral.
    phi : float or iterable
        Normalized Fermi energy above the band edge, i.e. (Ef-Ec)/kT.
    
    Returns
    -------
    value : float or iterable
        Value of the Fermi-Dirac integral.
    
    Raises
    ------
    NotImplementedError
        If the particular order is not implemented.
    '''
    if hasattr(phi, '__iter__'):
        value, err = fd.vfdk2(int(k*2), phi)
    else:
        value, err = fd.fdk2(int(k*2), phi)
    if err:
        raise NotImplementedError()
    return value

def dfdk(k, phi, d=1):
    '''
    Double precision derivative of the Fermi-Dirac integral of order k.
    
    Parameters
    ----------
    k : float
        Order of the Fermi-Dirac integral.
    phi : float or iterable
        Normalized Fermi energy above the band edge, i.e. (Ef-Ec)/kT.
    d : int (default=1)
        Order of dirivative.
    
    Returns
    -------
    value : float or iterable
        Value of the Fermi-Dirac integral.
    
    Raises
    ------
    NotImplementedError
        If the particular order is not implemented.
    '''
    if hasattr(phi, '__iter__'):
        value, err = fd.vdfdk2(int(k*2), phi, d)
    else:
        value, err = fd.dfdk2(int(k*2), phi, d)
    if err:
        raise NotImplementedError()
    return value

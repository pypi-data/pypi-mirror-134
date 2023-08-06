# Copyright (C) 2022, Giorgio Comitini
#
# This file is part of PySmeQcd, the Python library for the Screened Massive
# Expansion of QCD
#
# PySmeQcd is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# PySmeQcd is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# PySmeQcd. If not, see <https://www.gnu.org/licenses/>.
#
"""
Library of functions and routines for the one-loop quark propagator computed in the Screened Massive Expansion.
"""

from numpy import cos, exp, log, pi, sqrt, conjugate
from scipy.optimize import root_scalar
import sys

from PySmeQcd import settings
from PySmeQcd.oneloop import oneloop_settings


#--- Functions for the one-loop quark self-energy ---#
def quark_t(s, x = oneloop_settings.x):
    r"""Function :math:`t(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return sqrt((x+s)**2+2*(s-x)+1)

def quark_R(s, x = oneloop_settings.x):
    r"""Function :math:`R(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return (quark_t(s,x)-s+x-1)/(quark_t(s,x)+s+x-1)

def quark_CR(s, x = oneloop_settings.x):
    r"""Function :math:`C_{R}(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return quark_t(s,x)/(2*s**2)*((x+s)**2+(x-s)-2)

def quark_Cx(s, x = oneloop_settings.x):
    r"""Function :math:`C_{x}(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -quark_CR(s,x)/2+1/(4*s**2)*((x+s)**3-3*(x-s)+2)

def quark_Cxs(s, x = oneloop_settings.x):
    r"""Function :math:`C_{xs}(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -(x+s)**3/(2*s**2)

def quark_C0(s, x = oneloop_settings.x):
    r"""Function :math:`C_{0}(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return (x-2)/(2*s)-1/2


#--- Derivatives ---#
def dquark_t(s, x = oneloop_settings.x):
    r"""Derivative of :math:`t(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return (x+s+1)/quark_t(s,x)

def dquark_tdx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`t(s)` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return (x+s-1)/quark_t(s,x)

def dquark_R(s, x = oneloop_settings.x):
    r"""Derivative of :math:`R(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return ((1-quark_R(s,x))*dquark_t(s,x)-1-quark_R(s,x))/(quark_t(s,x)+s+x-1)

def dquark_Rdx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`R(s)` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return (1-quark_R(s,x))*(dquark_tdx(s,x)+1)/(quark_t(s,x)+s+x-1)

def dquark_CR(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{R}(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -2*quark_CR(s,x)/s+dquark_t(s,x)/(2*s**2)*((x+s)**2+(x-s)-2)+quark_t(s,x)/s**2*(x+s-1/2)

def dquark_CRdx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{R}(s)` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return dquark_tdx(s,x)/(2*s**2)*((x+s)**2+(x-s)-2)+quark_t(s,x)/s**2*(x+s+1/2)

def dquark_Cx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{x}(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -dquark_CR(s,x)/2-1/(4*s**3)*(2*x**3+3*x**2*s-6*x-s**3+3*s+4)

def dquark_Cxdx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{x}(s)` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -dquark_CRdx(s,x)/2+3/(4*s**2)*((x+s)**2-1)

def dquark_Cxs(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{xs}(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return (x+s)**2/(2*s**3)*(2*x-s)

def dquark_Cxsdx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{xs}(s)` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -3*(x+s)**2/(2*s**2)

def dquark_C0(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{0}(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return -(x-2)/(2*s**2)

def dquark_C0dx(s, x = oneloop_settings.x):
    r"""Derivative of :math:`C_{0}(s)` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
"""
    return 1/(2*s)


#--- One-loop quark self-energy ---#
def quark_SigV1(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Function :math:`\Sigma_{V}^{(1)}(p^{2})` -- vector component of the 1-loop self-energy uncrossed term.

Modulo a factor of :math:`\frac{\alpha_{s}}{3\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    res=quark_CR(s,x)*log(quark_R(s,x))+quark_Cx(s,x)*log(x)+quark_Cxs(s,x)*log(x/(x+s))+quark_C0(s,x)
    if xi != 0:
        res +=-xi*(2-(s+x)/s*(1+(s-x)/s*log((s+x)/x)))
    return res

def quark_SigS1(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Function :math:`\Sigma_{S}^{(1)}(p^{2})` -- scalar component of the 1-loop self-energy uncrossed term.

Modulo a factor of :math:`M\frac{\alpha_{s}}{\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    res=quark_t(s,x)/s*log(quark_R(s,x))-(quark_t(s,x)+s-x+1)/(2*s)*log(x)+log(x)
    if xi != 0:
        res *=xi/3*(2-(s+x)/s*log((s+x)/x))
    return res

def dquark_SigV1(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Derivative of :python:`quark_SigV1` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    p11=dquark_CR(s,x)*log(quark_R(s,x))+dquark_Cx(s,x)*log(x)+dquark_Cxs(s,x)*log(x/(x+s))+dquark_C0(s,x)
    p12=quark_CR(s,x)/quark_R(s,x)*dquark_R(s,x)-quark_Cxs(s,x)/(x+s)
    res = p11 + p12
    if xi != 0:
        res += -xi*(2*x/s**2-1/s-2*x/s**3*log((s+x)/x))
    return res

def dquark_SigV1dx(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Derivative of :python:`quark_SigV1` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    p11=dquark_CRdx(s,x)*log(quark_R(s,x))+dquark_Cxdx(s,x)*log(x)+dquark_Cxsdx(s,x)*log(x/(x+s))+dquark_C0dx(s,x)
    p12=quark_CR(s,x)/quark_R(s,x)*dquark_Rdx(s,x)+quark_Cx(s,x)/x+quark_Cxs(s,x)*s/(x*(x+s))
    res = p11 + p12
    if xi != 0:
        res += -xi*(1/x-2/s+2*x/s**2*log((s+x)/x))
    return res

def dquark_SigS1(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Derivative of :python:`quark_SigS1` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    p11=(dquark_t(s,x)-quark_t(s,x)/s)/s*log(quark_R(s,x))+quark_t(s,x)/s*dquark_R(s,x)/quark_R(s,x)
    p12=-(dquark_t(s,x)/(2*s)-quark_t(s,x)/(2*s**2)+(x-1)/(2*s**2))*log(x)
    res = p11 + p12
    if xi != 0:
        res += xi/3*(x/s**2*log((s+x)/x)-1/s)
    return res

def dquark_SigS1dx(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Derivative of :python:`quark_SigS1` with respect to :python:`x`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    p11=(dquark_tdx(s,x)*log(quark_R(s,x))+quark_t(s,x)*dquark_Rdx(s,x)/quark_R(s,x))/s-(dquark_tdx(s,x)-1)/(2*s)*log(x)
    p12=-(quark_t(s,x)+s-x+1)/(2*s)/x+1/x
    res = p11 + p12
    if xi != 0:
        res += xi/3*(-log((s+x)/x)/s+1/x)
    return res

def quark_SigV2(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Function :math:`\Sigma_{V}^{(2)}(p^{2})` -- vector component of the 1-loop self-energy uncrossed + quark-crossed terms.

Modulo a factor of :math:`\frac{\alpha_{s}}{3\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    res = quark_SigV1(s,x,xi)-2*x*dquark_SigV1dx(s,x,xi)
    if xi != 0:
        res += -2*xi
    return res

def quark_SigS2(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Function :math:`\Sigma_{S}^{(2)}(p^{2})` -- scalar component of the 1-loop self-energy uncrossed + quark-crossed terms.

Modulo a factor of :math:`M\frac{\alpha_{s}}{\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    res = -2*x*dquark_SigS1dx(s,x,xi)+2
    if xi != 0:
        res += 2/3*xi
    return res

def quark_SigVgl(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Function :math:`\Sigma_{V}^{(gl)}(p^{2})` -- vector component of the 1-loop self-energy gluon-crossed term.

Modulo a factor of :math:`\frac{\alpha_{s}}{3\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    return s*dquark_SigV1(s,x,xi)+x*dquark_SigV1dx(s,x,xi)

def quark_SigSgl(s, x = oneloop_settings.x, xi = settings.xi):
    r"""Function :math:`\Sigma_{S}^{(gl)}(p^{2})` -- scalar component of the 1-loop self-energy gluon-crossed term.

Modulo a factor of :math:`M\frac{\alpha_{s}}{\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
"""
    return s*dquark_SigS1(s,x,xi)+x*dquark_SigS1dx(s,x,xi)

def quark_SigV(s, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Function :math:`\Sigma_{V}(p^{2})` -- vector component of the 1-loop self-energy.

Modulo a factor of :math:`\frac{\alpha_{s}}{3\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    if type != 'cc':
        res = quark_SigV2(s,x,xi)
        if type=='vw':
            res += quark_SigVgl(s,x,xi)
        return res
    else:
        res = (exp(1j*phi)*quark_SigV2(s/p02,x/p02,xi)+exp(-1j*phi)*quark_SigV2(s/conjugate(p02),x/conjugate(p02),xi))/(2*cos(phi))
        if Zglue != 1:
            res *= Zglue
        if s.imag == 0:
            return res.real
        else:
            return res

def quark_SigS(s, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Function :math:`\Sigma_{S}(p^{2})` -- scalar component of the 1-loop self-energy.

Modulo a factor of :math:`M\frac{\alpha_{s}}{\pi}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    if type != 'cc':
        res = quark_SigS2(s,x,xi)
        if type == 'vw':
            res += quark_SigSgl(s,x,xi)
        return res
    else:
        res = (exp(1j*phi)*quark_SigS2(s/p02,x/p02,xi)+exp(-1j*phi)*quark_SigS2(s/conjugate(p02),x/conjugate(p02),xi))/(2*cos(phi))
        if Zglue != 1:
            res *= Zglue
        if s.imag == 0:
            return res.real
        else:
            return res


#--- One-loop quark propagator ---#
def quark_A(s, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Function :math:`A(p^{2})`.

Modulo a factor of :math:`\frac{\alpha_{s}}{3\pi}`.

:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    return H0-quark_SigV(s,x,xi,type,p02,phi,Zglue)

def quark_B(s, K0 = oneloop_settings.K0, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Function :math:`B(p^{2})`.

Modulo a factor of :math:`M\frac{\alpha_{s}}{\pi}`.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    return K0+quark_SigS(s,x,xi,type,p02,phi,Zglue)

def quark_Z(s, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02, phi = oneloop_settings.phi,
    Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m):
    r"""Quark :math:`Z`-function :math:`Z(p^{2})`.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the :math:`Z`-function
:param Z: if :python:`None`, renormalize the :math:`Z`-function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the :math:`Z`-function in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        res = 1/quark_A(s/m**2,H0,x,xi,type,p02,phi,Zglue)
    else:
        res = 1/quark_A(s,H0,x,xi,type,p02,phi,Zglue)
    if ren:
        if Z == None:
            Z = quark_A(mu0**2,H0,x,xi,type,p02,phi,Zglue)
        res *= Z
    return res

def quark_M(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue,
    dimensionful = False, m = oneloop_settings.m):
    r"""Quark mass function :math:`\mathcal{M}(p^{2})`.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the mass function by dividing it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        return 3*m*sqrt(x)*quark_B(s/m**2,K0,x,xi,type,p02,phi,Zglue)/quark_A(s/m**2,H0,x,xi,type,p02,phi,Zglue)
    else:
        return 3*sqrt(x)*quark_B(s,K0,x,xi,type,p02,phi,Zglue)/quark_A(s,H0,x,xi,type,p02,phi,Zglue)

def quark_Q(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue,
    dimensionful = False, m = oneloop_settings.m):
    r"""Function :math:`p^{2}+\mathcal{M}^{2}(p^{2})`.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the function by dividing it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    return s+quark_M(s,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m)**2

def quark_propV(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, ren = True, Z = None, mu0 = settings.mu0,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue,
    dimensionful = False, m = oneloop_settings.m):
    r"""Vector component of the quark propagator :math:`S_{V}(p^{2})`.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}.`

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)"""
    return quark_Z(s,H0,x,xi,type,ren,Z,mu0,p02,phi,Zglue,dimensionful,m)/quark_Q(s,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m)

def quark_propS(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m):
    r"""Scalar component of the quark propagator :math:`S_{S}(p^{2})`.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}.`

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)"""
    return quark_propV(s,K0,H0,x,xi,type,ren,Z,mu0,p02,phi,Zglue,dimensionful,m)*quark_M(s,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m)

def quark_spectralV(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m):
    r"""Vector component of the quark spectral function :math:`\rho_{S_{V}}(p^{2})` in Minkowski space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}.` The :math:`\varepsilon` for the difference across the branch cut is defined in the :python:`PySmeQcd.settings` module.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the spectral function
:param Z: if :python:`None`, renormalize the spectral function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the spectral function in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the spectral function by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful Minkowski momentum squared :math:`p^{2}_{M}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        step_h = m**2*settings.step_h
    else:
        step_h = settings.step_h
    res = 2*quark_propV(-s-1j*step_h,K0,H0,x,xi,type,ren,Z,mu0,p02,phi,Zglue,dimensionful,m)
    return res.imag

def quark_spectralS(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m):
    r"""Scalar component of the quark spectral function :math:`\rho_{S_{S}}(p^{2})` in Minkowski space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}.` The :math:`\varepsilon` for the difference across the branch cut is defined in the :python:`PySmeQcd.settings` module.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the spectral function
:param Z: if :python:`None`, renormalize the spectral function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the spectral function in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the spectral function by multiplying it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful Minkowski momentum squared :math:`p^{2}_{M}`
"""
    if dimensionful:
        step_h = m**2*settings.step_h
    else:
        step_h = settings.step_h
    res = 2*quark_propS(-s-1j*step_h,K0,H0,x,xi,type,ren,Z,mu0,p02,phi,Zglue,dimensionful,m)
    return res.imag


#--- More derivatives ---#
def dquark_SigV(s, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Numerical derivative of :python:`quark_SigV` with respect to :python:`s`.

The :math:`\varepsilon` for the finite difference is defined in the :python:`PySmeQcd.settings` module.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    return (quark_SigV(s+settings.step_h,x,xi,type,p02,phi,Zglue)-quark_SigV(s-settings.step_h,x,xi,type,p02,phi,Zglue))/(2*settings.step_h)

def dquark_SigS(s, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Numerical derivative of :python:`quark_SigS` with respect to :python:`s`.

The :math:`\varepsilon` for the finite difference is defined in the :python:`PySmeQcd.settings` module.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    return (quark_SigS(s+settings.step_h,x,xi,type,p02,phi,Zglue)-quark_SigS(s-settings.step_h,x,xi,type,p02,phi,Zglue))/(2*settings.step_h)

def dquark_A(s, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Numerical derivative of :python:`quark_A` with respect to :python:`s`.

The :math:`\varepsilon` for the finite difference is defined in the :python:`PySmeQcd.settings` module.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    return -dquark_SigV(s,x,xi,type,p02,phi,Zglue)

def dquark_B(s, x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue):
    r"""Numerical derivative of :python:`quark_B` with respect to :python:`s`.

The :math:`\varepsilon` for the finite difference is defined in the :python:`PySmeQcd.settings` module.

:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
"""
    return dquark_SigS(s,x,xi,type,p02,phi,Zglue)

def dquark_M(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, p02 = oneloop_settings.p02, phi = oneloop_settings.phi,
    Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m):
    r"""Numerical derivative of :python:`quark_M` with respect to :python:`s`.

The :math:`\varepsilon` for the finite difference is defined in the :python:`PySmeQcd.settings` module.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the derivative by multiplying it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        m2 = m**2
        p1 = quark_A(s/m2,H0,x,xi,type,p02,phi,Zglue)
        return (3/m)*sqrt(x)*(dquark_B(s/m2,x,xi,type,p02,phi,Zglue)-quark_B(s/m2,K0,x,xi,type,p02,phi,Zglue)*dquark_A(s/m2,x,xi,type,p02,phi,Zglue)/p1)/p1
    else:
        p1 = quark_A(s,H0,x,xi,type,p02,phi,Zglue)
        return 3*sqrt(x)*(dquark_B(s,x,xi,type,p02,phi,Zglue)-quark_B(s,K0,x,xi,type,p02,phi,Zglue)*dquark_A(s,x,xi,type,p02,phi,Zglue)/p1)/p1

def dquark_Q(s, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, p02 = oneloop_settings.p02, phi = oneloop_settings.phi,
    Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m):
    r"""Numerical derivative of :python:`quark_Q` with respect to :python:`s`.

The :math:`\varepsilon` for the finite difference is defined in the :python:`PySmeQcd.settings` module.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    return 1+2*quark_M(s,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m)*dquark_M(s,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m)


#--- Parameter conversion ---#
def quark_MB(K0 = oneloop_settings.K0, H0 = oneloop_settings.H0):
    r"""Quark bare mass :math:`M_{B}` from :math:`K_{0}` and :math:`H_{0}`.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
"""
    return 3*K0/H0

def quark_H0(Zpsi, a_s):
    r"""Quark :math:`H_{0}` parameter from :math:`Z_{\psi}` and :math:`\alpha_{s}`.

:param Zpsi: quark field-strength renormalization factor :math:`Z_{\psi}`
:param a_s: strong coupling constant :math:`\alpha_{s}=\frac{g^{2}}{4\pi}`
"""
    return 3*pi*Zpsi/a_s

def quark_K0(Zpsi, a_s, MB):
    r"""Quark :math:`K_{0}` parameter from :math:`Z_{\psi}` and :math:`\alpha_{s}`.

:param Zpsi: quark field-strength renormalization factor :math:`Z_{\psi}`
:param a_s: strong coupling constant :math:`\alpha_{s}=\frac{g^{2}}{4\pi}`
:param MB: quark bare mass :math:`M_{B}`
"""
    return pi*MB*Zpsi/a_s


#--- Quark Propagator Poles and Residues ---#
def quark_pole(K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x, xi = settings.xi,
    type = oneloop_settings.quarktype, p02 = oneloop_settings.p02, phi = oneloop_settings.phi,
    Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m, stp = settings.stp):
    r"""Pole of the quark propagator in Euclidean space.

If the pole cannot be found, prints to :console:`stderr` and raises a :python:`RuntimeError`.

:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the pole by dividing it by :python:`m`\ :sup:`2`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param stp: starting point for the root-finding algorithm
"""
    sol=root_scalar(lambda s: quark_Q(s,K0,H0,x,xi,type,p02,phi,Zglue,False,m), fprime = lambda s: dquark_Q(s,K0,H0,x,xi,type,p02,phi,Zglue,False,m), x0=stp, method="newton")
    if sol.converged:
        if dimensionful:
            return sol.root*m**2
        else:
            return sol.root
    else:
        if type != 'cc':
            print("quark_pole parameters: K0 =",K0,"H0 =",H0,"x =",x,"xi =",xi,"type =",type,"stp =",stp,file=sys.stderr)
        else:
            print("quark_pole parameters: K0 =",K0,"H0 =",H0,"x =",x,"xi =",xi,"type =",type,"p02 =",p02,"phi =",phi,"Zglue =",Zglue,"stp =",stp,file=sys.stderr)
        raise RuntimeError("quark_pole did not converge! Function value = "+str(quark_Q(sol.root,K0,H0,x,xi,type,p02,phi)))

def quark_residue(pole = None, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0, x = oneloop_settings.x,
    xi = settings.xi, type = oneloop_settings.quarktype, ren = True, Z = None, mu0 = settings.mu0,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue,
    dimensionful = False, m = oneloop_settings.m, stp = settings.stp):
    r"""Residue of the vector component of the quark propagator at its pole.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param pole: if :python:`None`, compute the pole before computing its residue (recommended); else use :python:`pole` as the Euclidean pole. See below for dimensions
:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the residue
:param Z: if :python:`None`, renormalize the residue in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the residue in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`True`, :python:`pole` is passed dimensionful (only if :python:`pole!=None`)
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param stp: starting point for the root-finding algorithm (only if :python:`pole=None`)
"""
    if pole==None:
        pole=quark_pole(K0,H0,x,xi,type,p02,phi,Zglue,False,m,stp)
    return quark_Z(pole,H0,x,xi,type,ren,Z,mu0,p02,phi,Zglue,dimensionful,m)/dquark_Q(pole,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m)


#--- Plots ---#
def quark_Z_plot(s = [0,25], N_s = 1000, H0 = oneloop_settings.H0, x = oneloop_settings.x,
    xi = settings.xi, type = oneloop_settings.quarktype, ren = True, Z = None, mu0 = settings.mu0,
    p02 = oneloop_settings.p02, phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = True, outf = None):
    r"""Plots the quark :math:`Z`-function in Euclidean space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the :math:`Z`-function
:param Z: if :python:`None`, renormalize the :math:`Z`-function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the :math:`Z`-function in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    Y=[quark_Z(ss,H0,x,xi,type,False,Z,mu0,p02,phi,Zglue,dimensionful,m) for ss in X]
    if ren:
        if Z == None:
            Z = quark_A(mu0**2,H0,x,xi,type,p02,phi,Zglue)
        Y = [y*Z for y in Y]
    if dimensionful:
        xlbl = r"$p^{2}$"
        ylbl = r"$Z(p^{2})$"
    else:
        xlbl = r"$p^{2}/m^{2}$"
        ylbl = r"$Z(p^{2}/m^{2})$"
    plt.figure()
    plt.plot(X,Y)
    if scale == 'log':
        plt.xscale('log')
    if title:
        plt.title(r"Quark $Z$-function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf == None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def quark_M_plot(s = [0,25], N_s = 1000, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0,
    x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = True, outf = None):
    r"""Plots the quark mass function in Euclidean space.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the mass function by dividing it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    Y=[quark_M(ss,K0,H0,x,xi,type,p02,phi,Zglue,dimensionful,m) for ss in X]
    if dimensionful:
        xlbl = r"$p^{2}$"
        ylbl = r"$\mathcal{M}(p^{2})$"
    else:
        xlbl = r"$p^{2}/m^{2}$"
        ylbl = r"$\mathcal{M}(p^{2}/m^{2})/m$"
    plt.figure()
    plt.plot(X,Y)
    if scale == 'log':
        plt.xscale('log')
    if title:
        plt.title(r"Quark mass function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf == None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def quark_propV_plot(s = [0,25], N_s = 1000, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0,
    x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False,
    m = oneloop_settings.m, scale = "log", title = True, outf = None):
    r"""Plots the vector component of the quark propagator in Euclidean space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[(s[0]+ds*k) for k in range(N_s+1) if s[0]+ds*k!=0]
    Y=[quark_propV(ss,K0,H0,x,xi,type,False,Z,mu0,p02,phi,Zglue,dimensionful,m) for ss in X]
    if ren:
        if Z == None:
            Z = quark_A(mu0**2,H0,x,xi,type,p02,phi,Zglue)
        Y = [y*Z for y in Y]
    if dimensionful:
        xlbl = r"$p^{2}$"
        ylbl = r"$S_{V}(p^{2})$"
    else:
        xlbl = r"$p^{2}/m^{2}$"
        ylbl = r"$m^{2}S_{V}(p^{2}/m^{2})$"
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Vector component of the quark propagator")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def quark_propS_plot(s = [0,25], N_s = 1000, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0,
    x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False,
    m = oneloop_settings.m, scale = "log", title = True, outf = None):
    r"""Plots the scalar component of the quark propagator in Euclidean space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[(s[0]+ds*k) for k in range(N_s+1) if s[0]+ds*k!=0]
    Y=[quark_propS(ss,K0,H0,x,xi,type,False,Z,mu0,p02,phi,Zglue,dimensionful,m) for ss in X]
    if ren:
        if Z == None:
            Z = quark_A(mu0**2,H0,x,xi,type,p02,phi,Zglue)
        Y = [y*Z for y in Y]
    if dimensionful:
        xlbl = r"$p^{2}$"
        ylbl = r"$S_{S}(p^{2})$"
    else:
        xlbl = r"$p^{2}/m^{2}$"
        ylbl = r"$m S_{S}(p^{2}/m^{2})$"
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Scalar component of the quark propagator")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def quark_spectralV_plot(s = [0,25], N_s = 1000, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0,
    x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False,
    m = oneloop_settings.m, scale = "log", title = True, outf = None):
    r"""Plots the vector component of the quark spectral function in Minkowski space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param s: a two-element list containing the minimum and maximum Minkowski momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the spectral function
:param Z: if :python:`None`, renormalize the spectral function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the spectral function in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the spectral function by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful Minkowski momentum squared :math:`p^{2}_{M}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[(s[0]+ds*k) for k in range(N_s+1) if s[0]+ds*k!=0]
    Y=[quark_spectralV(ss,K0,H0,x,xi,type,False,Z,mu0,p02,phi,Zglue,dimensionful,m) for ss in X]
    if ren:
        if Z == None:
            Z = quark_A(mu0**2,H0,x,xi,type,p02,phi,Zglue)
        Y = [y*Z for y in Y]
    if dimensionful:
        xlbl = r"$p^{2}$"
        ylbl = r"$\rho_{S_{V}}(p^{2})$"
    else:
        xlbl = r"$p^{2}/m^{2}$"
        ylbl = r"$m^{2}\rho_{S_{V}}(p^{2}/m^{2})$"
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Vector component of the quark spectral function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def quark_spectralS_plot(s = [0,25], N_s = 1000, K0 = oneloop_settings.K0, H0 = oneloop_settings.H0,
    x = oneloop_settings.x, xi = settings.xi, type = oneloop_settings.quarktype,
    ren = True, Z = None, mu0 = settings.mu0, p02 = oneloop_settings.p02,
    phi = oneloop_settings.phi, Zglue = oneloop_settings.Zglue, dimensionful = False,
    m = oneloop_settings.m, scale = "log", title = True, outf = None):
    r"""Plots the scalar component of the quark spectral function in Minkowski space.

Modulo a factor of :math:`\frac{3\pi}{\alpha_{s}}`.

:param s: a two-element list containing the minimum and maximum Minkowski momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param K0: normalized and adimensionalized quark bare mass :math:`K_{0}/M`
:param H0: additive renormalization constant :math:`H_{0}`
:param x: adimensional quark chiral mass squared :math:`x`
:param xi: gauge parameter :math:`\xi`
:param type: diagram selector: :python:`'ms'` if only the ordinary and quark-crossed loops are included, :python:`'vw'` if also the gluon-crossed loop is included; :python:`'cc'` for the c.c. scheme
:param ren: if :python:`True`, multiplicatively renormalize the spectral function
:param Z: if :python:`None`, renormalize the spectral function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the spectral function in the MOM scheme (only if :python:`ren=True`)
:param p02: pole of the gluon propagator in Minkowski space (c.c. scheme only)
:param phi: phase :math:`\varphi` of the residue of the gluon propagator at the pole :python:`p02` (c.c. scheme only)
:param Zglue: renormalization factor for the internal gluon line (c.c. scheme only)
:param dimensionful: if :python:`False`, adimensionalize the spectral function by multiplying it by :python:`m`; if :python:`True`, :python:`s` is the dimensionful Minkowski momentum squared :math:`p^{2}_{M}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[(s[0]+ds*k) for k in range(N_s+1) if s[0]+ds*k!=0]
    Y=[quark_spectralS(ss,K0,H0,x,xi,type,False,Z,mu0,p02,phi,Zglue,dimensionful,m) for ss in X]
    if ren:
        if Z == None:
            Z = quark_A(mu0**2,H0,x,xi,type,p02,phi,Zglue)
        Y = [y*Z for y in Y]
    if dimensionful:
        xlbl = r"$p^{2}$"
        ylbl = r"$\rho_{S_{S}}(p^{2})$"
    else:
        xlbl = r"$p^{2}/m^{2}$"
        ylbl = r"$m \rho_{S_{S}}(p^{2}/m^{2})$"
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Scalar component of the quark spectral function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

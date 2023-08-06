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
r"""
Library of functions and routines for the one-loop gluon propagator computed in the Screened Massive Expansion.
"""

from numpy import log, sqrt
from scipy.optimize import root_scalar
import sys

from PySmeQcd import settings
from PySmeQcd.oneloop import oneloop_settings


#--- Functions for the one-loop gluon propagator ---#
def gluon_F(s):
    r"""Function :math:`F(s)` -- 1-loop pure Yang-Mills Landau gauge term for the gluon polarization."""
    la=sqrt((4+s)/s)*(3*s**3-34*s**2-28*s-24)*log((sqrt(4+s)-sqrt(s))/(sqrt(4+s)+sqrt(s)))/s
    ra=-(4+s)/s*(s**2-20*s+12)
    lb=2*(1+s)**2/s**3*(3*s**3-20*s**2+11*s-2)*log(1+s)
    rb=2*(1+s)**2/s**2*(s**2-10*s+1)
    return (2-s**2+2/s**2+(2-3*s**2)*log(s)+la+ra+lb+rb)/72+5/(8*s)

def gluon_F_xi(s):
    r"""Function :math:`F_{\xi}(s)` -- 1-loop pure Yang-Mills gauge term for the gluon polarization."""
    p1=2*s*log(s)-2*(1-s)*(1-s**3)/s**3*log(1+s)
    p2=(3*s**2-3*s+2)/s**2
    return 1/(4*s)-(p1+p2)/12

def gluon_F_Q(s, x = oneloop_settings.x, N = settings.N):
    r"""Function :math:`F_{Q}(s)` -- 1-loop *uncrossed* quark term for the gluon polarization.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`"""
    p1=sqrt((s+4*x)/s)*(1-2*x/s)*log((sqrt(s+4*x)+sqrt(s))/((sqrt(s+4*x)-sqrt(s))))
    p2=-5/3+4*x/s
    return -2*(p1+p2)/(9*N)


#--- Derivatives ---#
def dgluon_F(s):
    r"""Derivative of :math:`F(s)` with respect to :python:`s`."""
    la=(6*s**4-16*s**3-68*s**2+80*s+144)/(s**2*(s+4))*sqrt((s+4)/s)*log((sqrt(s+4)-sqrt(s))/((sqrt(s+4)+sqrt(s))))
    lb=4*(1+s)/s**4*(3*s**4-10*s**3+10*s**2-10*s+3)*log(1+s)
    lc=-6*s*log(s)
    r=12/s+106/s**2-12/s**3
    return (la+lb+lc+r)/72-5/(8*s**2)

def dgluon_F_xi(s):
    r"""Derivative of :math:`F_{\xi}(s)` with respect to :python:`s`."""
    p1=(s**4+2*s-3)/(6*s**4)*log(1+s)-log(s)/6
    p2=(1-s)*(1-s**3)/(6*s**3*(1+s))+1/(3*s**3)-1/(2*s**2)-1/6
    return p1+p2

def dgluon_F_Q(s, x = oneloop_settings.x, N = settings.N):
    r"""Derivative of :math:`F_{Q}(s)` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`"""
    return -2*(12*x**2/s**3*sqrt(s/(s+4*x))*log((sqrt(s+4*x)+sqrt(s))/((sqrt(s+4*x)-sqrt(s))))+1/s-6*x/s**2)/(9*N)

def dgluon_F_Qdx(s, x = oneloop_settings.x, N = settings.N):
    r"""Derivative of :math:`F_{Q}(s)` with respect to :python:`x`.

Proportional to :math:`F_{Q}^{(cr)}(s)`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`"""
    return 2*(12*x/(s**2*sqrt((s+4*x)/s))*log((sqrt(s+4*x)+sqrt(s))/((sqrt(s+4*x)-sqrt(s))))+1/x-6/s)/(9*N)

def dgluon_F_Qdxds(s, x = oneloop_settings.x, N = settings.N):
    r"""Second derivative of :math:`F_{Q}(s)` with respect to :python:`x` and :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
"""
    return 2*(-24*x*(s+3*x)/(s**3*(s+4*x)*sqrt((s+4*x)/s))*log((sqrt(s+4*x)+sqrt(s))/((sqrt(s+4*x)-sqrt(s))))+12*x/(s**2*(s+4*x))+6/s**2)/(9*N)


#--- One-loop gluon propagator ---#
def gluon_J_inv(s, x = oneloop_settings.x, N = settings.N, xi = settings.xi, F0 = oneloop_settings.F0,
    Nf = settings.Nf, type = oneloop_settings.gluetype):
    r"""Inverse gluon dressing function :math:`J^{-1}(s).`

Modulo a factor of :math:`\alpha`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
"""
    res = gluon_F(s) + F0
    if xi != 0:
        res += xi*gluon_F_xi(s)
    if Nf != 0:
        res += Nf*gluon_F_Q(s,x,N)
        if type == "cr":
            res += -2*Nf*x*dgluon_F_Qdx(s,x,N)
    return res

def gluon_J(s, x = oneloop_settings.x, N = settings.N, xi = settings.xi, F0 = oneloop_settings.F0,
    Nf = settings.Nf, type = oneloop_settings.gluetype):
    r"""Gluon dressing function :math:`J(s).`

Modulo a factor of :math:`\alpha^{-1}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
"""
    return 1/gluon_J_inv(s,x,N,xi,F0,Nf,type)

def dgluon_J_inv(s, x = oneloop_settings.x, N = settings.N, xi = settings.xi, Nf = settings.Nf,
    type = oneloop_settings.gluetype):
    r"""Derivative of :python:`gluon_J_inv` with respect to :python:`s`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
"""
    res = dgluon_F(s)
    if xi != 0:
        res += xi*dgluon_F_xi(s)
    if Nf != 0:
        res += Nf*dgluon_F_Q(s,x,N)
        if type == "cr":
            res += -2*Nf*x*dgluon_F_Qdxds(s,x,N)
    return res

def gluon_prop(s, x = oneloop_settings.x, N = settings.N, xi = settings.xi,
    F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype, ren = True,
    Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m):
    r"""Gluon propagator :math:`\Delta(p^{2})`.

Modulo a factor of :math:`\alpha^{-1}`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        res = 1/(gluon_J_inv(s/m**2,x,N,xi,F0,Nf,type)*s)
    else:
        res = 1/(gluon_J_inv(s,x,N,xi,F0,Nf,type)*s)
    if ren == True:
        if Z != None:
            res *= Z
        else:
            res *= gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
    return res

def gluon_spectral(s, x = oneloop_settings.x, N = settings.N, xi = settings.xi,
    F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype, ren = True,
    Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m):
    r"""Gluon spectral function :math:`\rho_{\Delta}(p^{2})` in Minkowski space.

Modulo a factor of :math:`\alpha^{-1}`. The :math:`\varepsilon` for the difference across the branch cut is defined in the :python:`PySmeQcd.settings` module.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param ren: if :python:`True`, multiplicatively renormalize the spectral function
:param Z: if :python:`None`, renormalize the spectral function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the spectral function in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`False`, adimensionalize the spectral function by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful Minkowski momentum squared :math:`p^{2}_{M}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        step_h = m**2*settings.step_h
    else:
        step_h = settings.step_h
    res = 2*gluon_prop(-s-1j*step_h,x,N,xi,F0,Nf,type,ren,Z,mu0,dimensionful,m)
    return res.imag


#--- Gluon propagator poles and residues ---#
def gluon_pole(x = oneloop_settings.x, N = settings.N, xi = settings.xi, F0 = oneloop_settings.F0,
    Nf = settings.Nf, type = oneloop_settings.gluetype, dimensionful = False,
    m = oneloop_settings.m, stp = settings.stp):
    r"""Pole :math:`p_{0}^{2}` of the gluon propagator in Euclidean space.

If the pole cannot be found, prints to :console:`stderr` and raises a :python:`RuntimeError`.

:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param dimensionful: if :python:`False`, adimensionalize the pole by dividing it by :python:`m`\ :sup:`2`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param stp: starting point for the root-finding algorithm
"""
    sol=root_scalar(lambda s: gluon_J_inv(s,x,N,xi,F0,Nf,type), fprime = lambda s: dgluon_J_inv(s,x,N,xi,Nf,type), x0 = stp, method = "newton")
    if sol.converged:
        if dimensionful:
            return sol.root*m**2
        else:
            return sol.root
    else:
        print("gluon_pole parameters: x =",x,"N =",N,"xi =",xi,"F0 =",F0,"Nf =",Nf,"type =",type,"stp =",stp,file=sys.stderr)
        raise RuntimeError("gluon_pole did not converge! Function value = "+str(gluon_J_inv(sol.root,x,N,xi,F0,Nf,type)))

def gluon_residue(pole = None, x = oneloop_settings.x, N = settings.N,
    xi = settings.xi, F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m, stp = settings.stp):
    r"""Residue :math:`R` of the gluon propagator at its pole.

Modulo a factor of :math:`\alpha^{-1}`.

:param pole: if :python:`None`, compute the pole :math:`p_{0}^{2}` before computing its residue (recommended); else use :python:`pole` as the Euclidean pole. See below for dimensions
:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param ren: if :python:`True`, multiplicatively renormalize the residue
:param Z: if :python:`None`, renormalize the residue in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the residue in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`True`, :python:`pole` is passed dimensionful (only if :python:`pole!=None`)
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param stp: starting point for the root-finding algorithm (only if :python:`pole=None`)
"""
    if pole == None:
        pole = gluon_pole(x,N,xi,F0,Nf,type,False,m,stp)
    if dimensionful:
        res = m**2/(dgluon_J_inv(pole/m**2,x,N,xi,Nf,type)*pole)
    else:
        res = 1/(dgluon_J_inv(pole,x,N,xi,Nf,type)*pole)
    if ren:
        if Z == None:
            Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
        res *= Z
    return res


#--- Plots ---#
def gluon_J_plot(s = [0,25], N_s = 1000, x = oneloop_settings.x, N = settings.N, xi = settings.xi,
    F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype, inverse = False,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = True, outf = None):
    r"""Plots the gluon dressing function in Euclidean space.

Modulo a factor of :math:`\alpha^{-1}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param inverse: if :python:`True`, plot the inverse dressing function
:param ren: if :python:`True`, multiplicatively renormalize the dressing function
:param Z: if :python:`None`, renormalize the dressing function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the dressing function in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    if inverse:
        if dimensionful:
            m2 = m**2
            Y=[gluon_J_inv(ss/m2,x,N,xi,F0,Nf,type) for ss in X]
            ylbl = r"$J^{-1}(p^{2})$"
            xlbl = r"$p^{2}$"
        else:
            Y=[gluon_J_inv(ss,x,N,xi,F0,Nf,type) for ss in X]
            ylbl = r"$J^{-1}(p^{2}/m^{2})$"
            xlbl = r"$p^{2}/m^{2}$"
        if ren:
            if Z == None:
                Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
            Y=[y/Z for y in Y]
    else:
        if dimensionful:
            m2 = m**2
            Y=[1/gluon_J_inv(ss/m2,x,N,xi,F0,Nf,type) for ss in X]
            ylbl = r"$J(p^{2})$"
            xlbl = r"$p^{2}$"
        else:
            Y=[1/gluon_J_inv(ss,x,N,xi,F0,Nf,type) for ss in X]
            ylbl = r"$J(p^{2}/m^{2})$"
            xlbl = r"$p^{2}/m^{2}$"
        if ren:
            if Z == None:
                Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
            Y=[y*Z for y in Y]
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        if inverse:
            plt.title(r"Inverse gluon dressing function")
        else:
            plt.title(r"Gluon dressing function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf == None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def gluon_J_inv_contour(s_real = [-5,3], s_imag = [-4,4], N_s_real = 500, N_s_imag = 500,
    x = oneloop_settings.x, N = settings.N, xi = settings.xi, F0 = oneloop_settings.F0, Nf = settings.Nf,
    type = oneloop_settings.gluetype, dimensionful = False, m = oneloop_settings.m, title = True, outf = None):
    r"""Plots the zeroes of the real and imaginary part of the inverse gluon dressing function.

:param s_real: a two-element list containing the minimum and maximum real part of the momentum squared for the plot (see below for dimensions)
:param s_imag: a two-element list containing the minimum and maximum imaginary part of the momentum squared for the plot (see below for dimensions)
:param N_s_real: an integer specifying the number of subdivisions in the real direction
:param N_s_imag: an integer specifying the number of subdivisions in the imaginary direction
:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param dimensionful: if :python:`True`, :python:`s_real` and :python:`s_imag` are the real and imaginary parts of the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds_real = (s_real[1]-s_real[0])/N_s_real
    ds_imag = (s_imag[1]-s_imag[0])/N_s_imag
    X=[s_real[0]+ds_real*k for k in range(N_s_real+1)]
    Y=[s_imag[0]+ds_imag*k for k in range(N_s_imag+1) if s_imag[0]+ds_imag*k != 0]
    if dimensionful:
        m2 = m**2
        ZR=[[(gluon_J_inv((sr+si*1j)/m2,x,N,xi,F0,Nf,type)).real for sr in X] for si in Y]
        ZI=[[(gluon_J_inv((sr+si*1j)/m2,x,N,xi,F0,Nf,type)).imag for sr in X] for si in Y]
        xlbl = r"$\mathrm{Re}(p^{2})$"
        ylbl = r"$\mathrm{Im}(p^{2})$"
        tt = r"Zero set of $J^{-1}(p^{2})$"
    else:
        ZR=[[(gluon_J_inv(sr+si*1j,x,N,xi,F0,Nf,type)).real for sr in X] for si in Y]
        ZI=[[(gluon_J_inv(sr+si*1j,x,N,xi,F0,Nf,type)).imag for sr in X] for si in Y]
        xlbl = r"$\mathrm{Re}(p^{2}/m^{2})$"
        ylbl = r"$\mathrm{Im}(p^{2}/m^{2})$"
        tt = r"Zero set of the inverse gluon dressing function"
    plt.figure()
    plt.contour(X,Y,ZR,[0],colors="green")
    plt.contour(X,Y,ZI,[0],colors="gold")
    if title:
        plt.title(tt)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def gluon_J_3D_plot(value = "abs", s_real = [-5,3], s_imag = [-4,4], N_s_real = 1000,
    N_s_imag = 1000, x = oneloop_settings.x, N = settings.N, xi = settings.xi,
    F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype, inverse = False,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m,
    title = True, outf = None):
    r"""Plots the gluon dressing function in the complex plane (3D plot).

Modulo a factor of :math:`\alpha^{-1}`.

:param value: if :python:`'abs'`, plot the absolute value; if :python:`'real'`, plot the real part; if :python:`'imag'`, plot the imaginary part
:param s_real: a two-element list containing the minimum and maximum real part of the momentum squared for the plot (see below for dimensions)
:param s_imag: a two-element list containing the minimum and maximum imaginary part of the momentum squared for the plot (see below for dimensions)
:param N_s_real: an integer specifying the number of subdivisions in the real direction
:param N_s_imag: an integer specifying the number of subdivisions in the imaginary direction
:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param inverse: if :python:`True`, plot the inverse dressing function
:param ren: if :python:`True`, multiplicatively renormalize the dressing function
:param Z: if :python:`None`, renormalize the dressing function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the dressing function in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`True`, :python:`s_real` and :python:`s_imag` are the real and imaginary parts of the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from numpy import array, meshgrid
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    ds_real = (s_real[1]-s_real[0])/N_s_real
    ds_imag = (s_imag[1]-s_imag[0])/N_s_imag
    X=array([s_real[0]+ds_real*k for k in range(N_s_real+1)])
    Y=array([s_imag[0]+ds_imag*k for k in range(N_s_imag+1) if s_imag[0]+ds_imag*k != 0])
    X,Y= meshgrid(X,Y)
    if inverse:
        if dimensionful:
            m2 = m**2
            ZZ = gluon_J_inv((X+Y*1j)/m2,x,N,xi,F0,Nf,type)
            xlbl = r"$\mathrm{Re}(p^{2})$"
            ylbl = r"$\mathrm{Im}(p^{2})$"
        else:
            ZZ = gluon_J_inv(X+Y*1j,x,N,xi,F0,Nf,type)
            xlbl = r"$\mathrm{Re}(p^{2}/m^{2})$"
            ylbl = r"$\mathrm{Im}(p^{2}/m^{2})$"
        if ren:
            if Z == None:
                Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
            ZZ = ZZ/Z
        tt = "Inverse gluon dressing function"
    else:
        if dimensionful:
            m2 = m**2
            ZZ = 1/gluon_J_inv((X+Y*1j)/m2,x,N,xi,F0,Nf,type)
            xlbl = r"$\mathrm{Re}(p^{2})$"
            ylbl = r"$\mathrm{Im}(p^{2})$"
        else:
            ZZ = 1/gluon_J_inv(X+Y*1j,x,N,xi,F0,Nf,type)
            xlbl = r"$\mathrm{Re}(p^{2}/m^{2})$"
            ylbl = r"$\mathrm{Im}(p^{2}/m^{2})$"
        if ren:
            if Z == None:
                Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
            ZZ = Z*ZZ
        tt = "Gluon dressing function"
    if value=="abs":
        ZZ=abs(ZZ)
    elif value=="real":
        ZZ=ZZ.real
    elif value=="imag":
        ZZ=ZZ.imag
    ax = plt.axes(projection='3d')
    ax.plot_surface(X,Y,ZZ)
    if value=="abs":
        ax.set_zlim(-0.1, 4)
    elif value in ["real","imag"]:
        ax.set_zlim(-4, 4)
    Z0=0*X
    ax.plot_surface(X,Y,Z0,alpha=0.5,color="grey")
    if title:
        plt.title(tt)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def gluon_prop_plot(s = [0,25], N_s = 1000, x = oneloop_settings.x, N = settings.N,
    xi = settings.xi, F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = True, outf = None):
    r"""Plots the gluon propagator in Euclidean space.

Modulo a factor of :math:`\alpha^{-1}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[(s[0]+ds*k) for k in range(N_s+1) if s[0]+ds*k!=0]
    if dimensionful:
        m2 = m**2
        Y=[1/(ss*gluon_J_inv(ss/m2,x,N,xi,F0,Nf,type)) for ss in X]
        xlbl = r"$p^{2}$"
        ylbl=r"$D(p^{2})$"
    else:
        Y=[1/(ss*gluon_J_inv(ss,x,N,xi,F0,Nf,type)) for ss in X]
        xlbl = r"$p^{2}/m^{2}$"
        ylbl=r"$m^{2}D(p^{2}/m^{2})$"
    if ren:
        if Z == None:
            Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
        Y = [y*Z for y in Y]
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Gluon propagator")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def gluon_spectral_plot(s = [0,25], N_s = 1000, x = oneloop_settings.x, N = settings.N,
    xi = settings.xi, F0 = oneloop_settings.F0, Nf = settings.Nf, type = oneloop_settings.gluetype,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = True, outf = None):
    r"""Plots the gluon spectral function in Minkowski space.

Modulo a factor of :math:`\alpha^{-1}`.

:param s: a two-element list containing the minimum and maximum Minkowski momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param x: adimensional quark chiral mass squared :math:`x`
:param N: number of colors :math:`N`
:param xi: gauge parameter :math:`\xi`
:param F0: additive renormalization constant :math:`F_{0}`
:param Nf: number of quarks :math:`N_{f}`
:param type: diagram selector: :python:`'uc'` if only the ordinary quark loop is included, :python:`'cr'` if also the crossed quark loop is included (full QCD only)
:param ren: if :python:`True`, multiplicatively renormalize the spectral function
:param Z: if :python:`None`, renormalize the spectral function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the spectral function in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`False`, adimensionalize the spectral function by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful Minkowski momentum squared :math:`p^{2}_{M}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    ds = (s[1]-s[0])/N_s
    X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    if dimensionful:
        m2 = m**2
        Y=[gluon_spectral(ss/m2,x,N,xi,F0,Nf,type,False,Z,mu0,False,m)/m2 for ss in X]
        xlbl = r"$p^{2}$"
        ylbl =r"$\rho_{\Delta}(p^{2})$"
    else:
        Y=[gluon_spectral(ss,x,N,xi,F0,Nf,type,False,Z,mu0,False,m) for ss in X]
        xlbl = r"$p^{2}/m^{2}$"
        ylbl =r"$m^{2}\,\rho_{\Delta}(p^{2}/m^{2})$"
    if ren:
        if Z == None:
            Z = gluon_J_inv(mu0**2,x,N,xi,F0,Nf,type)
        Y = [y*Z for y in Y]
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Gluon spectral function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf==None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

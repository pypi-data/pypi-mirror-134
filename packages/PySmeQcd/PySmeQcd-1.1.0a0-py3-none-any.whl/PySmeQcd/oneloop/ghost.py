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
Library of functions and routines for the one-loop ghost propagator computed in the Screened Massive Expansion.
"""

from numpy import log, sqrt

from PySmeQcd import settings
from PySmeQcd.oneloop import oneloop_settings


###--- Building blocks for the one-loop ghost propagator ---###
def ghost_G(s):
    r"""Function :math:`G(s)` -- 1-loop Landau-gauge term for the ghost self-energy."""
    lg = (1+s)**2*(2*s-1)/s**2*log(1+s)-2*s*log(s)
    rg = 1/s+2
    return (lg+rg)/12

def ghost_G_xi(s):
    r"""Function :math:`G_{\xi}(s)` -- 1-loop gauge term for the ghost self-energy."""
    return -log(s)/12


###--- Derivatives ---###
def dghost_G(s):
    r"""Derivative of :math:`G(s)` with respect to :python:`s`."""
    lg = 2*(1+s**3)/s**3*log(1+s)-2*log(s)
    rg = -2/s**2+1/s
    return (lg+rg)/12

def dghost_G_xi(s):
    r"""Derivative of :math:`G_{\xi}(s)` with respect to :python:`s`."""
    return -1/(12*s)


###--- One-loop ghost propagator ---###
def ghost_chi_inv(s, xi = settings.xi, G0 = oneloop_settings.G0):
    r"""Inverse ghost dressing function :math:`\chi^{-1}(s)`.

Modulo a factor of :math:`\alpha`.

:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`"""
    res = ghost_G(s)+G0
    if xi != 0:
        res += xi*ghost_G_xi(s)
    return res

def dghost_chi_inv(s, xi = settings.xi):
    r"""Derivative of :python:`ghost_chi_inv` with respect to :python:`s`.

:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`"""
    res = dghost_G(s)
    if xi !=0:
        res += xi*dghost_G_xi(s)
    return res

def ghost_chi(s, xi = settings.xi, G0 = oneloop_settings.G0):
    r"""Ghost dressing function :math:`\chi(s)`.

Modulo a factor of :math:`\alpha^{-1}`.


:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`"""
    return 1/ghost_chi_inv(s,xi,G0)

def ghost_prop(s, xi = settings.xi, G0 = oneloop_settings.G0, ren = True, Z = None,
    mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m):
    r"""Ghost propagator :math:`\mathcal{G}(p^{2})`.

Modulo a factor of :math:`\alpha^{-1}`.

:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`
:param ren: if :python:`True`, multiplicatively renormalize the propagator
:param Z: if :python:`None`, renormalize the propagator in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the propagator in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`False`, adimensionalize the propagator by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
"""
    if dimensionful:
        res = 1/(s*ghost_chi_inv(s/m**2,xi,G0))
    else:
        res = 1/(s*ghost_chi_inv(s,xi,G0))
    if ren:
        if Z == None:
            Z = ghost_chi_inv(mu0**2,xi,G0)
        res *= Z
    return res

def ghost_spectral(s, xi = settings.xi, G0 = oneloop_settings.G0, ren = True, Z = None,
    mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m):
    r"""Ghost spectral function :math:`\rho_{\mathcal{G}}(p^{2})` in Minkowski space.

Modulo a factor of :math:`\alpha^{-1}`. The :math:`\varepsilon` for the difference across the branch cut is defined in the :python:`PySmeQcd.settings` module.

:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`
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
    res = 2*ghost_prop(-s-1j*step_h,xi,G0,ren,Z,mu0,dimensionful,m)
    return res.imag


###--- Plots ---###
def ghost_chi_plot(s = [1E-3,25], N_s = 1000, xi = settings.xi, G0 = oneloop_settings.G0,
    inverse = False, ren = True, Z = None, mu0 = settings.mu0, dimensionful = False,
    m = oneloop_settings.m, scale = "log", title = False, outf = None):
    r"""Plots the ghost dressing function in Euclidean space.

Modulo a factor of :math:`\alpha^{-1}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`
:param inverse: if :python:`True`, plot the inverse dressing function
:param ren: if :python:`True`, multiplicatively renormalize the dressing function
:param Z: if :python:`None`, renormalize the dressing function in the MOM scheme at the scale :python:`mu0`, else use :python:`Z` as the multiplicative renormalization factor (only if :python:`ren=True`)
:param mu0: adimensional renormalization scale :math:`\mu_{0}` for the renormalization of the dressing function in the MOM scheme (only if :python:`ren=True`)
:param dimensionful: if :python:`False`, adimensionalize the dressing function by multiplying it by :python:`m`\ :sup:`2`; if :python:`True`, :python:`s` is the dimensionful momentum squared :math:`p^{2}`
:param m: gluon mass parameter :math:`m` (only if :python:`dimensionful=True`)
:param scale: if set to :python:`'log'`, switch to a log-lin scale
:param title: if :python:`True`, show a title for the plot
:param outf: if not :python:`None`, save the output to the file specified by :python:`outf` rather than printing it out
"""
    from matplotlib import pyplot as plt
    if scale == 'log':
        from numpy import log10
        ds = (log10(s[1])-log10(s[0]))/N_s
        X=[10**(log10(s[0])+ds*k) for k in range(N_s+1)]
    else:
        ds = (s[1]-s[0])/N_s
        X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    if inverse:
        if dimensionful:
            m2 = m**2
            Y=[ghost_chi_inv(ss/m2,xi,G0) for ss in X]
            ylbl = r"$\chi^{-1}(p^{2})$"
            xlbl = r"$p^{2}$"
        else:
            Y=[ghost_chi_inv(ss,xi,G0) for ss in X]
            ylbl = r"$\chi^{-1}(p^{2}/m^{2})$"
            xlbl = r"$p^{2}/m^{2}$"
        if ren:
            if Z == None:
                Z = ghost_chi_inv(mu0**2,xi,G0)
            Y=[y/Z for y in Y]
    else:
        if dimensionful:
            m2 = m**2
            Y=[1/ghost_chi_inv(ss/m2,xi,G0) for ss in X]
            ylbl = r"$\chi(p^{2})$"
            xlbl = r"$p^{2}$"
        else:
            Y=[1/ghost_chi_inv(ss,xi,G0) for ss in X]
            ylbl = r"$\chi(p^{2}/m^{2})$"
            xlbl = r"$p^{2}/m^{2}$"
        if ren:
            if Z == None:
                Z = ghost_chi_inv(mu0**2,xi,G0)
            Y=[y*Z for y in Y]
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        if inverse:
            plt.title(r"Inverse ghost dressing function")
        else:
            plt.title(r"Ghost dressing function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf == None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def ghost_prop_plot(s = [1E-3,25], N_s = 1000, xi = settings.xi, G0 = oneloop_settings.G0,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = False, outf = None):
    r"""Plots the ghost propagator in Euclidean space.

Modulo a factor of :math:`\alpha^{-1}`.

:param s: a two-element list containing the minimum and maximum momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`
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
    if scale == 'log':
        from numpy import log10
        ds = (log10(s[1])-log10(s[0]))/N_s
        X=[10**(log10(s[0])+ds*k) for k in range(N_s+1)]
    else:
        ds = (s[1]-s[0])/N_s
        X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    if dimensionful:
        m2 = m**2
        Y=[1/(ss*ghost_chi_inv(ss/m2,xi,G0)) for ss in X]
        ylbl = r"$\mathcal{G}(p^{2})$"
        xlbl = r"$p^{2}$"
    else:
        Y=[1/(ss*ghost_chi_inv(ss,xi,G0)) for ss in X]
        ylbl = r"$m^{2}\mathcal{G}(p^{2}/m^{2})$"
        xlbl = r"$p^{2}/m^{2}$"
    if ren:
        if Z == None:
            Z = ghost_chi_inv(mu0**2,xi,G0)
        Y=[y*Z for y in Y]
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Ghost propagator")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf == None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

def ghost_spectral_plot(s = [1E-3,25], N_s = 1000, xi = settings.xi, G0 = oneloop_settings.G0,
    ren = True, Z = None, mu0 = settings.mu0, dimensionful = False, m = oneloop_settings.m,
    scale = "log", title = False, outf = None):
    r"""Plots the ghost spectral function in Minkowski space.

Modulo a factor of :math:`\alpha^{-1}`.

:param s: a two-element list containing the minimum and maximum Minkowski momentum squared for the plot (see below for dimensions)
:param N_s: an integer specifying the number of plot points
:param xi: gauge parameter :math:`\xi`
:param G0: additive renormalization constant :math:`G_{0}`
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
    if scale == 'log':
        from numpy import log10
        ds = (log10(s[1])-log10(s[0]))/N_s
        X=[10**(log10(s[0])+ds*k) for k in range(N_s+1)]
    else:
        ds = (s[1]-s[0])/N_s
        X=[s[0]+ds*k for k in range(N_s+1) if s[0]+ds*k!=0]
    if dimensionful:
        m2=m**2
        Y=[ghost_spectral(ss/m2,xi,G0,False,Z,mu0,False,m)/m2 for ss in X]
        ylbl = r"$\rho_{\mathcal{G}}(p^{2})$"
        xlbl = r"$p^{2}$"
    else:
        Y=[ghost_spectral(ss,xi,G0,False,Z,mu0,False,m) for ss in X]
        ylbl = r"$m^{2}\rho_{\mathcal{G}}(p^{2}/m^{2})$"
        xlbl = r"$p^{2}/m^{2}$"
    if ren:
        if Z == None:
            Z = ghost_chi_inv(mu0**2,xi,G0)
        Y=[y*Z for y in Y]
    plt.figure()
    plt.plot(X,Y)
    if scale=="log":
        plt.xscale("log")
    if title:
        plt.title(r"Ghost spectral function")
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    if outf == None:
        plt.show(block=False)
    else:
        plt.savefig(outf)

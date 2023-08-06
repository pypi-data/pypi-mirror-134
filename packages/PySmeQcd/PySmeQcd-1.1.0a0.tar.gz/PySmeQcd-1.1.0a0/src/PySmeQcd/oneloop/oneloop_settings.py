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
"""Default settings for the :python:`SmeQcd.oneloop` module."""

###--- Default Parameters ---###

##-- Type of propagator --##
gluetype = "uc"
r"""Diagram selector for the gluon propagator (full QCD only)"""
quarktype = "ms"
r"""Diagram selector for the quark propagator (full QCD only)"""

##-- Masses --#
m = 0.65577
r"""Gluon mass parameter :math:`m`\ , in GeV"""
x = 0.238171
r"""Quark/gluon mass ratio squared :math:`x`"""
K0 = 0.1190625
r"""Normalized and adimensionalized bare quark mass :math:`K_{0}/M`"""

##-- Renormalization constants & similia --##
F0 = -0.876
r"""Gluon polarization additive renormalization constant :math:`F_{0}`\ """
G0 = 0.14524
r"""Ghost self-energy additive renormalization constant :math:`G_{0}`\ """
H0 = 2.073
r"""Quark self-energy renormalization constant :math:`H_{0}`\ """
Zglue = 1
r"""Multiplicative gluon renormalization for the quark propagator :math:`Z_{\text{glue}}`"""

##-- Poles and residues --##
p02 = 0.457525+1.012980j
r"""Gluon pole :math:`p^{2}_{0}` in Minkowski space, adimensionalized by the gluon mass parameter :math:`m`"""
p0 = 0.885730 + 0.571833j
r"""Gluon pole :math:`p_{0}` in Minkowski space, adimensionalized by the gluon mass parameter :math:`m`"""
res_im_re = 3.131629
r"""Ratio Im/Re of the residue of the gluon propagator at its pole, :math:`\text{Im}\{R\}/\text{Re}\{R\}`"""
phi = 1.261708
r"""Phase :math:`\varphi` of the residue of the gluon propagator at its pole"""

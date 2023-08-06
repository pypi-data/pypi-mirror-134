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
r"""Global default settings for the :python:`PySmeQcd` package.
"""

###--- Default Parameters ---###

##-- Theory --##
N = 3
r"""Number of colors :math:`N`"""
Nf = 0
r"""Number of fermions :math:`N_{f}`"""
xi = 0
r"""Gauge parameter :math:`\xi`"""

##-- Renormalization constants & similia --##
mu0 = 6.099699589795203
r"""Adimensional renormalization scale :math:`\mu_{0}`"""

##-- Numerical parameters and starting points --##
step_h = 1E-8
r"""Step parameter for numerical derivatives and branch-cut differences"""
stp = -1-1j
r"""Starting point for complex root-finding algorithms"""

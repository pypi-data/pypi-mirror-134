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
Library of functions and routines for the Screened Massive Expansion of QCD.

The :python:`PySmeQcd` module contains the following submodules:

- :python:`PySmeQcd.settings`
- :python:`PySmeQcd.oneloop`

Also, the submodules of :python:`PySmeQcd.oneloop` are linked to this module.
"""

from PySmeQcd.oneloop import ghost, gluon, quark

__version__ = '1.0.0-alpha.1'

# PySmeQcd

**PySmeQcd** is a Python library for making calculations within the framework of
the Screened Massive Expansion of Quantum Chromodynamics.

Currently, PySmeQcd contains functions and routines related to the one-loop gluon,
ghost and quark propagators in any covariant gauge, both in
pure Yang-Mills theory and in full QCD.

## Features

- Compute the one-loop gluon, ghost and quark propagators in an arbitrary covariant gauge
- Plot the dressing functions, propagators, spectral functions, and more
- Find the poles and residues of the gluon and quark propagators
- Other features

## Installation

### Using ```pip```

PySmeQcd is available on PyPI. To install it, run

```console
$ pip install PySmeQcd
```

### From source

To use PySmeQcd from the source code:

1. Download the source code from [GitHub](https://github.com/GComitini/PySmeQcd/releases/download/v1.0.0-alpha/PySmeQcd-1.0.0a0.tar.gz).
  ```console
  $ wget https://github.com/GComitini/PySmeQcd/releases/download/v1.0.0-alpha/PySmeQcd-1.0.0a0.tar.gz
  ```

2. Unpack the archive and `cd` into the `src` directory.
  ```console
  $ tar -xzvf PySmeQcd-1.0.0a0.tar.gz
  $ cd PySmeQcd-1.0.0a0/src
  ```

3. Copy the ```PySmeQcd``` directory to the main directory of your project.
  ```console
  $ cp PySmeQcd <MY_PROJECT>
  ```

## Documentation

PySmeQcd's documentation is available on [Read the Docs](https://pysmeqcd.readthedocs.com).

## Dependencies

PySmeQcd supports Python 3 and depends on the following Python packages:

- matplotlib
- numpy
- scipy

## Authors

PySmeQcd was written by [Giorgio Comitini](giorgio.comitini@dfa.unict.it).

## License

PySmeQcd is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. See [LICENSE](https://github.com/GComitini/PySmeQcd/blob/master/LICENSE).

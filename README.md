# NormalModeDisplacement

This program will displace a geometry for a normal mode with a user-defined scaling factor.

# Requirements

1. Python3
2. ORCA .hess file from Versions 4 or 5

# To run, simply use the following:
/path/to/python/3/python displace.py FILENAME.hess MODE_NUMBER SCALING_FACTOR

- We note here, the mode counting starts with 0 as is done in ORCA
- The resulting geometry will be printed to the screen (XMOL XYZ).

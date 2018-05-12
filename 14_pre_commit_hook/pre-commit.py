#!/usr/bin/env python


import sys
import os
import unittest

cwd = os.getcwd()
if cwd.endswith('.git/hooks'):
    two_dirs_upper = os.path.abspath('../..')
    sys.path.append(two_dirs_upper)
else:
    sys.path.append(cwd)
from tests import QuadraticEquationTestCase


if __name__=='__main__':
    unittest.main()

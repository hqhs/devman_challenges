# Quadratic Equations Solver

get_roots(a, b, c) return roots for equations like a * x ^ 2 + b * x + c = 0.
tests.py is unittest module for automatic testing get_roots function.
pre-commit script starts tests.py every time you want to commit something in git, here's how to use it:

# Usage example

In this example, '~solver/bash' is a repository where git initialized. 

```#!bash
~/solver/bash/ $ ln -s ../../pre-commit.py .git/hooks/pre-commit #creates soft symlink to pre-commit.py 
#in git hooks
#that's all! lets check it out...
~/solver/bash/ $ git add quadratic_equation.py
~/solver/bash/ $ git commit -m 'commit message'
E...
======================================================================
ERROR: test_first_root_less_than_second (tests.QuadraticEquationTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/hqhs/workplace/14_pre_commit_hook/sources/tests.py", line 12, in test_first_root_less_than_second
    root1, root2 = get_roots(1, 2, -3)
TypeError: 'NoneType' object is not iterable

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (errors=1)
~/solver/bash/ $ vim quadratic_equation.py #find and fix error in text editor
~/solver/bash/ $ git add quadratic_equation.py 
~/solver/bash/ $ git commit -m 'explained why error occurs in the first place'
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
[master d029c33] error fixed
 1 file changed, 1 insertion(+)

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

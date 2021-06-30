# - Lets import unittest and pytest
# - These are the dependencies to create our test and run
# - To check if tests have passed/failed, in Terminal type `python -m pytest`

import unittest
import pytest

# - Create the tests (this is done before writing the code
from simple_calc import SimpleCalc

class Calctest(unittest.TestCase): # To use TestCast we need to inherit it from unittest package.
    calc = SimpleCalc()

# Assertions to write out test cases# The logic code which is use to test on
# - We will use our basic cal example to write the test first then the code

    def test_add(self):
        # Naming convention is essential, TEST needs to be in the name

        self.assertEqual(self.calc.add(3,2),5) # 2+3 should equal 5, if true the test would pass otherwise it would fail
        #return num1 + num2


    def test_subtract(self):
       self.assertEqual(self.calc.subtract(3,2),1)


    def test_multi(self):
      self.assertEqual(self.calc.multi(2,2),4)


    def test_divide(self):
         self.assertEqual(self.calc.divide(6,3),2)

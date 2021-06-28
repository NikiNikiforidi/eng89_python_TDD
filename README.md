# Test Driven Development TDD

### Steps to create TDD
- Create a file called calc_test.py
- Will use `unittest` and `pytest` (these are packages)
- Need to install `pip install pytest`  
- `python -m unittest`
- `python -m unittest discover -v` To see more information


- Lets import unittest and pytest
- These are the dependencies to create our test and run
- To check if tests have passed/failed, in Terminal type `python -m pytest`

```
import unittest
import pytest

from simple_calc import SimpleCalc # The code from simple_calc is below

class Calctest(unittest.TestCase):

    calc = SimpleCalc()
```
- Assertions to write out test cases
- We will use our basic cal example to write the test first then the code
```
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
         
```

- **Code below is from the separate python file named simple_calc**
```
class SimpleCalc:

# If outcome is 5, the test is true
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multi(self,num1,num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```

# **TDD in class diagram**
![TDD in class diagram](https://user-images.githubusercontent.com/86292184/123640932-9295b980-d819-11eb-93b8-a58c5a525798.png)

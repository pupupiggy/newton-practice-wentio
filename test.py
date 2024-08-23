import pytest
import numpy as np
import math

import newton

def test_basic_function () :
    assert np. isclose (newton, optimize(2.95, np, cos) ['x'], math.pi)
                        
def test_bad_input ():
## Ideally, our function would raise the exception with a useful message. 
    with pytest. raises (TypeError, match='x0 must be numeric'):
        newton. optinize(np.cos, 2.95)
        
def test_something() :
    with pytest. raises (RuntimeError, match = '......'):



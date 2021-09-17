# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:54:50 2021

@author: Quinten
"""
import io, os, sys, types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
from importing import find_notebook
from importing import NotebookLoader
from importing import NotebookFinder
sys.meta_path.append(NotebookFinder())
import power as  correct
import Introduction as student
import pytest
import math
import matplotlib.pyplot as plt
import numpy as np
import time


def test_Power(): #2 points
    x = 6;
    y=9
    power = student.power(x, y);
    power_correct = correct.z;
    
    rms_error_power = np.absolute(power_correct-power)
    assert rms_error_power <= 0, "Jacobian is not correct."
    

pytest.main() #["--tb=line"]
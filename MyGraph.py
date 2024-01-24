import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")


# ModuleNotFoundError: We do not have this module. Python is an open source language (no 
# governance really), so many people have developed libraries so we don't have to start from scratch.
# We need to install this library into this project for the module to run.
# When working on a project when using a library, create a virtual environment (a copy of your Python 
# interpreter/interpreter within the project - not installing into the root of your software).
# The virtual environment is then self-contained. Create, activate, and then install 3rd party module.

# Step 1: Create a virtual environment. Use py -3 -m venv nameofVE
# See name in folder section based on the name you gave.
# Saying yes, switches interpreter from the root interpreter to the virtual one.

# Step 2: Activate the VE: .\NameOfVE\Scripts\activate

# Step 3: Install 3rd party library/module: pip3 install NameOfLibrary
# Need to be in VE and have the VE interpreter selected.

# We installed it in the VE, not in the roote, so it will not be recognized if I use the root interpreter.
# THe bottom right hand corner tells you what interpreter you are using.

# If you don't activate your VE, it will install the 3rd party library in your root interpreter. So,
# working in your VE will not work because the library is not installed there.
# Uninstall by doing pip3 uninstall to remove the library.

# Source control is a way of keeping track of our project and track changes (who made them, when, etc.)
# Line across the file means that it is no longer existing.
# Installing the matplotlib module brought 4,000 + files.
# Not necessary to track changes for the VE. 
# Red indicates what was there before and green shows you what you changed it to.

# To ignore files/folders and not track changes, create a special file called .gitignore

# Clone is the same thing as a copy.

# Code on the left in red is what is in the repository, code in the green is what we want
# to put into the compository.
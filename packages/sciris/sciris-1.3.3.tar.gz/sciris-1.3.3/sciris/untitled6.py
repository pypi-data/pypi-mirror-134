import numpy as np
import pylab as pl
import pandas as pd
import sciris as sc
import covasim as cv
np; pl; pd; sc; cv

print(sc.getcaller(frame=1, tostring=False, includeline=True)) # See the line that called this function
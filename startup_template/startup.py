#startup template for Jupyter Notebook
# activate tab completion so I won't shy away from descriptive vars
# %config IPCompleter.use_jedi = False
# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests
from datetime import date, time, datetime, timedelta
from IPython.display import display, HTML
# Allow for multiple outputs from one cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


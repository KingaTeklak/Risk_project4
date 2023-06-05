import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data(path:str = "danekawa.csv" ):
    """Return pandas data"""

    return pd.read_csv(path)["data"]

def zwroty(table):
    zwrot = []
    for i in range(1, len(table)):
        zwrot.append(np.log(table[i]/table[i-1]) * 100)
        
    return zwrot

zwrot = zwroty(data())
print(zwrot)
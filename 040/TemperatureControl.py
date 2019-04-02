import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def ReadData():
    Xfile = Path("./TemperatureControlXData.dat")
    Yfile = Path("./TemperatureControlYData.dat")
    if Xfile.exists() & Yfile.exists():
        X = np.load(Xfile)
        Y = np.load(Yfile)
        return X,Y
    else:
        return None, None

if __name__ == '__main__':
    X, Y = ReadData()
    plt.plot(X, Y, '.')
    plt.show();
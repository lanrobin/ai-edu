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

def Gradient(X, Y):
    eta = 0.1
    w, b = 0.0, 0.0
    num_example = X.shape[0]
    for i in range(num_example):
        x = X[i]
        y = Y[i]
        z = w * x + b
        dz = z - y
        db = dz
        dw = dz * x
        w = w - eta * dw
        b = b - eta * db

    print(w, b)
    return w, b

if __name__ == '__main__':
    X, Y = ReadData()
    #plt.plot(X, Y, '.')
    #plt.show();
    Gradient(X, Y)

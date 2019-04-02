import numpy as np

# x=0,y=1; x=1,y=0
def ReadData():
    X = np.array([0,1]).reshape(1,2)
    Y = np.array([1,0]).reshape(1,2)
    return X,Y

def ForwardCalculation(w,b,x):
    z = w * x + b
    return z

def BackPropagation(x,y,z):
    dZ = z - y
    dB = dZ
    dW = dZ * x
    return dW, dB

def UpdateWeights(w, b, dW, dB, eta):
    w = w - eta*dW
    b = b - eta*dB
    return w,b

def CheckLoss(w, b, X, Y, count):
    Z = w * X + b
    LOSS = (Z - Y)**2
    loss = LOSS.sum()/count/2
    return loss

def Test(w,b):
    z1 = ForwardCalculation(w, b, 0)  # x=0, check if z==1
    z2 = ForwardCalculation(w, b, 1)  # x=1, check if z==0
    print (z1,z2)
    if np.abs(z1-1) < 0.001 and np.abs(z2-0)<0.001:
        return True
    return False

if __name__ == '__main__':
    # initialize_data
    eta = 0.1
    # set w,b=0, you can set to others values to have a try
    #w, b = np.random.random(),np.random.random()
    w, b = 0, 0
    eps = 1e-15
    max_epoch = 10000
    # calculate loss to decide the stop condition
    loss = 1
    # create mock up data
    X, Y = ReadData()
    # count of samples
    num_features = X.shape[0]
    num_example = X.shape[1]

    for epoch in range(max_epoch):
        for i in range(num_example):
            # get x and y value for one sample
            x = X[:,i]
            y = Y[:,i]
            # get z from x,y
            z = ForwardCalculation(w, b, x)
            # calculate gradient of w and b
            dW, dB = BackPropagation(x, y, z)
            # update w,b
            w, b = UpdateWeights(w, b, dW, dB, eta)
            # calculate loss for this batch
            loss = CheckLoss(w,b,X,Y,num_example)
            print(epoch,i,loss,w,b)

        if loss < eps:
            break

    print("w=%f,b=%f" %(w,b))

    print("result=", Test(w, b))
class BackPropagration:
    def fx(self, w, b):
        #print( "w=" + str(w) +", b=" + str(b) +"\n")
        result = 2 * w + 3*b
        return result
    
    def fy(self, w, b):
        #print( "w=" + str(w) +", b=" + str(b) +"\n")
        result = 2*b + 1
        return result

    def fz(self, w, b):
        return self.fx(w, b) * self.fy(w, b)

    def partialfzb(self, w, b):
        return 3 * self.fy(w,b) + 2 * self.fx(w,b)

    def partialfzw(self, w, b):
        return 2 * self.fy(w, b)

bp = BackPropagration()

targetZ = 150
loss = 1e-8
w = 3
b = 4
loop = 1
while True:
    z = bp.fz(w, b)
    print("Loop:" + str(loop) + ",w=" + str(w) +", b=" + str(b) +", z=" + str(z))
    deltaB = bp.partialfzb(w, b)
    print("deltaB= " + str(deltaB))
    deltaW = bp.partialfzw(w, b)
    print("deltaW= " + str(deltaW))
    deltaZ = abs(targetZ - z)
    print("deltaZ= " + str(deltaZ))
    if(deltaZ < loss):
        print("Final w=" + str(w) +", b=" + str(b))
        break;
    decreaseW = deltaZ/2.0/deltaW
    decreateB = deltaZ/2.0/deltaB
    print("decreaseW = " + str(decreaseW) +", decreateB = " + str(decreateB))
    w = w - decreaseW
    b = b - decreateB
    print("new w = " + str(w) +", new b = " + str(b))
    loop = loop + 1
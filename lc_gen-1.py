
# set up mag map


import random
import numpy as np

def circlesource(vel, s):
    box1 = mag[0:s, 0:s]
    for x in range(s):
        for y in range(s):
            r = np.sqrt((((s/2.) - x)**2) + (((s/2.) - y)**2))
            radius = (s/2.)
            if r>radius:
                box1[x, y] = 0
            else:
                box1[x, y] = 1
    circle = box1
    n = random.uniform(0, 2*np.pi)        
    pixv = vel * (86400.) * (3.24e-20) * (167.3)* (20./(5.0e-5))*(2000./20.)
    xvel = pixv*np.cos(n)
    yvel = pixv*np.sin(n)
    x = random.randint(0, 2000)
    y = random.randint(0, 2000)
    xstep = xvel
    ystep = yvel
    for t in range(100000):
        xr = math.ceil(x)
        yr = math.ceil(y)
        xbig = x + (1000*xstep)
        ybig = y + (1000*ystep)
        if xbig>(2000-s) or ybig>(2000-s):
            break
        if 0<=xr<(2000-s) and 0<=yr<(2000-s):
            box = mag[xr:xr+s, yr:yr+s]
            circnew = (box*circle)
            sum = circnew.sum()
            total.append(sum)
        if xr>=(2000-s) or yr>=(2000-s):
            break
        if len(total) == 1000:
            break
        x = x + xstep
        y = y + ystep


def lightcurve(source, vel, s):
    if source == 1:
        circlesource(vel, s)
        summ = total
        area = ((s/2.)**2)*(3.14)
        summ1 = [x/area for x in summ]
        if len(total) == 1000:
            return summ1
        else:
            return 0
    if source == 2: 
        s = input("Enter size s: ")
        squaresource(s)
        summ = total
        area = (s**2)
        summ1 = [x/area for x in summ]
        newvel = vel * (86400.) * (3.24e-20) * (167)
        timescale = (5.0e-5)/newvel
        if len(total) == 1000:
            return summ1
        else:
            return 0

for b in range(100000):
    total=[]
    x1=lightcurve(1,100,44)
    if x1 !=0:
        break
        print("1")

for b in range(100000):
    total=[]
    x2=lightcurve(1,100,44)
    if x2 !=0:
        break
        print("1")

p1 = vstack((x1,x2))

for b in range(1000000):
    total=[]
    a=lightcurve(1,100,44)
    if a != 0:
        p1 = vstack((p1,a))
    if shape(p1) == (100,1000):
        break
        print("1")

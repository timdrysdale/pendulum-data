# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# basic csv import but hard to plot data right away as each row is separate array
with open('../data/pend00-run00.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

#print(data)

# try again with pandas

df = pd.read_csv('../data/pend00-run00.csv')

t = df.loc[:,"Time/s"]
theta = df.loc[:,"Angle/rad"]

plt.plot(t,theta,"b-",label="measured")

plt.xlabel("Time/s")
plt.ylabel("Angle/rad")

plt.savefig("../img/pend00-run00-angle.png", dpi=300)

# Try some simulation data?
# for now, calculate some data just to show two traces on the same graph

ta = np.array(t)
thetaa = np.array(theta)

w0 = np.pi/20
w1= 8
y = np.sin(w0*ta)*np.sin(w1*ta)
plt.plot(ta,y, "r:", label="calculated")
plt.legend()

plt.savefig("../img/pend00-run00-angle-with-calculated.png", dpi=300)

 
plt.close()

df = pd.read_csv('../data/pend00-run07.csv')

t = df.loc[:,"Time/s"]
theta = df.loc[:,"Angle/rad"]

plt.plot(t,theta,"b-",label="measured")

plt.xlabel("Time/s")
plt.ylabel("Angle/rad")

plt.savefig("../img/pend00-run07-angle.png", dpi=300)

plt.close()

plt.figure()

a = 40
b = 110

plt.plot(t[a:b],theta[a:b],"b-",label="measured")

plt.xlabel("Time/s")
plt.ylabel("Angle/rad")

plt.savefig("../img/pend00-run07-angle-startup.png", dpi=300)





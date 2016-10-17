from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import airtime
import sys

fig = pylab.figure()
ax = Axes3D(fig)

nFrames = 64
basic_rate = 6.5

#MCS0
MCS_Mbps = 6.5
T_L = airtime.T_total(nFrames, MCS_Mbps, basic_rate)
Total_Power = [930.86, 961.9, 982.7, 1009.25, 1028.18, 1024.67, 1041.49, 1052.76, 1047.01] #Total Power
Throughput = [0.607, 1.2, 1.81, 3.01, 3.63, 4.23, 4.83, 5.47, 5.77] #Throughput
lambda_r = [(tput/(1470*8.0))*(10**6) for tput in Throughput]

#MCS1
"""
MCS_Mbps = 13.0
T_L = airtime.T_total(nFrames, MCS_Mbps, basic_rate)
Total_Power = [952.96, 977.36, 996.66, 1026.08, 1036.64, 1061.45, 1075.34, 1094.62, 1094.09]
Throughput = [1.11, 2.22, 3.34, 4.41, 5.52, 7.76, 8.83, 9.93, 11] #Throughput
lambda_r = [(tput/(1470*8.0))*(10**6) for tput in Throughput]
"""

X = Total_Power #Total Power
Y = [l_r*T_L for l_r in lambda_r]
Z = lambda_r

ax.set_xlabel('x1 (tau_rx)')      #X
ax.set_ylabel('x2 (lambda_r)')    #Y
ax.set_zlabel('y (Total_Power)')  #Z

#ax.scatter(X, Y, Z, c='b', marker='^')
ax.plot(Y, Z, X, c='b', marker='^')
pyplot.show()


from sklearn import linear_model

VAR = []
for index in range(0,len(Total_Power)):
	var = []
	var.append(Y[index])
	var.append(Z[index])
	VAR.append(var)
	
clf = linear_model.Ridge(alpha=0.5, fit_intercept=True)
clf.fit(VAR,X)
print clf.coef_


import statsmodels.api as sm

VAR = sm.add_constant(VAR)
est = sm.OLS(X, VAR).fit()
print est.summary()

# TODO add image and put this code into an appendix at the bottom
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import pylab
import statsmodels.api as sm
import numpy as np
# import airtime

# nFrames = 64
# basic_rate = 6.5

#MCS1
MCS_Mbps = 13
# T_L = airtime.T_total(nFrames, MCS_Mbps, basic_rate)
P = [1122.4, 1126.5, 1130.5, 1131.81, 1133.34, 1133.94, 1132.42, 1134.67, 1137.62, 1142.42, 1142.68, 1144.65, 1147.7, 1152.11, 1156.86, 1159.22, 1180.32, 1190.91, 1189.97, 1193.46, 1190.46, 1204.2, 1208.33, 1220.41, 1252.11, 1259.74, 1261.89, 1264.32, 1267.73, 1266.02, 1274.22, 1284.96, 1270.5, 1272.5, 1275.33, 1277.57, 1277.11, 1282.35, 1285.55, 1283.17, 1274.41, 1280.51, 1285.66, 1284.03, 1286.91, 1289.23, 1291.64, 1301.55, 1288.19, 1290.48, 1292.35, 1302.52, 1306.22, 1309.7, 1311.2, 1304.22, 1305.23, 1306.4, 1312.4, 1306.59, 1308.65, 1310.52, 1321.51, 1327] # Total power
lambda_r = [100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 400, 400, 400, 400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 800, 800, 800, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000]           # thruput [x_2]
tau_rx = [0.002962963, 0.005925926, 0.008888889, 0.014814815, 0.023703704, 0.02962963, 0.035555556, 0.043555556, 0.005925926, 0.011851852, 0.017777778, 0.02962963, 0.047407407, 0.059259259, 0.071111111, 0.087111111, 0.011851852, 0.023703704, 0.035555556, 0.059259259, 0.094814815, 0.118518519, 0.142222222, 0.174222222, 0.023703704, 0.047407407, 0.071111111, 0.118518519, 0.18962963, 0.237037037, 0.284444444, 0.348444444, 0.035555556, 0.071111111, 0.106666667, 0.177777778, 0.284444444, 0.355555556, 0.426666667, 0.522666667, 0.044444444, 0.088888889, 0.133333333, 0.222222222, 0.355555556, 0.444444444, 0.533333333, 0.653333333, 0.053333333, 0.106666667, 0.16, 0.266666667, 0.426666667, 0.533333333, 0.64, 0.784, 0.059259259, 0.118518519, 0.177777778, 0.296296296, 0.474074074, 0.592592593, 0.711111111, 0.871111111]         # [x_1]print len(Total_Power), len(Throughput)

X = []
for index in range(0,len(P)):
	x = []
	x.append(tau_rx[index])
	x.append(lambda_r[index])
	X.append(x)

y = P

## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
print est.summary()

## Create the 3d plot -- skip reading this
# TV/Radio grid for 3d plot
xx1, xx2 = np.meshgrid(np.linspace(min(tau_rx), max(tau_rx), 100), 
                       np.linspace(min(lambda_r), max(lambda_r), 100))
# plot the hyperplane by evaluating the parameters on the grid
Z = est.params[0] + est.params[1] * xx1 + est.params[2] * xx2

# create matplotlib 3d axes
fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig, azim=-115, elev=15)

# plot hyperplane
surf = ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.6, linewidth=0)

# plot data points - points over the HP are white, points below are black
"""
resid = y - est.predict(X)
ax.scatter(X[resid >= 0].TV, X[resid >= 0].Radio, y[resid >= 0], color='black', alpha=1.0, facecolor='white')
ax.scatter(X[resid < 0].TV, X[resid < 0].Radio, y[resid < 0], color='black', alpha=1.0)
"""
ax.plot(tau_rx, lambda_r, y, c='k', marker='^')

# set axis labels
ax.set_xlabel('tau_rx')
ax.set_ylabel('lambda_r')
ax.set_zlabel('Total Power')

plt.show()

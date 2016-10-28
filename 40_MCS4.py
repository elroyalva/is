# TODO add image and put this code into an appendix at the bottom
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import pylab
import statsmodels.api as sm
import numpy as np
# import airtime

#MCS6
P = [1106.28, 1112.35, 1111.26, 1116.17, 1121.32, 1122.11, 1127.2, 1119.23, 1136.45, 1138.75, 1140.16, 1144.23, 1146.3, 1147.97, 1148.23, 1154.2, 1170.38, 1178.42, 1185.52, 1188.22, 1191.23, 1189.23, 1196.32, 1199.36, 1203.64, 1199.54, 1209.95, 1216.47, 1219.84, 1217.25, 1220.32, 1224.35, 1252.77, 1259.61, 1263.44, 1267.17, 1270.44, 1283.45, 1296.11, 1303.25, 1250.56, 1248.89, 1261.52, 1262.52, 1276.36, 1274.04, 1280.56, 1284.47, 1270.68, 1274.36, 1277.32, 1278.23, 1281.43, 1282.37, 1280.23, 1286.32, 1273.41, 1276.4, 1280.29, 1283.26, 1287.43, 1286.43, 1285.62, 1294.25, 1283.33, 1286.24, 1291.11, 1296.44, 1296.15, 1299.82, 1300.04, 1307.22, 1290.84, 1298.66, 1307.97, 1314.23, 1316.78, 1320.37, 1319.77, 1317.56, 1304.56, 1307.22, 1312.64, 1320.45, 1325.49, 1327.12, 1330.18, 1332.41, 1329.61, 1333.41, 1331.12, 1338.96, 1340.22, 1343.52, 1347.19, 1361.23, 1340.29, 1345.28, 1357.82, 1363.24, 1367.76, 1367.61, 1370.25, 1382.12, 1385.32, 1392.32, 1396.77, 1393.45, 1397.23, 1406.23, 1414.53, 1408.23, 1426.31, 1433.21, 1434.12, 1438.56, 1442.03, 1443.89, 1444.33, 1441.12, 1453.24, 1456.75, 1466.4, 1461.23, 1476.81, 1471.25, 1469.52, 1471.97, 1459.23, 1461.79, 1468.67, 1462.52, 1476.61, 1482.33, 1482.67, 1481.23] # Total power
lambda_r = [100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 400, 400, 400, 400, 400, 400, 400, 400, 600, 600, 600, 600, 600, 600, 600, 600, 800, 800, 800, 800, 800, 800, 800, 800, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2700, 2700, 2700, 2700, 2700, 2700, 2700, 2700, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3200, 3700, 3700, 3700, 3700, 3700, 3700, 3700, 3700, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 4700, 4700, 4700, 4700, 4700, 4700, 4700, 4700, 5200, 5200, 5200, 5200, 5200, 5200, 5200, 5200, 5800, 5800, 5800, 5800, 5800, 5800, 5800, 5800]           # thruput [x_2]
tau_rx = [0.000987654, 0.001975309, 0.002962963, 0.004938272, 0.007901235, 0.009876543, 0.011851852, 0.014518519, 0.001975309, 0.003950617, 0.005925926, 0.009876543, 0.015802469, 0.019753086, 0.023703704, 0.029037037, 0.003950617, 0.007901235, 0.011851852, 0.019753086, 0.031604938, 0.039506173, 0.047407407, 0.058074074, 0.005925926, 0.011851852, 0.017777778, 0.02962963, 0.047407407, 0.059259259, 0.071111111, 0.087111111, 0.007901235, 0.015802469, 0.023703704, 0.039506173, 0.063209877, 0.079012346, 0.094814815, 0.116148148, 0.009876543, 0.019753086, 0.02962963, 0.049382716, 0.079012346, 0.098765432, 0.118518519, 0.145185185, 0.011851852, 0.023703704, 0.035555556, 0.059259259, 0.094814815, 0.118518519, 0.142222222, 0.174222222, 0.014814815, 0.02962963, 0.044444444, 0.074074074, 0.118518519, 0.148148148, 0.177777778, 0.217777778, 0.017777778, 0.035555556, 0.053333333, 0.088888889, 0.142222222, 0.177777778, 0.213333333, 0.261333333, 0.021728395, 0.04345679, 0.065185185, 0.108641975, 0.17382716, 0.217283951, 0.260740741, 0.319407407, 0.026666667, 0.053333333, 0.08, 0.133333333, 0.213333333, 0.266666667, 0.32, 0.392, 0.031604938, 0.063209877, 0.094814815, 0.158024691, 0.252839506, 0.316049383, 0.379259259, 0.464592593, 0.03654321, 0.07308642, 0.10962963, 0.182716049, 0.292345679, 0.365432099, 0.438518519, 0.537185185, 0.041481481, 0.082962963, 0.124444444, 0.207407407, 0.331851852, 0.414814815, 0.497777778, 0.609777778, 0.046419753, 0.092839506, 0.139259259, 0.232098765, 0.371358025, 0.464197531, 0.557037037, 0.68237037, 0.051358025, 0.102716049, 0.154074074, 0.256790123, 0.410864198, 0.513580247, 0.616296296, 0.754962963, 0.057283951, 0.114567901, 0.171851852, 0.286419753, 0.458271605, 0.572839506, 0.687407407, 0.842074074]         # [x_1]print len(Total_Power), len(Throughput)

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

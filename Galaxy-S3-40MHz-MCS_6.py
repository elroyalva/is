# TODO add image and put this code into an appendix at the bottom
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import pylab
import statsmodels.api as sm
import numpy as np
# import airtime

#MCS6
P = [1127.23, 1130.25, 1127.62, 1130.21, 1125.79, 1126.56, 1129.74, 1131.56, 1145.18, 1154.23, 1160.62, 1161.26, 1160.23, 1162.31, 1163.21, 1166.21, 1182.35, 1186.56, 1190.36, 1194.79, 1193.62, 1190.23, 1189.23, 1194.58, 1260.28, 1266.57, 1268.07, 1271.51, 1269.22, 1272.32, 1272.95, 1271.79, 1275.98, 1277.68, 1279.52, 1277.52, 1279.97, 1286.45, 1284.24, 1287.58, 1283.21, 1287.49, 1294.54, 1292.45, 1297.45, 1307.23, 1311.47, 1319.46, 1299.49, 1303.77, 1300.54, 1314.22, 1321.49, 1329.72, 1334.12, 1344.25, 1315.55, 1320.23, 1319.11, 1321.84, 1319.52, 1322.88, 1326.74, 1319.49, 1324.18, 1333.38, 1325.95, 1339.56, 1349.16, 1353.45, 1347.25, 1350.27, 1401.38, 1408.75, 1410.32, 1411.49, 1416.8, 1418.55, 1421.72, 1414.55, 1425.22, 1427.79, 1436.78, 1438.07, 1447.09, 1451.75, 1452.17, 1456.46, 1440.23, 1455.23, 1459.32, 1461.89, 1470.85, 1482.25, 1477.19, 1452.13, 1458.3, 1468.33, 1467.79, 1466.39, 1477.32, 1472.89, 1479.17, 1488.32, 1474.23, 1483.34, 1493.08, 1490.31, 1488.23, 1490.36, 1498.77, 1501.32, 1509.9, 1512.36, 1520.32, 1518.3, 1530.11, 1527.09, 1530.39, 1495.03] # Total power
lambda_r = [100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 400, 400, 400, 400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 800, 800, 800, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3800, 3800, 3800, 3800, 3800, 3800, 3800, 3800, 4600, 4600, 4600, 4600, 4600, 4600, 4600, 4600, 5400, 5400, 5400, 5400, 5400, 5400, 5400, 5400, 6200, 6200, 6200, 6200, 6200, 6200, 6200, 6200, 7000, 7000, 7000, 7000, 7000, 7000, 7000, 7000, 7900, 7900, 7900, 7900, 7900, 7900, 7900, 7900]           # thruput [x_2]
tau_rx = [0.000658436, 0.001316872, 0.001975309, 0.003292181, 0.00526749, 0.006584362, 0.007901235, 0.009679012, 0.001316872, 0.002633745, 0.003950617, 0.006584362, 0.010534979, 0.013168724, 0.015802469, 0.019358025, 0.002633745, 0.00526749, 0.007901235, 0.013168724, 0.021069959, 0.026337449, 0.031604938, 0.038716049, 0.00526749, 0.010534979, 0.015802469, 0.026337449, 0.042139918, 0.052674897, 0.063209877, 0.077432099, 0.007901235, 0.015802469, 0.023703704, 0.039506173, 0.063209877, 0.079012346, 0.094814815, 0.116148148, 0.009876543, 0.019753086, 0.02962963, 0.049382716, 0.079012346, 0.098765432, 0.118518519, 0.145185185, 0.011851852, 0.023703704, 0.035555556, 0.059259259, 0.094814815, 0.118518519, 0.142222222, 0.174222222, 0.014485597, 0.028971193, 0.04345679, 0.072427984, 0.115884774, 0.144855967, 0.17382716, 0.212938272, 0.019753086, 0.039506173, 0.059259259, 0.098765432, 0.158024691, 0.197530864, 0.237037037, 0.29037037, 0.025020576, 0.050041152, 0.075061728, 0.125102881, 0.200164609, 0.250205761, 0.300246914, 0.367802469, 0.030288066, 0.060576132, 0.090864198, 0.151440329, 0.242304527, 0.302880658, 0.36345679, 0.445234568, 0.035555556, 0.071111111, 0.106666667, 0.177777778, 0.284444444, 0.355555556, 0.426666667, 0.522666667, 0.040823045, 0.081646091, 0.122469136, 0.204115226, 0.326584362, 0.408230453, 0.489876543, 0.600098765, 0.046090535, 0.09218107, 0.138271605, 0.230452675, 0.36872428, 0.46090535, 0.55308642, 0.677530864, 0.052016461, 0.104032922, 0.156049383, 0.260082305, 0.416131687, 0.520164609, 0.624197531, 0.764641975]         # [x_1]print len(Total_Power), len(Throughput)

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

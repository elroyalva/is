#_id + rho_rx * tau_rx + lambda_r*gamma_xr
# y =    c   +     w_0 * x_1   +    x_2 * w_1 

if __name__ == "__main__":

	#import airtime

	nFrames = 64
	basic_rate = 6.5

	
	#MCS 1
	print "MCS 1"
	MCS_Mbps = 13.0
	#T_L = airtime.T_total(nFrames, MCS_Mbps, basic_rate)
	P = [962.0633333, 959.3966667, 983.1366667, 984.44, 982.08, 989.213333, 990.82, 991.0066667, 964.6566667, 973.19, 998.4133333, 1001.533333, 1002.67, 1006.11, 1007.023333, 1014.923333, 993.41, 991.9833333, 1027.646667, 1016.236667, 1029.3, 1034.786667, 1037.856667, 1040.316667, 1029.43, 1036.236667, 1058.6, 1058.553333, 1068.72, 1077.016667, 1081.916667, 1091.706667, 1035.183333, 1066.943333, 1080.946667, 1082.723333, 1084.743333, 1092.72, 1099.563333, 1102.876667, 1039.706667, 1081.97, 1088.23, 1096.856667, 1098.683333, 1109.226667, 1106.553333, 1095.77, 1054.22, 1075.29, 1086.446667, 1094.183333, 1100.22, 1091.836667, 1094.226667, 1097.173333] # Total power
	lambda_r = [0.08, 0.16, 0.24, 0.4, 0.64, 0.8, 0.96, 1.176, 0.16, 0.32, 0.48, 0.8, 1.28, 1.6, 1.92, 2.352, 0.32, 0.64, 0.96, 1.6, 2.56, 3.2, 3.84, 4.704, 0.64, 1.28, 1.92, 3.2, 5.12, 6.4, 7.68, 9.408, 0.96, 1.92, 2.88, 3.84, 4.8, 5.76, 7.68, 9.6, 1.2, 2.4, 3.6, 4.8, 6, 7.2, 8.4, 9.6, 1.44, 2.88, 4.32, 5.76, 7.2, 8.64, 10.08, 10.8]           # thruput [x_2]
	tau_rx = [0.006956522, 0.013913043, 0.020869565, 0.034782609, 0.055652174, 0.069565217, 0.083478261, 0.10226087, 0.013913043, 0.027826087, 0.04173913, 0.069565217, 0.111304348, 0.139130435, 0.166956522, 0.204521739, 0.027826087, 0.055652174, 0.083478261, 0.139130435, 0.222608696, 0.27826087, 0.333913043, 0.409043478, 0.055652174, 0.111304348, 0.166956522, 0.27826087, 0.445217391, 0.556521739, 0.667826087, 0.818086957, 0.083478261, 0.166956522, 0.250434783, 0.333913043, 0.417391304, 0.500869565, 0.667826087, 0.834782609, 0.104347826, 0.208695652, 0.313043478, 0.417391304, 0.52173913, 0.626086957, 0.730434783, 0.834782609, 0.125217391, 0.250434783, 0.375652174, 0.500869565, 0.626086957, 0.751304348, 0.876521739, 0.939130435]         # [x_1]
	#replace tau_rx with column I from sheet
	
	
	"""
	#MCS 4 
	print "MCS 4"
	MCS_Mbps = 39
	#T_L = airtime.T_total(nFrames, MCS_Mbps, basic_rate)
	P = [983.68, 965, 987.34, 990.1, 991.2, 987.6, 994.1, 1000.26, 997.51, 997.63, 998.13, 996.35, 1000.16, 998.24, 999.79, 1002.39, 1014.87, 1016.58, 1021.73, 1025.97, 1030.83, 1029.34, 1033.7, 1035.39, 1052.68, 1046.32, 1066.96, 1071.61, 1073.94, 1072.22, 1074.56, 1072.64, 1071.32, 1069.34, 1079.18, 1072.9, 1073.4, 1078.63, 1076.69, 1093.65, 1071.74, 1081.72, 1078.86, 1091.23, 1098.8, 1091.77, 1092.18, 1092.01, 1084.88, 1090.33, 1096.41, 1092.61, 1090.61, 1096.66, 1097.56, 1106.68, 1090.53, 1090.14, 1096.53, 1101.58, 1109.53, 1112.5, 1110.34, 1108.64, 1091.32, 1096.65, 1099.67, 1105.93, 1108.69, 1106.45, 1116.58, 1112.2, 1102.93, 1104.3, 1107.5, 1109.65, 1116.5, 1113.89, 1107.9, 1101.99, 1105.56, 1110.72, 1117.96, 1120.33, 1123.03, 1118.48, 1123.29, 1118.19, 1110.02, 1118.32, 1116.45, 1117.77, 1119.6, 1123.5, 1122.46, 1127.83, 1115.5, 1121.15, 1123.47, 1132.36, 1134.42, 1130.74, 1132.8, 1130.41, 1120.74, 1127.66, 1134.27, 1129.53, 1138.6, 1133.2, 1129.2, 1136.4] # Total power
	lambda_r = [0.08, 0.16, 0.24, 0.4, 0.64, 0.8, 0.96, 1.176, 0.16, 0.32, 0.48, 0.8, 1.28, 1.6, 1.92, 2.352, 0.32, 0.64, 0.96, 1.6, 2.56, 3.2, 3.84, 4.704, 0.64, 1.28, 1.92, 3.2, 5.12, 6.4, 7.68, 9.408, 0.96, 1.92, 2.88, 4.8, 7.68, 9.6, 11.52, 14.112, 1.2, 2.4, 3.6, 6, 9.6, 12, 14.4, 17.64, 1.44, 2.88, 4.32, 7.2, 11.52, 14.4, 17.28, 21.168, 1.6, 3.2, 4.8, 8, 12.8, 16, 19.2, 23.52, 1.76, 3.52, 5.28, 8.8, 14.08, 17.6, 21.12, 25.872, 1.92, 3.84, 5.76, 9.6, 15.36, 19.2, 23.04, 28.224, 2.08, 4.16, 6.24, 10.4, 16.64, 20.8, 24.96, 30.576, 2.24, 4.48, 6.72, 11.2, 17.92, 22.4, 26.88, 32.928, 2.4, 4.8, 7.2, 9.6, 12, 19.2, 24, 28.8, 2.56, 5.12, 7.68, 10.24, 12.8, 20.48, 25.6, 30.72]           # thruput [x_2]
	tau_rx = [0.00238806, 0.004776119, 0.007164179, 0.011940299, 0.019104478, 0.023880597, 0.028656716, 0.035104478, 0.004776119, 0.009552239, 0.014328358, 0.023880597, 0.038208955, 0.047761194, 0.057313433, 0.070208955, 0.009552239, 0.019104478, 0.028656716, 0.047761194, 0.07641791, 0.095522388, 0.114626866, 0.14041791, 0.019104478, 0.038208955, 0.057313433, 0.095522388, 0.152835821, 0.191044776, 0.229253731, 0.280835821, 0.028656716, 0.057313433, 0.085970149, 0.143283582, 0.229253731, 0.286567164, 0.343880597, 0.421253731, 0.035820896, 0.071641791, 0.107462687, 0.179104478, 0.286567164, 0.358208955, 0.429850746, 0.526567164, 0.042985075, 0.085970149, 0.128955224, 0.214925373, 0.343880597, 0.429850746, 0.515820896, 0.631880597, 0.047761194, 0.095522388, 0.143283582, 0.23880597, 0.382089552, 0.47761194, 0.573134328, 0.702089552, 0.052537313, 0.105074627, 0.15761194, 0.262686567, 0.420298507, 0.525373134, 0.630447761, 0.772298507, 0.057313433, 0.114626866, 0.171940299, 0.286567164, 0.458507463, 0.573134328, 0.687761194, 0.842507463, 0.062089552, 0.124179104, 0.186268657, 0.310447761, 0.496716418, 0.620895522, 0.745074627, 0.912716418, 0.066865672, 0.133731343, 0.200597015, 0.334328358, 0.534925373, 0.668656716, 0.80238806, 0.982925373, 0.071641791, 0.143283582, 0.214925373, 0.286567164, 0.358208955, 0.573134328, 0.71641791, 0.859701493, 0.07641791, 0.152835821, 0.229253731, 0.305671642, 0.382089552, 0.611343284, 0.764179104, 0.917014925]         # [x_1]
	"""
	
	"""
	#MCS 6
	print "MCS 6"
	MCS_Mbps = 58.5
	#T_L = airtime.T_total(nFrames, MCS_Mbps, basic_rate)
	P = [969.66, 975.39, 979.45, 984.37, 988.74, 989.71, 990.64, 991.56, 982.56, 984.5, 985.16, 988.17, 985.7, 986.74, 987.46, 989.37, 1007.68, 1016.4, 1015.24, 1017.74, 1021.2, 1022.31, 1020.59, 1023.87, 1031.52, 1037.64, 1042.63, 1043.06, 1045.53, 1044.37, 1047.22, 1048.66, 1032.39, 1046.41, 1049.65, 1051.35, 1053.67, 1064.49, 1068.66, 1070.47, 1052.39, 1063.84, 1075.23, 1077.54, 1085.9, 1079.11, 1088.88, 1096.43, 1080.93, 1088.47, 1085.34, 1093.73, 1095.8, 1096.21, 1100.35, 1108.43, 1088.92, 1090.21, 1098.45, 1102.35, 1104.8, 1106.86, 1108.46, 1106.54, 1102.43, 1103.46, 1106.41, 1112.36, 1116.46, 1118.21, 1119.93, 1118.46, 1103.21, 1108.46, 1113.09, 1109.65, 1111.94, 1116.74, 1119.56, 1121.64, 1115.61, 1120.9, 1124.32, 1126.1, 1131.6, 1126.87, 1114.32, 1116.07, 1129.56, 1131.56, 1137.93, 1133.72, 1129.68, 1132.41, 1123.66, 1124.69, 1146.89, 1147.73, 1150.73, 1143.66, 1145.23, 1146.88, 1148.65, 1130.41, 1165.04, 1165.23, 1167.07, 1152.21, 1151.4, 1144.17, 1148.23, 1146.23] # Total power
	lambda_r = [0.08, 0.16, 0.24, 0.4, 0.64, 0.8, 0.96, 1.176, 0.16, 0.32, 0.48, 0.8, 1.28, 1.6, 1.92, 2.352, 0.32, 0.64, 0.96, 1.6, 2.56, 3.2, 3.84, 4.704, 0.64, 1.28, 1.92, 3.2, 5.12, 6.4, 7.68, 9.408, 0.96, 1.92, 2.88, 4.8, 7.68, 9.6, 11.52, 14.112, 1.2, 2.4, 3.6, 6, 9.6, 12, 14.4, 17.64, 1.44, 2.88, 4.32, 7.2, 11.52, 14.4, 17.28, 21.168, 1.6, 3.2, 4.8, 8, 12.8, 16, 19.2, 23.52, 1.92, 3.84, 5.76, 9.6, 15.36, 19.2, 23.04, 28.224, 2.24, 4.48, 6.72, 11.2, 17.92, 22.4, 26.88, 32.928, 2.56, 5.12, 7.68, 12.8, 20.48, 25.6, 30.72, 37.632, 2.88, 5.76, 8.64, 14.4, 23.04, 28.8, 34.56, 42.336, 3.2, 6.4, 9.6, 16, 25.6, 32, 38.4, 44.8, 3.52, 7.04, 10.56, 14.08, 17.6, 28.16, 35.2, 46.464]           # thruput [x_2]
	tau_rx = [0.001367521, 0.00344086, 0.00516129, 0.008602151, 0.013763441, 0.017204301, 0.020645161, 0.025290323, 0.00344086, 0.00688172, 0.010322581, 0.017204301, 0.027526882, 0.034408602, 0.041290323, 0.050580645, 0.00688172, 0.013763441, 0.020645161, 0.034408602, 0.055053763, 0.068817204, 0.082580645, 0.10116129, 0.013763441, 0.027526882, 0.041290323, 0.068817204, 0.110107527, 0.137634409, 0.16516129, 0.202322581, 0.020645161, 0.041290323, 0.061935484, 0.103225806, 0.16516129, 0.206451613, 0.247741935, 0.303483871, 0.025806452, 0.051612903, 0.077419355, 0.129032258, 0.206451613, 0.258064516, 0.309677419, 0.379354839, 0.030967742, 0.061935484, 0.092903226, 0.15483871, 0.247741935, 0.309677419, 0.371612903, 0.455225806, 0.034408602, 0.068817204, 0.103225806, 0.172043011, 0.275268817, 0.344086022, 0.412903226, 0.505806452, 0.041290323, 0.082580645, 0.123870968, 0.206451613, 0.330322581, 0.412903226, 0.495483871, 0.606967742, 0.048172043, 0.096344086, 0.144516129, 0.240860215, 0.385376344, 0.48172043, 0.578064516, 0.708129032, 0.055053763, 0.110107527, 0.16516129, 0.275268817, 0.440430108, 0.550537634, 0.660645161, 0.809290323, 0.061935484, 0.123870968, 0.185806452, 0.309677419, 0.495483871, 0.619354839, 0.743225806, 0.910451613, 0.068817204, 0.137634409, 0.206451613, 0.344086022, 0.550537634, 0.688172043, 0.825806452, 0.96344086, 0.075698925, 0.151397849, 0.227096774, 0.302795699, 0.378494624, 0.605591398, 0.756989247, 0.999225806]         # [x_1]
	#replace tau_rx with column I from sheet
	"""

	X = []
	for index in range(0,len(tau_rx)):
		row = []
		row.append(tau_rx[index])
		row.append(lambda_r[index])
		X.append(row)

	from sklearn import linear_model
	
	clf = linear_model.Ridge(alpha = .5)
	clf.fit(X,P)
	print clf.coef_
	print clf


import numpy as np

data = []

s1 = [[1,2,3],[2,3,4]]
s2 = [[903,23,23],[52,73,84]]
s3 = np.array(s1)
s4 = np.array(s2)

data.append(s3)
data.append(s4)

data_np = np.array(data)

print(type(s1))
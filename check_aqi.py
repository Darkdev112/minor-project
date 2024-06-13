import h5py

with h5py.File('aqi.h5', 'r') as f:
    aqi1 = f['aqi1'][:]
    aqi2 = f['aqi2'][:]
    aqi3 = f['aqi3'][:]

print('aqi1 :',aqi1.shape)
print('aqi2 :',aqi2.shape)
print('aqi3 :',aqi3.shape)



import matplotlib.pyplot as plt
import numpy as np 
xpoints = np.array(['1-1','2-1','3-1','4-1','5-1','6-1','7-1','8-1','9-1','10-1','11-1','12-1','13-1','14-1','15-1','16-1','17-1','18-1','19-1','20-1','21-1'])
ypoints = np.array([0,10.9,0.8,20.3,1.3,2.5,0,0,0,4.1,5.3,2.5,8.1,19.8,15.2,13.5,3,6.1,0,8.6,4.8])
plt.plot(xpoints, ypoints) 
plt.show()
plt.close()
import matplotlib.pyplot as plt
import numpy as np
acc_data = np.loadtxt("acc.txt")
mag_data = np.loadtxt("magn.txt")

plot1 = plt.figure(1)
plt.plot(acc_data[:,0], acc_data[:,1], '.', acc_data[:,0], acc_data[:,2],'.' ,acc_data[:,1], acc_data[:,2], '.')
plt.grid()

plot3 = plt.figure(3)
plt.plot(mag_data[:,0], mag_data[:,1], '.', mag_data[:,0], mag_data[:,2],'.' ,mag_data[:,1], mag_data[:,2], '.')


acc_off_x = 0.12187561755180452
acc_off_y =  -0.03042032238066657
acc_off_z =  -0.010204560937592139

acc_scale_x = 0.6676820770956592
acc_scale_y = 1.0382231685223033
acc_scale_z = 1.1490605875002575

mag_off_x = 0.8895519691843171
mag_off_y =  18.962751211663612
mag_off_z =  23.858323053599666

mag_scale_x = 34.2572367490163
mag_scale_y = 33.98348550824384
mag_scale_z = 31.33994407313422

plot2 = plt.figure(2)
plt.plot(((acc_data[:,0]-acc_off_x)*acc_scale_x), ((acc_data[:,1]-acc_off_y)*acc_scale_y),'.', ((acc_data[:,0]-acc_off_x)*acc_scale_x),((acc_data[:,2]-acc_off_z)*acc_scale_z),'.', ((acc_data[:,1]-acc_off_y)*acc_scale_y), ((acc_data[:,2]-acc_off_z)*acc_scale_z),'.')

plot4 = plt.figure(4)
plt.plot(((mag_data[:,0]-mag_off_x)*mag_scale_x), ((mag_data[:,1]-mag_off_y)*mag_scale_y),'.', ((mag_data[:,0]-mag_off_x)*mag_scale_x),((mag_data[:,2]-mag_off_z)*mag_scale_z),'.', ((mag_data[:,1]-mag_off_y)*mag_scale_y), ((mag_data[:,2]-mag_off_z)*mag_scale_z),'.')

plt.grid()
plt.show()
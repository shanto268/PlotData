import matplotlib.pyplot as plt
import datetime
import numpy as np
from numpy import matrix
with open('DataLog(C).txt', 'r') as f:
        
        lines = f.readlines()
        dates = [str(line.split()[0]) for line in lines]
        desired_lines = lines[0:4000:16]
        datesc = [str(line.split()[0]) for line in desired_lines]
        y = [float(line.split()[1]) for line in lines]
        z = [float(line.split()[3]) for line in lines]
        w = [float(line.split()[2]) for line in lines]
        date = [datetime.datetime.strptime(x,'%m/%d/%Y-%H:%M:%S') for x in dates]
        plt.subplot(3,1,1)
        #yc = [float(line.split()[2]) for line in desired_lines]
        #zc = [float(line.split()[4]) for line in desired_lines]
        #wc = [float(line.split()[6]) for line in desired_lines]
        #datec = [datetime.datetime.strptime(x,'%m/%d/%Y-%H:%M:%S') for x in datesc]



with open('DataLog(B).txt', 'r') as s:
        lines = s.readlines()
        datesp = [str(line.split()[0]) for line in lines]
              
      #  yp = [float(line.split(",")[1]) for line in lines]
      #  zp = [float(line.split(",")[2]) for line in lines]
      #  wp = [float(line.split(",")[3]) for line in lines]
      #  datep = [datetime.datetime.strptime(x,'%m/%d/%Y-%H:%M:%S') for x in datesp]
        
        
        desired_lines = lines[0:4000:16]
        datesc = [str(line.split()[0]) for line in desired_lines]
        y = [float(line.split()[1]) for line in lines]
        z = [float(line.split()[3]) for line in lines]
        w = [float(line.split()[2]) for line in lines]
        date = [datetime.datetime.strptime(x,'%m/%d/%Y-%H:%M:%S') for x in dates]
        plt.subplot(3,1,1)
        #yc = [float(line.split()[2]) for line in desired_lines]

        #yd = np.subtract(yp, yc)
        #zd = np.subtract(zp, zc)
        #wd = np.subtract(wp, wc)
        
        plt.title('Temperature & Humidity')
        plt.ylabel('Temperature' + u'\u2103')
        plt.plot(date, y, 'r.-',color="red")
        plt.plot(datep, yp, 'r.-', color='blue')
        plt.grid(True)
        

        plt.subplot(3,1,2)
        plt.plot_date(date, z, 'b.-',color='red')
        plt.plot(datep, zp, 'r.-', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Humidity RH%'.decode('unicode-escape'))
        plt.grid(True)
        
        plt.subplot(3,1,3)
        plt.plot_date(date, w, 'b.-', color='red')
        plt.plot(datep, wp, 'r.-', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Pressure KPA'.decode('unicode-escape'))
        plt.grid(True)
        
    
        
        

plt.show()

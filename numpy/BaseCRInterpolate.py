
import numpy as np
from scipy import interpolate


# Define the three data points
x = np.array([2, 5, 10,15])
y = np.array([3.05,4.57, 6.1,7.62,9.14])
z= np.array([[0.08,0.15,0.51,1.14],
            [0.1,0.23,0.69,1.78],
            [0.13,0.3,0.89,2.54],
            [0.2,0.38,1.09,3.81],
            [0.28,0.46,1.27,5.08]])


x_interp = float(input("Enter NH4Hs: "))
y_interp = float(input("Enter Velocity: "))

interp_func = interpolate.interp2d(x, y, z)
z_interp = interp_func(x_interp, y_interp)

#z_interp = np.interp(x_interp, x, z) + np.interp(y_interp, y, z)
print(f"Baseline CR = {z_interp}")

# Print the interpolated value


#for ampo in range (1,15):
    # Define the point at which you want to interpolate the value
 #   x_interp=ampo
    # Interpolate the value using linear interpolation
  #  y_interp = np.interp(x_interp, x, y)
   # print (f"{ampo} = {y_interp}")

import numpy as np
from scipy import interpolate


# Define the three data points
x = np.array([4.75, 5.25, 5.75,6.25,6.75])
y = np.array([38,52, 79,93])
z= np.array([[0.03,0.02,0.01,0.01,0.01],
            [0.08,0.05,0.04,0.03,0.01],
            [0.13,0.08,0.05,0.04,0.02],
            [0.18,0.1,0.08,0.05,0.03]])


x_interp = float(input("Enter pH: "))
y_interp = float(input("Enter Temperature: "))

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
import matplotlib.pyplot as plt
import numpy as np

#x_length = [70, 90, 93.1, 115, 120, 125, 130, 135, 144]    #black bars
#y_frequency = [1501, 936, 869, 587, 538, 488, 460, 429, 379] #measured frequency from black bars

#Fill in aquired lengths and frequency for your 13 bars.
x_length = [74.5, 79.2, 84.1, 86.8, 92.1, 97.8, 103.9, 107.1, 113.7, 120.9, 125, 133, 140] #white bars
y_frequency = [1371, 1219, 1072, 1020, 920, 820, 724, 671, 601, 545, 510, 451, 398] #measured frequency from white bars

xn = xn = np.linspace(70, 145, 750)

popt = np.polyfit(x_length, y_frequency, 4)
print(popt)

#yn_black = np.polyval(popt, xn)
#yn_white =0.9867*yn_black #factor for filament conversion, will differ between different filaments.
yn = np.polyval(popt, xn)
plt.plot(x_length, y_frequency, 'or')
plt.plot(xn, yn)
plt.show()

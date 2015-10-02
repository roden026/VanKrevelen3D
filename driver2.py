'''
Takes a csv as an input and works through the compounds to extract the number of C, H, and O 
present. Then calculates the ratios of H:C and O:C and plots them. 
'''
import sys
import os
from extractNeededElementalData import extractNeededElementalData
from processElementalData import processElementalData
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import six
import dateutil

usage_mesg = 'driver2.py <csv file(s)>'

# Checks if files are available.
filename_csv = sys.argv[1]
if( not os.access(filename_csv,os.R_OK) ):
    print "%s is not accessible."%filename_csv
    print usage_mesg
    sys.exit(1)

# Checks to see if you want to test pos and neg or just one or the other
#***** see if this is needed ****
if(len(sys.argv) == 2 ):
    filename_csv = sys.argv[1]
    elementalList = extractNeededElementalData(filename_csv)
    ratiosList = processElementalData(elementalList)
    #Note, at this point the elementalList and ratiosList will not be aligned
    #because the processing of the ratios removes lines where not all 3 elements
    #were present (rare occurance but may happen)

# Creates the actual graph itself.	

print "Displaying plot"
	
# Graphs the data provided and labels axes

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
fig.suptitle('3D Van Krevelen Diagram', fontsize = 14, fontweight = 'bold')

ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('O:C Ratio')
ax.set_ylabel('H:C Ratio')
ax.set_zlabel('N:C Ratio')

ax.scatter(ratiosList[1], ratiosList[0], ratiosList[2], zdir=u'z', s = 20)
plt.show()


'''
area = 10.0

fig = plt.figure()
fig.suptitle('Van Krevelen Diagram', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

ax.set_xlabel('O:C Ratio')
ax.set_ylabel('H:C Ratio')

ax.scatter(ratiosList[1], ratiosList[0], s=area, alpha = .25)
ax.axis([0, 1.25, 0, 2.5])

plt.show()
'''
print("done")
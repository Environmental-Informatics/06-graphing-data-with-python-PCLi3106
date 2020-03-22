"""
Created on Thu Mar 12 16:30:20 2020
@author: Pin-Ching Li
This script is created to load files with Numpy command and visualize it.
The output format is pdf and with only one page containing all the graphs. 
Code can be rerun with different input name
"""
# import numpy
import numpy as np
import matplotlib.pyplot as plt
# Draw plots and export plots as pdf file in one page
# store plots for exporting in one page
import matplotlib.gridspec as gridspec
# export plots to pdf file
from matplotlib.backends.backend_pdf import PdfPages

# Let users input the filename 
in_name = input('Please insert name of your .txt file without .txt \n file needs to be stored in current folder\n')
filename_in = in_name + '.txt'
# Create output filename based on input name
filename_out= in_name + '.pdf'
#read file by numpy.genfromtxt
Annual_Metrics = np.genfromtxt(filename_in, dtype=['int','float','float','float','float','float','float'],
                      names = True)

# Plot for WC
# filename of pdf
pp = PdfPages(filename_out)
# three plots a page
gs = gridspec.GridSpec(3, 1)

# first plot
ax1 = plt.subplot(gs[0])
# Plot of mean,max,min of streamflow
# create figure and axis of plot
# plot three lines
plt.plot(Annual_Metrics['Year'],Annual_Metrics['Mean'],label= 'Mean',color='k')
plt.plot(Annual_Metrics['Year'],Annual_Metrics['Max'] ,label= 'Max' ,color='r')
plt.plot(Annual_Metrics['Year'],Annual_Metrics['Min'] ,label= 'Min' ,color='b')
# add title of plot
plt.title('Annual Metrics')
# add legend of plot
plt.legend(loc='upper left',ncol=3,bbox_to_anchor=(0, 1.4))
# add the label of x and y axis
plt.xlabel('Year')
plt.ylabel('Streamflow(cfs)')

# second plot
ax2 = plt.subplot(gs[1])
# multiple Tqmean with 100
TQ = Annual_Metrics['Tqmean']*100
# draw scatter plot (plot with symbols)
plt.scatter(Annual_Metrics['Year'],TQ)
plt.title('Tqmean')
plt.xlabel('Year')
plt.ylabel('Tqmean (%)')
# third plot
ax3 = plt.subplot(gs[2])
# draw bar plot
plt.bar(Annual_Metrics['Year'],Annual_Metrics['RBindex'])
# add title
plt.title('R-B Index')
# add label of x and y axis
plt.xlabel('Year')
plt.ylabel('R-B Index (ratio)')
# split plots in case they are overlapped
plt.tight_layout()
# save as pdf
pp.savefig(papertype = 'a4')
pp.close()

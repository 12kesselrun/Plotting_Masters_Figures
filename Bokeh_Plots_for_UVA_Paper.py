# Reads and Plots MAT data for Attacks 1-4
def readFirstFourAttacks():
    attacks=['SHD_XY','Solid_XY','Solid_XZ','Solid_XZ_with_Notch','Solid_XZ_with_Seam']
    # Create a dictionary to store each figure
    f={}
    legendColors=['navy','olive','firebrick','orange','purple','red']
    titles=['Density Adjustment','Orientation Change','Control Specimen','Notch Insertion','Seam Placement']
    i=int(1)
    # Load the mat file for each temperature
    mat = sio.loadmat('Tensile_Test_Data.mat')
    # Iterate through attacks
    for x in attacks:
        # Format the Bokeh plots for the temperature graphs
        f[x]= figure(width=900, plot_height=600, title=titles[i-1] + ' ASTM D638 Results',x_axis_label='Strain',y_axis_label='Stress',x_range=(0,0.0825), y_range=(0,34))
        output_file("Attack_"+str(i)+"_"+x+".html")
        f[x].title.text_font='Segoe UI'
        f[x].title.text_font_size='26pt'
        f[x].title.align='center'
        f[x].xaxis.axis_label_text_font_size='26pt'
        f[x].xaxis.major_label_text_font_size='24pt'
        f[x].yaxis.axis_label_text_font_size='26pt'
        f[x].yaxis.major_label_text_font_size='24pt'
        nums=np.array([[0,1,2,3,4,5],[None,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,4,5,None],[0,1,2,3,4,5]])
        # Iterate through all five specimens
        for specimen in nums[i-1,:]:
            if specimen!=None:
                # Assign values for stress and strain from the MAT file
                stress=mat[x]['stress'][0][0][:,specimen]
                strain=mat[x]['strain'][0][0][:,specimen]
                f[x].line(strain,stress, legend=None, line_width=1,line_color=legendColors[specimen])
        i=i+1
        # Write output files
        outputWrite='Plot_'+x+'.png'
        # export_png(p,filename=outputWrite)
        print("Finished Writing File: "+outputWrite)
        reset_output()
        # Debugging
        show(f[x])

# Reads and Plots MAT data for Attack 5
def readTempData():
    stress=[[]]
    strain=[[]]
    attacks=['190C','200C','210C','220C','230C']
    legendColors=['navy','olive','firebrick','orange','purple']
    i=int(1)
    # Iterate through all 5 temperature attacks (190C-230C)
    p = figure(width=900, plot_height=600, title='Temperature Attacks', x_axis_label='Strain', y_axis_label='Stress (MPa)', x_range=(0,0.0225), y_range=(0,34))
    # Format the Bokeh plots for the temperature graphs
    output_file("Attack_5.html")
    p.title.text_font='Segoe UI'
    p.title.text_font_size='26pt'
    p.title.align='center'
    p.xaxis.axis_label_text_font_size='26pt'
    p.xaxis.major_label_text_font_size='24pt'
    p.yaxis.axis_label_text_font_size='26pt'
    p.yaxis.major_label_text_font_size='24pt'
    p.min_border=35
    for x in attacks:
        # Load the mat file for each temperature
        mat = sio.loadmat('Attack_5_'+x+'.mat')
        # Iterate through all five specimens
        # Assign values for stress and strain from the MAT file
        stress[i-1]=np.matrix(mat['Temp_Test_Batch_'+str(i)+'_'+x]['stress'][0][0]).mean(1)
        strain[i-1]=np.matrix(mat['Temp_Test_Batch_'+str(i)+'_'+x]['strain'][0][0]).mean(1)
        i=i+1
    p.line(strain,stress, legend=None, line_width=1)
    # Write output files
    outputWrite='Plot.png'
    show(p)
    # export_png(p,filename=outputWrite)
    print("Finished Writing File: "+outputWrite)
    reset_output()
    # export_png(l,filename='Gridplot.png')
'''
Bokeh_Plots_for_UVA_Paper.py
Notes:
- This code plots the MATLAB data files saved from
- Move this python code into the working directory and change the "fileName" variable in the "Constants" section below

Install Requirements:
- Python 3.6 or newer
- NumPy
- Bokeh
- SciPy
- OS
'''
# Import Libraries
from bokeh.plotting import figure, output_file, show, reset_output, gridplot
from bokeh.io import export_png
import scipy.io as sio
import os
import numpy as np
# Prep the system
os.system('cls')

################################################################################
######                                MAIN                                ######
################################################################################

# readFirstFourAttacks()
readTempData()

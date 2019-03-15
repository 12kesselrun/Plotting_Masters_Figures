# Reads and Plots MAT data for Attacks 1-4
def NotchAndSeamAttacks():
    attacks=['Solid_XZ','Solid_XZ_with_Notch','Solid_XZ_with_Seam']
    # Create a dictionary to store each figure
    f={}
    legendColors=['navy','olive','firebrick','orange','purple','red']
    titles=['On-Edge Control Specimen','Notch Insertion','Seam Placement']
    i=int(1)
    # Load the mat file for all of the attacks
    mat = sio.loadmat('Tensile_Test_Data.mat')
    # Iterate through attacks
    for x in attacks:
        # Format the Bokeh plots for the temperature graphs
        f[x]= figure(width=900, plot_height=600, title=titles[i-1] + ' ASTM D638 Results',x_axis_label='Strain',y_axis_label='Stress (MPa)',x_range=(0,0.0825), y_range=(0,34))
        output_file("Attack_"+str(i)+"_"+x+".html", mode='inline')
        f[x].title.text_font='Segoe UI'
        f[x].title.text_font_size='26pt'
        f[x].title.align='center'
        f[x].xaxis.axis_label_text_font_size='26pt'
        f[x].xaxis.major_label_text_font_size='24pt'
        f[x].yaxis.axis_label_text_font_size='26pt'
        f[x].yaxis.major_label_text_font_size='24pt'
        nums=np.array([[0,1,2,3,4,5],[0,1,2,4,5,None],[0,1,2,3,4,5]])
        # Iterate through all five specimens (nums designates which specimens are being used for each attack case)
        for specimen in nums[i-1,:]:
            if specimen!=None:
                # Assign values for stress and strain from the MAT file. The mean() function averages the data for each specimen to show only one solid line
                stressMatrix=np.matrix(mat[x]['stress'][0][0]).mean(1).tolist() # Average across the specimens using the numpy matrix mean() function then strip of matrix notation
                stress=[x[0] for x in stressMatrix]                             # Reorient the matrix from N-by-1 to 1-by-N
                strainMatrix=np.matrix(mat[x]['strain'][0][0]).mean(1).tolist()
                strain=[x[0] for x in strainMatrix]
        f[x].line(strain,stress, legend=None, line_width=1,line_color='blue')
        i=i+1
        # Write output files
        # outputWrite='Plot_'+x+'.png'
        # export_png(f[x],filename=outputWrite)
        # print("Finished Writing File: "+outputWrite)
        # Debugging
        show(f[x])
        reset_output()

# Reads and Plots MAT data for Attack 5
def readTempData():
    # Initialize data structures to overlay data from each temperature case on this graph
    stress=[[],[],[],[],[]]
    stressMatrix=[[],[],[],[],[]]
    strain=[[],[],[],[],[]]
    strainMatrix=[[],[],[],[],[]]
    attacks=['190C','200C','210C','220C','230C']
    legendColors=['blue','orange','black','olive','red']
    dashing=['solid','solid','solid','dashed','dashed']
    i=int(1)
    # Iterate through all 5 temperature attacks (190C-230C)
    p = figure(width=900, plot_height=600, title='Temperature Change ASTM D638 Results', x_axis_label='Strain', y_axis_label='Stress (MPa)', x_range=(0,0.0175), y_range=(0,34))
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

    # Load the attack case files into an array
    for x in attacks:
        # Load the mat file for each temperature
        mat = sio.loadmat('Attack_5_'+x+'.mat')
        # Iterate through all five specimens
        # Assign values for stress and strain from the MAT file (probably don't need the indexing; could have just overwritten the stress variable each time - live and learn :)
        stressMatrix[i-1]=np.matrix(mat['Temp_Test_Batch_'+str(i)+'_'+x]['stress'][0][0]).mean(1).tolist()
        stress[i-1]=[x[0] for x in stressMatrix[i-1]]
        strainMatrix[i-1]=np.matrix(mat['Temp_Test_Batch_'+str(i)+'_'+x]['strain'][0][0]).mean(1).tolist()
        strain[i-1]=[x[0] for x in strainMatrix[i-1]]
        i=i+1
    for j in range(5):
        p.line(strain[j],stress[j], legend=attacks[j], line_width=2, line_color=legendColors[j], line_dash = dashing[j])
        p.legend.glyph_width=125
        p.legend.label_text_font_size='18pt'
        p.legend.label_height=35
        p.legend.glyph_height=35
        p.legend.location='bottom_right'
    # Write output files
    outputWrite='Plot_Temp_Attack.png'
    # show(p)
    export_png(p,filename=outputWrite)
    print("Finished Writing File: "+outputWrite)
    reset_output()
    # export_png(l,filename='Gridplot.png')
'''
Bokeh_Plots_for_UVA_Paper.py
Notes:
- This code plots the MATLAB data files saved from my Master's Tensile Testing
- Move this python code into the working directory

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

NotchAndSeamAttacks()
# readTempData()

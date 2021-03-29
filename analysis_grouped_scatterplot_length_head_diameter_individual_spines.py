import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="white")


#load the data in; set to either iSPN or dSPN
individual_spine_features = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Part_Diameter_by_individual_spines.xlsx', sheet_name='iSPNs')

#make the plot
g = sns.relplot(x='spine_neck_diameter', y='spine_head_diameter', hue='genotype', palette="cubehelix", data=individual_spine_features)
g.fig.suptitle('Het iSPN vs. WT iSPN')
#g.savefig('/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/python_spine_analyses/seaborn_individual_spines_dSPN_spinenecklength_spineheaddiameter') 
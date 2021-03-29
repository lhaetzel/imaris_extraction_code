import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="white")


#load the data in; set to either iSPN or dSPN
spine_features = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/average_values_compiled.xlsx', sheet_name='iSPNs')

#make the plot
g = sns.relplot(x='spine_part_length_neck', y='spine_part_diameter_head', hue='genotype', palette="cubehelix", data=spine_features)
g.fig.suptitle('Het iSPN vs. WT iSPN')
g.savefig('/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/python_spine_analyses/seaborn_iSPN_spinenecklength_spineheaddiameter') 
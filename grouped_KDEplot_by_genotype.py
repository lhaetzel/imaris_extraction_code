import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="white")


#load the data in; set to either iSPN or dSPN
spine_features = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/average_values_compiled.xlsx', sheet_name='iSPNs')

#make the plot
g = sns.jointplot(data=spine_features, x='spine_length_mean', y='spine_part_diameter_head', hue='genotype', kind ='kde')
g.savefig('/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/python_spine_analyses/iSPN_spinelengthmean_spineheaddiameter_jointplot') 
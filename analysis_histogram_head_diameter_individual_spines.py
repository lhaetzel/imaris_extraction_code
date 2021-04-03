import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="white")

#load the data in; set to either iSPN or dSPN
individual_spine_features = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad_School/Rotations/Bateup Lab/Imaris_Export/individual_spines/individual_spine_values_compiled.xlsx', sheet_name = 'dSPNs')

g = sns.displot(individual_spine_features, x="Spine Part Mean Diameter Head", hue="genotype", kde = 'true')
g.savefig('/Users/lhaetzel/Desktop/Grad_School/Rotations/Bateup Lab/python_spine_analyses/dSPNs_histogram_head_diameter_indiv_spines') 
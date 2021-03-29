import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="dark")

individual_spine_features = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Part_Diameter_by_individual_spines.xlsx', sheet_name='iSPNs')


# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x='spine_length', y='spine_head_diameter', data = individual_spine_features, hue = 'genotype', s=5, color=".15")
sns.histplot(x='spine_length', y='spine_head_diameter', data = individual_spine_features, hue = 'genotype', bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x='spine_length', y='spine_head_diameter',data = individual_spine_features, hue = 'genotype', levels=5, color="w", linewidths=1)
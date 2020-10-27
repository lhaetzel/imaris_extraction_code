import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#import PCA data
pca_df = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/average_values_compiled.xlsx', sheet_name='PCA')

features = ['spine_density','spine_area_mean','spine_diameter_mean','spine_length_mean','spine_part_length_ground','spine_part_length_head','spine_part_length_neck','spine_part_diameter_ground','spine_part_diameter_head','spine_part_diameter_neck','spine_volume_mean']

# Separating out the features
x = pca_df.loc[:, features].values

# Separating out the target
y = pca_df.loc[:,['genotype']].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

#pca projection onto 2D

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

#final dataframe before plotting the data
finalDf = pd.concat([principalDf, pca_df[['genotype']]], axis = 1)

#visualize 2D projection

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('Het dSPN vs. WT dSPN (all spine features)', fontsize = 20)
targets = [ 'HETD2-', 'WTD2-']
colors = ['r', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['genotype'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)

fig.savefig('/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/python_PCA_analyses/dSPN_allfeatures.png')
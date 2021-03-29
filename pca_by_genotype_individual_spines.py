import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#import PCA data
pca_df = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/individual_spines/individual_spine_values_compiled.xlsx')

features = ['Spine Area','Spine Orientation Angle','Spine Part Mean Diameter Ground','Spine Part Mean Diameter Head','Spine Part Mean Diameter Neck','Spine Part Length Ground','Spine Part Length Head','Spine Part Length Neck','Spine Straightness','Spine Volume']
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
ax.set_title('WT iSPN', fontsize = 20)
targets = [ 'WTD2+']
colors = ['b','r']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['genotype'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)


fig.savefig('/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/python_spine_analyses/WT_iSPN_individual_spines_allfeatures.png')
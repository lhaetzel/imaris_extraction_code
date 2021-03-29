
# Importing Modules
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Loading dataset
individual_spine_features_df = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/individual_spines/individual_spine_values_compiled.xlsx', sheet_name='tSNE')
individual_spine_features_df = individual_spine_features_df.set_index(individual_spine_features_df.columns[0])



# Defining Model
model = TSNE(learning_rate=100)

individual_spine_features_df.target = individual_spine_features_df.columns
individual_spine_features_df.data = individual_spine_features_df

# Fitting Model
transformed = model.fit_transform(individual_spine_features_df.data)

# Plotting 2d t-Sne
x_axis = transformed[:, 0]
y_axis = transformed[:, 1]

plt.scatter(x_axis, y_axis, c=individual_spine_features_df.target)
plt.show()


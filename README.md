# imaris_extraction

Contains the code to extract spine features from the imaris statistics export. Imaris generates a folder for each cell analyzed. Each folder contains multiple .csv files. There is one .csv file per feature analyzed for that cell (e.g. spine density, spine diameter, spine length etc.). In order to easily extract these features, you need to loop over all the folders and then extract the parameter of interest from the .csv file within the folder. Depending on the parameter you're interested in, the .csv file is formatted differently. Therefore, a different function is needed for each parameter.

The different functions can be found in this repository. They are currently designed to be run out of a Jupyter Notebook or the Python Interactive console in VS Code. They will save an excel file to a folder you specify, so make sure all of the paths are formated correctly. Some functions also require a list of cells by genotype to be imported from a spreadsheet. 

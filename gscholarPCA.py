import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from removeZero import removeZero
from binSalary import binSalary
from convertPos import convertPos
from convertAff import convertAff
from filterOutlier import filterOutlier
from mpl_toolkits.mplot3d import Axes3D
### Import CSV file 
df = pd.read_csv('salary_gscholar_Washington.csv')

### Filter out rows with empty Google Scholar
df.dropna(how='any', inplace=True)
df = df.reset_index()

### Convert Position to Ordinals
df = convertPos(df)


### Convert Affiliation to Ordinals
df = convertAff(df)

##### Filter out zeroes
df_2012, df_2013, df_2014, df_2015, df_2016 = removeZero(df)

### Filter out Outliers

##df_filt = filterOutlier(df)

### Bin salaries
df_2014 = binSalary(df_2014)


### Standardize data (feature scaling)
from sklearn.preprocessing import StandardScaler
features = ['h-index', '5 year h-index', '5 year i10-index', 'i10-index', 'Total Citations', 'Affiliation', 'Position']
x = df_2014.loc[:, features].values
##y = df_2014.loc[:,['2014']].values
x = StandardScaler().fit_transform(x)

### PCA projection to 2D
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df_2014[['2014']]], axis = 1)

print finalDf

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
##ax = Axes3D(fig)

ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
##ax.set_zlabel('Principal Componen 3', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['IC Class1', 'IC Class2', 'IC Class3', 'IC Class4', 'IC Class5']
colors = ['r', 'g', 'b', 'y', 'm']
sz = 10
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['2014'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
plt.show()

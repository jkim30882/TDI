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
##df = convertPos(df)


### Convert Affiliation to Ordinals
##df = convertAff(df)

##### Filter out zeroes
##df_2012, df_2013, df_2014, df_2015, df_2016 = removeZero(df)

### Filter out Outliers

df_filt = filterOutlier(df)

### Bin salaries
df_filt = binSalary(df_filt)

df_filt = df_filt.drop(['index', 'Name', 'Total Citations', 'h-index', '5 year h-index', 'i10-index', '5 year i10-index', 'Sum of 5 Year Salaries', 'Norm2012', 'Norm2013', 'Norm2014', 'Norm2015', 'Norm2016', 'NormHindex', 'Ratio2012', 'Ratio2013', 'Ratio2014', 'Ratio2015', 'Ratio2016' ], axis=1)
##print df_filt

df_filt.to_csv('MCA_df.csv')



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from removeZero import removeZero
### Plot Salary Distribution for each Year

### Import CSV file 
df = pd.read_csv('salary_gscholar_Washington.csv')
df.dropna(how='any', inplace=True)
df = df.reset_index()



df_2012, df_2013, df_2014, df_2015, df_2016 = removeZero(df)




##f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, sharex=True)
##
##sns.distplot(df_2012['2012'], ax=ax1)
##sns.distplot(df_2013['2013'], ax=ax2)
##sns.distplot(df_2014['2014'], ax=ax3)
##sns.distplot(df_2015['2015'], ax=ax4)
##sns.distplot(df_2016['2016'], ax=ax5)
##plt.setp(ax4.get_xticklabels(), rotation=90)
##plt.setp(ax5.get_xticklabels(), rotation=90)
##plt.setp(ax6.get_xticklabels(), rotation=90)
##
##
##plt.show()
   
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, sharex=False)

sns.distplot(df_2012['Total Citations'], ax=ax1)
sns.distplot(df_2013['h-index'], ax=ax2)
sns.distplot(df_2014['5 year h-index'], ax=ax3)
sns.distplot(df_2015['i10-index'], ax=ax4)
sns.distplot(df_2016['5 year i10-index'], ax=ax5)
##plt.setp(ax4.get_xticklabels(), rotation=90)
##plt.setp(ax5.get_xticklabels(), rotation=90)
##plt.setp(ax6.get_xticklabels(), rotation=90)


plt.show()

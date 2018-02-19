import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### Import CSV file 
df = pd.read_csv('salary_gscholar_OU_extraMining.csv')

def parseCitesPerYear(df):
    ### Initialize 3D matrix to store annual citations from 2010 to 2017
    M = np.zeros((len(df),2,8)) #i = scholar index in df, j = 2 (year and citations), k = 8 (8 years, 2010-2017)
    M[:,0,0] = 2010
    M[:,0,1] = 2011
    M[:,0,2] = 2012
    M[:,0,3] = 2013
    M[:,0,4] = 2014
    M[:,0,5] = 2015
    M[:,0,6] = 2016
    M[:,0,7] = 2017
    for index in range(0, len(df)):
##        print "Processing... index:", index+1, "/", len(df), "(", df.Name[index], ")"
        temp = df['cites_per_year'][index]
        temp = temp.split('{')[1]
        temp = temp.split('}')[0]
        temp = temp.split(',')
        if temp == ['']:
            continue
        else:
            for n in range(0, len(temp)):
                year = int(temp[n].split(':')[0])
                cites = int(temp[n].split(':')[1].strip())
                if year == 2010:
                    M[index,1,0] = cites
                if year == 2011:
                    M[index,1,1] = cites
                if year == 2012:
                    M[index,1,2] = cites
                if year == 2013:
                    M[index,1,3] = cites
                if year == 2014:
                    M[index,1,4] = cites
                if year == 2015:
                    M[index,1,5] = cites
                if year == 2016:
                    M[index,1,6] = cites
                if year == 2017:
                    M[index,1,7] = cites
    return M

def percentDiffSalary(df):
    df['PerDiff2013'] = 100*(df['2013']-df['2012'])/(df['2012'])
    df['PerDiff2014'] = 100*(df['2014']-df['2013'])/(df['2013'])
    df['PerDiff2015'] = 100*(df['2015']-df['2014'])/(df['2014'])
    df['PerDiff2016'] = 100*(df['2016']-df['2015'])/(df['2015'])
    df = df.replace([np.inf, -np.inf],np.nan)
    return df

def percentDiffCites(M):
    PerDiffCit_2012 = []
    PerDiffCit_2013 = []
    PerDiffCit_2014 = []
    PerDiffCit_2015 = []

    for index in range(0, len(M)):
        if M[index,1,1] == 0:
            PerDiffCit_2012_temp = 'NaN'
        else:
            PerDiffCit_2012_temp = 100*(M[index,1,2] - M[index,1,1])/M[index,1,1]

        if M[index,1,2] == 0:
            PerDiffCit_2013_temp = 'NaN'
        else:
            PerDiffCit_2013_temp = 100*(M[index,1,3] - M[index,1,2])/M[index,1,2]

        if M[index,1,3] == 0:
            PerDiffCit_2014_temp = 'NaN'
        else:
            PerDiffCit_2014_temp = 100*(M[index,1,4] - M[index,1,3])/M[index,1,3]

        if M[index,1,4] == 0:
            PerDiffCit_2015_temp = 'NaN'
        else:
            PerDiffCit_2015_temp = 100*(M[index,1,5] - M[index,1,4])/M[index,1,4]

            
        PerDiffCit_2012.append(PerDiffCit_2012_temp)
        PerDiffCit_2013.append(PerDiffCit_2013_temp)
        PerDiffCit_2014.append(PerDiffCit_2014_temp)
        PerDiffCit_2015.append(PerDiffCit_2015_temp)

    return PerDiffCit_2012, PerDiffCit_2013, PerDiffCit_2014, PerDiffCit_2015 



M = parseCitesPerYear(df)
PerDiffCit_2012, PerDiffCit_2013, PerDiffCit_2014, PerDiffCit_2015  = percentDiffCites(M)
df['PerDiffCit_2012'] = PerDiffCit_2012
df['PerDiffCit_2013'] = PerDiffCit_2013
df['PerDiffCit_2014'] = PerDiffCit_2014
df['PerDiffCit_2015'] = PerDiffCit_2015
df = percentDiffSalary(df)
df = df[np.isfinite(df['PerDiff2016'])]
df = df[pd.to_numeric(df['PerDiffCit_2015'], errors='coerce').notnull()]


##df = df.dropna(subset=['PerDiffCit_2012'])
##df2 = df.PerDiff2013.dropna(how='any',inplace=True)
##df2 = df[df.PerDiff2013 != 'NaN']

##df = df[df.PerDiff2013 != inf]
print df




sns.regplot(x='PerDiffCit_2015', y='PerDiff2016', data=df, fit_reg=False)
plt.show()

##print df['2013_PerDiff'].describe()


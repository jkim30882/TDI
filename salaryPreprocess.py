import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### Import CSV file 
df = pd.read_csv('salary_gscholar_Washington.csv')

### Filter out rows with empty Google Scholar
df.dropna(how='any', inplace=True)
df = df.reset_index()

### Normalize salaries based on the maximum salary of each position
def normSalary(df):
    prof = df[df.Position == 'PROFESSOR']
    associate = df[df.Position == 'ASSOCIATE PROFESSOR']
    assistant = df[df.Position == 'ASSISTANT PROFESSOR']
    max_professor = max(max(prof['2012']), max(prof['2013']), max(prof['2014']), max(prof['2015']), max(prof['2016']))
    max_associate = max(max(associate['2012']), max(associate['2013']), max(associate['2014']), max(associate['2015']), max(associate['2016']))
    max_assistant = max(max(assistant['2012']), max(assistant['2013']), max(assistant['2014']), max(assistant['2015']), max(assistant['2016']))
    
    print "Highest Professor Salary:", max_professor
    print "Highest Associate Professor Salary:", max_associate
    print "Highest Assistant Professor Salary:", max_assistant

    # Normalized all PROFESSOR salaries
    df['Normalized_2012_Prof'] = (df['2012']/float(max_professor)).where(df['Position'] == 'PROFESSOR')
    df['Normalized_2013_Prof'] = (df['2013']/float(max_professor)).where(df['Position'] == 'PROFESSOR')
    df['Normalized_2014_Prof'] = (df['2014']/float(max_professor)).where(df['Position'] == 'PROFESSOR')
    df['Normalized_2015_Prof'] = (df['2015']/float(max_professor)).where(df['Position'] == 'PROFESSOR')
    df['Normalized_2016_Prof'] = (df['2016']/float(max_professor)).where(df['Position'] == 'PROFESSOR')

    # Normalized all ASSOCIATE PROFESSOR salaries
    df['Normalized_2012_Associate'] = (df['2012']/float(max_associate)).where(df['Position'] == 'ASSOCIATE PROFESSOR')
    df['Normalized_2013_Associate'] = (df['2013']/float(max_associate)).where(df['Position'] == 'ASSOCIATE PROFESSOR')
    df['Normalized_2014_Associate'] = (df['2014']/float(max_associate)).where(df['Position'] == 'ASSOCIATE PROFESSOR')
    df['Normalized_2015_Associate'] = (df['2015']/float(max_associate)).where(df['Position'] == 'ASSOCIATE PROFESSOR')
    df['Normalized_2016_Associate'] = (df['2016']/float(max_associate)).where(df['Position'] == 'ASSOCIATE PROFESSOR')
    
    # Normalized all ASSISTANT PROFESSOR salaries
    df['Normalized_2012_Assistant'] = (df['2012']/float(max_assistant)).where(df['Position'] == 'ASSISTANT PROFESSOR')
    df['Normalized_2013_Assistant'] = (df['2013']/float(max_assistant)).where(df['Position'] == 'ASSISTANT PROFESSOR')
    df['Normalized_2014_Assistant'] = (df['2014']/float(max_assistant)).where(df['Position'] == 'ASSISTANT PROFESSOR')
    df['Normalized_2015_Assistant'] = (df['2015']/float(max_assistant)).where(df['Position'] == 'ASSISTANT PROFESSOR')
    df['Normalized_2016_Assistant'] = (df['2016']/float(max_assistant)).where(df['Position'] == 'ASSISTANT PROFESSOR')


    df['Normalized_2012'] = df['Normalized_2012_Prof'].combine_first(df['Normalized_2012_Associate'].combine_first(df['Normalized_2012_Assistant']))
    df['Normalized_2013'] = df['Normalized_2013_Prof'].combine_first(df['Normalized_2013_Associate'].combine_first(df['Normalized_2013_Assistant']))
    df['Normalized_2014'] = df['Normalized_2014_Prof'].combine_first(df['Normalized_2014_Associate'].combine_first(df['Normalized_2014_Assistant']))
    df['Normalized_2015'] = df['Normalized_2015_Prof'].combine_first(df['Normalized_2015_Associate'].combine_first(df['Normalized_2015_Assistant']))
    df['Normalized_2016'] = df['Normalized_2016_Prof'].combine_first(df['Normalized_2016_Associate'].combine_first(df['Normalized_2016_Assistant']))

    df = df.drop(['Normalized_2012_Prof', 'Normalized_2013_Prof', 'Normalized_2014_Prof', 'Normalized_2015_Prof', 'Normalized_2016_Prof'], axis=1)
    df = df.drop(['Normalized_2012_Associate', 'Normalized_2013_Associate', 'Normalized_2014_Associate', 'Normalized_2015_Associate', 'Normalized_2016_Associate'], axis=1)
    df = df.drop(['Normalized_2012_Assistant', 'Normalized_2013_Assistant', 'Normalized_2014_Assistant', 'Normalized_2015_Assistant', 'Normalized_2016_Assistant'], axis=1)

    return df

### Normalize h-index based on the maximum h-index of each position
def normHindex(df):
    prof = df[df.Position == 'PROFESSOR']
    associate = df[df.Position == 'ASSOCIATE PROFESSOR']
    assistant = df[df.Position == 'ASSISTANT PROFESSOR']
    max_professor = max(prof['h-index'])
    max_associate = max(associate['h-index'])
    max_assistant = max(assistant['h-index'])
    
    print "Highest Professor h-index:", max_professor
    print "Highest Associate Professor h-index:", max_associate
    print "Highest Assistant Professor h-index:", max_assistant

    # Normalized all PROFESSOR h-index
    df['Normalized_Hindex_Prof'] = (df['h-index']/float(max_professor)).where(df['Position'] == 'PROFESSOR')

    # Normalized all ASSOCIATE PROFESSOR salaries
    df['Normalized_Hindex_Associate'] = (df['h-index']/float(max_associate)).where(df['Position'] == 'ASSOCIATE PROFESSOR')
    
    # Normalized all ASSISTANT PROFESSOR salaries
    df['Normalized_Hindex_Assistant'] = (df['h-index']/float(max_assistant)).where(df['Position'] == 'ASSISTANT PROFESSOR')

    df['Normalized_Hindex'] = df['Normalized_Hindex_Prof'].combine_first(df['Normalized_Hindex_Associate'].combine_first(df['Normalized_Hindex_Assistant']))

    df = df.drop(['Normalized_Hindex_Prof', 'Normalized_Hindex_Associate', 'Normalized_Hindex_Assistant'], axis=1)
##    print df
    return df

### Remove zero salaries for each year
def removeZero(df):
    #Count number of zeros in each year's salary
    print "2012 Salary, Number of Zeros", len(df[df['2012'] == 0]), '/', len(df)
    print "2013 Salary, Number of Zeros", len(df[df['2013'] == 0]), '/', len(df)
    print "2014 Salary, Number of Zeros", len(df[df['2014'] == 0]), '/', len(df)
    print "2015 Salary, Number of Zeros", len(df[df['2015'] == 0]), '/', len(df)
    print "2016 Salary, Number of Zeros", len(df[df['2016'] == 0]), '/', len(df)

    df_2012 = df.loc[(df['2012']!=0)].reset_index()
    df_2013 = df.loc[(df['2013']!=0)].reset_index()
    df_2014 = df.loc[(df['2014']!=0)].reset_index()
    df_2015 = df.loc[(df['2015']!=0)].reset_index()
    df_2016 = df.loc[(df['2016']!=0)].reset_index()
      
    return df_2012, df_2013, df_2014, df_2015, df_2016

### Filter out Outliers
def filterOutlier(df):
    min_lim = 0.0
    max_lim = 100
    max2012 = max(df['2012'])
    max2013 = max(df['2013'])
    max2014 = max(df['2014'])
    max2015 = max(df['2015'])
    max2016 = max(df['2016'])
    maxHindex = max(df['h-index'])

    df['Norm2012'] = df['2012']/float(max2012)
    df['Norm2013'] = df['2013']/float(max2013)
    df['Norm2014'] = df['2014']/float(max2014)
    df['Norm2015'] = df['2015']/float(max2015)
    df['Norm2016'] = df['2016']/float(max2016)
    df['NormHindex'] = df['h-index']/float(maxHindex)
    df['Ratio2012'] = df['Norm2012']/df['NormHindex']
    df['Ratio2013'] = df['Norm2013']/df['NormHindex']
    df['Ratio2014'] = df['Norm2014']/df['NormHindex']
    df['Ratio2015'] = df['Norm2015']/df['NormHindex']
    df['Ratio2016'] = df['Norm2016']/df['NormHindex']

    ### remove rows with ratio < 0.1 and >4
    df_temp1 = df.loc[(df['Ratio2012'] >min_lim) & (df['Ratio2012'] <max_lim)].reset_index(drop=True)
    df_temp2 = df_temp1.loc[(df_temp1['Ratio2013'] >min_lim) & (df_temp1['Ratio2013'] <max_lim)].reset_index(drop=True)
    df_temp3 = df_temp2.loc[(df_temp2['Ratio2014'] >min_lim) & (df_temp2['Ratio2014'] <max_lim)].reset_index(drop=True)
    df_temp4 = df_temp3.loc[(df_temp3['Ratio2015'] >min_lim) & (df_temp3['Ratio2015'] <max_lim)].reset_index(drop=True)
    df_filt = df_temp4.loc[(df_temp4['Ratio2016'] >min_lim) & (df_temp4['Ratio2016'] <max_lim)].reset_index(drop=True)
    
    return df_filt


### Bin salaries into 5 categories (IC Class1 = $0-100000, IC Class2 = $100000-200000, IC Class3 = $200000-300000, IC Class4 = $300000-400000, IC Class5 = greater than $400000
def binSalary(df):

    df.loc[df['2012'] >= 400000, '2012'] = 'IC Class5'
    df.loc[df['2012'] < 100000, '2012'] = 'IC Class1'
    df.loc[df['2012'] < 200000, '2012'] = 'IC Class2'
    df.loc[df['2012'] < 300000, '2012'] = 'IC Class3'
    df.loc[df['2012'] < 400000, '2012'] = 'IC Class4'

    df.loc[df['2013'] >= 400000, '2013'] = 'IC Class5'
    df.loc[df['2013'] < 100000, '2013'] = 'IC Class1'
    df.loc[df['2013'] < 200000, '2013'] = 'IC Class2'
    df.loc[df['2013'] < 300000, '2013'] = 'IC Class3'
    df.loc[df['2013'] < 400000, '2013'] = 'IC Class4'

    df.loc[df['2014'] >= 400000, '2014'] = 'IC Class5'
    df.loc[df['2014'] < 100000, '2014'] = 'IC Class1'
    df.loc[df['2014'] < 200000, '2014'] = 'IC Class2'
    df.loc[df['2014'] < 300000, '2014'] = 'IC Class3'
    df.loc[df['2014'] < 400000, '2014'] = 'IC Class4'

    df.loc[df['2015'] >= 400000, '2015'] = 'IC Class5'
    df.loc[df['2015'] < 100000, '2015'] = 'IC Class1'
    df.loc[df['2015'] < 200000, '2015'] = 'IC Class2'
    df.loc[df['2015'] < 300000, '2015'] = 'IC Class3'
    df.loc[df['2015'] < 400000, '2015'] = 'IC Class4'

    df.loc[df['2016'] >= 400000, '2016'] = 'IC Class5'
    df.loc[df['2016'] < 100000, '2016'] = 'IC Class1'
    df.loc[df['2016'] < 200000, '2016'] = 'IC Class2'
    df.loc[df['2016'] < 300000, '2016'] = 'IC Class3'
    df.loc[df['2016'] < 400000, '2016'] = 'IC Class4'

    return df

### Convert Positions to Ordinal values
def convertPos(df):

    df.loc[df['Position'] == 'PROFESSOR', 'Position'] = 1
    df.loc[df['Position'] == 'ASSOCIATE PROFESSOR', 'Position'] = 2
    df.loc[df['Position'] == 'ASSISTANT PROFESSOR', 'Position'] = 3

    return df

### Convert Affiliations to Ordinal values
def convertAff(df):

    df.loc[df['Affiliation'] == 'University of Washington', 'Affiliation'] = 1
    df.loc[df['Affiliation'] == 'Washington State University', 'Affiliation'] = 2
    df.loc[df['Affiliation'] == 'Central Washington University', 'Affiliation'] = 3
    df.loc[df['Affiliation'] == 'Eastern Washington University', 'Affiliation'] = 4
    df.loc[df['Affiliation'] == 'Western Washington University', 'Affiliation'] = 5

    return df

##df = convertAff(df)
##print df
    






##df = normSalary(df)
##df = normHindex(df)


##df_filt = filterOutlier(df)
##
##
df_2012, df_2013, df_2014, df_2015, df_2016 = removeZero(df)

####### Plot Salaries vs. Total Citations
f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1,5, sharey=True)
sns.regplot(x="h-index", y="2012", data=df_filt, fit_reg=False, ax=ax1)
sns.regplot(x="h-index", y="2013", data=df_filt, fit_reg=False, ax=ax2)
sns.regplot(x="h-index", y="2014", data=df_filt, fit_reg=False, ax=ax3)
sns.regplot(x="h-index", y="2015", data=df_filt, fit_reg=False, ax=ax4)
sns.regplot(x="h-index", y="2016", data=df_filt, fit_reg=False, ax=ax5)

plt.show(f)

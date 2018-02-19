### Filter out Outliers
def filterOutlier(df):
    min_lim = 0.2
    max_lim = 4
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

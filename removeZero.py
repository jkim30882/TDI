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

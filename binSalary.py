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

##    df.loc[df['2012'] >= 250000, '2012'] = 'Super High'
##    df.loc[df['2012'] < 50000, '2012'] = 'Low'
##    df.loc[df['2012'] < 150000, '2012'] = 'Normal'
##    df.loc[df['2012'] < 250000, '2012'] = 'High'
##
##    df.loc[df['2013'] >= 250000, '2013'] = 'Super High'
##    df.loc[df['2013'] < 50000, '2013'] = 'Low'
##    df.loc[df['2013'] < 150000, '2013'] = 'Normal'
##    df.loc[df['2013'] < 250000, '2013'] = 'High'
##
##    df.loc[df['2014'] >= 250000, '2014'] = 'Super High'
##    df.loc[df['2014'] < 50000, '2014'] = 'Low'
##    df.loc[df['2014'] < 150000, '2014'] = 'Normal'
##    df.loc[df['2014'] < 250000, '2014'] = 'High'
##
##    df.loc[df['2015'] >= 250000, '2015'] = 'Super High'
##    df.loc[df['2015'] < 50000, '2015'] = 'Low'
##    df.loc[df['2015'] < 150000, '2015'] = 'Normal'
##    df.loc[df['2015'] < 250000, '2015'] = 'High'
##
##    df.loc[df['2016'] >= 250000, '2016'] = 'Super High'
##    df.loc[df['2016'] < 50000, '2016'] = 'Low'
##    df.loc[df['2016'] < 150000, '2016'] = 'Normal'
##    df.loc[df['2016'] < 250000, '2016'] = 'High'
##





##    df.loc[df['2012'] >= 200000, '2012'] = 'High'
##    df.loc[df['2012'] < 50000, '2012'] = 'Low'
##    df.loc[df['2012'] < 200000, '2012'] = 'Normal'
##
##    df.loc[df['2013'] >= 200000, '2013'] = 'High'
##    df.loc[df['2013'] < 50000, '2013'] = 'Low'
##    df.loc[df['2013'] < 200000, '2013'] = 'Normal'
##
##    df.loc[df['2014'] >= 200000, '2014'] = 'High'
##    df.loc[df['2014'] < 50000, '2014'] = 'Low'
##    df.loc[df['2014'] < 200000, '2014'] = 'Normal'
##
##    df.loc[df['2015'] >= 200000, '2015'] = 'High'
##    df.loc[df['2015'] < 50000, '2015'] = 'Low'
##    df.loc[df['2015'] < 200000, '2015'] = 'Normal'
##
##    df.loc[df['2016'] >= 200000, '2016'] = 'High'
##    df.loc[df['2016'] < 50000, '2016'] = 'Low'
##    df.loc[df['2016'] < 200000, '2016'] = 'Normal'
    
    return df

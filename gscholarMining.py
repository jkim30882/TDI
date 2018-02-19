def gscholarMining(aff, pos):
        
    import scholarly
    import pandas as pd
    import time
    from time import sleep
    from random import randint


    ### Import CSV file containing salaries of Washington State Employees, and remove white spaces in each column
    df = pd.read_csv('WaStEmployeeHistSalary.csv')
    df['Name'] = df['Name'].str.strip()
    df['Affiliation'] = df['Affiliation'].str.strip()
    df['Position'] = df['Position'].str.strip()

    ### Remove rows that are listed as 'Name Withheld'
    df = df[df.Name != 'Name Withheld']

    ### Filter out affiliations
    df = df[df.Affiliation == aff]

    ### Filter out positions
    df = df[df.Position == pos].reset_index()

    ### Create a new dataframe for our google scholar query
    fname = 'gscholar_' + pos + '_' + aff + '.csv'
    df_gscholar = pd.DataFrame(columns=['Name','Total Citations', 'h-index', '5 year h-index', 'i10-index', '5 year i10-index'])
    df_gscholar.to_csv(fname)

    ### Data mining from google scholar. Go through all the names in df, and extract publication record of each individual from google scholar
    start_time = time.time()
    aff = aff
    n = len(df)
    with open(fname, 'a') as f:
        for index in range(0, n):
            sleep(randint(1,10)) ### randomly sleep between 1 to 10 seconds for each iteration to prevent being blocked by Google
            print "Searching Number:", index+1, '/', n
            name = df.Name[index]
            position = df.Position[index]
            print name, "(", position, ")", "in",  aff
            search_query = scholarly.search_author(name + ',' + aff)
            author = next(search_query, None)
            if author is None:
                row = [name, 'NA', 'NA', 'NA', 'NA', 'NA']
                df_gscholar.loc[index] = row
                continue
            else:
                try:
                    author = author.fill()
                    row = [name, author.citedby, author.hindex, author.hindex5y, author.i10index, author.i10index5y]
                    df_gscholar.loc[index] = row
                except AttributeError:
                    row = [name, 'NA', 'NA', 'NA', 'NA', 'NA']
        df_gscholar.to_csv(f,header=False)
    elapsed_time = time.time() - start_time    
    print "Done!", time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    return df_gscholar

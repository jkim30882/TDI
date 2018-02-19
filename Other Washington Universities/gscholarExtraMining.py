import scholarly
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
from time import sleep
from random import randint

### Import CSV file containing salaries and gscholar information of UW professsors
df = pd.read_csv('salary_gscholar_OU.csv')

### Filter out NA
df.dropna(how='any', inplace=True)
df = df.reset_index()

### Extra data mining from google scholar. Go through all names in df, extract yearly citations and research interests
start_time = time.time()
n = len(df)
interests = []
cites_per_year = []
for index in range(0,n):
    sleep(randint(1,10))
    print "Searching Number:", index+1, '/', n
    name = df.Name[index]
    position = df.Position[index]
    aff = df.Affiliation[index]
    print name, "(", position, ")", "in", aff
    search_query = scholarly.search_author(name + ',' + aff)
    author = next(search_query, None)
    author = author.fill()
    try:
        interests.append( author.interests )       
    except AttributeError:
        interests.append( 'NA' )
    try:
        cites_per_year.append( author.cites_per_year )
    except AttributeError:
        cites_per_year.append( 'NA' )
        
df['interests'] = interests
df['cites_per_year'] = cites_per_year
##print df.head()
df.to_csv('salary_gscholar_OU_extraMining.csv')
elapsed_time = time.time() - start_time
print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))




### Extract journal names
##for pub in author.publications:
##    pub = pub.fill()
##    try:
##        print pub.bib['journal']
##    except KeyError:
##        print 'NA'


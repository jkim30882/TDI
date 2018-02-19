import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### Import CSV file 
df = pd.read_csv('salary_gscholar_Washington.csv')
      


### Plot number of scholars with google scholar ID (Yes or No)
def plotGscholarID(df):
    # Filter out NA
    n_total = len(df)
    n_NA = df['Total Citations'].isnull().sum()
    df.dropna(how='any', inplace=True)
    n = len(df)
    print "Number of scholars missing Google Scholar:", n_NA, "/", n_total
    print "Number of scholars with Google Scholar:", n, "/", n_total
    # Plot pie chart
    labels = 'Yes', 'No'
    sizes = [n, n_NA]
    colors = ['lightskyblue', 'lightcoral']
    explode = (0.1,0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
    plt.axis('equal')
    plt.title('Google Scholar ID')
    plt.show()
    return

### Count number of scholars with google scholar ID for each affiliation and position
def countGscholarID_aff(df):
    # Filter out NA
    df.dropna(how='any', inplace=True)
    # Draw countplot
    sns.countplot(x="Affiliation", data=df, hue='Position')
    plt.title('Number of Scholars with Google Scholar ID for each Affiliation')
    plt.show()
    return
    
### Plot average number of total citations for each affiliation and position
def avgCitations(df):
    # Filter out NA
    df.dropna(how='any', inplace=True)
    # Plot bar graph
    sns.barplot(x="Affiliation", y="Total Citations", data=df, hue='Position')
    plt.title('Average of Total Citations for each Affiliation')
    plt.show()
    return

### Plot average number of h-index for each affiliation and position
def avgHindex(df):
    # Filter out NA
    df.dropna(how='any', inplace=True)
    # Plot bar graph
    sns.barplot(x="Affiliation", y="h-index", data=df, hue='Position')
    plt.title('Average of h-index for each Affiliation')
    plt.show()
    return

### Plot average number of h-index for each position
def avgHindex_Pos(df):
    # Filter out NA
    df.dropna(how='any', inplace=True)
    # Plot bar graph
    sns.barplot(x="Position", y="h-index", data=df)
    plt.title('Average of h-index for each Position')
    plt.show()
    return

### Plot average salaries for each affiliation and position
def avgSalaries(df):
    # Filter out NA
    df.dropna(how='any', inplace=True)
    # Plot salaries
    f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, sharex=True)
##    sns.barplot(x="Affiliation", y="2012", data=df, hue='Position', ax=ax1)
##    sns.barplot(x="Affiliation", y="2013", data=df, hue='Position', ax=ax2)
##    sns.barplot(x="Affiliation", y="2014", data=df, hue='Position', ax=ax3)
##    sns.barplot(x="Affiliation", y="2015", data=df, hue='Position', ax=ax4)
##    sns.barplot(x="Affiliation", y="2016", data=df, hue='Position', ax=ax5)
##    sns.barplot(x="Affiliation", y="Sum of 5 Year Salaries", data=df, hue='Position', ax=ax6)
    sns.barplot(x="Affiliation", y="2012", data=df, ax=ax1)
    sns.barplot(x="Affiliation", y="2013", data=df, ax=ax2)
    sns.barplot(x="Affiliation", y="2014", data=df, ax=ax3)
    sns.barplot(x="Affiliation", y="2015", data=df, ax=ax4)
    sns.barplot(x="Affiliation", y="2016", data=df, ax=ax5)
    sns.barplot(x="Affiliation", y="Sum of 5 Year Salaries", data=df, ax=ax6)
    plt.setp(ax4.get_xticklabels(),rotation=90)
    plt.setp(ax5.get_xticklabels(),rotation=90)
    plt.setp(ax6.get_xticklabels(),rotation=90)
    plt.suptitle('Average of Salaries for each Affilication')
    plt.show()
    return

def avgSalaries_Pos(df):
    # Filter out NA
    df.dropna(how='any', inplace=True)
    # Plot salaries
    f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, sharex=True)
    sns.barplot(x="Position", y="2012", data=df, ax=ax1)
    sns.barplot(x="Position", y="2013", data=df, ax=ax2)
    sns.barplot(x="Position", y="2014", data=df, ax=ax3)
    sns.barplot(x="Position", y="2015", data=df, ax=ax4)
    sns.barplot(x="Position", y="2016", data=df, ax=ax5)
    sns.barplot(x="Position", y="Sum of 5 Year Salaries", data=df, ax=ax6)
    plt.setp(ax4.get_xticklabels(),rotation=90)
    plt.setp(ax5.get_xticklabels(),rotation=90)
    plt.setp(ax6.get_xticklabels(),rotation=90)
    plt.suptitle('Average of Salaries for each Affilication')
    plt.show()
    return
   

plotGscholarID(df)
countGscholarID_aff(df)
avgCitations(df)
avgHindex(df)
avgHindex_Pos(df)
avgSalaries(df)
avgSalaries_Pos(df)

##### Plot Salaries vs. Total Citations
##f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, sharex=True)
##sns.regplot(x="Total Citations", y="2012", data=df, fit_reg=False, ax=ax1)
####ax1.set_ylim(-1000000,4000000)
##sns.regplot(x="Total Citations", y="2013", data=df, fit_reg=False, ax=ax2)
####ax2.set_ylim(-1000000,4000000)
##sns.regplot(x="Total Citations", y="2014", data=df, fit_reg=False, ax=ax3)
####ax3.set_ylim(-1000000,4000000)
##sns.regplot(x="Total Citations", y="2015", data=df, fit_reg=False, ax=ax4)
####ax4.set_ylim(-1000000,4000000)
##sns.regplot(x="Total Citations", y="2016", data=df, fit_reg=False, ax=ax5)
####ax5.set_ylim(-1000000,4000000)
##sns.regplot(x="Total Citations", y="Sum of 5 Year Salaries", data=df, fit_reg=False, ax=ax6)
####ax6.set_ylim(-1000000,4000000)
##
##plt.show(f)

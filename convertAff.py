### Convert Affiliations to Ordinal values
def convertAff(df):

    df.loc[df['Affiliation'] == 'University of Washington', 'Affiliation'] = 1
    df.loc[df['Affiliation'] == 'Washington State University', 'Affiliation'] = 2
    df.loc[df['Affiliation'] == 'Central Washington University', 'Affiliation'] = 3
    df.loc[df['Affiliation'] == 'Eastern Washington University', 'Affiliation'] = 4
    df.loc[df['Affiliation'] == 'Western Washington University', 'Affiliation'] = 5

    return df

### Convert Positions to Ordinal values
def convertPos(df):

    df.loc[df['Position'] == 'PROFESSOR', 'Position'] = 1
    df.loc[df['Position'] == 'ASSOCIATE PROFESSOR', 'Position'] = 2
    df.loc[df['Position'] == 'ASSISTANT PROFESSOR', 'Position'] = 3

    return df

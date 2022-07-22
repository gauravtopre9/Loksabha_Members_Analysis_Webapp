import pandas as pd

def statewise_mps(df):
    states = df['State'].value_counts().reset_index().sort_values('index')['index'].values
    mps = df['State'].value_counts().reset_index().sort_values('index')['State'].values
    return states,mps

def mp(df,first='Overall',party='Overall',state='Overall'):
    if first!= 'Overall':
        if party == 'Overall' and state == 'Overall':
            return df[df['First time']==first][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
        elif party == 'Overall' and state != 'Overall':
            return df[(df['First time']==first) & (df['State']==state)][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
        elif party != 'Overall' and state == 'Overall':
            return df[(df['Party Name']==party) & (df['First time']==first)][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
        else:
            return df[(df['Party Name']==party) & (df['First time']==first) & (df['State']==state)][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
    else:
        if party == 'Overall' and state == 'Overall':
            return df[['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
        elif party == 'Overall' and state != 'Overall':
            return df[df['State']==state][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
        elif party != 'Overall' and state == 'Overall':
            return df[df['Party Name']==party][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]
        else:
            return df[(df['Party Name']==party) & (df['State']==state)][['Name of Member','Constituency','State','Party Name','Gender','Category','Age of Member']]


def top_3(df,state='Overall'):
    df1 = df[df['UT']=='No']
    if state != 'Overall':
        return df1[df1['State']==state]['Party Name'].value_counts().reset_index().rename(columns={'index':'Party Name','Party Name':'No.of MPs'})
    else:
        return df1['Party Name'].value_counts().reset_index().rename(columns={'index':'Party Name','Party Name':'No.of MPs'})

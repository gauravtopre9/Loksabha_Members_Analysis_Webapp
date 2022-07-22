def preprocessing(df):
    df[df['Name of Member']=='Angadi, Smt. Mangal Suresh'] = df[df['Name of Member']=='Angadi, Smt. Mangal Suresh'].fillna('26/10/1963')
    df[df['Name of Member']=='Samadani, Shri Abdussamad'] = df[df['Name of Member']=='Samadani, Shri Abdussamad'].fillna('01/01/1959')
    df[df['Name of Member']=='Gill, Shri Jasbir Singh'] = df[df['Name of Member']=='Gill, Shri Jasbir Singh'].fillna('08/11/1968')
    df[df['Name of Member']=='Vasanth, Shri vijayakumar (Alias) Vijay'] = df[df['Name of Member']=='Vasanth, Shri vijayakumar (Alias) Vijay'].fillna('20/05/1983')
    df[df['Name of Member']=='Chakraborty, Ms. Mimi'] = df[df['Name of Member']=='Chakraborty, Ms. Mimi'].fillna('11/02/1989')

    df['Age of Member'] = df['DOB']
    df['Age of Member'] = 2022 - df['Age of Member'].str.split('/',expand = True)[2].astype(int)
    df.drop(['Age'],axis=1,inplace = True)
    df.rename(columns = {'Woman':'Gender'},inplace = True)
    df.Gender = df.Gender.replace({0:'Male',1:'Female'})
    df['First time'] = df['First time'].replace({0:'No',1:'Yes'})
    df.UT = df.UT.replace({1:'Yes',0:'No'})

    return df


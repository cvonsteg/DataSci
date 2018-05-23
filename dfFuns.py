import pandas as pd

df1 = pd.read_csv('/home/tino/Documents/FinProj/barclays.csv')

def preProcess(df):

    print('Rows: ', df.shape[0])
    print('Columns: ', df.shape[1])

    x = df.isnull().sum()
    y = df.count()
    z = (y-x)/y
    comp = pd.concat([x,z], axis = 1, keys = ['Missing', 'CompPerc'])
    print(comp)

    print(df.describe())

    df.columns = df.columns.str.lower()



preProcess(df1)



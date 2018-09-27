import pandas as pd

class Dataset:
    def __init__(self, df):
        self.df = df

    def Dims(self):
        print('Data Frame Format: \n Rows: ', 
        self.df.shape[0],
        '\n Columns: ', self.df.shape[1])

    def Comp(self):
        x = self.df.isnull().sum()
        y = (self.df.isnull().count() - self.df.isnull().sum())/self.df.isnull().count()*100
        compdf = pd.concat([x,y], axis = 1, keys = ['Missing','Completeness'])
        print(compdf)

    def Desc(self):
        print(self.df.describe())

    def LowCols(self):
        self.df.columns = self.df.columns.str.lower()

    def index_checker(self, col):
        if self.df.groupby(col)[col].count().is_unique:
            self.df.set_index(col, inplace=True)
        else:
            print('Cannot change index - values in column are not unique')


import pandas as pd

class Dataset:
    """Simple methods for doing common operations on any pandas data frame"""
    def __init__(self, df):
        self.df = df

    def dimensions(self):
        """Prints dimensions of dataframe"""
        print('Data Frame Format: \n Rows: ', 
        self.df.shape[0],
        '\n Columns: ', self.df.shape[1])

    def completeness(self):
        """Checks for proportion of missing values in each column"""
        x = self.df.isnull().sum()
        y = (self.df.isnull().count() - self.df.isnull().sum())/self.df.isnull().count()*100
        compdf = pd.concat([x,y], axis = 1, keys = ['Missing','Completeness'])
        print(compdf)

    #def Desc(self):
    #    print(self.df.describe())

    def lower_cols(self):
        """Casts column names to lower case"""
        self.df.columns = self.df.columns.str.lower()

    def upper_cols(self):
        """Casts column names to upper case"""
        self.df.columns = self.df.columns.str.lower()

    def index_checker(self, col):
        if self.df.groupby(col)[col].count().is_unique:
            self.df.set_index(col, inplace=True)
        else:
            print('Cannot change index - values in column are not unique')


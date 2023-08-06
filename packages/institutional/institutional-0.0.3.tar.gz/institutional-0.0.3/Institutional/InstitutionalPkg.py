class spx_neural():
    
    def __init__(self):
        self.keeper = 'tbd'
    
    def import_csv(self):
        import pandas as pd
        self.df = pd.read_csv('MSFT.csv')
        self.df['Date'] = pd.to_datetime(self.df['Date']) #converts Date column dtype from object to date dtype
        return self.df
    
    def data_summary(self, df):
        print('The statistics of the data:')
        display(df.describe())
        print('\nThe summary of empty values:')
        print(df.isnull().sum()) #counts the number of rows with empty values
        print('\nThe number of records is: ', len(df))
        print('\nThe datatypes are: \n', df.dtypes)
        
    def empty_cell_rmvl(self, df):
        import pandas as pd
        df.dropna(subset = ["Open"], inplace=True)
        df.reset_index(inplace = True)
        df['Date'] = pd.to_datetime(df['Date']) #converts Date dtype from object to date dtype
        return df
    
    def zero_rmvl(self, df):        
        import pandas as pd

        i = 0
        while i < len(df):
            if df.iloc[i, -2] == 0.0:
                #print('index: ', i, df.iloc[i,:])
                df = df.drop([i])
                df.reset_index(drop = True, inplace = True)
                i -= 1
            else:
                i += 1
                
        df['Date'] = pd.to_datetime(df['Date']) #converts Date dtype from object to date dtype; needs to be done after every reset index
        return df
    
    def obj_to_date(self, df):
        import pandas as pd
        df['Date'] = pd.to_datetime(df['Date'])
    
    def differences(self, df):
        df['high_low'] = df['High'] - df['Low']
        df['open_close'] = df['Open'] - df['Close']
        df['open_high'] = df['Open'] - df['High']
        df['open_low'] = df['Open'] - df['Low']
        df['high_close'] = df['High'] - df['Close']
        return df    
    
    def rmv_columns(self, df):
        columns_list = list(df.columns.values) #makes a list from the df column headers 
        print('Here are the columns: ', columns_list)
        self.keeper = input('What column do you want to keep? ')
        columns_list.remove(self.keeper) #removes the df header of choice from the list that will be dropped from the df
        df.drop(columns = columns_list, axis = 1, inplace = True) #drops all of the unwanted columns
        return df
    
    def add_days_column(self, df):
        #creates a new column that has a repeating set of integers from 1 to 5; it will be converted after transposing
        #https://stackoverflow.com/questions/64541504/how-do-i-add-a-column-with-a-repeating-series-of-values-to-a-dataframe
        import numpy as np
        days = [1,2,3,4,5]
        df['Days'] = 0
        np.put(np.asarray(df['Days']), np.arange(len(df)), days, mode = 'clip')
        return df
        
    def accumulated(self,df):
        import pandas
        
        '''Create a sixth column to denote the difference between the stock close and its high of the day. 
        Stocks that close above the open but at or just below the high price of the day are probably being accumulated.
        '''
        
        df['close_to_high'] = 0.9 * df['High'] #defines the close to high value as 90% of the high value
        i = 0
        while i < len(df):
            if (df.loc[i,'Close'] > df.loc[i,'Open'] and df.loc[i,'Close'] <= df.loc[i,'High'] and df.loc[i,'Close'] > df.loc[i,'close_to_high']):
                df.loc[i,'Accumulation'] = True
            else:
                df.loc[i,'Accumulation'] = False
            i += 1
        return df
    
    def simMovAve(self,df):
        import pandas as pd
        import numpy as np
        df['Vol_SMA'] = df['Volume'].rolling(20).mean()
        df.dropna(inplace = True)
        df.reset_index(inplace = True)
        df.drop(['index'], axis = 1, inplace = True)
        return df
    
    def accum_to_num(self, df):
        import pandas as pd
        import numpy as np
        
        i = 0
        while i < len(df):
            if df.loc[i, 'Accumulation'] == True:
                df.loc[i, 'Accum_Num'] = 1
            else:
                df.loc[i, 'Accum_Num'] = 0
                
            i += 1                
        return df
        
    def normalization(self,df):
        import pandas as pd
        import numpy as np
        
        df_max_scaled = df.copy()

        for column in df_max_scaled.columns:
            df_max_scaled[column] = df_max_scaled[column] / df_max_scaled[column].abs().max()
        return df_max_scaled
    
    def remove_records(self,df):
        print('The total number of records is: ', len(df))
        rec_in = input('What the record number that is the upper range of the group you want removed?')
        rec = int(rec_in)
        df.drop(df.index[0:rec], axis = 0, inplace = True) #drops all but about 50 records
        df.reset_index(drop = True, inplace = True) #reindexes the dataframe
        return df
    
    def remove_columns(self,df):
        df1 = df.copy()
        df1.drop(columns = ['Open', 'High', 'Low', 'Adj Close', 'Volume', 'close_to_high', 'open_close', 
                            'open_high', 'open_low', 'high_close', 'Date', 'Accumulation'], axis = 1, inplace = True)
        return df1
    
    def yahoo_api(self):
        import pandas as pd
        import yfinance as yf
        from datetime import datetime, timedelta
        
        symbol = input('What is the stock symbol? ')
        today = datetime.now()
        d = timedelta(days = 60) #get 60 days worth of data that will yield 40 records (first 20 dropped when calculated 20 sma.)
        a = today - d # goes back 60 days and produces the date
        end_date = today.strftime('%Y-%m-%d') #keeps only the date ... removes the time stamp
        begin_date = a.strftime('%Y-%m-%d')
       
        df = yf.download(symbol,
        start = begin_date,
        end = end_date,
        progress = False)
        return df
    
    def df_plot(self,df, df_max_scaled):
        import matplotlib.pyplot as plt
        import datetime
        i = 0
        x = []
        labels = []

        while i < len(df_max_scaled):
            x.append(i) #defines x axis tick marks
            z = df.loc[i,'Date']
            zdf = z.strftime('%Y-%m-%d')
            labels.append(zdf) #defines x axis labels
            i += 1

        f = plt.figure()

        plt.plot(df_max_scaled['Vol_SMA'], label = 'Vol_SMA')
        plt.plot(df_max_scaled['Close'], label = 'Close')
        plt.plot(df_max_scaled['Accum_Num'], label = 'Accum_Num')
        plt.plot(df_max_scaled['high_low'], label = 'high_low')

        f.set_figwidth(20)
        f.set_figheight(5)

        plt.xticks(x, labels, rotation = 45)
        plt.legend()
        plt.show
        return labels
        
    def user_notes(self, labels, df): #user notes on how to interpret the graph
        print('PLEASE NOTE: This is a beta release. It is not to be used in any decisions, financial or otherwise. The user assumes ')
        print('all the risk for their decisions.')
    
        print('The most recent date is: ', labels[len(df) - 1])
        print('The oldest date is: ', labels[0])
        print('\n1. Is the high low range narrowing which is negative slope? ')
        print('2. Is there accumulation?')
        print('3. Is the volume 20 day sma flat?')
        print('If all three of the questions are yes then it is probable that institutional investors are purchasing the equity.')
        print('Combine the results in steps 1, 2, and 3 and look for patterns as described. \nThese are stocks under accumulation.')
        print('If stock volume increases on a day when the stock is up, that should be considered confirmation of the trend. If stock')
        print(' volume is up and stock price is down, this is considered a distribution day. This could be a sign of institutional') 
        print(' selling.')
        print('ref: https://pocketsense.com/track-smart-money-flow-markets-5057233.html')
        

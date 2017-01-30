# import pandas as pd
import quandl
import math

# df = data frame
df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# Volotility
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
# Daily movement
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100
# define new data frame with only information of interest
# these are the Features (different from Labels)
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forcast_col = 'Adj. Close'
# dealing with missing data - i.e. fill in with outlier
df.fillna(-99999, inplace=True)

# forcast out by 1% of the data frame
forecast_out = int(math.ceil(0.01*len(df)))

# with this the label column for each row will be the
#    Adj. Close price 1% of df length into the future
df['label'] = df[forcast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())

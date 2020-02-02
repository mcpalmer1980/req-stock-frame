
import time
import statsmodels.api as sm 
from scipy import stats
import TSprice


l = ['AAPL','AMZN','TSLA']
df = TSprice.buildTimeSeries(l)
print(df)

def extract_lr(x):
    lr = stats.linregress(x['timepoint'].astype(int), x['price'].astype(float))
    return lr.slope

df3 = df.groupby('ticker').apply(extract_lr)
print(df3)

algoTracker = pd.Dataframe()

market_close = datetime.datetime.now().replace(hour=16, minute=0) 
while datetime.datetime.now() < market_close:
    df = TSprice.buildTimeSeries(l)
    mktstatus= df.groupby('ticker').apply(extract_lr)
    positions = getPosition()
    run_algos(mktstatus,positions, algoTracker)


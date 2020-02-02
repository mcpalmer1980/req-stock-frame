
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

algos= pd.Dataframe()


def run_active_algos(mkdstat_df, position_df, algoTracker_df):
    pass

def run_new_algos:
    pass

def reconcile(algos,positions) -> algos:
    pass

def find_opportunity(mkstatus) -> new_algo:
    pass

market_close = datetime.datetime.now().replace(hour=16, minute=0) 
while datetime.datetime.now() < market_close:
    df = TSprice.buildTimeSeries(l)
    mktstatus= df.groupby('ticker').apply(extract_lr)
    positions = getPosition()
    reconcile(positions, algos)
    run_algos(mktstatus,positions, algos)
    find_opportunity(mktstatus)




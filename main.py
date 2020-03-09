
import time
import statsmodels.api as sm 
from scipy import stats
import TSprice
from typing import Tuple, List, Dict

l = ['AAPL','AMZN','TSLA']
df = TSprice.buildTimeSeries(l)
print(df)

def extract_lr(x):
    lr = stats.linregress(x['timepoint'].astype(int), x['price'].astype(float))
    return lr.slope

df3 = df.groupby('ticker').apply(extract_lr)
print(df3)

ticker: str
activeAlgos: List[Tuple[ticker, algo]]


def runActiveAlgos(activeAlgos) -> None:
    for tk, algo in activeAlgos:
        algo(tk)


def run_new_algos:
    pass

def reconcile(activeAlgos) -> activeAlgos:
    pos = getPosition(conn)


def getPosition(ibxConnn) -> position:
    pass

def find_opportunity(mkstatus) -> new_algo:
    pass

def triage(conn) -> None:
    pnlList = getPnl()
    for tk, pnl in pnlList:
        if pnl < -0.05:
            sell(pk)



market_close = datetime.datetime.now().replace(hour=16, minute=0) 
while datetime.datetime.now() < market_close:
    # first thing --- check pnl for each stock in portfolio
    # sell any stock with 5% or more loss:
    triage(ibxconn)
    df = TSprice.buildTimeSeries(l)
    mktstatus= df.groupby('ticker').apply(extract_lr)
    triage(ibxconn)
    reconcile(activeAlgos)
    runActiveAlgos(activeAlgos)
    find_opportunity(mktstatus)




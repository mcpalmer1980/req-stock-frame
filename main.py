import time
import statsmodels.api as sm 
from scipy import stats
import TSprice
from typing import Tuple, List, Dict
from dataclasses import dataclass

## helper function to be used with pandas apply
def linearRegress(x):
    lr = stats.linregress(x['timepoint'].astype(int), x['price'].astype(float))
    return lr.slope

## New Function
Portfolio: List[Tuple[ticker, algo]]
def reconcile(p: Portfolio) -> Portfolio:
    pos = getPosition(conn)

ticker: str
position: List[ticker]
def getPosition(ibxConnn) -> position:
    pass

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def triage(conn) -> Portfolio:
    pnlList = getPnl()
    for tk, pnl in pnlList:
        if pnl < -0.05:
            sell(pk)


## New Function with dataclass and hints define
mktStat: pd.DataFrame
@dataclass
class Trend: 
    algoFn : 

            
def findTrend(mks: mktStat) -> Trend:
    pass

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def runAlgo(t: Trend) -> None:
    pass

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def runActiveAlgo(p: Portfolio) -> None:
    pass


l = ['AAPL','AMZN','TSLA']
market_close = datetime.datetime.now().replace(hour=16, minute=0) 
while datetime.datetime.now() < market_close:
    # first thing --- check pnl for each stock in portfolio
    # sell any stock with 5% or more loss:
    portfolio = triage(ibxconn)

    # step 2: get the dataframe with 5 time points
    # use this list for now; implement stock seletion later
    df = TSprice.buildTimeSeries(l)

    # perform regression to get market status
    mktstatus= df.groupby('ticker').apply(linearRegress)

    # triage again since previous 2 statements may take more than 2 minutes
    # secon triage may not be necessary depending on performance
    portfolio = triage(ibxconn)

    # synchronize portfolio and algo list
    reconcile(activeAlgos)

    # after reconciling, the portfolio should be in sync with online account
    # all algos will make 2 decisions: keep or sell the stock
    runActiveAlgos(portfolio)

    # this is self explanatory
    trend = findTrend(mktstatus)
    runAlgo(trend)




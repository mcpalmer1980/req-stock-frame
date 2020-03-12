import time
import statsmodels.api as sm 
from scipy import stats
import TSprice
from typing import Tuple, List, Dict
from dataclasses import dataclass

'''
CHANGES
# Moved algo and trend functions to algo.py
# moved triage/reconcile to broker.py
# Removed ibxConn parameters from all functions
    * broker.py will handle connections with global interface

'''

Portfolio: List[Tuple[ticker, algo]]

'''
not sure what the following bit is for
a position is considered the number of shares of one stock, right?

it looks like you want getPosition to receive a list of owned stocks
Isn't that a porfolio?

my old ibx class had
    ib.GetPortfolio(None) -> List of Tuples(ticker, shares)

I imagine this sort of functionality belonging to broker.py, using ib/alpaco/etc
'''

'''
ticker: str
position: List[ticker]
def getPosition(ibxConnn) -> position:
    pass
'''

## New Function with dataclass and hints define
mktStat: pd.DataFrame
@dataclass
class Trend:
    Uptick: float    # percentage of stock trending up
    Downtick: float  # percentage of stocks trending down
TradeStrategy: List[Tuple[ticker,algo]] 


stockInterests = ['AAPL','AMZN','TSLA']
stockList = classes.ticker_data['SP500']
market_close = datetime.datetime.now().replace(hour=16, minute=0) 
pfl = Portfolio[]

while datetime.datetime.now() < market_close:
    # first thing --- check pnl for each stock in portfolio
    # sell any stock with 5% or more loss:
    pfl = broker.triage(pfl, ibxconn)

    mktstatus = TSprice.getMarketStatus(stockList)

    # this is self explanatory
    trend = findTrend(mktstatus)
    algo = runAlgo(trend)
    pfl = plf.addAlgo(algo)

    # all algos will make 2 decisions: keep or sell the stock
    # rerun all algo in the portfolio
    runActiveAlgos(pfl)
    




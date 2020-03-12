

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


## Stock Selection process
## Find the stock and corresponding algo
def selectStock(sp: SP500) -> TargetStrategy:
    pass

# reconciliation with portfolio is complete
# ready to run algo
def randomAlgo(tk: ticker, stat: marketStatus) -> None:
    pnl = getPnL(tk)

    # check market status
    if stat == 'random' and pnl > 40.0:
       sell(tk)
   elif stat == 'random' and pnl < 40.0:
       pass
    elif stat != 'random' or pnl < 40.0
        sell(tk)




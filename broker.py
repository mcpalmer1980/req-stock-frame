def sell(ticker: str) -> None:
    pass

def buy(ticker: str) -> None:
    pass

def sellAll(None) -> None:
    pass

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def triage(p: Portfolio, conn) -> Portfolio:
    pnlList = getPnl()
    for tk, pnl in pnlList:
        if pnl < -0.05:
            sell(pk)
    # synchronize portfolio and algo list
    p2 = reconcile(p)
    return p2

def reconcile(p: Portfolio) -> Portfolio:
    pos = getPosition(conn)
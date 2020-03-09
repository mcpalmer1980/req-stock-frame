

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




'''
The broker module handles trading with the Alpaca Python API

It includes functions to buy, sell, and list positions
It also handles triage and reconciles broker portfolio with the algos
An API instance is created upon import
A secret key is needed when the API instance is created
The module will search the 'alpaca_secret' enviroment variable followed by the clipboard
'''

import typing
import alpaca_trade_api as tradeapi
import os
import pyperclip

endpoint = "https://paper-api.alpaca.markets"
key = "PKRE8PFNC2XVNA5CQWG8"

def sell(ticker: str) -> None:
    assert api, "Not connected to alpaca trade api"
    api.submit_order(
        symbol=ticker,
        side='sell',
        type='market',
        qty=quantity,
        time_in_force='day')

def buy(ticker: str, quantity: int) -> None:
    assert api, "Not connected to alpaca trade api"
    api.submit_order(
        symbol=ticker,
        side='buy',
        type='market',
        qty=quantity,
        time_in_force='day')

def sellAll() -> None:
    pass

def getPositions() -> None:
    assert api, "Not connected to alpaca trade api"
    positions = api.list_positions()
    print(positions)

def getSecretKey() -> str:
    clipboard = pyperclip.paste()
    envVar = os.getenv('alpaca_secret')
    secret = envVar or clipboard
    assert secret, "No Alpaca secret found"
    return secret

def connect(secret_key : str = '') -> None:
    global api
    if not secret_key:
        secret_key = getSecretKey()

    print('Connecting to alpaca trade api')
    print(f'Trying secret key: {secret_key}')

    try: # initiate connection or print error message if failed
        api = tradeapi.REST(key, secret_key, endpoint)
        print(api.get_account())
    except:
        api = None
        print('Failed connecting to alpaca trade api')
        print("Set enviroment variable 'alpaca_secret' to secret key or copy it to clipboard")

api = None
connect()


'''
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
'''
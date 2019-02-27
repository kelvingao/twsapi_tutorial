# app.py
"""
There are two parts to the IB story: a wrapper and a client. 
The client asks the IB server (gateway or TWS) to do stuff, and the wrapper receives the messages.

Writing for the ibapi consists of extending the EClient which asks the server to do something, 
and extending the EWrapper to deal with what comes back.
"""
from ibapi.wrapper import EWrapper
from ibapi.client import EClient

class App(EWrapper, EClient):
  def __init__(self, ipaddress, portid, clientid):
    EClient.__init__(self, wrapper=self)
    EWrapper.__init__(self)
    self.connect(ipaddress, portid, clientid)
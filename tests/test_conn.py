# test_app.py
import pytest

from ibapi.wrapper import EWrapper
from ibapi.client import EClient

@pytest.fixture
def app(request):
  app = App("127.0.0.1", 4002, 10)
  yield app
  app.disconnect()

class App(EWrapper, EClient):
  def __init__(self, ipaddress, portid, clientid):
    EClient.__init__(self, wrapper=self)
    EWrapper.__init__(self)
    self.connect(ipaddress, portid, clientid)
    
class TestApp:
  def test_connection_attributes(self, app):
    assert app.isConnected()
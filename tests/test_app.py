# test_app.py

class TestApp:
  def test_connection_attributes(self, app):
    assert app.isConnected()
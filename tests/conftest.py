# conftest.py

import pytest
from .app import App

@pytest.fixture
def app(request):
  app = App("127.0.0.1", 4002, 10)
  yield app
  app.disconnect()
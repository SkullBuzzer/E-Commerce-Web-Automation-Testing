""" Base class to use setup fixture from the conftest.py file """

import pytest
from Utility_Classes.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class BaseClass:
    """ class to use setup fixture and any other methods """
    pass

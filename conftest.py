import pytest
import os

QA_config = 'qa.prop'
prod_config = 'prod.prop'

def pytest_addoption(parser):
    parser.addoption("--cmdopt", default='QA')

@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n In CmdOpt fixture function")
    opt = pytestconfig.getoption("cmdopt")
    if opt == "Prod":
        f = open(os.path.join(os.path.dir(__file__), prod_config), "r")
    else:
        f = open(os.path.join(os.path.dir(__file__), QA_config), "r")
    yield f
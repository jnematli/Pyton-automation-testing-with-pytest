import pytest

def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']

@pytest.fixture(scope='module')
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append('thur')
    yield wk
    print("\n Fixture setup01 closing")
    #wk.pop() #remove the last element from the list

@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2

@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months")
    print("\n in Fixture setup04")
    print("\n Fixture Scope: " + str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    mon.append("Apr")
    yield mon

@pytest.fixture
def setup05():
    def get_structure(name):
        if name == 'list':
            return [1, 2, 3]
        elif name == 'tuple':
            return (1, 3, 4)
    return get_structure
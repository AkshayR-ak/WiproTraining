import pytest

@pytest.fixture(scope='function', autouse=True)
#setup - like a constructor always run first
def setup_teardown():
    print('Starting.........')
    yield#Split into setup & teardown
    print('Ending...........')

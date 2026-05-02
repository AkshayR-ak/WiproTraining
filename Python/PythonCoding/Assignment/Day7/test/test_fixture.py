from test.conftest import num_list


def test_fixture(num_list):
    assert len(num_list) == 5
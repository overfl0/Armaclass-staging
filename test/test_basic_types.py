from armaclass import parse


def test_empty():
    expected = {}
    result = parse('')
    assert result == expected


def test_string():
    expected = {'var': 'foo'}
    result = parse('var="foo";')
    assert result == expected
    assert type(result['var']) == str


def test_float():
    expected = {'var': 12.3}
    result = parse('var=12.3;')
    assert result == expected
    assert type(result['var']) == float


def test_int():
    expected = {'var': 12}
    result = parse('var=12;')
    assert result == expected
    assert type(result['var']) == int


def test_class():
    expected = {'var': {}}
    result = parse('class var {};')
    assert result == expected
    assert type(result['var']) == dict


def test_empty_array():
    expected = {'var': []}
    result = parse('var[]={};')
    assert result == expected
    assert type(result['var']) == list


def test_array():
    expected = {'var': [1, 2, 3]}
    result = parse('var[]={1, 2, 3};')
    assert result == expected
    assert type(result['var']) == list

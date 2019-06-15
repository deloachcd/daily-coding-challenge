from solution import suggest_completions


def test_their_cases():
    assert suggest_completions('de', ['dog', 'deer', 'deal']) == ['deer', 'deal']


def test_my_cases():
    completions = suggest_completions('pos', [
        'positive_variable',
        'negative_variable',
        'positive_variable1987',
        'PositiveVariable',
        'girlsnightout',
        'system.out',
        'pos.rootnode',
        'boiyouknow',
        'darren, what happened to jimmy?'
    ])
    expected = [
        'positive_variable',
        'positive_variable1987',
        'pos.rootnode',
    ]
    assert [word in completions for word in expected]
    assert [word in expected for word in completions]

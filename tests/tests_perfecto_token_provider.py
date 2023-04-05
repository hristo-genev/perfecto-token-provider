from perfecto_token_provider import perfecto_token_provider


def test_missing_environement_variable():
    res = perfecto_token_provider.get_token_for_cloud(None)
    assert res is None


def test_load_token():
    res = perfecto_token_provider.get_token_for_cloud("dummy")
    assert res is not None

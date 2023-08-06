from pandas import DataFrame

def assert_required_columns(df: DataFrame, *required):
    _missing = [col for col in required if col not in df]

    if _missing:
        raise KeyError(*_missing)
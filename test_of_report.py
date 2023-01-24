from create_dataframe import df

# add to this list names of fields that should have only unique values
ls_of_unique_fields = []

# add to this list names of fields that should be without empty values
ls_of_not_null_fields = []

# add to this list names of fields which should have values more or equal zero
ls_of_not_bellow_zero_fields = []


# funсtion for validate all dataframe for duplicates
def test_duplicate():
    duplicate_raw = df[df.duplicated() == True]
    is_duplicate = duplicate_raw.shape[0]  # shape gives tuple, where first value its count of rows in df
    assert is_duplicate == 0, 'duplicate in dataframe'


# function for validating unique values from ls_of_unique_fields
def test_check_unique():
    for el in ls_of_unique_fields:
        for e in df[el].duplicated():
            assert e is False, 'there are duplicate'


# function for validating empty values in ls_of_unique_fields
def test_check_null_for_unique():
    for el in ls_of_unique_fields:
        for e in df[el].isna():
            assert e is False, 'there are nulls in unique fields'


# function for validating empty values in ls_of_not_null_fields
def test_check_null():
    for el in ls_of_not_null_fields:
        for e in df[el].isna():
            assert e is False, 'there are nulls'


# function for validating values that < 0 in ls_of_bellow_zero_fields
def test_check_values_bellow_zero():
    for i in ls_of_not_bellow_zero_fields:
        for e in df[i]:
            e = float(e)
            assert e >= 0, 'There is values < 0'


# function for validating DataFrame for existing symbols
def test_check_validity():
    denied = ['!', '#', '%', '&', '/', '@', '`', '~', '=', '}', '{', ']' ',']

    # use apply() method with any() function to check if any value in the dataframe contains a symbol
    df_to_str = df.astype(str)
    contains_hash = df_to_str.apply(lambda x: x.str.contains('|'.join(denied)).any())
    for i in contains_hash:
        assert i is False, f'there is symbols in {contains_hash}'

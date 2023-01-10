import pandas as pd
from config import file_name, file_type, ls_of_unique_fields, ls_of_not_null_fields, ls_of_not_bellow_zero_fields

PATH = f'C:/Users/User/Downloads/{file_name}.{file_type}'
TYPE_FUNC = {'csv': pd.read_csv, 'xlsx': pd.read_excel, 'json': pd.read_json}

df = TYPE_FUNC[file_type](PATH)


# function for validating unique values from ls_of_unique_fields
def check_unique(ls):
    for el in ls_of_unique_fields:
        for e in df[el].duplicated():
            assert e is False, 'there are duplicate'


# function for validating empty values in ls_of_not_null_fields
def check_null(ls):
    for el in ls_of_not_null_fields:
        for e in df[el].isna():
            assert e is False, 'there are nulls'


# function for validating values that < 0 in ls_of_bellow_zero_fields
def check_values_bellow_zero(ls):
    for i in ls_of_not_null_fields:
        for e in df[i]:
            assert e >= 0, 'There is values < 0'


# function for validating DataFrame for existing symbols
def check_validity(dataframe):
    denied = ['!', '#', '%', '&', '/', '@', '`', '~', '=', '}', '{', ']' ',']

    # use apply() method with any() function to check if any value in the dataframe contains a symbol
    df_to_str = df.astype(str)
    contains_hash = df_to_str.apply(lambda x: x.str.contains('|'.join(denied)).any())
    assert contains_hash is False, f'there is symbols in {contains_hash}'


def main():
    check_null(ls_of_not_null_fields)
    check_unique(ls_of_unique_fields)
    check_validity(df)
    check_values_bellow_zero(ls_of_not_bellow_zero_fields)


if __name__ == "__main__":
    main()

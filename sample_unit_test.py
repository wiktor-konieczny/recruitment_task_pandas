import pandas as pd
from solution import add_virtual_column

def test_sum_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=[
        "label_one", "label_two", "label_three"
    ])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), (
        f"The function should sum the columns: label_one and label_two.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )

def test_multiplication_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 1]] * 2, columns=[
        "label_one", "label_two", "label_three"
    ])
    df_result = add_virtual_column(df, "label_one * label_two", "label_three")
    assert df_result.equals(df_expected), (
        f"The function should multiply the columns: label_one and label_two.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )

def test_subtraction_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 0]] * 2, columns=[
        "label_one", "label_two", "label_three"
    ])
    df_result = add_virtual_column(df, "label_one - label_two", "label_three")
    assert df_result.equals(df_expected), (
        f"The function should subtract the columns: label_one and label_two.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )

def test_empty_result_when_invalid_labels():
    df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label3")
    assert df_result.empty, (
        f"Should return an empty df when the \"new_column\" is invalid.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )

    df = pd.DataFrame([[1, 2]] * 3, columns=["label-one", "label_two"])
    df_result = add_virtual_column(df, "label-one + label_two", "label")
    assert df_result.empty, (
        f"Should return an empty df when both df columns and roles are invalid.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )

    df = pd.DataFrame([[1, 2]] * 3, columns=["label-one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label")
    assert df_result.empty, (
        f"Should return an empty df when a df column is invalid.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )

def test_empty_result_when_invalid_rules():
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one \ label_two", "label_three")
    assert df_result.empty, (
        f"Should return an empty df when the role has an invalid character: '\\'.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )

    df_result = add_virtual_column(df, "label&one + label_two", "label_three")
    assert df_result.empty, (
        f"Should return an empty df when the role has an invalid character: '&'.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )

    df_result = add_virtual_column(df, "label_five + label_two", "label_three")
    assert df_result.empty, (
        f"Should return an empty df when the role has a column which isn't in the df: "
        f"'label_five'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    )

def test_when_extra_spaces_in_rules():
    df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=[
        "label_one", "label_two", "label_three"
    ])
    
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), (
        f"Should work when the role has no spaces between the operation and the column.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )

    df_result = add_virtual_column(df, "label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), (
        f"Should work when the role has spaces between the operation and the column.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )

    df_result = add_virtual_column(df, " label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), (
        f"Should work when the role has extra spaces at the start/end.\n\n"
        f"Result:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    )
import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    # Checking if the column names have the correct format
    if not re.fullmatch(r'[a-zA-Z_]+', new_column):
        return pandas.DataFrame([])
    if not all(re.fullmatch(r'[a-zA-Z_]+', col) for col in df.columns):
        return pandas.DataFrame([])

    # Dividing given equation into pieces
    pattern = r'[a-zA-Z_]+|[+\-*]'
    tokens = re.findall(pattern, role)

    expr = '' 
    for element in tokens:
        if element in df.columns:
            # Building the expression
            expr += f'df["{element}"]'
        elif element in ['+', '-', '*']:
            # Adding signs to equation
            expr += f' {element} '
        else:
            # Catching non-existent columns
            return pandas.DataFrame([])

    # Return if the expression is empty
    if not expr:
        return pandas.DataFrame([])

    # Execute the operation using eval()
    try:
        df_copy = df.copy()
        df_copy[new_column] = eval(expr)
        return df_copy
    except Exception:
        return pandas.DataFrame([])
"""preprocessing module of the vboUtil package, mainly for preprocessing purposes."""

import pandas as pd
import numpy as np

def outlier_thresholds(df, variable, lower=0.05, upper=0.95):

    """
preprocessing.outlier_thresholds(df, variable, lower=0.01, upper=0.99)
    Returns the outlier threshold values for a variable in the DataFrame,
    given the upper and lower quantile values.

    Parameters: df: pandas.DataFrame object
                    DataFrame object containing the variable
                variable: str
                    Name of the variable inspected
                lower: int or float
                    Lower quantile value for the threshold
                upper: int or float
                    Upper quantile value for the threshold

    Return: low_limit: float
                Lower limit for the outlier threshold
            up_limit: float
                Upper limit for the outlier threshold

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame object.")

    if not type(variable)==str:
        raise TypeError("'variable' must be a string.")

    if not (type(lower)==float):
        raise TypeError("'lower' must be a float value.")

    if not (type(upper)==float):
        raise TypeError("'upper' must be a float value.")

    quartile1 = df[variable].quantile(lower)
    quartile3 = df[variable].quantile(upper)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_with_thresholds(df, variable, lower=0.05, upper=0.95):

    """
preprocessing.replace_with_threshold(df, variable, lower=0.05, upper=0.95)
    Replaces the outliers of a variable of the DataFrame with the
    threshold values.

    Parameters: df: pandas.DataFrame object
                    DataFrame object containing the variable
                variable: str
                    Name of the variable inspected
                lower: int or float
                    Lower quantile value for the threshold
                upper: int or float
                    Upper quantile value for the threshold

    Return: None

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame object.")

    if not type(variable) == str:
        raise TypeError("'variable' must be a string.")

    if not (type(lower)==float):
        raise TypeError("'lower' must be a float value.")

    if not (type(upper)==float):
        raise TypeError("'upper' must be a float value.")

    low_limit, up_limit = outlier_thresholds(df, variable, lower, upper)
    df.loc[(df[variable] < low_limit), variable] = low_limit
    df.loc[(df[variable] > up_limit), variable] = up_limit

def remove_outliers(df, col_name, lower, upper):
    """
preprocessing.remove_outliers(df, variable, lower=0.05, upper=0.95)
    Removes the outliers of a variable of the DataFrame that are
    outside of the interval defined by threshold values.

    Parameters: df: pandas.DataFrame object
                    DataFrame object containing the variable
                col_name: str
                    Name of the variable inspected
                lower: int or float
                    Lower quantile value for the threshold
                upper: int or float
                    Upper quantile value for the threshold

    Return: None

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' should be a pandas DataFrame object.")

    if not type(col_name) == str:
        raise TypeError("'variable' must be a string.")

    if not ((type(lower)==int) or (type(lower)==float)):
        raise TypeError("'lower' must be a float value.")

    if not ((type(upper)==int) or (type(upper)==float)):
        raise TypeError("'upper' must be a float value.")


    low_limit, up_limit = outlier_thresholds(df, col_name, lower, upper)
    df_without_outliers = df[~((df[col_name] < low_limit) | (df[col_name] > up_limit))]
    return df_without_outliers

def rare_encoder(df, rare_perc):
    """
preprocessing.rare_encoder
    For each categorical column: Convert the levels of the categories
    with low frequencies to a single level

    Parameters: df: pandas.DataFrame object
                    DataFrame to be rare encoded
                rare_perc: float
                    Threshold value for frequencies
                    to decide if a level is rare

    Return: pandas.DataFrame object: Rare encoded data
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a DataFrame object")
    if not type(rare_perc)==float:
        raise TypeError("'rare_perc' must be a float")

    temp_df = df.copy()

    rare_columns = [col for col in temp_df.columns if temp_df[col].dtypes == 'O'
                    and (temp_df[col].value_counts() / len(temp_df) < rare_perc).any(axis=None)]

    for var in rare_columns:
        tmp = temp_df[var].value_counts() / len(temp_df)
        rare_labels = tmp[tmp < rare_perc].index
        temp_df[var] = np.where(temp_df[var].isin(rare_labels), 'Rare', temp_df[var])

    return temp_df
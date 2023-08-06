"""eda module of the vboUtil package, mainly for EDA purposes."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import preprocessing


def check_df(df, head=5):
    """
explatory.check_df(df, head=5)
    Quick look at the data

    Parameters: df: pandas.DataFrame object
                    DataFrame object to be inspected
                head: integer
                    First and Last n rows to be shown

    Returns: None
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object must be given as the 'df' parameter.")

    if not type(head)==int:
        raise TypeError("'head' parameter must be defined as an integer.")


    print("##################### Shape #####################")
    print(df.shape)
    print("##################### Types #####################")
    print(df.dtypes)
    print("##################### Head #####################")
    print(df.head(head))
    print("##################### Tail #####################")
    print(df.tail(head))
    print("##################### NA #####################")
    print(df.isnull().sum())
    print("##################### Quantiles #####################")
    print(df.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

def check_outlier(df, col_name, lower=0.05, upper=0.95):
    """
explatory.check_outlier(df, col_name)
    Check if the variable has any outlier

    Parameters: df: pandas.DataFrame object
                    DataFrame object containing the variable
                col_name: str
                    Name of the variable inspected
                lower: int or float
                    Lower quantile value for the threshold
                upper: int or float
                    Upper quantile value for the threshold

    Returns: None
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame object.")

    if not type(col_name) == str:
        raise TypeError("'variable' must be a string.")

    if not (type(lower) == float):
        raise TypeError("'lower' must be a float value.")

    if not (type(upper) == float):
        raise TypeError("'upper' must be a float value.")

    low_limit, up_limit = preprocessing.outlier_thresholds(df, col_name, lower, upper)
    if df[(df[col_name] > up_limit) | (df[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False

def grab_outliers(df, col_name, index=False, lower=0.05, upper=0.95):
    """
explatory.grab_outliers(df, col_name)
    Print the outlier values

    Parameters: df: pandas.DataFrame object
                    DataFrame object containing the variable
                col_name: str
                    Name of the variable inspected
                index: bool
                    If true, return indexes of the outliers
                lower: int or float
                    Lower quantile value for the threshold
                upper: int or float
                    Upper quantile value for the threshold

    Returns: None or pandas.Index if index=True
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame object.")

    if not type(col_name) == str:
        raise TypeError("'variable' must be a string.")

    if not type(index)==bool:
        raise TypeError("'index' must be a bool.")

    if not (type(lower) == float):
        raise TypeError("'lower' must be a float value.")

    if not (type(upper) == float):
        raise TypeError("'upper' must be a float value.")

    low, up = preprocessing.outlier_thresholds(df, col_name, lower, upper)
    if df[((df[col_name] < low) | (df[col_name] > up))].shape[0] > 10:
        print(df[((df[col_name] < low) | (df[col_name] > up))].head())
    else:
        print(df[((df[col_name] < low) | (df[col_name] > up))])

    if index:
        outlier_index = df[((df[col_name] < low) | (df[col_name] > up))].index
        return outlier_index

def rare_analyser(df, target, cat_cols):
    """
eda.rare_analyser(df, target, cat_cols)
    Prints the counts and frequencies of the levels of the categories and
    their relation with the output

    Parameters: df: pandas.DataFrame object
                    DataFrame object to inspect
                target: str
                    Name of the target column
                cat_cols: array-like
                    Names of the categorical columns to inspect

    Return: None

    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame object.")

    if not type(target) == str:
        raise TypeError("'target' must be a string.")

    for col in cat_cols:
        print(col, ":", len(df[col].value_counts()))
        print(pd.DataFrame({"COUNT": df[col].value_counts(),
                            "RATIO": df[col].value_counts() / len(df),
                            "TARGET_MEAN": df.groupby(col)[target].mean()}), end="\n\n\n")

def missing_values_table(df, na_name=False):
    """
eda.missing_values_table(df, na_name=False
    Prints the number and ratio of the missing values

    Parameters: df: pandas DataFrame object
                    DataFrame object to inspect
                na_name: bool
                    If true, returns the names of the columns
                    that contains missing values

    Return: None or list if na_name=True

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object must be given as the 'df' parameter.")

    if not type(na_name)==bool:
        raise TypeError("'na_name' parameter must be defined as a bool.")

    na_columns = [col for col in df.columns if df[col].isnull().sum() > 0]
    n_miss = df[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (df[na_columns].isnull().sum() / df.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")
    if na_name:
        return na_columns

def missing_vs_target(df, target, na_columns):
    """
eda.missing_vs_target(df, target, na_columns)
    Prints the number and ratio of the missing values

    Parameters: df: pandas DataFrame object
                    DataFrame object to inspect
                target: str
                    Name of the target variable column
                na_columns: array-like
                    Name/Names of the columns with missing value

    Return: None

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object must be given as the 'df' parameter.")

    if not type(target) == str:
        raise TypeError("'target' parameter must be defined as a str.")

    temp_df = df.copy()
    for col in na_columns:
        temp_df[col + '_NA_FLAG'] = np.where(temp_df[col].isnull(), 1, 0)
    na_flags = temp_df.loc[:, temp_df.columns.str.contains("_NA_")].columns
    for col in na_flags:
        print(pd.DataFrame({"TARGET_MEAN": temp_df.groupby(col)[target].mean(),
                            "Count": temp_df.groupby(col)[target].count()}), end="\n\n\n")

def cat_summary(df, col_name, plot=False):
    """
    explatory.cat_summary(df, col_name, plot=False)
        Prints the frequencies of the categories in a column

        Parameters: df: pandas.DataFrame object
                        DataFrame object to be inspected
                    col_name: string
                        Name of the column to be inspected
                    plot: bool
                        If True, plot the frequencies as a seaborn countplot

        Returns: None
        """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not type(col_name)==str:
        raise TypeError("'col_name' parameter must be defined as a string.")

    if not type(plot)==bool:
        raise TypeError("'plot' parameter must be defined as a bool.")

    print(pd.DataFrame({col_name: df[col_name].value_counts(),
                        "Ratio": 100 * df[col_name].value_counts() / len(df)}))
    print("##########################################")
    if plot:
        sns.countplot(x=df[col_name], data=df)
        plt.show()

def num_summary(df, numerical_col, plot=False, bins=20):
    """
        explatory.num_summary(df, numerical_col, plot=False)
            Prints the distributional statistics

            Parameters: df: pandas.DataFrame object
                            DataFrame object to be inspected
                        numerical_col: string
                            Name of the column to be inspected
                        plot: bool
                            If True, plot the histogram of the variable
                        bins: integer
                            If plot=True, number of the bins on the histogram

            Returns: None
            """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not type(numerical_col)==str:
        raise TypeError("'col_name' parameter must be defined as a string.")

    if not type(plot)==bool:
        raise TypeError("'plot' parameter must be defined as a bool.")

    if not type(bins)==int:
        raise TypeError("'bins' parameter must be defined as an integer.")

    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(df[numerical_col].describe(quantiles).T)

    if plot:
        df[numerical_col].hist(bins=bins)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show()

def grab_col_names(df, cat_th=10, car_th=20):
    """

    Returns the categorical, numerical and categorical-with-high-cardinality columns.
    Note: Integer-looking categorical variables are included in the categorical columns.


    Parameters: df: pandas.DataFrame object
                    DataFrame object to be inspected
                cat_th: int
                    For integer columns, if nunique<cat_th,
                    the column is treated as a categorical one.
                car_th: int
                    For categorical columns, if nunique>car_th,
                    the column is treated as a numerical one.

    Returns:    cat_cols: list
                    List of categorical variables
                num_cols: list
                    List of numerical variables
                cat_but_car: list
                    List of categorical variables with high cardinality

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = total number of variables
        num_but_cat is included in the cat_cols.

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not type(car_th)==int:
        raise TypeError("'car_th' parameter must be defined as an integer.")

    if not type(cat_th)==int:
        raise TypeError("'cat_th' parameter must be defined as an integer.")

    # cat_cols, cat_but_car
    cat_cols = [col for col in df.columns if df[col].dtypes == "O"]
    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and
                   df[col].dtypes != "O"]
    cat_but_car = [col for col in df.columns if df[col].nunique() > car_th and
                   df[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in df.columns if df[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {df.shape[0]}")
    print(f"Variables: {df.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car

def target_summary_with_cat(df, target, categorical_col):
    """
    Prints the mean of the target value after grouping the data by categorical_col.

    Parameters: df: pandas.DataFrame object
                    DataFrame object to be inspected
                target: str
                    Name of the target variable
                categorical_col: str
                    Name of the categorical variable that we want to observe the relation
                    with the target variable

    Return: None
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not type(target)==str:
        raise TypeError("'target' parameter must be defined as a string.")

    if not type(categorical_col)==str:
        raise TypeError("'categorical_col' parameter must be defined as a string.")

    print(pd.DataFrame({"TARGET_MEAN": df.groupby(categorical_col)[target].mean()}), end="\n\n\n")

def target_summary_with_num(df, target, numerical_col):
    """
        Prints the mean of a numerical input after grouping the data by categorical output.

        Parameters: df: pandas.DataFrame object
                        DataFrame object to be inspected
                    target: str
                        Name of the target variable
                    numerical_col: str
                        Name of the numerical variable that we want to observe the relation
                        with the target variable

        Return: None
        """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not type(target)==str:
        raise TypeError("'target' parameter must be defined as a string.")

    if not type(numerical_col)==str:
        raise TypeError("'numerical_col' parameter must be defined as a string.")

    print(df.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

def high_correlated_cols(df, plot=False, corr_th=0.90):
    """
        Prints the mean of a numerical input after grouping the data by categorical output.

        Parameters: df: pandas.DataFrame object
                        DataFrame object to be inspected
                    plot: bool
                        If True, plot the correlation heatmap
                    corr_th: float
                        Threshold for the variable correlation.
                        If two variables have a correlation more
                        than this threshold, one of them is dropped.
                        Should be between -1 and 1.

            Return: drop_list: Highly correlated columns to be dropped
            """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not type(plot)==bool:
        raise TypeError("'plot' parameter must be defined as a bool.")

    if not type(corr_th)==float:
        raise TypeError("'corr_th' parameter must be defined as a float.")

    corr = df.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


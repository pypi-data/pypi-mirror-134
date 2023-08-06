"""methods module of the vboUtil package, mainly for basic methods related
 to real-life business practices."""

import pandas as pd
import datetime as dt
import sklearn
import vboUtil.preprocessing
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter



def create_rfm(df):

    """
create_rfm(df)
    Returns the RFM results as DataFrame.

    DataFrame given to this function must have columns named as
    'Price', 'Quantity', 'Invoice', 'InvoiceDate' and 'Customer ID'.
    'Price' and 'Quantity' must have float or integer type, 'InvoiceDate'
    must have datetime.datetime object type.

    Parameters: df: pandas.DataFrame object
                    DataFrame that contains the feature information
                    required for RFM analysis.

    Return:     rfm: pandas.DataFrame object
                    RFM analysis results

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    df["TotalPrice"] = df["Quantity"] * df["Price"]
    df.dropna(inplace=True)
    dataframe = df[~df["Invoice"].str.contains("C", na=False)]

    today_date = dt.datetime(2011, 12, 11)
    rfm = dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'Invoice': lambda num: num.nunique(),
                                                "TotalPrice": lambda price: price.sum()})
    rfm.columns = ['recency', 'frequency', "monetary"]
    rfm = rfm[(rfm['monetary'] > 0)]

    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

    rfm['rfm_segment'] = rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str)

    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm['rfm_segment'] = rfm['rfm_segment'].replace(seg_map, regex=True)
    rfm = rfm[["recency", "frequency", "monetary", "rfm_segment"]]
    return rfm

def create_cltv_c(df, profit=0.10):
    """
create_cltv_c(df, profit=0.10)
    Returns the CLTV results as DataFrame.

    DataFrame given to this function must have columns named as
    'Price', 'Quantity', 'Invoice', 'InvoiceDate' and 'Customer ID'.
    'Price' and 'Quantity' must have float or integer type, 'InvoiceDate'
    must have datetime.datetime object type.

    Parameters: df: pandas.DataFrame object
                    DataFrame that contains the feature information
                    required for RFM analysis.
                profit: float
                    Average profit earned from the products sold

    Return:     cltv_c: pandas.DataFrame object
                    CLTV analysis results

    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not ((type(profit)==float) or (type(profit)==int)):
        raise TypeError("'profit' should be either a float or an integer")

    dataframe = df[~df["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[(dataframe['Quantity'] > 0)]
    dataframe.dropna(inplace=True)
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    cltv_c = dataframe.groupby('Customer ID').agg({'Invoice': lambda x: x.nunique(),
                                                   'Quantity': lambda x: x.sum(),
                                                   'TotalPrice': lambda x: x.sum()})
    cltv_c.columns = ['total_transaction', 'total_unit', 'total_price']

    # avg_order_value
    cltv_c['avg_order_value'] = cltv_c['total_price'] / cltv_c['total_transaction']

    # purchase_frequency
    cltv_c["purchase_frequency"] = cltv_c['total_transaction'] / cltv_c.shape[0]

    # repeat rate & churn rate
    repeat_rate = cltv_c[cltv_c.total_transaction > 1].shape[0] / cltv_c.shape[0]
    churn_rate = 1 - repeat_rate

    # profit_margin
    cltv_c['profit_margin'] = cltv_c['total_price'] * profit

    # Customer Value
    cltv_c['customer_value'] = (cltv_c['avg_order_value'] * cltv_c["purchase_frequency"])

    # Customer Lifetime Value
    cltv_c['cltv'] = (cltv_c['customer_value'] / churn_rate) * cltv_c['profit_margin']

    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaler.fit(cltv_c[["cltv"]])
    cltv_c["scaled_cltv"] = scaler.transform(cltv_c[["cltv"]])

    # Segment
    cltv_c["segment"] = pd.qcut(cltv_c["scaled_cltv"], 4, labels=["D", "C", "B", "A"])

    return cltv_c

def create_cltv_p(df, month=3):
    """
create_cltv_p(df, month=3)
    Returns the CLTV predicitons as DataFrame.

    DataFrame given to this function must have columns named as
    'Price', 'Quantity', 'Invoice', 'InvoiceDate' and 'Customer ID'.
    'Price' and 'Quantity' must have float or integer type, 'InvoiceDate'
    must have datetime.datetime object type.

    Parameters: df: pandas.DataFrame object
                    DataFrame that contains the feature information
                    required for RFM analysis.
                month: integer
                    Length of the prediction horizon (in months)

    Return:     cltv_final: pandas.DataFrame object
                    CLTV Prediction analysis results

    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("pandas DataFrame object should be given as the 'df' parameter.")

    if not (type(month) == int):
        raise TypeError("'profit' should be either a float or an integer")

    df.dropna(inplace=True)
    dataframe = df[~df["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]

    vboUtil.preprocessing.replace_with_thresholds(dataframe, "Quantity")
    vboUtil.preprocessing.replace_with_thresholds(dataframe, "Price")

    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    today_date = dt.datetime(2011, 12, 11)
    cltv_df = dataframe.groupby('Customer ID').agg({'InvoiceDate': [lambda date: (date.max() - date.min()).days,
                                                                    lambda date: (today_date - date.min()).days],
                                                    'Invoice': lambda num: num.nunique(),
                                                    'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

    cltv_df.columns = cltv_df.columns.droplevel(0)
    cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']
    cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]
    cltv_df = cltv_df[cltv_df["monetary"] > 0]
    cltv_df["recency"] = cltv_df["recency"] / 7
    cltv_df["T"] = cltv_df["T"] / 7
    cltv_df = cltv_df[(cltv_df['frequency'] > 1)]

    bgf = BetaGeoFitter(penalizer_coef=0.001)
    bgf.fit(cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T'])

    cltv_df["expected_purc_1_week"] = bgf.predict(1,
                                                  cltv_df['frequency'],
                                                  cltv_df['recency'],
                                                  cltv_df['T'])

    cltv_df["expected_purc_1_month"] = bgf.predict(4,
                                                   cltv_df['frequency'],
                                                   cltv_df['recency'],
                                                   cltv_df['T'])

    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(cltv_df['frequency'], cltv_df['monetary'])
    cltv_df["expected_average_profit"] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                                 cltv_df['monetary'])

    cltv = ggf.customer_lifetime_value(bgf,
                                       cltv_df['frequency'],
                                       cltv_df['recency'],
                                       cltv_df['T'],
                                       cltv_df['monetary'],
                                       time=month,  # 3 aylık
                                       freq="W",  # T'nin frekans bilgisi.
                                       discount_rate=0.01)

    cltv = cltv.reset_index()
    cltv_final = cltv_df.merge(cltv, on="Customer ID", how="left")
    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaler.fit(cltv_final[["clv"]])
    cltv_final["scaled_clv"] = scaler.transform(cltv_final[["clv"]])

    cltv_final["segment"] = pd.qcut(cltv_final["scaled_clv"], 4, labels=["D", "C", "B", "A"])

    return cltv_final


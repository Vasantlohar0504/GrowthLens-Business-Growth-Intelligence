def add_time_features(df):
    
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Month_Name'] = df['Order Date'].dt.month_name()

    return df


def calculate_profit_margin(df):

    df['Profit_Margin'] = df['Profit'] / df['Sales']

    return df
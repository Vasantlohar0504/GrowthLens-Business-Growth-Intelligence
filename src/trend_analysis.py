def monthly_sales(df):
    
    df['MonthYear'] = df['Order Date'].dt.to_period('M')

    monthly = df.groupby('MonthYear')['Sales'].sum()

    return monthly


def yearly_sales(df):

    yearly = df.groupby('Year')['Sales'].sum()

    return yearly


def region_sales(df):

    return df.groupby("Region")["Sales"].sum()
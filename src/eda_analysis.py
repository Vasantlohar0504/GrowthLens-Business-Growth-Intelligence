def category_sales(df):
    
    return df.groupby("Category")["Sales"].sum().sort_values(ascending=False)


def segment_sales(df):

    return df.groupby("Segment")["Sales"].sum()


def top_products(df):

    return df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)


def city_sales(df):

    return df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)
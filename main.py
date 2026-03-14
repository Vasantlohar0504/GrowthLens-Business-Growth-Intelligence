from src.data_cleaning import clean_data, save_clean_data
from src.data_processing import add_time_features, calculate_profit_margin
from src.eda_analysis import category_sales, top_products
from src.trend_analysis import monthly_sales, region_sales
from src.visualization import plot_sales_trend, plot_region_sales, plot_category_sales, plot_top_products

file_path = "data/raw/global_superstore_2016.xlsx"

df = clean_data(file_path)

df = add_time_features(df)

df = calculate_profit_margin(df)

save_clean_data(df, "data/processed/cleaned_sales_data.csv")

monthly = monthly_sales(df)
regions = region_sales(df)
categories = category_sales(df)
products = top_products(df)

plot_sales_trend(monthly)
plot_region_sales(regions)
plot_category_sales(categories)
plot_top_products(products)
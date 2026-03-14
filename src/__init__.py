"""
Business Growth Analytics Package

This package contains modules used for the Business Growth Analytics project.
It includes functionality for data cleaning, processing, exploratory data
analysis (EDA), trend analysis, and data visualization.

Modules Included:
- data_cleaning: Handles loading and cleaning of raw datasets.
- data_processing: Adds new features and prepares data for analysis.
- eda_analysis: Performs exploratory data analysis.
- trend_analysis: Identifies business growth trends.
- visualization: Generates charts and visual reports.
"""

# Import functions from modules for easier access

from .data_cleaning import clean_data, save_clean_data
from .data_processing import add_time_features, calculate_profit_margin
from .eda_analysis import category_sales, segment_sales, top_products, city_sales
from .trend_analysis import monthly_sales, yearly_sales, region_sales
from .visualization import (
    plot_sales_trend,
    plot_region_sales,
    plot_category_sales,
    plot_top_products
)

# Define what is available when importing *
__all__ = [
    "clean_data",
    "save_clean_data",
    "add_time_features",
    "calculate_profit_margin",
    "category_sales",
    "segment_sales",
    "top_products",
    "city_sales",
    "monthly_sales",
    "yearly_sales",
    "region_sales",
    "plot_sales_trend",
    "plot_region_sales",
    "plot_category_sales",
    "plot_top_products"
]
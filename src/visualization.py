import matplotlib.pyplot as plt
import os

os.makedirs("reports/figures", exist_ok=True)


def plot_sales_trend(monthly_sales):

    plt.figure(figsize=(10,5))
    monthly_sales.plot()

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.savefig("reports/figures/sales_trend.png")

    plt.show()


def plot_region_sales(region_sales):

    plt.figure(figsize=(7,7))

    region_sales.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Region Wise Sales")

    plt.savefig("reports/figures/region_sales.png")

    plt.show()


def plot_category_sales(category_sales):

    plt.figure(figsize=(8,5))

    category_sales.plot(kind="bar")

    plt.title("Category Sales")

    plt.savefig("reports/figures/category_sales.png")

    plt.show()


def plot_top_products(top_products):

    plt.figure(figsize=(10,6))

    top_products.plot(kind="bar")

    plt.title("Top 10 Products")

    plt.savefig("reports/figures/top_products.png")

    plt.show()
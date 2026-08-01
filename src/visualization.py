import matplotlib.pyplot as plt
import seaborn as sns
import os

# create image folder automatically
os.makedirs("images",exist_ok=True)

def monthly_sales_trend(df):
    monthly_sales = df.groupby('YearMonth')['Revenue'].sum().reset_index()
    plt.figure(figsize=(10,5))
    plt.plot(monthly_sales['YearMonth'].astype(str),
             monthly_sales['Revenue'],
             marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/monthly_sales_trend.png")
    plt.show()
    
def product_bar_chart(df):
    top_products = (
        df.groupby('Description')['Quantity']
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )
    plt.figure(figsize=(12,5))
    sns.barplot(x=top_products.index,
                y=top_products.values)
    plt.title("Top 10 Best Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("images/product_bar_chart.png")
    plt.show()
    
def revenue_histogram(df):
    sample_df = df.sample(1000, random_state=42)
    plt.figure(figsize=(8,5))
    sns.histplot(sample_df['Revenue'], bins=30, kde=True)
    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.savefig("images/revenue_histogram.png")
    plt.show()
    
def customer_spending(df):
    sample_df = df.sample(1000, random_state=42)
    spending = sample_df.groupby('CustomerID')['Revenue'].sum()
    plt.figure(figsize=(8,5))
    sns.histplot(spending, bins=30, kde=True)
    plt.title("Customer Spending Distribution")
    plt.xlabel("Total Spending")
    plt.savefig("images/customer_spending_distribution.png")
    plt.show()
    
def quantity_vs_revenue(df):
    sample_df = df.sample(1000, random_state=42)
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        x='Quantity',
        y='Revenue',
        data=sample_df
    )
    plt.title("Quantity vs Revenue")
    plt.savefig("images/scatter_plot.png")
    plt.show()
    
def country_pie(df):
    country = (
        df.groupby('Country')['Revenue']
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )
    plt.figure(figsize=(8,8))
    country.plot(
        kind='pie',
        autopct='%1.1f%%'
    )
    plt.ylabel("")
    plt.title("Revenue by Country")
    plt.savefig("images/country_pie.png")
    plt.show()
    
def revenue_boxplot(df):
    sample_df = df.sample(1000, random_state=42)
    plt.figure(figsize=(8,5))
    sns.boxplot(y=sample_df['Revenue'])
    plt.title("Revenue Boxplot")
    plt.savefig("images/revenue_boxplot.png")
    plt.show()
    
def heatmap(df):
    plt.figure(figsize=(7,5))
    sns.heatmap(
        df[['Quantity','UnitPrice','Revenue']].corr(),
        annot=True,
        cmap='Blues'
    )
    plt.title("Correlation Heatmap")
    plt.savefig("images/heatmap.png")
    plt.show()
    
def pair_plot(df):
    sample_df = df[['Quantity', 'UnitPrice', 'Revenue']].sample(1000, random_state=42)
    sns.pairplot(sample_df)
    plt.savefig("images/pairplot.png")
    plt.show()
    
def top_customer_chart(df):
    top_customers = (
        df.groupby('CustomerID')['Revenue']
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )
    plt.figure(figsize=(10,5))
    sns.barplot(
        x=top_customers.index.astype(str),
        y=top_customers.values
    )
    plt.title("Top 10 Customers by Revenue")
    plt.xlabel("Customer ID")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/top_customers.png")
    plt.show()


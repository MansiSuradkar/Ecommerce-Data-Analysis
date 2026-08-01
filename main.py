
#import modules
from src.load_data import load_data
from src.preprocessing import*
from src.analysis import*
from src.visualization import*
from src.report import generate_report


#load dataset
print("="*60)
print("Loading Dataset")
print("="*60)

df=load_data("data/online_retail.csv")

#Data Preprocessing
print("="*60)
print("Data Processing")
print("="*60)

dataset_info(df)

check_missing_values(df)

check_duplicates(df)

df=remove_duplicates(df)

df=remove_missing(df)

save_clean_data(df)

overall_insights(df)

#Data Analysis
customer_behaviour(df)

product_analysis(df)

monthly_analysis(df)

clv(df)

top_customers(df)

revenue_analysis(df)

product_prof(df)

#Data Visuialization
monthly_sales_trend(df)

product_bar_chart(df)

revenue_histogram(df)

customer_spending(df)

quantity_vs_revenue(df)

country_pie(df)

revenue_boxplot(df)

heatmap(df)

pair_plot(df)

top_customer_chart(df)

#Report Generation
generate_report(df)
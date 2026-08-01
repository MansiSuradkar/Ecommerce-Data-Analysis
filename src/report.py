import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Image,
    Spacer
)

def generate_report(df):
    print("Inside report function...")
    os.makedirs("reports",exist_ok=True)
    
    pdf = SimpleDocTemplate(
        "reports/Final_Report.pdf"
    )
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    elements.append(
        Paragraph(
            "E-Commerce Customer Purchase Analysis",
            styles["Title"]
        )     
    )
    elements.append(Spacer(1,20))
    
    
    # Business Insights
    elements.append(
        Paragraph(
            "<b>Business Insights</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Orders: {df['InvoiceNo'].nunique()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Customers: {df['CustomerID'].nunique()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Revenue: {round(df['Revenue'].sum(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Order Value: {round(df.groupby('InvoiceNo')['Revenue'].sum().mean(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Top Selling Product: {df.groupby('Description')['Quantity'].sum().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Revenue Country: {df.groupby('Country')['Revenue'].sum().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Repeat Customers: {(df.groupby('CustomerID')['InvoiceNo'].nunique()>1).sum()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Customer Lifetime Value: {round(df.groupby('CustomerID')['Revenue'].sum().mean(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1,20))
    
    # Charts
    elements.append(
        Paragraph(
            "<b>Charts</b>",
            styles["Heading2"]
        )
    )

    charts = [
        "monthly_sales_trend.png",
        "product_bar_chart.png",
        "revenue_histogram.png",
        "customer_spending_distribution.png",
        "scatter_plot.png",
        "country_pie.png",
        "revenue_boxplot.png",
        "heatmap.png",
        "pairplot.png",
        "top_customers.png"
    ]

    for chart in charts:
        elements.append(Image(f"images/{chart}", width=400, height=250))
        elements.append(Spacer(1,10))
        
    # Final Summary
    elements.append(
        Paragraph(
            "<b>Final Summary</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Revenue Generated: {round(df['Revenue'].sum(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Orders Processed: {df['InvoiceNo'].nunique()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Customers: {df['CustomerID'].nunique()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Order Value: {round(df.groupby('InvoiceNo')['Revenue'].sum().mean(),2)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Top Revenue Country: {df.groupby('Country')['Revenue'].sum().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1,20))
    
    # Recommendations
    elements.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    recommendations = [
        "1. Retain high-value customers through loyalty programs and personalized offers.",
        "2. Maintain adequate inventory for top-selling products to avoid stock shortages.",
        "3. Promote low-performing products using discounts or bundled offers.",
        "4. Focus marketing efforts on countries generating the highest revenue.",
        "5. Use monthly sales trends to plan seasonal promotions and inventory."
    ]

    for rec in recommendations:
        elements.append(
            Paragraph(rec, styles["BodyText"])
        )
    
    print("Building PDF...")
    pdf.build(elements)
    print("PDF Generated Successfully!")
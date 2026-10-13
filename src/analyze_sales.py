from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / 'data' / 'sales_data.csv'
OUTPUT_DIR = BASE_DIR / 'output'
OUTPUT_DIR.mkdir(exist_ok=True)


def load_and_clean_data():
    df = pd.read_csv(INPUT_FILE)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0)
    df = df.dropna(subset=['order_id', 'customer_id', 'product', 'order_date'])
    df = df.drop_duplicates(subset=['order_id'])
    df['revenue'] = df['quantity'] * df['unit_price']
    df['month'] = df['order_date'].dt.to_period('M').astype(str)
    return df


def build_reports(df):
    kpis = pd.DataFrame({
        'metric': ['Total Revenue', 'Total Orders', 'Unique Customers', 'Average Order Value'],
        'value': [
            round(df['revenue'].sum(), 2),
            int(df['order_id'].nunique()),
            int(df['customer_id'].nunique()),
            round(df.groupby('order_id')['revenue'].sum().mean(), 2)
        ]
    })

    monthly = df.groupby('month', as_index=False).agg(
        revenue=('revenue', 'sum'),
        orders=('order_id', 'nunique'),
        customers=('customer_id', 'nunique')
    )

    customer = df.groupby(['customer_id', 'customer_name'], as_index=False).agg(
        revenue=('revenue', 'sum'),
        orders=('order_id', 'nunique'),
        units=('quantity', 'sum')
    ).sort_values('revenue', ascending=False)

    product = df.groupby(['product', 'category'], as_index=False).agg(
        revenue=('revenue', 'sum'),
        units=('quantity', 'sum'),
        orders=('order_id', 'nunique')
    ).sort_values('revenue', ascending=False)

    region = df.groupby('region', as_index=False).agg(
        revenue=('revenue', 'sum'),
        orders=('order_id', 'nunique')
    ).sort_values('revenue', ascending=False)

    df.to_csv(OUTPUT_DIR / 'cleaned_sales_data.csv', index=False)
    kpis.to_csv(OUTPUT_DIR / 'kpi_summary.csv', index=False)
    monthly.to_csv(OUTPUT_DIR / 'monthly_sales.csv', index=False)
    customer.to_csv(OUTPUT_DIR / 'customer_analysis.csv', index=False)
    product.to_csv(OUTPUT_DIR / 'product_analysis.csv', index=False)
    region.to_csv(OUTPUT_DIR / 'regional_analysis.csv', index=False)

    with pd.ExcelWriter(OUTPUT_DIR / 'sales_analytics.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Cleaned Data', index=False)
        kpis.to_excel(writer, sheet_name='KPIs', index=False)
        monthly.to_excel(writer, sheet_name='Monthly Sales', index=False)
        customer.to_excel(writer, sheet_name='Customers', index=False)
        product.to_excel(writer, sheet_name='Products', index=False)
        region.to_excel(writer, sheet_name='Regions', index=False)

    print(kpis.to_string(index=False))
    print(f'\nReports generated in: {OUTPUT_DIR}')


if __name__ == '__main__':
    sales = load_and_clean_data()
    build_reports(sales)

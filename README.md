# Sales & Customer Analytics Dashboard

A Python and SQL analytics portfolio project that cleans transactional sales data and prepares KPI, customer, product, regional, and monthly trend datasets for analysis and dashboarding in Power BI or Excel.

## Tech Stack
- Python
- SQL / MySQL
- Pandas
- NumPy
- Power BI
- Excel
- Git

## What the project does
- Loads transactional sales data from CSV
- Cleans dates, numeric fields, missing values, and duplicate order IDs
- Calculates transaction revenue
- Produces total revenue, order count, unique customer count, and average order value KPIs
- Aggregates monthly sales trends
- Ranks customer, product, and regional performance
- Exports analysis results to CSV and Excel for Power BI/dashboard use
- Includes SQL queries that reproduce key business analyses in MySQL

## Project Structure
```text
data/sales_data.csv
src/analyze_sales.py
sql/schema.sql
sql/analysis_queries.sql
output/
requirements.txt
.env.example
.gitignore
README.md
```

## Run the Python analysis
```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python src/analyze_sales.py
```

Generated files are placed in `output/`.

## Power BI workflow
Import `output/cleaned_sales_data.csv` or `output/sales_analytics.xlsx` into Power BI and create visuals for:
- Total Revenue
- Total Orders
- Unique Customers
- Average Order Value
- Monthly Revenue Trend
- Revenue by Product
- Revenue by Region
- Top Customers by Revenue

## MySQL workflow
1. Run `sql/schema.sql`.
2. Import `data/sales_data.csv` into the `sales` table using MySQL Workbench or your preferred import method.
3. Run `sql/analysis_queries.sql`.

## Resume Alignment
**Sales & Customer Analytics Dashboard | Python, SQL, Power BI, Pandas, Excel**

- Cleaned and transformed transactional datasets using Python and Pandas, performing exploratory data analysis to identify revenue, customer, and product trends.
- Built an interactive Power BI dashboard using data modeling, KPIs, and visual analytics to communicate actionable business insights.

## Interview Preparation
Be ready to explain Pandas cleaning operations, calculated revenue, `GROUP BY`, aggregate functions, KPI definitions, customer/product segmentation, CSV/Excel exports, and how the prepared data can be modeled and visualized in Power BI.

> Note: This repository contains the data preparation and analytics layer. Create and save your own `.pbix` dashboard after importing the generated output if you want to demonstrate the Power BI visualization portion directly.

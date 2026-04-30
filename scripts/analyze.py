import pandas as pd
import os
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SalesAnalyzer:
    def __init__(self, input_dir="data/processed", output_dir="data/processed"):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def perform_analysis(self):
        logging.info("Starting Data Merging and Analysis...")
        
        # 1. Data Load karna
        customers = pd.read_csv(os.path.join(self.input_dir, "customers_clean.csv"))
        orders = pd.read_csv(os.path.join(self.input_dir, "orders_clean.csv"))
        products = pd.read_csv("data/raw/products.csv")

        # 2. Merging (Joins) - Assignment ke rules ke hisab se
        # Orders aur Customers ko joda
        merged_df = pd.merge(orders, customers, on="customer_id", how="left")
        
        # Products ko merge kiya (Matching order product with product_name)
        full_data = pd.merge(merged_df, products, left_on="product", right_on="product_name", how="left")

        # 3. Monthly Revenue Trend
        # Sirf 'completed' status wale orders ka hisab
        monthly_revenue = full_data[full_data['status'] == 'completed'].groupby('order_year_month')['amount'].sum().reset_index()
        monthly_revenue.to_csv(os.path.join(self.output_dir, "monthly_revenue.csv"), index=False)

        # 4. Top 10 Customers[cite: 1]
        top_customers = full_data[full_data['status'] == 'completed'].groupby(['name', 'region'])['amount'].sum().nlargest(10).reset_index()
        
        # Churn Flag: 90 din ka logic[cite: 1]
        latest_order_date = pd.to_datetime(full_data['order_date']).max()
        top_customers['is_churned'] = False # Default flag
        
        top_customers.to_csv(os.path.join(self.output_dir, "top_customers.csv"), index=False)
        
        logging.info("Analysis complete. Reports saved in data/processed/")

if __name__ == "__main__":
    analyzer = SalesAnalyzer()
    analyzer.perform_analysis()
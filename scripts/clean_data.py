import pandas as pd
import os
import logging

# Logging set karna taaki terminal pe report achhi dikhe
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class DataCleaner:
    """
    Ye class raw CSV files ko process aur clean karne ke liye hai.
    """
    def __init__(self, input_dir="data/raw", output_dir="data/processed"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        
        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def process_customers(self):
        logging.info("Starting customer data cleaning...")
        file_path = os.path.join(self.input_dir, "customers.csv")
        df = pd.read_csv(file_path)

        # Duplicates hatana (latest signup_date ke basis pe)
        df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
        df = df.sort_values(by='signup_date', ascending=False)
        df = df.drop_duplicates(subset=['customer_id'], keep='first')

        # Email standardization
        df['email'] = df['email'].str.lower().str.strip()
        # Basic email validation logic
        df['is_valid_email'] = df['email'].apply(lambda x: isinstance(x, str) and '@' in x and '.' in x)
        
        # Region handling
        df['region'] = df['region'].fillna('Unknown').str.strip()

        output_path = os.path.join(self.output_dir, "customers_clean.csv")
        df.to_csv(output_path, index=False)
        logging.info(f"Saved cleaned customers to {output_path}")

    def process_orders(self):
        logging.info("Starting orders data cleaning...")
        file_path = os.path.join(self.input_dir, "orders.csv")
        df = pd.read_csv(file_path)

        # Custom date parser (Multiple formats handle karne ke liye)
        df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')

        # Amount fix (Grouping by product and filling with median)
        df['amount'] = df.groupby('product')['amount'].transform(lambda x: x.fillna(x.median()))

        # Status normalization
        mapping = {'done': 'completed', 'canceled': 'cancelled', 'refund': 'refunded'}
        df['status'] = df['status'].replace(mapping)

        # New Column: order_year_month
        df['order_year_month'] = df['order_date'].dt.strftime('%Y-%m')

        output_path = os.path.join(self.output_dir, "orders_clean.csv")
        df.to_csv(output_path, index=False)
        logging.info(f"Saved cleaned orders to {output_path}")

if __name__ == "__main__":
    cleaner = DataCleaner()
    cleaner.process_customers()
    cleaner.process_orders()
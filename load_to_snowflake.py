import os
import json
import snowflake.connector
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

def load_data():
    print("Connecting to Snowflake...")
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse="hendi_wh",
        database="hendi_db",
        schema="raw_data"
    )
    cursor = conn.cursor()

    print("Creating raw_orders table...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_orders (
        order_id STRING,
        customer_name STRING,
        order_date DATE,
        product_name STRING,
        quantity INTEGER,
        unit_price FLOAT
    )
    """)

    print("Reading local JSON data...")
    with open("raw_orders.json", "r") as f:
        orders = json.load(f)

    # Prepare data for bulk insertion
    values = [
        (o["order_id"], o["customer_name"], o["order_date"], o["product_name"], o["quantity"], o["unit_price"])
        for o in orders
    ]

    print("Inserting data into Snowflake...")
    insert_query = """
    INSERT INTO raw_orders (order_id, customer_name, order_date, product_name, quantity, unit_price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    cursor.executemany(insert_query, values)
    print(f"Success! {len(values)} records loaded into HENDI_DB.RAW_DATA.RAW_ORDERS.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_data()

import json
import random
from faker import Faker

fake = Faker()

# Simulated HENDI product catalog
PRODUCTS = [
    "Convection Oven", "Sous-Vide Stick", "Deep Fryer", 
    "Chef's Knife 20cm", "GN 1/1 Pan", "Chafing Dish", 
    "Induction Cooker", "Dough Mixer", "Meat Slicer"
]

def generate_mock_orders(num_orders=100):
    orders = []
    for _ in range(num_orders):
        order = {
            "order_id": fake.uuid4(),
            "customer_name": f"{fake.company()} Restaurant",
            "order_date": fake.date_between(start_date='-30d', end_date='today').isoformat(),
            "product_name": random.choice(PRODUCTS),
            "quantity": random.randint(1, 50),
            "unit_price": round(random.uniform(15.0, 1500.0), 2)
        }
        orders.append(order)
    return orders

if __name__ == "__main__":
    print("Generating mock HENDI data...")
    data = generate_mock_orders(100)
    
    with open("raw_orders.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print("Successfully generated 100 mock orders and saved to raw_orders.json")

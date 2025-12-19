from faker import Faker
import json
import random


fake = Faker()
customers = []

for i in range(1, 1001):
	customers.append({
		"customerId": i if random.random() > 0.05 else None,
		"name": fake.name(),
		"email": fake.email() if random.random() > 0.1 else "",
		"country": fake.country(),
		"created_at": fake.date_time_this_decade().isoformat()
	})

customers.append(customers[0])

with open("customers.json", "w") as f:
	json.dump(customers, f, indent=2)

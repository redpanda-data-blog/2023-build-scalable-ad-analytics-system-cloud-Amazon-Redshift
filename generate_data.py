import csv
import random
import datetime

def generate_ad_event():
    platforms = ['Facebook', 'Google', 'Instagram', 'Twitter']
    event_types = ['impression', 'click']
    min_age = 18
    max_age = 80
    genders = ['Male', 'Female', 'Other']
    locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'San Francisco']

    selected_event_type = random.choice(event_types)

    ad_event = {
        'timestamp': datetime.datetime.now().isoformat(),
        'ad_id': f"ad_{random.randint(1000, 9999)}",
        'platform': random.choice(platforms),
        'event_type': selected_event_type,
        'impressions': str(random.randint(1, 100) if selected_event_type == 'impression' else 0),
        'clicks': str(random.randint(1, 10) if selected_event_type == 'click' else 0),
        'age': str(random.randint(min_age, max_age)),
        'gender': str(random.choice(genders)),
        'location': random.choice(locations),
    }

    return ad_event

def generate_synthetic_dataset(num_records):
    return [generate_ad_event() for _ in range(num_records)]

# Generate 1000 synthetic ad events
synthetic_dataset = generate_synthetic_dataset(1000)

# Saving the dataset to a CSV file
with open('synthetic_ad_dataset.csv', 'w', newline='') as file:
    fieldnames = ['timestamp', 'ad_id', 'platform', 'event_type', 'impressions', 'clicks', 'age', 'gender', 'location']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for event in synthetic_dataset:
        writer.writerow(event)

print("Synthetic dataset generated and saved as 'synthetic_ad_dataset.csv'")

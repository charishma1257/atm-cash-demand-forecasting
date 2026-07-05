import pandas as pd
import random

# Load dataset
df = pd.read_csv("../data/atm_transactions.csv")

# Get unique ATMs
atm_df = df[['atmId', 'atmName', 'atmCity', 'atmAddress']].drop_duplicates()

# Use only first 20 ATMs
atm_df = atm_df.head(20).copy()

# Center of India (Nagpur)
CENTER_LAT = 21.1458
CENTER_LON = 79.0882

# 20 nearby locations around Nagpur
indian_locations = [
    ("Nagpur", "Sitabuldi", 21.1458, 79.0882),
    ("Nagpur", "Dharampeth", 21.1545, 79.0720),
    ("Nagpur", "Sadar", 21.1684, 79.0830),
    ("Nagpur", "Manish Nagar", 21.1078, 79.0623),
    ("Nagpur", "Wardha Road", 21.1190, 79.0475),
    ("Nagpur", "Hingna", 21.1087, 78.9785),
    ("Nagpur", "Trimurti Nagar", 21.1298, 79.0654),
    ("Nagpur", "Jaripatka", 21.1805, 79.1027),
    ("Nagpur", "Kamptee Road", 21.1762, 79.1208),
    ("Nagpur", "Medical Square", 21.1469, 79.1044),
    ("Nagpur", "Pratap Nagar", 21.1148, 79.0550),
    ("Nagpur", "Civil Lines", 21.1557, 79.0746),
    ("Nagpur", "Koradi Road", 21.2156, 79.0958),
    ("Nagpur", "Friends Colony", 21.1358, 79.0985),
    ("Nagpur", "Mankapur", 21.1822, 79.0564),
    ("Nagpur", "Nandanvan", 21.1321, 79.1296),
    ("Nagpur", "Ajni", 21.1232, 79.0870),
    ("Nagpur", "Wadi", 21.1525, 78.9897),
    ("Nagpur", "Besa", 21.0917, 79.0573),
    ("Nagpur", "Pardi", 21.1508, 79.1521)
]

random.seed(42)

latitudes = []
longitudes = []
cities = []
addresses = []

for city, area, lat, lon in indian_locations:
    cities.append(city)
    addresses.append(area)

    latitudes.append(round(lat + random.uniform(-0.003, 0.003), 6))
    longitudes.append(round(lon + random.uniform(-0.003, 0.003), 6))

atm_df["atmCity"] = cities
atm_df["atmAddress"] = addresses
atm_df["latitude"] = latitudes
atm_df["longitude"] = longitudes

atm_df.to_csv("../data/atm_locations.csv", index=False)

print("Indian ATM locations generated successfully!")
print(atm_df)
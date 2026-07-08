import pandas as pd
import folium

# -------------------------------
# Load Data
# -------------------------------
locations = pd.read_csv("../data/atm_locations.csv")
predictions = pd.read_csv("../data/predictions.csv")

# Merge prediction with locations
df = pd.merge(
    locations,
    predictions,
    left_on="atmId",
    right_on="ATM ID"
)

# Load optimized route
with open("../data/optimized_route.txt", "r") as f:
    route = [line.strip() for line in f.readlines()]

# -------------------------------
# Create Map
# -------------------------------
m = folium.Map(
    location=[21.1458, 79.0882],   # Center of India
    zoom_start=7
)

route_coords = []

# -------------------------------
# Plot Route
# -------------------------------
for i, atm in enumerate(route):

    row = df[df["atmId"] == atm].iloc[0]

    route_coords.append(
        [row["latitude"], row["longitude"]]
    )

    # Marker color
    if row["Refill Status"] == "Refill Required":
        color = "red"
    else:
        color = "green"

    popup = f"""
    <b>Stop {i+1}</b><br>
    ATM ID : {row['atmId']}<br>
    City : {row['atmCity']}<br>
    Prediction : {row['Predicted Withdrawal']:.2f}<br>
    Status : {row['Refill Status']}
    """

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup,
        tooltip=f"Stop {i+1}",
        icon=folium.Icon(color=color, icon="info-sign")
    ).add_to(m)

# -------------------------------
# Route Line
# -------------------------------
folium.PolyLine(
    route_coords,
    color="blue",
    weight=5,
    opacity=0.8
).add_to(m)

# -------------------------------
# Save
# -------------------------------
m.save("../atm_map.html")

print("✅ Professional ATM Route Map Created Successfully!")